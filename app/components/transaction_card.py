import flet as ft

from app.models.transaction import Transaction
from app.enums.transaction_type import TransactionType
from app.theme import colors


class TransactionCard:

    def __init__(self, transaction: Transaction):

        self.transaction = transaction

    def build(self):

        icon = (
            ft.Icons.ARROW_DOWNWARD
            if self.transaction.transaction_type == TransactionType.INCOME
            else ft.Icons.ARROW_UPWARD
        )

        icon_color = (
            colors.SUCCESS
            if self.transaction.transaction_type == TransactionType.INCOME
            else colors.ERROR
        )

        amount = f"RD$ {float(self.transaction.amount):,.2f}"

        return ft.Container(
            bgcolor=colors.SURFACE,
            border_radius=12,
            padding=15,

            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                controls=[

                    ft.Row(
                        spacing=15,

                        controls=[

                            ft.Icon(
                                icon,
                                color=icon_color,
                                size=28,
                            ),

                            ft.Column(
                                spacing=3,
                                alignment=ft.MainAxisAlignment.CENTER,

                                controls=[

                                    ft.Text(
                                        self.transaction.category,
                                        weight=ft.FontWeight.BOLD,
                                        color=colors.TEXT_PRIMARY,
                                    ),

                                    ft.Text(
                                        self.transaction.description,
                                        color=colors.TEXT_SECONDARY,
                                        size=13,
                                    ),

                                    ft.Text(
                                        self.transaction.date.strftime("%d/%m/%Y"),
                                        size=12,
                                        color=colors.TEXT_SECONDARY,
                                    ),
                                ],
                            ),
                        ],
                    ),

                    ft.Text(
                        amount,
                        weight=ft.FontWeight.BOLD,
                        color=icon_color,
                    ),
                ],
            ),
        )