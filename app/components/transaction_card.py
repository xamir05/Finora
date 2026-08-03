import flet as ft

from app.models.transaction import Transaction
from app.enums.transaction_type import TransactionType
from app.theme import colors


class TransactionCard:

    def __init__(
        self,
        transaction: Transaction,
        on_edit=None,
        on_delete=None,
    ):

        self.transaction = transaction
        self.on_edit = on_edit
        self.on_delete = on_delete


    def build(self):

        is_income = (
            self.transaction.transaction_type
            == TransactionType.INCOME
        )


        icon = (
            ft.Icons.ARROW_DOWNWARD
            if is_income
            else ft.Icons.ARROW_UPWARD
        )


        color = (
            colors.SUCCESS
            if is_income
            else colors.ERROR
        )


        amount = (
            f"RD$ {float(self.transaction.amount):,.2f}"
        )


        return ft.Container(

            bgcolor=colors.BACKGROUND,

            border_radius=14,

            padding=15,

            border=ft.Border(
                left=ft.BorderSide(1, "#374151"),
                top=ft.BorderSide(1, "#374151"),
                right=ft.BorderSide(1, "#374151"),
                bottom=ft.BorderSide(1, "#374151"),
            ),


            content=ft.Row(

                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                controls=[


                    # Información izquierda
                    ft.Row(

                        spacing=15,

                        controls=[


                            ft.Container(

                                width=45,
                                height=45,

                                border_radius=50,

                                bgcolor=color,


                                content=ft.Icon(
                                    icon,
                                    color="white",
                                    size=22,
                                ),
                            ),



                            ft.Column(

                                spacing=4,

                                controls=[


                                    ft.Text(
                                        self.transaction.category,
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=colors.TEXT_PRIMARY,
                                    ),



                                    ft.Text(
                                        self.transaction.description
                                        if self.transaction.description
                                        else "Sin descripción",
                                        size=13,
                                        color=colors.TEXT_SECONDARY,
                                    ),



                                    ft.Text(
                                        self.transaction.date.strftime(
                                            "%d/%m/%Y"
                                        ),
                                        size=12,
                                        color=colors.TEXT_SECONDARY,
                                    ),

                                ],
                            ),
                        ],
                    ),



                    # Información derecha
                    ft.Column(

                        horizontal_alignment=ft.CrossAxisAlignment.END,

                        spacing=8,

                        controls=[


                            ft.Text(
                                amount,
                                size=17,
                                weight=ft.FontWeight.BOLD,
                                color=color,
                            ),



                            ft.Row(

                                spacing=0,

                                controls=[


                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        icon_color=colors.TEXT_SECONDARY,
                                        tooltip="Editar",
                                        on_click=lambda e:
                                        self.on_edit(self.transaction)
                                        if self.on_edit
                                        else None,
                                    ),



                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        icon_color=colors.ERROR,
                                        tooltip="Eliminar",
                                        on_click=lambda e:
                                        self.on_delete(self.transaction)
                                        if self.on_delete
                                        else None,
                                    ),

                                ],
                            ),

                        ],
                    ),

                ],
            ),
        )