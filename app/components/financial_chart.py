import flet as ft
import plotly.graph_objects as go
import os

from app.theme import colors


class FinancialChart:

    def __init__(
        self,
        monthly_totals: list[dict],
    ):

        self.monthly_totals = monthly_totals


    def build(self):

        months = []
        incomes = []
        expenses = []


        month_names = {
            "01": "Ene",
            "02": "Feb",
            "03": "Mar",
            "04": "Abr",
            "05": "May",
            "06": "Jun",
            "07": "Jul",
            "08": "Ago",
            "09": "Sep",
            "10": "Oct",
            "11": "Nov",
            "12": "Dic",
        }


        for data in self.monthly_totals:

            month_number = data["month"].split("-")[1]


            months.append(
                month_names[month_number]
            )


            incomes.append(
                float(data["income"])
            )


            expenses.append(
                float(data["expenses"])
            )


        fig = go.Figure()


        fig.add_trace(
            go.Bar(
                x=months,
                y=incomes,
                name="Ingresos",
                marker_color="#22C55E",
            )
        )


        fig.add_trace(
            go.Bar(
                x=months,
                y=expenses,
                name="Gastos",
                marker_color="#EF4444",
            )
        )


        fig.update_layout(

            barmode="group",

            template="plotly_dark",

            height=400,

            margin=dict(
                l=60,
                r=30,
                t=30,
                b=50,
            ),

            yaxis=dict(
                tickformat=",.0f",
            ),

        )


        os.makedirs(
            "assets/charts",
            exist_ok=True,
        )


        image_path = (
            "assets/charts/"
            "financial_chart.png"
        )


        fig.write_image(
            image_path,
            width=900,
            height=450,
        )


        return ft.Container(

            height=450,

            bgcolor=colors.SURFACE,

            border_radius=16,

            padding=20,


            content=ft.Column(

                controls=[


                    ft.Text(
                        "Flujo financiero mensual",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=colors.TEXT_PRIMARY,
                    ),


                    ft.Divider(),


                    ft.Image(
                        src="charts/financial_chart.png",
                        expand=True,
                    ),

                ],

            ),

        )