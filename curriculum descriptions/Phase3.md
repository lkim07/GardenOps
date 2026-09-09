Phase 3 — Database Modeling & Relationships 

Now, I have these core models:

User (Django built-in)
 │
 ├───────────────┐
 │               │
 ▼               ▼
GardenMembership  Comment
 │               │
 ▼               ▼
Garden ───────── Task
 │                │
 └── Plant ───────┘
 │
 └── Activity

More specifically:

3.1 Garden
Garden
├── name
└── description

3.2 Plant
Plant
├── garden
├── name
└── description

One Garden → many Plants.

3.3 Garden Membership + Roles
Garden ←→ User
       │
       └── GardenMembership
             ├── role
             └── joined_at

Roles:

OWNER
MEMBER
VIEWER

This gives the foundation for the permission system I'll implement later.

3.4 Task
Task
├── garden
├── plant (optional)
├── title
├── description
├── assignee
├── status
├── due_date
├── created_at
└── updated_at

Status:

TODO
IN_PROGRESS
DONE

3.5 Task → Plant

I decided that:
    If a Plant is deleted, its associated Tasks should also be deleted.

So:

plant = models.ForeignKey(
    Plant,
    on_delete=models.CASCADE,
    ...
)

while plant itself remains optional because GardenOps can have garden-level tasks.

3.6 Task → Comment
Task
 │
 └── Comments
      ├── author
      ├── content
      ├── created_at
      └── updated_at

I tested:

Task → comments
User → comments
comment creation
comment editing
timestamps
CASCADE deletion

3.7 Garden → Activity

Finally:

Garden
 │
 └── Activity
      ├── user
      ├── action
      ├── description
      └── created_at

I tested:

plant activity
task creation activity
task completion activity
comment activity
chronological ordering
Garden → activities
User → activities

So this isn't just a collection of models, I've actually tested the relationships through Django ORM.

One important thing I deliberately haven't done yet

I'm manually creating Activity objects:

Activity.objects.create(...)


I don't want to implement automatic activity generation inside the model yet.

Later, when I build the API, I'll make the application do something like:

User
 │
 ▼
POST /api/tasks/
 │
 ├── Create Task
 │
 └── Create Activity

and:

User
 │
 ▼
PATCH /api/tasks/5/
 │
 ├── Change status → DONE
 │
 └── Create "COMPLETED_TASK" Activity

That separation is useful because I'm learning database modeling first and application/API behavior later.


Phase 3 overall assessment

I have learned several genuinely important Django/database concepts:

Concept	GardenOps implementation
One-to-many	Garden → Plant
One-to-many	Garden → Task
One-to-many	Plant → Task
Many-to-many	Garden ↔ User
Through model	GardenMembership
Roles	Owner / Member / Viewer
Foreign keys	Task, Comment, Activity
Optional relationship	Task → Plant
CASCADE	Plant → Task, Task → Comment
SET_NULL	Task → Assignee
Choices	Task Status / Membership Role / Activity Action
Reverse relationships	garden.tasks, task.comments, etc.
Timestamps	created_at, updated_at
ORM querying	filter, get, exclude, order_by, etc.
Database migrations	makemigrations / migrate





Next: Phase 4 — Django REST Framework


So far I've mostly interacted with GardenOps like this:

Python shell
      ↓
Django ORM
      ↓
PostgreSQL

Now I'll build:

React
  │
  │ HTTP / JSON
  ▼
Django REST Framework
  │
  ▼
Django ORM
  │
  ▼
PostgreSQL

For example, eventually a frontend will be able to request:

GET /api/gardens/

and receive:

[
  {
    "id": 1,
    "name": "Backyard Garden",
    "description": "Our family garden"
  }
]

Or:

GET /api/gardens/1/tasks/

and receive the garden's tasks.

I'll learn:

4.1 Install/configure Django REST Framework
4.2 Understand serializers
4.3 Create a Garden serializer
4.4 Create API views
4.5 Configure URL routing
4.6 Build Garden CRUD endpoints
4.7 Test APIs with the DRF Browsable API
4.8 Test APIs with HTTP requests
4.9 Serialize relationships
4.10 Build Plant endpoints
4.11 Build Task endpoints
4.12 Build Comment endpoints
4.13 Build Activity endpoints
4.14 API validation and error handling
4.15 API structure/refactoring