import flet as ft

from app.theme import colors


class PrimaryButton:

    def __init__(
        self,
        text: str,
        on_click=None,
        width: int = 220,
        icon=None,
    ):

        self.text_control = ft.Text(
            text,
            color="white",
        )

        self.button = ft.ElevatedButton(

            content=self.text_control,

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


    def get_control(self):

        return self.button


    def set_text(self, text: str):

        self.text_control.value = text
        self.text_control.update()