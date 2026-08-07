from app.models.transaction import Transaction
from app.services.transaction_service import TransactionService
from decimal import Decimal


class TransactionController:

    def __init__(self, service: TransactionService):
        self.service = service

    def create_transaction(self, transaction: Transaction) -> Transaction:
        return self.service.create_transaction(transaction)

    def get_transactions(self) -> list[Transaction]:
        return self.service.get_transactions()

    def get_latest_transactions(
        self,
        limit: int = 20,
    ) -> list[Transaction]:
        return self.service.get_latest_transactions(limit)

    def get_transaction_by_id(
        self,
        transaction_id: int,
    ) -> Transaction | None:
        return self.service.get_transaction_by_id(transaction_id)

    def update_transaction(self, transaction: Transaction) -> Transaction:
        return self.service.update_transaction(transaction)

    def delete_transaction(self, transaction: Transaction) -> None:
        self.service.delete_transaction(transaction)

    def get_total_income(self) -> Decimal:

        return self.service.get_total_income()


    def get_total_expenses(self) -> Decimal:

        return self.service.get_total_expenses()


    def get_balance(self) -> Decimal:

        return self.service.get_balance()

    def count_transactions(self) -> int:

        return self.service.count_transactions()

    def get_average_amount(self) -> float:

        return self.service.get_average_amount()

    def get_max_expense(self) -> float:

        return self.service.get_max_expense()

    def get_monthly_totals(self) -> list[dict]:

        return self.service.get_monthly_totals()

    def get_dashboard_data(self) -> dict:

        return {

            "balance": self.get_balance(),

            "income": self.get_total_income(),

            "expenses": self.get_total_expenses(),

            "transaction_count": self.count_transactions(),

            "average_amount": self.get_average_amount(),

            "max_expense": self.get_max_expense(),

            "latest_transactions": self.get_latest_transactions(5),

            "monthly_totals": self.get_monthly_totals(),

        }