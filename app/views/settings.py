import flet as ft
from app.theme import colors

def settings():
    return ft.Container(
        padding=30,
        content=ft.Text(
            "Configuración",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=colors.TEXT_PRIMARY,
        )
    )