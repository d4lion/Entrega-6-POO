import flet as ft

from page.Page import Page
from Database import Context


def main(page: ft.Page):
    DatabaseContext = Context()
    SPA = Page(DatabaseContext)

    page.add(SPA)

    SPA.table.update_table()


ft.app(main)
