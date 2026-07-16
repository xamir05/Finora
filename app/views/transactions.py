import flet as ft

from app.components.amount_field import AmountField
from app.components.category_dropdown import CategoryDropdown
from app.components.date_picker import DatePicker
from app.components.description_field import DescriptionField
from app.components.primary_button import PrimaryButton
from app.components.transaction_type_selector import TransactionTypeSelector
from app.models.transaction import Transaction

from app.theme import colors


class TransactionsView:

    def __init__(self, controller):

        self.transaction_type = TransactionTypeSelector()
        self.amount = AmountField()
        self.category = CategoryDropdown()
        self.date = DatePicker()
        self.description = DescriptionField()
        self.controller = controller

        self.content = ft.Container(
            padding=30,
            bgcolor=colors.BACKGROUND,

            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Text(
                        "Nueva Transacción",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=colors.TEXT_PRIMARY,
                    ),

                    self.transaction_type.get_control(),

                    self.amount.get_control(),  #type: ignore

                    self.category.get_control(),

                    self.date.get_control(),

                    self.description.get_control(),

                    PrimaryButton(
                        text="Guardar",
                        on_click=self.save_transaction,
                    ),
                ],
            ),
        )

    def save_transaction(self, e):

        transaction = Transaction(
            amount=self.amount.get_value(),
            transaction_type=self.transaction_type.get_value(),
            category=self.category.get_value(),
            description=self.description.get_value(),
            date=self.date.get_value(),
        )

        saved = self.controller.create_transaction(transaction)

        print(f"Transacción guardada: {saved.id}")

    def build(self):
        return self.content

def transactions(controller):
    return TransactionsView(controller).build()
