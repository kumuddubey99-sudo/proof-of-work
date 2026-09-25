import flet as ft


def credit_transactions_page(page, open_dashboard=None):

    transaction_id = ft.TextField(
        label="Transaction ID",
        value="Auto",
        read_only=True
    )

    customer = ft.TextField(
        label="Customer ID / Customer Name"
    )

    transaction_date = ft.TextField(
        label="Transaction Date"
    )

    due_date = ft.TextField(
        label="Due Date"
    )

    amount = ft.TextField(
        label="Total Amount"
    )

    payment_status = ft.Dropdown(
        label="Payment Status",
        options=[
            ft.dropdown.Option("Pending"),
            ft.dropdown.Option("Paid"),
            ft.dropdown.Option("Overdue")
        ]
    )

    notes = ft.TextField(
        label="Notes",
        multiline=True
    )

    # -------------------------
    # Buttons
    # -------------------------

    def save(e):
        print("Saved")

    def update(e):
        print("Updated")

    def clear(e):

        customer.value = ""
        transaction_date.value = ""
        due_date.value = ""
        amount.value = ""
        payment_status.value = None
        notes.value = ""

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

    def update_transaction(e):
        print("Transaction Updated")

    def delete_transaction(e):
        print("Transaction Deleted")

    def open_transaction(e):

        details_dialog.title = ft.Text("Transaction Details")

        details_dialog.content = ft.Column(
            tight=True,
            controls=[
                ft.Text("Transaction ID : TR001"),
                ft.Text("Customer ID : C001"),
                ft.Text("Customer Name : Rahul"),
                ft.Text("Transaction Date : 10-07-2026"),
                ft.Text("Due Date : 20-07-2026"),
                ft.Text("Total Amount : ₹2500"),
                ft.Text("Payment Status : Pending"),
                ft.Text("Notes : Grocery Items")
            ]
        )

        details_dialog.actions = [

            ft.ElevatedButton(
                "Update",
                on_click=update_transaction
            ),

            ft.ElevatedButton(
                "Delete",
                bgcolor="red",
                color="white",
                on_click=delete_transaction
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
    # View All Transactions
    # -------------------------

    table = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("Transaction ID")),
            ft.DataColumn(ft.Text("Customer")),
            ft.DataColumn(ft.Text("Amount")),
            ft.DataColumn(ft.Text("Status"))

        ],

        rows=[

            ft.DataRow(

                cells=[

                    ft.DataCell(

                        ft.TextButton(
                            "TR001",
                            on_click=open_transaction
                        )

                    ),

                    ft.DataCell(ft.Text("Rahul")),

                    ft.DataCell(ft.Text("₹2500")),

                    ft.DataCell(ft.Text("Pending"))

                ]

            ),

            ft.DataRow(

                cells=[

                    ft.DataCell(

                        ft.TextButton(
                            "TR002",
                            on_click=open_transaction
                        )

                    ),

                    ft.DataCell(ft.Text("Amit")),

                    ft.DataCell(ft.Text("₹4200")),

                    ft.DataCell(ft.Text("Paid"))

                ]

            )

        ]

    )

    return ft.Column(

        scroll="auto",

        controls=[

            ft.Text(
                "Credit Transactions",
                size=25,
                weight=ft.FontWeight.BOLD
            ),

            ft.Divider(),

            transaction_id,

            customer,

            transaction_date,

            due_date,

            amount,

            payment_status,

            notes,

            ft.Row(

                controls=[

                    ft.ElevatedButton(
                        "Save",
                        on_click=save
                    ),

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
                "View All Credit Transactions",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            table

        ]

    )