import flet as ft
from app.theme import colors

def reports():
    return ft.Container(
        padding=30,
        content=ft.Text(
            "Reportes",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=colors.TEXT_PRIMARY,
        )
    )