import flet as ft

from app.components.dashboard_header import DashboardHeader
from app.components.summary_card import SummaryCard
from app.components.transaction_list import TransactionList

from app.theme import colors


class DashboardView:

    def __init__(self, controller):

        self.controller = controller

        balance = controller.get_balance()
        income = controller.get_total_income()
        expenses = controller.get_total_expenses()

        transaction_count = controller.count_transactions()
        average_amount = controller.get_average_amount()
        max_expense = controller.get_max_expense()

        latest_transactions = controller.get_latest_transactions(5)

        self.content = ft.Container(
            expand=True,
            padding=30,
            bgcolor=colors.BACKGROUND,

            content=ft.Column(
                spacing=25,
                scroll=ft.ScrollMode.AUTO,

                controls=[

                    DashboardHeader().build(),

                    ft.Row(
                        spacing=20,

                        controls=[

                            SummaryCard(
                                title="Balance",
                                value=f"RD$ {balance:,.2f}",
                                icon=ft.Icons.ACCOUNT_BALANCE_WALLET,
                                icon_color=colors.PRIMARY,
                                subtitle="Balance disponible",
                            ).build(),

                            SummaryCard(
                                title="Ingresos",
                                value=f"RD$ {income:,.2f}",
                                icon=ft.Icons.TRENDING_UP,
                                icon_color=colors.SUCCESS,
                                subtitle="Total de ingresos",
                            ).build(),

                            SummaryCard(
                                title="Gastos",
                                value=f"RD$ {expenses:,.2f}",
                                icon=ft.Icons.TRENDING_DOWN,
                                icon_color=colors.ERROR,
                                subtitle="Total de gastos",
                            ).build(),
                        ],
                    ),


                    ft.Row(
                        spacing=20,
                        controls=[

                            SummaryCard(
                                title="Transacciones",
                                value=str(transaction_count),
                                icon=ft.Icons.RECEIPT_LONG,
                                icon_color=colors.PRIMARY,
                                subtitle="Movimientos registrados",
                            ).build(),

                            SummaryCard(
                                title="Promedio",
                                value=f"RD$ {average_amount:,.2f}",
                                icon=ft.Icons.ANALYTICS,
                                icon_color=colors.SECONDARY,
                                subtitle="Promedio por movimiento",
                            ).build(),

                             SummaryCard(
                                title="Mayor gasto",
                                value=f"RD$ {max_expense:,.2f}",
                                icon=ft.Icons.WARNING_AMBER,
                                icon_color=colors.ERROR,
                                subtitle="Gasto individual más alto",
                            ).build(),

                            ft.Container(expand=True),

                        ],
                    ),



                    ft.Divider(),

                    ft.Text(
                        "Últimas transacciones",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=colors.TEXT_PRIMARY,
                    ),

                    ft.Container(
                        height=350,
                        content=ft.Column(

                            scroll=ft.ScrollMode.AUTO,

                            controls=[

                                TransactionList(
                                    transactions=latest_transactions
                                ).build(),
                            ],
                        ),
                    ),
                ],
            ),
        )

    def build(self):

        return self.content