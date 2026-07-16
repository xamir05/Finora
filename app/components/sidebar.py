import flet as ft

from app.theme import colors
from app.components.nav_item import NavItem


def sidebar(controller):

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
                    "Dashboard",
                    on_click=lambda _: controller.navigate("dashboard"),
                ),

                NavItem(
                    ft.Icons.ARROW_DOWNWARD,
                    "Ingresos",
                    on_click=lambda _: controller.navigate("income"),
                ),

                NavItem(
                    ft.Icons.ARROW_UPWARD,
                    "Gastos",
                    on_click=lambda _: controller.navigate("expenses"),
                ),

                NavItem(
                    ft.Icons.RECEIPT_LONG,
                    "Transacciones",
                    on_click=lambda _: controller.navigate("transactions"),
                ),

                NavItem(
                    ft.Icons.ACCOUNT_BALANCE,
                    "Presupuestos",
                    on_click=lambda _: controller.navigate("budgets"),
                ),

                NavItem(
                    ft.Icons.INSERT_CHART,
                    "Reportes",
                    on_click=lambda _: controller.navigate("reports"),
                ),

                NavItem(
                    ft.Icons.SETTINGS,
                    "Configuración",
                    on_click=lambda _: controller.navigate("settings"),
                ),

            ],
        ),
    )