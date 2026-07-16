from datetime import date
from decimal import Decimal

from app.core.dependencies import Dependencies
from app.database.init_db import init_database
from app.enums.transaction_type import TransactionType
from app.models.transaction import Transaction


def main():
    init_database()

    dependencies = Dependencies()

    transaction = Transaction(
        amount=Decimal("3500.00"),
        transaction_type=TransactionType.EXPENSE,
        category="Comida",
        description="Almuerzo",
        date=date.today(),
    )

    saved = dependencies.transaction_controller.create_transaction(
        transaction
    )

    print(saved.id)
    print(saved.category)


if __name__ == "__main__":
    main()