# ADR 0002: Use PostgreSQL



## Context

GardenOps contains structured and relational data including:

* Users
* Gardens
* Garden memberships
* Plants
* Tasks
* Comments
* Activities

These entities have relationships with one another. For example, a garden can contain multiple plants, users can belong to multiple gardens, and tasks can be associated with plants and assigned to users.

The application therefore requires a relational database with support for constraints, relationships, transactions, and reliable querying.

## Decision

We will use **PostgreSQL** as the primary database for GardenOps.

Django's ORM will be used to interact with PostgreSQL rather than writing database queries throughout the application.

PostgreSQL will run as a Docker container during local development.

## Consequences

### Positive

* Strong support for relational data.
* Supports foreign keys and database constraints.
* Provides transactions for operations that must remain consistent.
* Closely matches the type of database commonly used in production backend systems.
* Provides useful experience with SQL and relational database design.
* Docker makes the database environment reproducible.

### Negative

* Requires more setup than SQLite.
* Developers must understand database migrations and containerized database development.
* Local development depends on the PostgreSQL container being available.

## Alternatives Considered

### SQLite

SQLite is convenient for initial Django development and requires no separate database server.

However, GardenOps is intended to become a multi-user application with relational data and concurrent operations. PostgreSQL provides a more appropriate development environment for the project's intended architecture.

### MySQL

MySQL is also a valid relational database, but PostgreSQL was selected for GardenOps because of its strong Django integration and the project's need for a robust relational database.

## Result

PostgreSQL is the canonical database for GardenOps development and deployment.
