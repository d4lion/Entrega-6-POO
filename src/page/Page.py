import flet as ft

from .Form import Formulario
from .Table import Table


class Page(ft.ResponsiveRow):
    def __init__(self, DatabaseContext):
        super().__init__(expand=True)

        self.table = Table(DatabaseContext)
        self.formulario = Formulario(DatabaseContext, self.table)

        self.table.set_form_context(self.formulario)

        self.controls = [
            self.formulario,
            self.table
        ]
