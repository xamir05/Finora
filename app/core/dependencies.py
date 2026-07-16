from app.database.database import SessionLocal
from app.repositories.transaction_repository import TransactionRepository
from app.services.transaction_service import TransactionService
from app.controllers.transaction_controller import TransactionController


class Dependencies:

    def __init__(self):
        self.db = SessionLocal()

        self.transaction_repository = TransactionRepository(self.db)

        self.transaction_service = TransactionService(
            self.transaction_repository
        )

        self.transaction_controller = TransactionController(
            self.transaction_service
        )