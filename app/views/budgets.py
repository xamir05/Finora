import flet as ft
from app.theme import colors

def budgets():
    return ft.Container(
        padding=30,
        content=ft.Text(
            "Presupuestos",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=colors.TEXT_PRIMARY,
        )
    )