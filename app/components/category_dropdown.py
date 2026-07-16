import flet as ft

from app.theme import colors


class CategoryDropdown:

    def __init__(self):

        self.dropdown = ft.Dropdown(
            label="Categoría",
            hint_text="Selecciona una categoría",
            border_radius=10,
            filled=True,
            bgcolor=colors.SURFACE,
            color=colors.TEXT_PRIMARY,
            options=[
                ft.dropdown.Option("Salario"),
                ft.dropdown.Option("Comida"),
                ft.dropdown.Option("Transporte"),
                ft.dropdown.Option("Entretenimiento"),
                ft.dropdown.Option("Otros"),
            ],
        )

    def get_control(self):
        return self.dropdown

    def get_value(self):
        return self.dropdown.value