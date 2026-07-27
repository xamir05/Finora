import flet as ft

from app.theme import colors


class DescriptionField:

    def __init__(self):

        self.field = ft.TextField(
            label="Descripción",
            hint_text="Ej. Pago de supermercado",
            multiline=True,
            min_lines=2,
            max_lines=3,
            border_radius=10,
            filled=True,
            bgcolor=colors.SURFACE,
            color=colors.TEXT_PRIMARY,
        )

    def get_control(self):
        return self.field

    def get_value(self):
        return self.field.value

    def set_value(self, value: str):

        self.field.value = value
        self.field.update()

    def clear(self):

        self.field.value = ""
        self.field.update()