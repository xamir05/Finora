import flet as ft

from app.theme import colors
from app.components.nav_item import NavItem


def sidebar():

    return ft.Container(
        width=250,
        bgcolor=colors.SURFACE,
        padding=20,

        content=ft.Column(
            spacing=15,

            controls=[

                ft.Text(
                    "FINORA",
                    size=26,
                    weight=ft.FontWeight.BOLD,
                    color=colors.TEXT_PRIMARY,
                ),

                ft.Divider(),

                NavItem(
                    ft.Icons.DASHBOARD,
                    "Dashboard"
                ),

                NavItem(
                    ft.Icons.ARROW_DOWNWARD,
                    "Ingresos"
                ),

                NavItem(
                    ft.Icons.ARROW_UPWARD,
                    "Gastos"
                ),

                NavItem(
                    ft.Icons.ACCOUNT_BALANCE,
                    "Presupuestos"
                ),

                NavItem(
                    ft.Icons.INSERT_CHART,
                    "Reportes"
                ),

                NavItem(
                    ft.Icons.SETTINGS,
                    "Configuración"
                ),

            ],
        ),
    )