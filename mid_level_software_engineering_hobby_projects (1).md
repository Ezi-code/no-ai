# Three Engineering Projects for a Mid-Level Software Engineer

## Purpose

These three projects are designed as serious hobby projects for strengthening independent engineering ability. The goal is not simply to produce portfolio applications. It is to practise problem decomposition, architecture, implementation, debugging, testing, security, deployment, and systems thinking **without relying on coding agents**.

The projects deliberately cover different areas of software engineering:

1. **CommunityOS** — product engineering and application architecture.
2. **CommerceFlow** — transactional systems, data consistency, and payment workflows.
3. **TaskForge** — distributed systems, concurrency, networking, and systems engineering.

The suggested order is intentional: build a substantial application first, then tackle transactional correctness, and finally work closer to the operating-system and distributed-systems layers.

---

# 1. CommunityOS — Developer Community Management Platform

**Focus:** Product engineering, application architecture, APIs, data modelling, and background processing.  
**Difficulty:** Intermediate to advanced.  
**Suggested duration:** 6–8 weeks of focused part-time work.

## Project idea

Build a platform that helps technical communities manage members, events, chapters, volunteers, mentorship programmes, and activities.

It can be thought of as a focused combination of Meetup, Eventbrite, and a community administration platform. It could eventually be used to manage Python-Wa, PostgreSQL Ghana, Apache Ghana, or other technical communities.

## Core features

### Community management
- Create and manage multiple communities.
- Support multiple chapters under a parent organization.
- Member registration and profiles.
- Membership approval and verification.
- Role-based access control.
- Community announcements.
- Member activity history.

### Event management
- Create events, workshops, and conferences.
- Event registration and ticket management.
- Capacity limits and waitlists.
- QR-code-based attendance.
- Speaker and volunteer management.
- Event feedback and post-event reports.
- Email notifications and reminders.

### Mentorship management
- Mentor and mentee profiles.
- Mentorship applications.
- Mentor–mentee matching.
- Session scheduling.
- Mentorship progress tracking.

### Administration
- Community analytics.
- Member growth reports.
- Event attendance reports.
- Volunteer management.
- Audit logs.
- Multiple administrator roles.

## Engineering topics to practise

| Area | Concepts and tools |
|---|---|
| Architecture | Modular monolith, domain-driven design, clear module boundaries |
| Backend | REST APIs, request validation, background processing |
| Database | PostgreSQL, relational modelling, constraints, indexing, migrations |
| Authentication | JWT, OAuth2, RBAC, authorization policies |
| Caching | Redis, cache invalidation, cache expiry |
| Async tasks | Celery or a comparable worker system |
| Real-time | WebSockets for live event updates |
| Testing | pytest, unit tests, integration tests, end-to-end tests |
| Security | Rate limiting, audit logs, input validation, access-control testing |
| Frontend | React/Next.js or Django with HTMX |
| DevOps | Docker, GitHub Actions, automated deployment |
| Observability | Structured logging, metrics, error tracking |

## Engineering challenges

### Multi-tenancy
Design the application so that several communities can use one deployment while each community's administrators and members can only access data they are authorized to see. Decide how tenant identity is represented, how it is enforced in queries, and how you will test for data leakage.

### QR attendance integrity
Prevent a ticket from being checked in more than once. Consider duplicate scans, concurrent requests, expired tickets, and the audit trail required to investigate attendance disputes.

### Permissions design
Model roles and permissions carefully. A chapter administrator should not automatically have the same authority as a parent-organization administrator. Avoid scattering authorization checks throughout the codebase without a consistent policy.

## Suggested milestones

1. Write requirements and define community, chapter, member, event, and ticket terminology.
2. Design the data model and authorization rules.
3. Implement authentication and community membership.
4. Implement events, registrations, and capacity limits.
5. Add QR check-in and duplicate-scan protection.
6. Add background notifications and reminders.
7. Add reporting, audit logs, tests, and deployment.

---

