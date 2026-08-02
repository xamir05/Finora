import flet as ft

from app.views.dashboard import DashboardView
from app.views.income import income
from app.views.expenses import expenses
from app.views.budgets import budgets
from app.views.reports import reports
from app.views.settings import settings
from app.views.transactions import TransactionsView

from app.database.database import SessionLocal

from app.repositories.transaction_repository import TransactionRepository
from app.services.transaction_service import TransactionService
from app.controllers.transaction_controller import TransactionController


class AppController:

    def __init__(self):

        self.content = ft.Container(
            expand=True
        )

        db = SessionLocal()

        transaction_repository = TransactionRepository(db)

        transaction_service = TransactionService(
            transaction_repository
        )

        self.transaction_controller = TransactionController(
            transaction_service
        )

        self.routes = {
            "dashboard": DashboardView,
            "income": income,
            "expenses": expenses,
            "transactions": self.transactions_view,
            "budgets": budgets,
            "reports": reports,
            "settings": settings,
        }


    def transactions_view(self):

        view = TransactionsView(
            self.transaction_controller
        )

        view.load_transactions()

        return view.build()


    def navigate(self, route: str):

        view = self.routes.get(route)

        if not view:
            return

        if route == "dashboard":

            self.content.content = DashboardView(
                self.transaction_controller
            ).build()

        elif route == "transactions":

            self.content.content = self.transactions_view()

        else:
            self.content.content = view()

            self.content.update()