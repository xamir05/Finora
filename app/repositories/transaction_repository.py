from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository[Transaction]):

    def __init__(self, db: Session):
        super().__init__(db, Transaction)

    def get_latest(self, limit: int = 20) -> list[Transaction]:
        statement = (
            select(Transaction)  
            .order_by(Transaction.date.desc())
            .limit(limit)
        )

        return list(
            self.db.scalars(statement).all()
        )