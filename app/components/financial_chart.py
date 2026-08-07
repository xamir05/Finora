import flet as ft
import flet_charts as ftc

from app.theme import colors


class FinancialChart:
    
    def __init__(
            self,
            income: float,
            expenses: float,
            balance: float,
    ):
        self.income = income
        self.expenses = expenses
        self.balance = balance

    def build(self):

        return ft.Container(
            col={"xs":12, "lg":7},

            height=300,

            bgcolor=colors.SURFACE,

            border_radius=16,

            padding=20,

            content=ft.Column(

                controls=[

                    ft.Text(
                        "Resumen financiero",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=colors.TEXT_PRIMARY,
                    ),

                    ft.Divider(),

                    ft.Text(
                        "Aqui irá el grafico",
                        color=colors.TEXT_SECONDARY,
                    ),
                ],
            ),
        )