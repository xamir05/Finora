import flet as ft

from app.components.sidebar import sidebar
from app.views.dashboard import dashboard

from app.theme import colors


def main_layout():

    return ft.Row(
        expand=True,
        controls=[

            sidebar(),

            ft.Container(
                expand=True,
                bgcolor=colors.BACKGROUND,
                padding=30,
                content=dashboard(),
            ),

        ],
    )