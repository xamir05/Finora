import flet as ft

from app.components.sidebar import sidebar
from app.theme import colors


def main_layout(controller):

    return ft.Row(
        expand=True,
        controls=[
            sidebar(controller),

            ft.Container(
                expand=True,
                bgcolor=colors.BACKGROUND,
                content=controller.content,
            ),
        ],
    )