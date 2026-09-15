# ADR 0005: Use Cascade Deletion for Dependent Data



## Context

GardenOps contains dependent relationships between entities.

For example, a `Task` can be associated with a `Plant`.

A task such as:

```text
Water the tomatoes
```

may no longer be meaningful if the associated plant is permanently removed from the garden.

Leaving the task in the database after deleting its associated plant could result in orphaned or misleading records.

## Decision

For relationships where the dependent record has no meaningful existence without its parent, GardenOps will use Django's `CASCADE` deletion behavior.

For example:

```python
plant = models.ForeignKey(
    Plant,
    on_delete=models.CASCADE
)
```

When a plant is deleted, its dependent tasks will therefore also be deleted.

This decision will be applied selectively rather than universally. Relationships representing historical or independently meaningful information may use a different deletion strategy.

## Consequences

### Positive

* Prevents orphaned dependent records.
* Keeps the database consistent with the application's domain model.
* Simplifies cleanup of dependent objects.
* Makes the intended ownership relationship explicit.

### Negative

* Deleting a parent can delete multiple related records.
* Accidental deletion can result in loss of dependent data.
* Important destructive operations should therefore be protected by appropriate application-level authorization and confirmation.

## Alternatives Considered

### SET_NULL

`SET_NULL` would preserve the dependent record after its parent was deleted.

This was not selected for the Plant → Task relationship because a task associated with a deleted plant does not currently have independent meaning in GardenOps.

### PROTECT

`PROTECT` would prevent the parent from being deleted while dependent records exist.

This could be appropriate for some relationships, but it would make deleting a plant unnecessarily difficult when its tasks are intentionally part of the plant's lifecycle.

## Result

GardenOps will use cascade deletion for dependent data when the dependent object has no meaningful independent existence after its parent is removed.
