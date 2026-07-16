import flet as ft

from datetime import date

from app.theme import colors


class DatePicker:

    def __init__(self):

        self.selected_date = date.today()

        self.picker = ft.DatePicker(
            on_change=self.change_date,
            on_dismiss=self.close_picker,
        )

        self.field = ft.TextField(
            label="Fecha",
            value=self.selected_date.strftime("%d/%m/%Y"),
            read_only=True,

            suffix_icon=ft.Icons.CALENDAR_MONTH,

            border_radius=10,
            filled=True,
            bgcolor=colors.SURFACE,
            color=colors.TEXT_PRIMARY,

            on_click=self.open_picker,
        )


    def open_picker(self, e):

        page = self.field.page

        if page:
            page.overlay.append(self.picker)

            self.picker.open = True
            page.update()


    def close_picker(self, e):
        self.picker.open = False


    def change_date(self, e):

        if e.control.value:

            self.selected_date = e.control.value.date()

            self.field.value = (
                self.selected_date.strftime("%d/%m/%Y")
            )

            self.field.update()


    def get_control(self):

        return self.field


    def get_value(self):

        return self.selected_date