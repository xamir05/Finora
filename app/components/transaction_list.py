import flet as ft

from app.models.transaction import Transaction
from app.components.transaction_card import TransactionCard


class TransactionList:

    def __init__(self, transactions: list[Transaction]):
        self.transactions = transactions


    def build(self):

        return ft.Column(
            spacing=10,
            controls=[
                TransactionCard(transaction).build()
                for transaction in self.transactions
            ],
        )