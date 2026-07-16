# Project Rules

## Architecture

The project follows a layered architecture.

Views never access the database.

Controllers never contain business logic.

Services contain business rules.

Repositories only communicate with SQLAlchemy.

---

## Coding Style

- Type hints required.
- Small functions.
- Reusable components.
- One responsibility per class.

---

## Git

Every feature must:

- Compile
- Pass tests
- Be committed