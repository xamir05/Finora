import flet as ft

from app.enums.transaction_type import TransactionType
from app.theme import colors


class TransactionTypeSelector:

    def __init__(self):
        self.value = TransactionType.EXPENSE

        self.radio_group = ft.RadioGroup(
            value=self.value.value,
            content=ft.Row(
                controls=[
                    ft.Radio(
                        value=TransactionType.INCOME.value,
                        label="Ingreso",
                        fill_color=colors.SUCCESS,
                    ),
                    ft.Radio(
                        value=TransactionType.EXPENSE.value,
                        label="Gasto",
                        fill_color=colors.ERROR,
                    ),
                ],
                spacing=20,
            ),
        )

    def get_control(self):
        return self.radio_group

    def get_value(self) -> TransactionType:
        return TransactionType(self.radio_group.value)