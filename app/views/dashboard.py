import flet as ft

from app.components.stat_card import StatCard
from app.theme import colors


def dashboard():

    return ft.Container(
        padding=30,
        content=ft.Column(
            spacing=25,
            controls=[

                ft.Text(
                    "Resumen financiero",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=colors.TEXT_PRIMARY,
                ),

                ft.Row(
                    spacing=20,
                    controls=[

                        StatCard(
                            "Saldo",
                            "RD$25,430",
                            ft.Icons.ACCOUNT_BALANCE_WALLET,
                            colors.SUCCESS,
                        ),

                        StatCard(
                            "Ingresos",
                            "RD$40,000",
                            ft.Icons.TRENDING_UP,
                            colors.PRIMARY,
                        ),

                        StatCard(
                            "Gastos",
                            "RD$14,570",
                            ft.Icons.TRENDING_DOWN,
                            colors.ERROR,
                        ),

                    ],
                ),
            ],
        ),
    )