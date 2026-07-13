import flet as ft

from app.layouts.main_layout import main_layout
from app.theme import colors


def main(page: ft.Page):

    page.title = "Finora"

    page.theme_mode = ft.ThemeMode.DARK

    page.bgcolor = colors.BACKGROUND

    page.window.width = 1200
    page.window.height = 800

    page.add(
        main_layout()
    )


ft.run(main)