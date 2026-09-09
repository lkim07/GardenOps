from django.contrib import admin
from .models import Garden, GardenMembership, Plant, Task, Comment, Activity

# Register your models here.

admin.site.register(Garden)
admin.site.register(GardenMembership)
admin.site.register(Plant)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Activity)


# Phase 1   Django basics                 
# Phase 1A  Django Admin + Models        
# Phase 1B  Django ORM / CRUD            
# Phase 2   PostgreSQL + Docker          
# Phase 3   Database relationships    
#               ↓   
# Phase 4   Django REST Framework APIs
# Phase 5   React + TypeScript frontend
# Phase 6   Authentication + Roles
# Phase 7   Testing / QA
# Phase 8   Dockerize Django + React
# Phase 9   CI/CD with GitHub Actions
# Phase 10  AWS + Security + Deployment


# Phase 3.7 — Designing roles