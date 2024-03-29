import flet as ft
import gpio_scripts.test_led as test_led


def main(page: ft.Page):
    page.title = "test flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def lit(e):
        test_led.lit()

    def blink(e):
        test_led.blink()

    page.add(
        ft.Row(
            [
                ft.ElevatedButton("lit", on_click=lit),
                ft.ElevatedButton("blink", on_click=blink),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


def app_close(page: ft.Page):
    page.window_destroy()


if __name__ == '__main__':
    ft.app(target=main)
    # ft.app(target=main, view=ft.WEB_BROWSER)
