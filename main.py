import flet as ft

from app.controllers.app_controller import AppController
from app.layouts.main_layout import main_layout
from app.theme import colors
from app.database.init_db import init_database
from app.views.dashboard import DashboardView



def main(page: ft.Page):


    page.title = "Finora"

    page.theme_mode = ft.ThemeMode.DARK

    page.bgcolor = colors.BACKGROUND


    page.window.width = 1200
    page.window.height = 800


    init_database()


    controller = AppController()


    controller.content.content = DashboardView(
        controller.transaction_controller
    ).build()


    page.add(
        main_layout(controller)
    )


    page.update()



ft.run(
    main,
    assets_dir="assets",
)