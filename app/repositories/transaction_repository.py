from decimal import Decimal

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.enums.transaction_type import TransactionType
from app.models.transaction import Transaction
from app.repositories.base_repository import BaseRepository
from sqlalchemy import func, select

class TransactionRepository(BaseRepository[Transaction]):

    def __init__(self, db: Session):

        super().__init__(db, Transaction)

    def get_latest(
        self,
        limit: int = 20,
    ) -> list[Transaction]:

        statement = (
            select(Transaction)
            .order_by(Transaction.date.desc())
            .limit(limit)
        )

        return list(
            self.db.scalars(statement).all()
        )

    def get_total_income(self) -> Decimal:

        statement = select(
            func.sum(Transaction.amount)
        ).where(
            Transaction.transaction_type == TransactionType.INCOME
        )

        result = self.db.scalar(statement)

        return result or Decimal("0.00")

    def get_total_expenses(self) -> Decimal:

        statement = select(
            func.sum(Transaction.amount)
        ).where(
            Transaction.transaction_type == TransactionType.EXPENSE
        )

        result = self.db.scalar(statement)

        return result or Decimal("0.00")

    def get_balance(self) -> Decimal:

        return (
            self.get_total_income()
            - self.get_total_expenses()
        )

    def count_transactions(self) -> int:

        statement = select(
            func.count(Transaction.id)
        )

        return self.db.scalar(statement) or 0

    def get_average_amount(self) -> float:

        statement = select(
            func.avg(Transaction.amount)
        )

        average = self.db.scalar(statement)

        return float(average or 0)

    def get_max_expense(self) -> float:

         statement = select(
             func.max(Transaction.amount)
         ).where(
             Transaction.transaction_type == "EXPENSE"
         )

         maximum = self.db.scalar(statement)

         return float(maximum or 0)