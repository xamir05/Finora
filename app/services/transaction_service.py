from app.models.transaction import Transaction


class TransactionService:

    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def create_transaction(self, transaction: Transaction) -> Transaction:
        return self.repository.create(transaction)