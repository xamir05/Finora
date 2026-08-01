import flet as ft

from app.components.amount_field import AmountField
from app.components.category_dropdown import CategoryDropdown
from app.components.date_picker import DatePicker
from app.components.description_field import DescriptionField
from app.components.primary_button import PrimaryButton
from app.components.transaction_list import TransactionList
from app.components.transaction_type_selector import TransactionTypeSelector
from decimal import Decimal

from app.models.transaction import Transaction

from app.theme import colors


class TransactionsView:


    def __init__(self, controller):

        self.controller = controller
        
        self.editing_transaction: Transaction | None = None
        self.transaction_type = TransactionTypeSelector()
        self.amount = AmountField()
        self.category = CategoryDropdown()
        self.date = DatePicker()
        self.description = DescriptionField()

        self.transactions_container = ft.Container(
            expand=True,
        )


        self.save_button = PrimaryButton(
            text="Guardar",
            on_click=self.save_transaction,
        )

        self.content = ft.Container(

            padding=30,
            bgcolor=colors.BACKGROUND,

            content=ft.Column(

                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,

                controls=[

                    ft.Text(
                        "Nueva Transacción",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=colors.TEXT_PRIMARY,
                    ),


                    self.transaction_type.get_control(),

                    self.amount.get_control(), 

                    self.category.get_control(),

                    self.date.get_control(),

                    self.description.get_control(),


                    self.save_button.get_control(),



                    ft.Divider(),


                    ft.Text(
                        "Últimas transacciones",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=colors.TEXT_PRIMARY,
                    ),


                    self.transactions_container,

                ],
            ),
        )


    def save_transaction(self, e):

        # Modo edición
        if self.editing_transaction:

            self.editing_transaction.amount = Decimal(
                str(self.amount.get_value())
            )

            self.editing_transaction.transaction_type = (
                self.transaction_type.get_value()
            )

            self.editing_transaction.category = (
                self.category.get_value() or "Otros"
            )

            self.editing_transaction.description = (
                self.description.get_value() or ""
            )

            self.editing_transaction.date = (
                self.date.get_value()
            )


            updated = self.controller.update_transaction(
                self.editing_transaction
            )


            print(
                f"Transacción actualizada: {updated.id}"
            )


        # Modo creación
        else:

            transaction = Transaction(

                amount=Decimal(
                    str(self.amount.get_value())
                ),

                transaction_type=self.transaction_type.get_value(),

                category=self.category.get_value() or "Otros",

                description=self.description.get_value() or "",

                date=self.date.get_value(),

            )


            saved = self.controller.create_transaction(
                transaction
            )


            print(
                f"Transacción guardada: {saved.id}"
            )


        self.clear_form()

        self.load_transactions()

        self.content.update()



    def load_transactions(self):

        transactions = (
            self.controller.get_latest_transactions()
        )


        print(
            f"Transacciones encontradas: {len(transactions)}"
        )


        self.transactions_container.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                TransactionList(
                    transactions=transactions,
                    on_edit=self.edit_transaction,
                    on_delete=self.delete_transaction,
                ).build()
            ],
        )

    def edit_transaction(self, transaction: Transaction):

        self.editing_transaction = transaction

        self.save_button.set_text("Actualizar")


        self.amount.set_value(float(transaction.amount))
        self.category.set_value(transaction.category)
        self.date.set_value(transaction.date)
        self.description.set_value(transaction.description)

        self.transaction_type.set_value(
        transaction.transaction_type
    )

        print(
            f"Editando transacción {transaction.id}"
        )

    def delete_transaction(self, transaction: Transaction):

        self.controller.delete_transaction(transaction)

        print(f"Eliminar transacción {transaction.id}")

        self.load_transactions()

        self.content.update()    


    def clear_form(self):

        self.editing_transaction = None

        self.amount.clear()

        self.category.clear()

        self.date.clear()

        self.description.clear()

        self.transaction_type.clear()

        self.save_button.set_text("Guardar")

    def build(self):

        return self.content