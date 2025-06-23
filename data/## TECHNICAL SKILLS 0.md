## TECHNICAL SKILLS

- **Backend Development:** Java (Java 8+, Streams API, Lambda expressions), Spring Boot, Spring MVC, Spring Data JPA, Hibernate ORM
- **Frontend & Scripting:** JavaScript, TypeScript, React, Next.js, Node.js, Python, Ruby, Rails, HTML5, CSS
- **Cloud & Infrastructure:** AWS (EC2, ELB, ECR, Lambda, RDS, API Gateway, S3, CloudFront, CloudWatch), Docker, Kubernetes, Nginx, Varnish
- **DataBase Management:** MySQL, MongoDB, Aerospike, Redis, Solr 9, ElasticSearch, Zookeeper
- **Messaging & Integration:** Kafka, RabbitMQ, RESTful APIs, gRPC

## PROFESSIONAL EXPERIENCE

### TEST COMPANY

**Software Development Engineer 2** | _June 2023 - Present_

#### Search and Recommendation Engine

- Achieved a **20% increase in click-through rates** for product recommendations by implementing a hybrid search solution using multimodal embedding model (**Fashion CLIP)** to get semantically and visually Top-K similar results using K-NN algorithm.
- Reduced search and recommendation API response time by **50% by leading** the migration to a **Solr 9 cloud** infrastructure with vector search capabilities, integrating **Zookeeper ensemble** for cluster management and **Varnish HTTP proxy caching** for performance improvements.
- Built a **Java Spring Boot microservice** for real-time product data synchronization to Solr by implementing an event-driven architecture using Kafka messages, ensuring reliable data updates.
- Cut infrastructure costs for Search system by **50%** through migrating Solr to **Graviton based instances utilsing varnish cache, reducing embedding service load using Redis LRU cache and setting up Auto-scaling to upscale and descale the servers depending upon traffic.**

#### S2S Payment Service

- Developed and maintained a **payment gateway-agnostic S2S payment service** in **Spring Boot ** using **strategy pattern**, achieving seamless integrations across multiple providers.
- Minimized payment downtimes through **intelligent gateway selection** based on real-time success rates, and Implemented **circuit breaker pattern** with **Resilience4j** to handle service failures, preventing cascading failures.
- Reduced cost for payment status tracking by Integrating **webhooks** for real-time payment status notifications, and sending Server Sent Events to frontend instead of short-polling mechanism.
- Increased checkout conversions by **8%** by launching the **"Pay with Rewards"** feature using third-party APIs, ensuring accurate refund flows and efficient transaction processing.
