import flet as ft
from app.theme import colors


def StatCard(
    title: str,
    value: str,
    icon: str,
    color: str,
):
    return ft.Container(
        width=250,
        height=140,
        bgcolor=colors.SURFACE,
        border_radius=15,
        padding=20,
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Icon(
                    icon,
                    color=color,
                    size=32,
                ),
                ft.Text(
                    title,
                    size=16,
                    weight=ft.FontWeight.W_500,
                    color=colors.TEXT_PRIMARY,
                ),
                ft.Text(
                    value,
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=colors.TEXT_PRIMARY,
                ),
            ],
        ),
    )