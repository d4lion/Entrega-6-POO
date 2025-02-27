import flet as ft


class Button(ft.OutlinedButton):
    def __init__(self,  function_call=None, bg: str = "#d1732a", text: str = "", text_color: str = "#e8a36d", icon: ft.Icon = None, icon_color: str = "#cf6d21"):
        super().__init__()

        self.bgcolor = bg
        self.icon_color = icon_color
        self.text = text
        self.icon = icon

        self.style = ft.ButtonStyle(color=text_color)
        self.on_click = function_call
