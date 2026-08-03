import flet as ft

from app.components.transaction_list import TransactionList
from app.theme import colors


class RecentTransactions:

    def __init__(
        self,
        transactions,
        on_edit=None,
        on_delete=None,
    ):

        self.transactions = transactions
        self.on_edit = on_edit
        self.on_delete = on_delete


    def build(self):

        transaction_list = TransactionList(
            transactions=self.transactions,
            on_edit=self.on_edit,
            on_delete=self.on_delete,
        ).build()


        return ft.Container(

            bgcolor=colors.SURFACE,

            border_radius=16,

            padding=20,


            content=ft.Column(

                spacing=15,

                controls=[


                    ft.Text(
                        "Últimas transacciones",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=colors.TEXT_PRIMARY,
                    ),


                    ft.Divider(height=1),



                    ft.Container(

                        height=350,

                        content=ft.Column(

                            scroll=ft.ScrollMode.AUTO,

                            spacing=12,

                            controls=transaction_list.controls,

                        ),
                    ),
                ],
            ),
        )