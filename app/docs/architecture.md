# Finora - Architecture

## Overview

Finora is a desktop personal finance application built with Python and Flet.

The project follows a layered architecture to keep responsibilities separated, making the code easier to maintain, test and extend.

---

# Architecture

```
                Flet UI
                    │
                    ▼
             Controllers
                    │
                    ▼
               Services
                    │
                    ▼
            Repositories
                    │
                    ▼
         SQLAlchemy ORM
                    │
                    ▼
              SQLite Database
```

Each layer has a single responsibility.

---

# Project Structure

```
app/
│
├── assets/
├── components/
├── controllers/
├── core/
├── database/
├── exceptions/
├── layouts/
├── models/
├── repositories/
├── services/
├── theme/
├── views/
```

---

# Layers

## Views

Responsible for:

- Displaying information.
- Receiving user input.
- Calling controllers.

Views never access the database directly.

---

## Controllers

Responsible for:

- Receiving actions from the UI.
- Calling the appropriate service.
- Returning the result to the interface.

Controllers do not contain business logic.

---

## Services

Responsible for business rules.

Examples:

- Validate transaction amount.
- Validate categories.
- Calculate balances.
- Validate dates.

Services never communicate directly with the UI.

---

## Repositories

Responsible for data persistence.

Repositories communicate with SQLAlchemy and SQLite.

They contain no business rules.

---

## Database

Persistence layer.

Current database:

- SQLite

ORM:

- SQLAlchemy 2.0

---

# Dependency Injection

All application dependencies are created in:

```

app/core/dependencies.py

```

This centralizes object creation and avoids coupling between layers.

---

# Repository Pattern

Finora uses the Repository Pattern.

A generic BaseRepository contains common CRUD operations.

```

BaseRepository
│
├── create()
├── get_all()
├── get_by_id()
├── update()
└── delete()

```

Specific repositories inherit from it.

Example:

```

TransactionRepository(BaseRepository)

```

---

# Exception System

Custom exceptions are used to separate application errors.

Current exceptions:

- ValidationException
- DatabaseException
- NotFoundException

All exceptions inherit from:

```

FinoraException

```

---

# Design Principles

The project follows these principles:

- Single Responsibility Principle (SRP)
- Dependency Injection
- Repository Pattern
- Layered Architecture
- Separation of Concerns

---

# Current Technologies

- Python 3.14
- Flet
- SQLAlchemy 2.0
- SQLite

---

# Future Improvements

Planned features:

- Budgets
- Financial goals
- Charts
- Statistics
- Reports
- CSV/PDF export
- User settings
- Theme customization

---

# Development Philosophy

Every new feature follows this workflow:

1. Design
2. Repository
3. Service
4. Controller
5. Test
6. UI Integration
7. Git Commit

This ensures that every feature is fully implemented and tested before moving to the next one.