import flet as ft
from language import languages

def login_page(page, selected_language, open_dashboard):

    username = ft.TextField(
        label=languages[selected_language]["username"],
        width=300
    )

    password = ft.TextField(
        label=languages[selected_language]["password"],
        password=True,
        width=300
    )

    role = ft.Dropdown(
        label=languages[selected_language]["login_as"],
        width=300,
        value="Admin",
        options=[
            ft.dropdown.Option("Admin"),
            ft.dropdown.Option("Staff"),
        ],
    )

    def login(e):
        # Database will be added later
        open_dashboard()

    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(
                languages[selected_language]["login"],
                size=25,
                weight=ft.FontWeight.BOLD,
            ),

            username,
            password,
            role,

            ft.ElevatedButton(
                text=languages[selected_language]["login"],
                on_click=login,
            ),
        ],
    )