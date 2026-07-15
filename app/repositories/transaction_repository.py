from sqlalchemy.orm import Session
from app.models.transaction import Transaction


class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(self, transaction: Transaction) -> Transaction:
        """
        Guarda una transacción en la base de datos.
        """
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction