import flet as ft

def main(page: ft.Page):
    page.tittle = "Contador de ejemplo de Flet"
    
    val = ft.TextField(value="0")
    vol = ft.TextField(value="1")

    def click_mas(e):
        val.value = str(int(val.value) + 1)
        page.update()

    def click_menos(e):
        val.value = str(int(val.value) - 1)
        page.update()
    
    def click_dividir(e):
        vol.value = str(float(vol.value) / 2)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=click_menos),
                ft.IconButton(ft.Icons.ADD, on_click=click_mas),
                val,
            ]
        )
    )

    page.add(
        ft.Row(
            [
                ft.IconButton(content=ft.Text("/", size=50), on_click=click_dividir),
                vol,
            ]
        )
    )

ft.app(main)
