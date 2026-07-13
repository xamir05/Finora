import flet as ft


from . import colors


def get_theme():

    return ft.Theme(
        color_scheme=colors.ColorScheme(
            primary=colors.PRIMARY,
            secondary=colors.SECONDARY,
            background=colors.BACKGROUND,
        )
    )