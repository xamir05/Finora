import flet as ft

from app.components.stat_card import StatCard


def main(page: ft.Page):

    page.title = "Finora"

    page.theme_mode = ft.ThemeMode.DARK

    page.bgcolor = "#111827"

    page.window.width = 1200
    page.window.height = 800

    page.add(
        ft.Row(
            spacing=20,
            controls=[
                StatCard(
                    "Saldo",
                    "RD$25,430",
                    ft.Icons.ACCOUNT_BALANCE_WALLET,
                    "#4CAF50",
                ),
                StatCard(
                    "Ingresos",
                    "RD$40,000",
                    ft.Icons.TRENDING_UP,
                    "#2196F3",
                ),
                StatCard(
                    "Gastos",
                    "RD$14,570",
                    ft.Icons.TRENDING_DOWN,
                    "#F44336",
                ),
            ],
        )
    )


ft.run(main)