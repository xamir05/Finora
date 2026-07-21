from app.models.transaction import Transaction
from app.services.transaction_service import TransactionService


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