# 2. CommerceFlow — E-commerce and Order Fulfilment System

**Focus:** Transactional systems, data consistency, concurrency, payments, and application security.  
**Difficulty:** Advanced.  
**Suggested duration:** 8–10 weeks of focused part-time work.

## Project idea

Build a single-vendor e-commerce platform that handles product catalogues, shopping carts, checkout, payments, inventory, orders, and delivery.

Use books and branded T-shirts as sample products. Start as a single-vendor store rather than building a multi-vendor marketplace.

## Core features

### Product catalogue
- Product categories and collections.
- Product variants such as sizes, colours, and editions.
- Product image management.
- Stock availability.
- Product search and filtering.
- Product reviews and ratings.

### Shopping and checkout
- Shopping carts.
- Guest and registered-customer checkout.
- Discount codes.
- Shipping-address management.
- Delivery-fee calculations.
- Order summaries.

### Payment processing
- Mobile Money and card payment integration using a payment provider's sandbox.
- Payment confirmation through verified webhooks.
- Refund processing.
- Failed-payment handling.
- Payment transaction history.

### Inventory
- Stock reservations.
- Inventory adjustments.
- Low-stock notifications.
- Inventory movement history.
- Stock release when orders expire or are cancelled.

### Order fulfilment
- Order lifecycle management.
- Delivery assignment.
- Shipment tracking.
- Order-status notifications.
- Returns and refunds.
- Sales reports.

## Engineering topics to practise

| Area | Concepts and tools |
|---|---|
| Architecture | Domain-driven design, modular services, bounded contexts |
| Database | ACID transactions, constraints, indexes, isolation levels |
| Concurrency | Race conditions, optimistic locking, row-level locking |
| Payments | Idempotency, webhook verification, reconciliation |
| Distributed systems | Transactional outbox pattern, retry-safe processing |
| Caching | Redis and product caching |
| Search | PostgreSQL full-text search |
| Background processing | Payment reconciliation, notifications, order expiry |
| Security | Payment security, authorization, OWASP risks |
| Testing | Integration tests, contract tests, concurrency tests |
| Performance | Load testing, query optimization |
| Deployment | Docker, CI/CD, cloud deployment |

## Engineering challenges

### Inventory race conditions
Suppose only one copy of a book remains, but two customers attempt to purchase it simultaneously. Ensure that both customers cannot successfully reserve or purchase the same unit. Implement the logic using database transactions and appropriate locking or atomic updates, then test it with concurrent requests.

### Duplicate payment webhooks
Payment providers may deliver the same webhook more than once. Ensure duplicate events cannot create multiple payment records, fulfil an order twice, or trigger repeated side effects. Store and enforce idempotency using a stable provider event or transaction identifier.

### Payment succeeds but order update fails
A payment can succeed while your application crashes before updating its order record. Design a recovery process that can reconcile provider transactions with local orders without charging the customer again. Practise idempotency, transactional outbox processing, retry policies, and scheduled reconciliation.

### Order and inventory lifecycle
Define what happens to reserved stock when payment fails, a checkout session expires, a customer cancels an order, or a refund is issued. Make transitions explicit and test invalid state changes.

## Suggested milestones

1. Define product, variant, cart, order, payment, inventory, and shipment states.
2. Design the schema and transaction boundaries.
3. Implement the catalogue, cart, and checkout flow.
4. Implement inventory reservation and concurrency protection.
5. Integrate a payment provider's sandbox and verify webhooks.
6. Implement idempotent order fulfilment and reconciliation.
7. Add refunds, notifications, reporting, security tests, and deployment.

---

# 3. TaskForge — Distributed Job Execution and Scheduling Platform

**Focus:** Systems engineering, distributed systems, concurrency, networking, and performance.  
**Difficulty:** Advanced to expert.  
**Suggested duration:** 8–12 weeks of focused part-time work.

## Project idea

Build a lightweight distributed task execution platform. Applications submit jobs to an API, and distributed workers execute those jobs asynchronously.

