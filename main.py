import flet as ft

from app.theme import colors
from app.views.dashboard import dashboard


def main(page: ft.Page):

    page.title = "Finora"

    page.theme_mode = ft.ThemeMode.DARK

    page.bgcolor = colors.BACKGROUND

    page.window.width = 1200
    page.window.height = 800


    page.add(
        dashboard()
    )


ft.run(main)