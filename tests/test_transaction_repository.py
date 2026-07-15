from datetime import date
from decimal import Decimal

from app.database.database import SessionLocal
from app.models.enums import TransactionType
from app.models.transaction import Transaction
from app.repositories.transaction_repository import TransactionRepository
from app.database.init_db import init_database


def main():
    # Asegura que existan las tablas
    init_database()

    db = SessionLocal()

    repository = TransactionRepository(db)

    transaction = Transaction(
        amount=Decimal("25000.00"),
        transaction_type=TransactionType.INCOME,
        category="Salario",
        description="Pago mensual",
        date=date.today(),
    )

    saved_transaction = repository.create(transaction)

    print(f"ID: {saved_transaction.id}")
    print("Transacción guardada correctamente.")

    db.close()


if __name__ == "__main__":
    main()