# ADR 0003: Use Docker for Local Services



## Context

GardenOps requires PostgreSQL for local development.

Installing PostgreSQL directly on the host operating system can create environment-specific problems, including:

* Different PostgreSQL versions.
* Conflicting database services.
* Different local users and passwords.
* Port conflicts.
* Differences between development environments.

GardenOps should provide a reproducible development environment that can be recreated without depending heavily on host-specific database installations.

## Decision

We will run PostgreSQL using Docker Compose.

The PostgreSQL service will be defined in `docker-compose.yml`.

The application will connect to the PostgreSQL container through the configured host port during local development.

Database credentials and configuration will be defined through environment configuration rather than being duplicated throughout the application.

## Consequences

### Positive

* PostgreSQL version is explicitly defined.
* The database environment can be recreated consistently.
* Developers do not need a separate native PostgreSQL installation.
* Database lifecycle can be managed through Docker Compose.
* The approach is closer to common containerized development environments.

### Negative

* Docker Desktop becomes a development dependency.
* Docker networking and container lifecycle introduce additional concepts.
* Problems with Docker or WSL can temporarily prevent local development.

## Alternatives Considered

### Native PostgreSQL installation

This can work, but multiple PostgreSQL installations or services on the same machine can cause port and authentication conflicts.

### SQLite

SQLite would remove the need for a database container, but it would not provide the same development environment as the intended PostgreSQL-based application.

## Result

PostgreSQL will be containerized with Docker Compose for GardenOps development.
