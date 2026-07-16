from app.core.dependencies import Dependencies
from app.database.init_db import init_database


def main():
    init_database()

    dependencies = Dependencies()

    transactions = (
        dependencies.transaction_controller.get_transactions()
    )

    print(f"Se encontraron {len(transactions)} transacciones:\n")

    for transaction in transactions:
        print(
            f"ID: {transaction.id} | "
            f"{transaction.category} | "
            f"{transaction.amount}"
        )


if __name__ == "__main__":
    main()