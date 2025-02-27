from flet import TextField as ftTextField
from flet import Icon, InputBorder


class TextField(ftTextField):
    def __init__(self, place_holder: str = "", max_len: int = 20, bd_color: str = "#eb8034",
                 suffix_icono: Icon = None, on_change_function=None, border_type: InputBorder = None):
        super().__init__()

        self.label = place_holder
        self.max_length = max_len
        self.border_color = bd_color
        self.suffix_icon = suffix_icono

        # On change event
        self.on_change = on_change_function
        self.border = border_type
