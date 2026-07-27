import flet as ft

from app.models.transaction import Transaction
from app.components.transaction_card import TransactionCard


class TransactionList:

    def __init__(
        self,
        transactions: list[Transaction],
        on_edit=None,
        on_delete=None,
    ):
        self.transactions = transactions
        self.on_edit = on_edit
        self.on_delete = on_delete

    def build(self):

        return ft.Column(
            spacing=10,
            controls=[
                TransactionCard(
                    transaction=transaction,
                    on_edit=self.on_edit,
                    on_delete=self.on_delete,
                ).build()
                for transaction in self.transactions
            ],
        )