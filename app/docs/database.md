# Database

Current database:

SQLite

ORM:

SQLAlchemy 2.0

---

## Tables

### transactions

| Field | Type |
|--------|------|
| id | Integer |
| amount | Decimal |
| transaction_type | Enum |
| category | String |
| description | String |
| date | Date |
| created_at | DateTime |
| updated_at | DateTime |