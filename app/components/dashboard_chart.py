import flet as ft

from app.theme import colors


class DashboardChart:

    def __init__(self):

        self.container = ft.Container(

            expand=True,

            bgcolor=colors.SURFACE,

            border_radius=16,

            padding=20,

            content=ft.Column(

                spacing=20,

                controls=[

                    ft.Text(
                        "Resumen financiero",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=colors.TEXT_PRIMARY,
                    ),

                    ft.Divider(height=1),

                    ft.Container(

                        expand=True,


                        content=ft.Column(

                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,

                            controls=[

                                ft.Icon(
                                    ft.Icons.INSERT_CHART,
                                    size=70,
                                    color=colors.SECONDARY,
                                ),

                                ft.Text(
                                    "Gráfico disponible próximamente",
                                    size=16,
                                    color=colors.TEXT_SECONDARY,
                                ),

                            ],
                        ),
                    ),
                ],
            ),
        )

    def build(self):

        return self.container