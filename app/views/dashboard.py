import flet as ft

from app.components.financial_chart import FinancialChart
from app.components.dashboard_header import DashboardHeader
from app.components.recent_transactions import RecentTransactions
from app.components.summary_card import SummaryCard

from app.theme import colors


class DashboardView:

    def __init__(self, controller):

        self.controller = controller

        # Estadísticas
        dashboard = controller.get_dashboard_data()

        balance = dashboard["balance"]
        income = dashboard["income"]
        expenses = dashboard["expenses"]

        transaction_count = dashboard["transaction_count"]
        average_amount = dashboard["average_amount"]
        max_expense = dashboard["max_expense"]

        latest_transactions = dashboard["latest_transactions"]
        monthly_totals = dashboard["monthly_totals"]

        self.content = ft.Container(

            expand=True,

            padding=30,

            bgcolor=colors.BACKGROUND,

            content=ft.Column(

                spacing=25,

                scroll=ft.ScrollMode.AUTO,

                controls=[

                    DashboardHeader().build(),


                    # ==========================
                    # Tarjetas principales
                    # ==========================

                    ft.ResponsiveRow(

                        spacing=20,

                        run_spacing=20,

                        controls=[

                            ft.Container(

                                col={
                                    "xs": 12,
                                    "md": 4,
                                },

                                content=SummaryCard(
                                    title="Balance",
                                    value=f"RD$ {balance:,.2f}",
                                    icon=ft.Icons.ACCOUNT_BALANCE_WALLET,
                                    icon_color=colors.PRIMARY,
                                    subtitle="Balance disponible",
                                ).build(),
                            ),

                            ft.Container(

                                col={
                                    "xs": 12,
                                    "md": 4,
                                },

                                content=SummaryCard(
                                    title="Ingresos",
                                    value=f"RD$ {income:,.2f}",
                                    icon=ft.Icons.TRENDING_UP,
                                    icon_color=colors.SUCCESS,
                                    subtitle="Total de ingresos",
                                ).build(),
                            ),

                            ft.Container(

                                col={
                                    "xs": 12,
                                    "md": 4,
                                },

                                content=SummaryCard(
                                    title="Gastos",
                                    value=f"RD$ {expenses:,.2f}",
                                    icon=ft.Icons.TRENDING_DOWN,
                                    icon_color=colors.ERROR,
                                    subtitle="Total de gastos",
                                ).build(),
                            ),

                        ],
                    ),


                    # ==========================
                    # Tarjetas secundarias
                    # ==========================

                    ft.ResponsiveRow(

                        spacing=20,

                        run_spacing=20,

                        controls=[

                            ft.Container(

                                col={
                                    "xs": 12,
                                    "md": 4,
                                },

                                content=SummaryCard(
                                    title="Transacciones",
                                    value=str(transaction_count),
                                    icon=ft.Icons.RECEIPT_LONG,
                                    icon_color=colors.PRIMARY,
                                    subtitle="Movimientos registrados",
                                ).build(),
                            ),

                            ft.Container(

                                col={
                                    "xs": 12,
                                    "md": 4,
                                },

                                content=SummaryCard(
                                    title="Promedio",
                                    value=f"RD$ {average_amount:,.2f}",
                                    icon=ft.Icons.ANALYTICS,
                                    icon_color=colors.SECONDARY,
                                    subtitle="Promedio por movimiento",
                                ).build(),
                            ),

                            ft.Container(

                                col={
                                    "xs": 12,
                                    "md": 4,
                                },

                                content=SummaryCard(
                                    title="Mayor gasto",
                                    value=f"RD$ {max_expense:,.2f}",
                                    icon=ft.Icons.WARNING_AMBER,
                                    icon_color=colors.ERROR,
                                    subtitle="Gasto individual más alto",
                                ).build(),
                            ),

                        ],
                    ),

                    ft.Divider(),


                    # ==========================
                    # Gráfico + Transacciones
                    # ==========================

                    ft.ResponsiveRow(

                        spacing=20,

                        run_spacing=30,

                        controls=[

                            ft.Container(

                                col={
                                    "xs": 12,
                                    "lg": 7,
                                },

                                content=FinancialChart(
                                    monthly_totals=monthly_totals,
                                ).build(),
                            ),

                            ft.Container(

                                col={
                                    "xs": 12,
                                    "lg": 5,
                                },

                                content=RecentTransactions(
                                    transactions=latest_transactions,
                                ).build(),
                            ),

                        ],
                    ),

                ],
            ),
        )

    def build(self):

        return self.content