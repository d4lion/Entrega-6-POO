import flet as ft

from .components.TextField import TextField


class Table(ft.Container):
    def __init__(self, DatabaseContext) -> None:
        super().__init__()

        # Conexion con la base de datos
        self.database = DatabaseContext

        # Variables de control
        self.selected_row = None
        self.selected_row_data = []
        self.row_are_editable = False

        # Configuraciones del frame
        self.col = 8
        self.bgcolor = "#222222"

        # Search input
        self.search_input = TextField(place_holder="Buscar por nombre",
                                      suffix_icono=ft.Icons.SEARCH, border_type=ft.InputBorder.UNDERLINE)

        # Edit button
        self.edit_button = ft.IconButton(
            icon=ft.Icons.EDIT, icon_color="#eb8034", on_click=self.__edit_row)

        self.help_bar = ft.Container(
            padding=ft.padding.all(10),
            content=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.search_input,
                    self.edit_button
                ]
            )
        )

        # Data table
        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2, "orange"),
            border_radius=10,
            show_checkbox_column=True,

            # Configuraciones de la tabla
            columns=[
                ft.DataColumn(ft.Text("Cedula", weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("Nombre", weight="bold")),
                ft.DataColumn(ft.Text("Apellidos", weight="bold")),
                ft.DataColumn(ft.Text("Correo", weight="bold")),
                ft.DataColumn(ft.Text("Telefono", weight="bold"), numeric=True)
            ]
        )

        self.content = ft.Column(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        self.help_bar,
                        self.data_table
                    ]
                )
            ]
        )

    def update_table(self, e=None) -> None:
        self.data_table.rows = []

        try:
            for user in self.database.get_all_users():
                self.data_table.rows.append(
                    ft.DataRow(
                        on_select_changed=self.__get_selected_row,
                        cells=[
                            ft.DataCell(ft.Text(user[0])),
                            ft.DataCell(ft.Text(user[1])),
                            ft.DataCell(ft.Text(user[2])),
                            ft.DataCell(ft.Text(user[3])),
                            ft.DataCell(ft.Text(user[4])),
                        ]
                    )
                )
        except e:
            raise e
        finally:
            self.update()

    def __get_selected_row(self, e) -> int:
        if not e.control.selected:
            e.control.selected = True
            self.selected_row = e.control.cells[0].content.value
            self.row_are_editable = True
            self.selected_row_data = e.control.cells

        else:
            e.control.selected = False
            self.selected_row_data = []
            self.selected_row = None
            self.row_are_editable = False

        self.update()

    def __edit_row(self, e) -> list:
        if not self.row_are_editable:
            return

        data = []

        for cell in self.selected_row_data:
            data.append(cell.content.value)

        return data
