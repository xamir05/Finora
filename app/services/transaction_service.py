from app.models.transaction import Transaction

from app.repositories.transaction_repository import TransactionRepository

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