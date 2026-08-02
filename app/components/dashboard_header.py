import flet as ft

from app.theme import colors


class DashboardHeader:

    def __init__(self):

        self.container = ft.Column(

            spacing=5,

            controls=[

                ft.Text(
                    "Dashboard",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=colors.TEXT_PRIMARY,
                ),

                ft.Text(
                    "Resumen general de tus finanzas",
                    color=colors.TEXT_SECONDARY,
                    size=15,
                ),
            ],
        )

    def build(self):

        return self.container