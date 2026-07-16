from app.models.transaction import Transaction

from app.repositories.transaction_repository import TransactionRepository

class TransactionService:

    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def create_transaction(self, transaction: Transaction) -> Transaction:
        return self.repository.create(transaction)

    def get_transactions(self) -> list[Transaction]:
        return self.repository.get_all()