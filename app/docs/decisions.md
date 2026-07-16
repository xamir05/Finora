# Technical Decisions

---

## Decision 001

### Use Flet instead of PySide6

Reason:

- Easier deployment.
- Better Python integration.
- Simpler UI development.
- Suitable for portfolio projects.

---

## Decision 002

### Use SQLAlchemy instead of raw SQLite

Reason:

- Better abstraction.
- ORM support.
- Easier migrations.
- Cleaner code.

---

## Decision 003

### Implement Repository Pattern

Reason:

- Decouples persistence from business logic.
- Improves maintainability.
- Makes testing easier.

---

## Decision 004

### Use Dependency Injection

Reason:

- Reduces coupling.
- Easier object management.
- Improves scalability.

---

## Decision 005

### Introduce BaseRepository

Reason:

Avoid duplicated CRUD implementations across repositories.