Think of a simplified combination of Celery, BullMQ, and a workflow scheduler.

Example jobs:
- Send emails.
- Generate PDF reports.
- Process uploaded images.
- Import large datasets.
- Execute scheduled database backups.
- Process webhook deliveries.

## Core features

### Job management
- Submit jobs through an API.
- Create scheduled jobs.
- Support delayed execution.
- Define job priorities.
- Cancel pending jobs.
- Track execution status.
- Retrieve execution results.

### Worker management
- Register workers.
- Worker heartbeats.
- Worker health monitoring.
- Worker concurrency configuration.
- Graceful worker shutdown.
- Worker failure detection.

### Queue management
- Multiple queues.
- Priority queues.
- Job retries.
- Exponential backoff.
- Dead-letter queues.
- Job timeout management.
- Rate limiting.

### Monitoring
- Job execution logs.
- Worker statistics.
- Queue depth.
- Execution duration.
- Failed-job reports.
- Throughput monitoring.

## Engineering topics to practise

| Area | Concepts and tools |
|---|---|
| Systems design | Distributed architecture, control plane and worker responsibilities |
| Concurrency | Threads, processes, synchronization, race conditions |
| Networking | HTTP, TCP, sockets, connection lifecycle |
| Data structures | Queues, heaps, priority queues |
| Database | Durable job persistence, atomic claiming, indexes |
| Messaging | RabbitMQ, Redis Streams, or NATS |
| Reliability | Retries, acknowledgements, leases, heartbeats |
| Scheduling | Delayed and recurring tasks |
| Performance | Throughput, latency, backpressure |
| Observability | OpenTelemetry, Prometheus, Grafana |
| Infrastructure | Docker, Linux, systemd |
| Testing | Concurrency tests, fault injection, integration tests |

## Build the first version without a message broker

Do not start by depending on Celery, RabbitMQ, or another established task queue. First build a simple job queue using PostgreSQL as the durable job store.

Implement:
1. A job-submission API.
2. A worker that polls for available jobs.
3. Atomic job claiming using database transactions.
4. Job locking and lease expiration.
5. Retry mechanisms.
6. Dead-letter handling.

Once this works, introduce a broker such as RabbitMQ or NATS and compare the two architectures. Document what becomes easier, what becomes harder, and what reliability guarantees change.

## Rust challenge

After the Python implementation works, write the worker engine in Rust. Keep the Python application as the control plane initially, while the Rust implementation handles job execution and worker coordination.

This gives you practical exposure to ownership, memory safety, concurrency, networking, process management, and performance. Compare the Python and Rust implementations using the same workload and measurable benchmarks.

Do not execute arbitrary user-supplied code in workers. Begin with registered, trusted task handlers. Secure sandboxed execution is a separate engineering challenge.

## Suggested milestones

1. Specify job states, worker states, retry semantics, and delivery guarantees.
2. Implement durable job submission and a PostgreSQL-backed queue.
3. Implement atomic worker claiming and lease expiry.
4. Implement acknowledgements, retries, timeouts, and dead-letter handling.
5. Add scheduled jobs, multiple queues, and priorities.
6. Add monitoring, metrics, failure injection, and load tests.
7. Introduce a message broker and compare the design.
8. Implement a Rust worker and benchmark it against the Python worker.

---

# 4. Suggested technology toolkit

Use a consistent foundation across the projects, then introduce tools when a real engineering problem calls for them. You do not need every tool in every project.

| Category | Suggested technologies |
|---|---|
| Backend | Python, Django, FastAPI, Rust, C |
| Frontend | TypeScript, Next.js, React, HTMX |
| Data and messaging | PostgreSQL, Redis, RabbitMQ, NATS |
| Testing and quality | pytest, Playwright, Ruff, mypy, k6, pre-commit |
| Infrastructure | Linux, Docker, GitHub Actions, Terraform, Nginx, systemd |
| Observability and security | OpenTelemetry, Prometheus, Grafana, OWASP practices, Trivy, Dependabot |

