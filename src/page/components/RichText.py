import flet as ft


class GradientText(ft.Text):
    def __init__(self, text: str, text_size: float = 40, font_weight: ft.FontWeight = ft.FontWeight.BOLD):
        super().__init__()

        self.spans = [
            ft.TextSpan(
                f"{text}",
                ft.TextStyle(
                    size=text_size,
                    weight=font_weight,
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (0, 20), (150, 20), [
                                ft.Colors.RED, ft.Colors.YELLOW]
                        )
                    ),
                ),
            )
        ]
