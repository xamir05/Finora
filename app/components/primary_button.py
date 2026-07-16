import flet as ft

from app.theme import colors


def PrimaryButton(
    text: str,
    on_click=None,
    width: int = 220,
    icon=None,
):

    return ft.ElevatedButton(
        content=ft.Text(
            text,
            color="white",
        ),

        icon=icon,

        width=width,
        height=48,

        bgcolor=colors.PRIMARY,

        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(
                radius=10,
            ),
        ),

        on_click=on_click,
    )