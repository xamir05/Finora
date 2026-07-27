import flet as ft

from app.theme import colors


class AmountField:

    def __init__(self):

        self.field = ft.TextField(
            label="Monto",
            hint_text="0.00",

            prefix=ft.Text(
                "RD$",
                color=colors.TEXT_SECONDARY,
            ),

            keyboard_type=ft.KeyboardType.NUMBER,

            border_radius=10,
            filled=True,
            bgcolor=colors.SURFACE,
            color=colors.TEXT_PRIMARY,
        )

    def get_control(self):
        return self.field

    def get_value(self):

        if not self.field.value:
            return 0

        return float(self.field.value)

    def set_value(self, value: float):

        self.field.value = str(value)
        self.field.update()

    def clear(self):

        self.field.value = ""
        self.field.update()