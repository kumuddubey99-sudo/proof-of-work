import flet as ft


def outstanding_balance_page(page, open_dashboard=None):

    # -------------------------
    # Outstanding Balance Form
    # -------------------------

    customer_id = ft.TextField(
        label="Customer ID"
    )

    transaction_id = ft.TextField(
        label="Transaction ID"
    )

    customer_name = ft.TextField(
        label="Customer Name"
    )

    total_due = ft.TextField(
        label="Total Due"
    )

    pending_amount = ft.TextField(
        label="Pending Amount"
    )

    last_updated = ft.TextField(
        label="Last Updated"
    )

    # -------------------------
    # Buttons
    # -------------------------

    def update(e):
        print("Outstanding Balance Updated")

    def clear(e):

        customer_id.value = ""
        transaction_id.value = ""
        customer_name.value = ""
        total_due.value = ""
        pending_amount.value = ""
        last_updated.value = ""

        page.update()

    # -------------------------
    # Details Dialog
    # -------------------------

    details_dialog = ft.AlertDialog(
        modal=True
    )

    def close_dialog(e):
        details_dialog.open = False
        page.update()

    def update_balance(e):
        print("Outstanding Balance Updated")

    def open_balance(e):

        details_dialog.title = ft.Text("Outstanding Balance Details")

        details_dialog.content = ft.Column(
            tight=True,
            controls=[

                ft.Text("Customer ID : C001"),

                ft.Text("Transaction ID : TR001"),

                ft.Text("Customer Name : Rahul"),

                ft.Text("Total Due : ₹5000"),

                ft.Text("Pending Amount : ₹2000"),

                ft.Text("Last Updated : 15-07-2026")

            ]
        )

        details_dialog.actions = [

            ft.ElevatedButton(
                "Update",
                on_click=update_balance
            ),

            ft.ElevatedButton(
                "Close",
                on_click=close_dialog
            )

        ]

        page.dialog = details_dialog
        details_dialog.open = True
        page.update()

    # -------------------------
    # View All Outstanding Balances
    # -------------------------

    balance_table = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("Customer ID")),

            ft.DataColumn(ft.Text("Transaction ID")),

            ft.DataColumn(ft.Text("Customer Name")),

            ft.DataColumn(ft.Text("Total Due")),

            ft.DataColumn(ft.Text("Pending Amount"))

        ],

        rows=[

            ft.DataRow(

                cells=[

                    ft.DataCell(

                        ft.TextButton(
                            "C001",
                            on_click=open_balance
                        )

                    ),

                    ft.DataCell(ft.Text("TR001")),

                    ft.DataCell(ft.Text("Rahul")),

                    ft.DataCell(ft.Text("₹5000")),

                    ft.DataCell(ft.Text("₹2000"))

                ]

            ),

            ft.DataRow(

                cells=[

                    ft.DataCell(

                        ft.TextButton(
                            "C002",
                            on_click=open_balance
                        )

                    ),

                    ft.DataCell(ft.Text("TR002")),

                    ft.DataCell(ft.Text("Amit")),

                    ft.DataCell(ft.Text("₹7000")),

                    ft.DataCell(ft.Text("₹1500"))

                ]

            )

        ]

    )

    # -------------------------
    # Page
    # -------------------------

    return ft.Column(

        scroll="auto",

        controls=[

            ft.Text(
                "Outstanding Balance",
                size=25,
                weight=ft.FontWeight.BOLD
            ),

            ft.Divider(),

            customer_id,

            transaction_id,

            customer_name,

            total_due,

            pending_amount,

            last_updated,

            ft.Row(

                controls=[

                    ft.ElevatedButton(
                        "Update",
                        on_click=update
                    ),

                    ft.ElevatedButton(
                        "Clear",
                        on_click=clear
                    )

                ]

            ),

            ft.Divider(),

            ft.Text(
                "View All Outstanding Balances",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            balance_table

        ]

    )