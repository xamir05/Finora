import flet as ft


def main(page: ft.Page):
    page.title = "Finora"

    page.window.width = 1200
    page.window.height = 800

    page.theme_mode = ft.ThemeMode.DARK

    page.add(
        ft.Text(
            "Bienvenido a Finora",
            size = 30,
            weight=ft.FontWeight.BOLD
        )
    )


ft.app(target=main)