import flet as ft

from .Form import Formulario
from .Table import Table


class Page(ft.ResponsiveRow):
    def __init__(self, DatabaseContext):
        super().__init__(expand=True)

        self.table = Table(DatabaseContext)

        self.controls = [
            Formulario(DatabaseContext, self.table),
            self.table
        ]
