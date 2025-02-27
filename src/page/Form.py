import flet as ft

from .components.TextField import TextField
from .components.Button import Button
from .components.RichText import GradientText
from .Table import Table as TableDataType
from .interfaces.IDatabaseContext import Context as IContext


class Formulario(ft.Container):
    def __init__(self, DatabaseContext: IContext, Table: TableDataType):
        super().__init__()
        self.database = DatabaseContext
        self.table_data = Table

        # Configuraciones de frame
        self.col = 4

        # Inputs
        self.name = TextField(place_holder="Nombre")
        self.last_name = TextField(place_holder="Apellido")
        self.id = TextField(place_holder="Documento")
        self.phone = TextField(place_holder="Telefono")
        self.email = TextField(place_holder="Correo", max_len=50)

        # Buttons
        self.save = Button(text="Save", icon=ft.Icons.SAVE,
                           function_call=self.__create_user)

        self.delete = Button(text="Delete", icon=ft.Icons.DELETE,
                             function_call=self.__delete_user)

        self.update = Button(text="Update", icon=ft.Icons.UPDATE)

        # Buttons container
        self.buttons_container = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.save,
                self.delete,
                self.update
            ]
        )

        # Inputs container
        self.inputs_container = ft.Column(
            controls=[
                self.id,
                self.name,
                self.last_name,
                self.phone,
                self.email
            ]
        )

        # Contenedor de pagina
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                GradientText("Registro de datos personales"),
                self.inputs_container,
                self.buttons_container
            ]
        )

    def __create_user(self, e=None):
        name = self.name.value
        last_name = self.last_name.value
        id = self.id.value
        phone = self.phone.value
        email = self.email.value

        if not name or not id or not phone or not email:
            return

        try:
            self.database.create_new_user(id, name, email, phone, last_name)
        except e:
            raise e
        finally:
            self.clean_fields()
            self.table_data.update_table()

    def __delete_user(self, e=None):
        if self.table_data.selected_row is None:
            return

        try:
            self.database.delete_user(int(self.table_data.selected_row))
        except:
            raise "Error al eliminar usuario"
        finally:
            self.table_data.update_table()

    def clean_fields(self):
        self.name.value = ""
        self.name.update()
        self.last_name.value = ""
        self.last_name.update()
        self.id.value = ""
        self.id.update()
        self.phone.value = ""
        self.phone.update()
        self.email.value = ""
        self.email.update()
