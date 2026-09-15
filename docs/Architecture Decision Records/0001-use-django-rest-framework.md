# ADR 0001: Use Django REST Framework



## Context

GardenOps is designed as a multi-user garden management platform with a Django backend and a future React/TypeScript frontend.

The backend needs to expose structured APIs for gardens, plants, tasks, comments, activities, memberships, and future features such as real-time communication and AI-powered recommendations.

The application could use Django views that directly render HTML, but the planned frontend is a separate React application. The backend therefore needs a consistent API layer between the frontend and the database.

## Decision

We will use **Django REST Framework (DRF)** to build the GardenOps API.

DRF will be responsible for:

* Serializing Django models into JSON responses.
* Validating incoming API data.
* Handling API requests and responses.
* Providing reusable serializers and views.
* Supporting authentication and authorization as the project develops.
* Providing a foundation for future API testing.

The Django ORM will remain responsible for database access and model relationships.

## Consequences

### Positive

* Provides a clear separation between the frontend and backend.
* Makes the API reusable by web, mobile, or other clients in the future.
* Provides built-in tools for serialization and validation.
* Makes API behavior easier to test.
* Provides a natural foundation for authentication and permissions.

### Negative

* Introduces additional concepts such as serializers, API views, routers, and permissions.
* Requires more code than a simple server-rendered Django application.
* The frontend and backend must be developed and maintained as separate layers.

## Alternatives Considered

### Django server-rendered views

This would be simpler for a traditional Django website, but it would couple the UI more closely to the backend.

### Flask or FastAPI

These frameworks could provide an API backend, but Django already provides the ORM, authentication system, admin interface, and project structure needed by GardenOps.

## Result

GardenOps will use Django REST Framework as the primary API layer between the backend and future frontend applications.
