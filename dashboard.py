import flet as ft
from language import languages


def dashboard_page(page, selected_language):

    dashboard = ft.Column(

        expand=True,

        controls=[

            ft.Text(
                languages[selected_language]["dashboard"],
                size=30,
                weight=ft.FontWeight.BOLD
            ),

            ft.Divider(),

            ft.Row(

                wrap=True,

                controls=[

                    create_card(
                        "Total Customers",
                        "0",
                        ft.Colors.LIGHT_BLUE
                    ),

                    create_card(
                        "Total Credit",
                        "₹0",
                        ft.Colors.LIGHT_GREEN
                    ),

                    create_card(
                        "Total Payments",
                        "₹0",
                        ft.Colors.ORANGE
                    ),

                    create_card(
                        "Outstanding",
                        "₹0",
                        ft.Colors.PINK
                    )

                ]

            ),

            ft.Divider(),

            ft.Text(
                "Recent Activity",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            ft.DataTable(

                columns=[

                    ft.DataColumn(ft.Text("Customer")),
                    ft.DataColumn(ft.Text("Transaction")),
                    ft.DataColumn(ft.Text("Amount")),
                    ft.DataColumn(ft.Text("Status"))

                ],

                rows=[]

            )

        ]

    )

    return dashboard



def create_card(title, value, color):

    return ft.Container(

        width=180,
        height=100,
        bgcolor=color,
        alignment=ft.alignment.center,

        content=ft.Column(

            alignment=ft.MainAxisAlignment.CENTER,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[

                ft.Text(
                    title,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    value,
                    size=25
                )

            ]

        )

    )