A sensible progression is to use Python and PostgreSQL for the first two projects, then introduce more systems-level work and Rust in TaskForge.

---

# 5. Rules for building without coding agents

The objective is to rebuild independent reasoning and implementation ability. Use official documentation, books, technical articles, and community discussions, but do not ask coding agents to generate implementations for you.

## Rule 1: Design before implementation

Before writing code, produce:
- A problem statement.
- Functional requirements.
- Non-functional requirements.
- Database entity-relationship diagrams.
- API specifications.
- Architecture diagrams.
- Initial deployment architecture.

Do not begin implementation until you can explain how the system is intended to work.

## Rule 2: Write your own implementations

When you encounter a problem:
1. Attempt to solve it independently.
2. Read the relevant documentation.
3. Experiment with small, isolated examples.
4. Implement your solution.
5. Write tests to verify your understanding.

## Rule 3: Do not hide behind frameworks

Understand the concepts behind the libraries you use:
- Password hashing and authentication flows.
- JWT signing and verification.
- Database transactions and isolation.
- Connection pooling.
- HTTP request processing.
- Concurrency and shared state.
- Caching and invalidation.

You do not need to reinvent production cryptography. You should understand the mechanisms and trade-offs behind the libraries you use.

## Rule 4: Treat debugging as part of development

When something breaks, investigate the system rather than trying random fixes. Useful tools include:
- Python debugger (`pdb`).
- Linux tools (`strace`, `lsof`, `ss`, `top`).
- PostgreSQL `EXPLAIN ANALYZE`.
- Browser developer tools.
- Logs and stack traces.
- Network inspection tools.

## Rule 5: Document engineering decisions

Maintain an `ARCHITECTURE.md`, an `ADRs/` directory, and an engineering journal. For important decisions, record:
- The problem.
- Possible solutions.
- Trade-offs.
- Why you selected the implementation.
- What you would change at a larger scale.

## A useful memory-building exercise

After completing a major feature, close the original implementation and recreate it from memory in a separate branch or small scratch project. Compare the two implementations, note what you forgot, and identify the concepts that need more practice.

---

# 6. Recommended build order

| Order | Project | Main learning focus | Suggested duration |
|---|---|---|---|
| 1 | CommunityOS | Application architecture, data modelling, authentication, APIs, background processing | 6–8 weeks |
| 2 | CommerceFlow | Transactions, concurrency, third-party integrations, consistency, application security | 8–10 weeks |
| 3 | TaskForge | Operating systems, networking, distributed systems, Rust, concurrency, performance | 8–12 weeks |

These are planning estimates for focused part-time work, not deadlines. Adjust them according to the time available and the depth of implementation you choose.

---

# 7. Definition-of-done checklist

Do not consider a project complete until you can demonstrate and explain the following. Mark each item as you finish it.

- [ ] Written requirements and acceptance criteria.
- [ ] Architecture diagram and documented design decisions.
- [ ] Database schema and migration strategy.
- [ ] Documented API contracts.
- [ ] Authentication, authorization, and security controls.
- [ ] Unit, integration, and end-to-end tests.
- [ ] Docker-based local development environment.
- [ ] Automated CI pipeline.
- [ ] Production deployment with HTTPS.
- [ ] Structured logging and error reporting.
- [ ] Metrics and monitoring.
- [ ] Database backup and tested restoration.
- [ ] Load testing and performance measurements.
- [ ] README, setup instructions, and operational runbook.

---

# Final advice

Build these as engineering exercises, not just portfolio demos. Maintain a separate `engineering-notes` repository where you document what you learned, bugs you encountered, algorithms you implemented, architectural trade-offs, and concepts you initially misunderstood.

The goal is to become comfortable sitting in front of an empty editor, understanding a problem, decomposing it, and implementing a solution without needing an agent to reason through it for you.

**The muscle worth rebuilding is independent engineering judgement.**
