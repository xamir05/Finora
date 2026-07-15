import flet as ft

from app.views.dashboard import dashboard
from app.views.income import income
from app.views.expenses import expenses
from app.views.budgets import budgets
from app.views.reports import reports
from app.views.settings import settings


class AppController:
    def __init__(self):
        self.content = ft.Container(expand=True)

        self.routes = {
            "dashboard": dashboard,
            "income": income,
            "expenses": expenses,
            "budgets": budgets,
            "reports": reports,
            "settings": settings,
        }

    def navigate(self, route: str):
        view = self.routes.get(route)

        if view:
            self.content.content = view()