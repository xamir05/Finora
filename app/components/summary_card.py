import flet as ft

from app.theme import colors


class SummaryCard:

    def __init__(
        self,
        title: str,
        value: str,
        icon,
        icon_color: str,
        subtitle: str | None = None,
    ):

        controls = [

            ft.Row(

                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                controls=[

                    ft.Text(
                        title,
                        size=16,
                        color=colors.TEXT_SECONDARY,
                    ),

                    ft.Container(

                        bgcolor=icon_color,

                        border_radius=10,

                        padding=8,

                        content=ft.Icon(
                            icon,
                            color="white",
                            size=22,
                        ),
                    ),
                ],
            ),


            ft.Text(
                value,
                size=28,
                weight=ft.FontWeight.BOLD,
                color=colors.TEXT_PRIMARY,
            ),
        ]


        if subtitle:

            controls.append(

                ft.Text(
                    subtitle,
                    size=13,
                    color=colors.TEXT_SECONDARY,
                )
            )


        self.container = ft.Container(

            expand=True,

            bgcolor=colors.SURFACE,

            border_radius=16,

            padding=20,

            content=ft.Column(

                spacing=12,

                controls=controls,

            ),
        )


    def build(self):

        return self.container