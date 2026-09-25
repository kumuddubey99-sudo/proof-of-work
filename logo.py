import flet as ft


def app_logo():

    return ft.Row(

        spacing=10,

        vertical_alignment=ft.CrossAxisAlignment.CENTER,

        controls=[

            ft.Image(
                src="assets/logo.png",
                width=50,
                height=50,
                fit=ft.ImageFit.CONTAIN
            ),

            ft.Column(

                spacing=0,

                controls=[

                    ft.Text(
                        "Udhaar Management System",
                        size=24,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(
                        "Udhaar Management for Shopkeepers",
                        size=12,
                        color=ft.Colors.GREY_700
                    )

                ]

            )

        ]

    )