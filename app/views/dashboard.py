import flet as ft
from app.theme import colors


def dashboard():
    return ft.Container(
        expand=True,
        padding=30,
        content=ft.Text(
            "Dashboard",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=colors.TEXT_PRIMARY,
        ),
    )