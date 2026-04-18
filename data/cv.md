# Yash Malani
+91 79766 40069 | yashmalani340@gmail.com | linkedin.com/in/yashmalani340 | github.com/yashmalani | Hyderabad, India

## Professional Summary
Java and Spring Boot engineer with around 4 years of production experience at NCR Voyix, building and scaling high-throughput microservices that serve millions of transactions daily. Specializes in GraphQL/REST API design, event-driven architecture, and cloud-native deployments on GCP and Kubernetes - with a track record of delivering latency reduction, QA automation coverage, and faster CI/CD pipelines. Comfortable owning full SDLC cycles and mentoring engineers in distributed-systems design.

## Experience

### NCR Voyix | Software Engineer 2 | Hyderabad, India
*07/2022 - Present*
* Re-architected a legacy Spring Batch synchronization pipeline into an event-driven workflow using Spring Boot and Pub/Sub, cutting end-to-end sync latency.
* Designed and delivered GraphQL and RESTful microservices with Spring Boot and Hibernate, introducing optimized N+1-free data persistence layers that reduced average API response time by 35% and enabled seamless integration across 8 distributed services.
* Migrated file-based data processing to a Redis-backed caching and storage layer, redesigning cache invalidation strategies to cut synchronization latency by 50% and reduce database read load by 40% under peak traffic.
* Built a Java automated testing framework using JUnit 5 and Mockito, integrating contract tests and data-generation utilities that eliminated 60% of manual QA effort and caught regressions 3x faster in CI.
* Reduced Maven/Gradle build times by 40% through dependency graph restructuring, parallel module compilation, and build cache configuration - cutting CI pipeline feedback loops by 8-10 minutes.
* Integrated SonarQube static analysis into Jenkins pipelines with quality gate enforcement, reducing production defect escape rates by 30% and raising code coverage across Spring Boot services.
* Engineered Docker and Kubernetes (GKE) deployment infrastructure with Helm charts and GitHub Actions CI/CD, enabling zero-downtime rolling deployments and reducing release cycle time by 35%.

### NCR Corporation | Software Engineer Intern | Hyderabad, India
*01/2022 - 07/2022*
* Containerized and deployed SaaS microservices on Google Kubernetes Engine (GKE) using Docker and Helm Charts, improving deployment repeatability and reducing environment drift across dev/staging/production.
* Developed backend modules with Spring Boot and PostgreSQL/MongoDB, contributing to a data persistence refactor that improved query throughput by 25% under simulated load.

## Projects

### StockTracker
*Java, Spring Boot, Kafka, MongoDB, REST*
* Architected an event-driven stock tracking system using Kafka producers/consumers for real-time price streaming and MongoDB for time-series persistence, with a mock data generation layer simulating realistic ticker fluctuations for end-to-end pipeline testing without live market dependencies.
* Exposed stock data via a Spring Boot REST API supporting filtering, pagination, and real-time price queries - backed by live Kafka stream consumers and MongoDB reads optimized for high-frequency time-series data.

### Custom Memory Allocator
*C++, mmap, Google Benchmark*
* Implemented a custom memory allocator in C++ with malloc/free equivalents using a free-list allocation strategy, managing heap memory directly via sbrk/mmap syscalls with real-time internal and external fragmentation ratio tracking across allocation patterns.
* Benchmarked the custom allocator against glibc's malloc under allocation-heavy workloads, profiling throughput, fragmentation overhead, and per-operation latency to surface concrete performance trade-offs.

## Education

### Vellore Institute of Technology
*07/2018 - 07/2022*
* Bachelor of Technology (B.Tech) in Computer Science
* CGPA: 8.85/10

## Technical Skills
* **Languages:** Java (primary), C++, Python, JavaScript
* **Frameworks & Libraries:** Spring Boot, Spring MVC, Hibernate, JUnit 5, Mockito, GraphQL Java, REST
* **Databases:** PostgreSQL, MySQL, MongoDB, Redis
* **DevOps & Cloud:** Docker, Kubernetes (GKE), Helm, Terraform, GitHub Actions, Jenkins, GCP
* **Observability:** Prometheus, Grafana, SLF4J/Logback, SonarQube
* **Concepts:** Distributed Systems, Event-Driven Architecture, Microservices, TDD, Agile/Scrum