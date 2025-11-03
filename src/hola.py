import flet as ft
import time

def main(page: ft.Page):
    mi_texto = ft.Text("¡Hola mundo!", color="orange", size=40)
    page.controls.append(mi_texto)
    page.update()

    mi_otro_texto = ft.Text()
    page.add(mi_otro_texto)

    for i in range(10, 0, -1):
        mi_otro_texto.value = f'Cuenta regresiva: {i}'
        page.update()
        time.sleep(0.5)
    
    page.add(ft.Text('BOOM!', color='red', size=32))
    page.update()

    page.add(
    ft.Row(
        controls=[
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("D")
            ]
        )
    )
    page.update()

ft.app(main)
