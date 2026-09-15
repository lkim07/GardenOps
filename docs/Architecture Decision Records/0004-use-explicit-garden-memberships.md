# ADR 0004: Use Explicit Garden Memberships



## Context

GardenOps is intended to support multiple family members collaborating on multiple gardens.

A garden therefore needs to represent not only which users have access, but also what role each user has.

The initial design used a many-to-many relationship between `Garden` and `User`.

However, a simple many-to-many relationship does not provide a natural place to store information about the user's relationship with a specific garden.

GardenOps requires roles such as:

* Owner
* Member
* Viewer

For example:

```text
Backyard Garden

Mom   → Owner
Alice → Member
Bob   → Viewer
```

The application may also need to add additional membership-specific information in the future.

## Decision

We will use an explicit `GardenMembership` model between `Garden` and Django's `User` model.

Conceptually:

```text
User
  │
  │
  ▼
GardenMembership
  │
  │
  ▼
Garden
```

Each membership will contain at least:

* `garden`
* `user`
* `role`

A uniqueness constraint will prevent the same user from being added to the same garden more than once.

## Consequences

### Positive

* Roles are represented explicitly.
* Permissions can be determined per garden.
* The model can be extended with additional membership-specific information.
* Duplicate memberships can be prevented at the database level.
* The design supports future authorization requirements.

### Negative

* The data model is more complex than a simple many-to-many relationship.
* Queries involving membership may require joins.
* Application code must work with the membership model when checking access or roles.

## Alternatives Considered

### Simple ManyToManyField

A direct many-to-many relationship is simpler when the relationship itself contains no additional information.

It was rejected because GardenOps needs to store a role for each user-garden relationship.

### Storing members and roles in a JSON field

A JSON-based approach could store users and roles together, but it would weaken relational integrity and make querying and enforcing uniqueness more complicated.

## Result

GardenOps will represent access to gardens through an explicit `GardenMembership` model with a role for each user.
