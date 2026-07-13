import flet as ft

from app.theme import colors

def NavItem(icon, text):

    return ft.Container(
        border_radius=10,
        padding=10,
        content=ft.Row(
            spacing=15,
            controls=[
                ft.Icon(
                    icon,
                    color=colors.TEXT_SECONDARY,
                ),

                ft.Text(
                    text,
                    color=colors.TEXT_PRIMARY,
                    size=15,
                ),
            ],
        ),
    )