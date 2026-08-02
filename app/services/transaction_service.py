from app.models.transaction import Transaction

from app.repositories.transaction_repository import TransactionRepository
from decimal import Decimal

class TransactionService:

    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def create_transaction(self, transaction: Transaction) -> Transaction:
        return self.repository.create(transaction)

    def get_transactions(self) -> list[Transaction]:
        return self.repository.get_all()

    def get_latest_transactions(self,limit: int = 20)   ->  list[Transaction]:
        return self.repository.get_latest(limit)

    def update_transaction(self, transaction: Transaction) -> Transaction:
        return self.repository.update(transaction)


    def delete_transaction(self, transaction: Transaction) -> None:
        self.repository.delete(transaction)


    def get_transaction_by_id(self, transaction_id: int) -> Transaction | None:
        return self.repository.get_by_id(transaction_id)

    def get_total_income(self) -> Decimal:
        return self.repository.get_total_income()

    def get_total_expenses(self) -> Decimal:
        return self.repository.get_total_expenses()

    def get_balance(self) -> Decimal:
        return self.repository.get_balance()

    def count_transactions(self) -> int:

        return self.repository.count_transactions()

    def get_average_amount(self) -> float:

        return self.repository.get_average_amount()

    def get_max_expense(self) -> float:

        return self.repository.get_max_expense()