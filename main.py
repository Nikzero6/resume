from pathlib import Path
from rendercv.data import read_a_yaml_file
from rendercv.api import create_a_pdf_from_a_python_dictionary as create_pdf

cv_yaml_root = "data"

CV_YAML_OPTIONS = ["backend-java", "backend-node", "frontend-react", "fullstack-java", "fullstack-node", "fullstack-react"]

MANDATORY_DICTS = ["root", "cv", "social_networks", "education", "experience", "skills"]


def is_array(value):
    return isinstance(value, list)


def is_dict(value):
    return isinstance(value, dict)


def is_primitive(value):
    return not is_array(value) and not is_dict(value)


def pretty_print(value):
    """
    Creates a pretty string representation of a value depending on its type recursively, and prints when final string is ready.
    """

    def pretty_print_helper(value, indent=0):
        string = ""

        if is_array(value):
            for i, item in enumerate(value):
                string += (
                    f"\n{indent * '  '}{i + 1}. {pretty_print_helper(item, indent + 1)}"
                )
        elif is_dict(value):
            for key, val in value.items():
                string += (
                    f"\n{indent * '  '}{key}: {pretty_print_helper(val, indent + 1)}"
                )
        else:
            string = str(value)

        return string

    print(pretty_print_helper(value))


def choose_array_items(items):
    """
    Choose items from a list of items.
    """
    pretty_print(items)

    choices = input("\nChoose the items in order separated by commas (e.g. 2,1,3): ")

    if not choices:
        return items

    choices = choices.split(",")

    return [items[int(choice) - 1] for choice in choices]


def modify_array(array, parent_key=None):
    """
    Modify an array depending on its type.
    """

    array = choose_array_items(array)

    for i, item in enumerate(array):
        array[i] = modify_value(item, parent_key=parent_key)

    return array


def modify_dict(dict, parent_key=None):
    """
    Modify a dictionary depending on its type.
    """
    keys = list(dict.keys())

    if len(keys) == 0:
        return dict

    if parent_key not in MANDATORY_DICTS:
        keys = choose_array_items(keys)
        dict = {key: dict[key] for key in keys}

    for key, value in dict.items():
        if not is_primitive(value):
            print(f"\n{key}:")

        dict[key] = modify_value(value, parent_key=key)

    return dict


def modify_value(value, parent_key=None):
    """
    Modify a value depending on its type.
    """
    if is_array(value):
        return modify_array(value, parent_key=parent_key)
    elif is_dict(value):
        return modify_dict(value, parent_key=parent_key)
    else:
        return value


def create_resume(cv_dict, resume_option):
    """
    Create a resume from a dictionary.
    """
    resume_name = input("\nName of the resume file: ")
    resume_name = resume_option if not resume_name else resume_name.strip()
    
    output_path = Path(f"output/{resume_name}.pdf")

    create_pdf(cv_dict, output_path)


def main():
    """Main function to run the script.
    """
    print("Welcome to the CV generator!")
    
    resume_options = choose_array_items(CV_YAML_OPTIONS)

    resume_option = resume_options[0]

    cv_yaml_path = Path(cv_yaml_root) / (resume_option + ".yaml")
    
    cv_dict = read_a_yaml_file(cv_yaml_path)
    
    # cv_dict = modify_dict(cv_dict, parent_key="root")

    create_resume(cv_dict, resume_option)


if __name__ == "__main__":
    main()
