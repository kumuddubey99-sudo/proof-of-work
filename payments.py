import flet as ft


def payments_page(page, open_dashboard=None):

    # Payment Form


    payment_id = ft.TextField(
        label="Payment ID",
        value="Auto",
        read_only=True
    )

    transaction_id = ft.TextField(
        label="Transaction ID"
    )

    customer_id = ft.TextField(
        label="Customer ID"
    )

    payment_amount = ft.TextField(
        label="Payment Amount"
    )

    payment_date = ft.TextField(
        label="Payment Date"
    )

    payment_method = ft.Dropdown(
        label="Payment Method",
        options=[
            ft.dropdown.Option("Cash"),
            ft.dropdown.Option("UPI"),
            ft.dropdown.Option("Card")
        ]
    )

    reference_id = ft.TextField(
        label="Reference ID"
    )

    payment_status = ft.Dropdown(
        label="Payment Status",
        options=[
            ft.dropdown.Option("Paid"),
            ft.dropdown.Option("Pending")
        ]
    )



    # Buttons


    def save(e):
        print("Payment Saved")

    def update(e):
        print("Payment Updated")

    def clear(e):

        transaction_id.value = ""
        customer_id.value = ""
        payment_amount.value = ""
        payment_date.value = ""
        payment_method.value = None
        reference_id.value = ""
        payment_status.value = None

        page.update()


    # Payment Details Dialog


    details_dialog = ft.AlertDialog(
        modal=True
    )

    def close_dialog(e):
        details_dialog.open = False
        page.update()

    def update_payment(e):
        print("Payment Updated")

    def delete_payment(e):
        print("Payment Deleted")

    def open_payment(e):

        details_dialog.title = ft.Text("Payment Details")

        details_dialog.content = ft.Column(
            tight=True,
            controls=[
                ft.Text("Payment ID : P001"),
                ft.Text("Transaction ID : TR001"),
                ft.Text("Customer ID : C001"),
                ft.Text("Payment Amount : ₹1000"),
                ft.Text("Payment Date : 15-07-2026"),
                ft.Text("Payment Method : UPI"),
                ft.Text("Reference ID : REF123"),
                ft.Text("Payment Status : Paid")
            ]
        )

        details_dialog.actions = [

            ft.ElevatedButton(
                "Update",
                on_click=update_payment
            ),

            ft.ElevatedButton(
                "Delete",
                bgcolor="red",
                color="white",
                on_click=delete_payment
            ),

            ft.ElevatedButton(
                "Close",
                on_click=close_dialog
            )

        ]

        page.dialog = details_dialog
        details_dialog.open = True
        page.update()


    # View All Payments


    payment_table = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("Payment ID")),

            ft.DataColumn(ft.Text("Transaction ID")),

            ft.DataColumn(ft.Text("Customer ID")),

            ft.DataColumn(ft.Text("Amount")),

            ft.DataColumn(ft.Text("Payment Date")),

            ft.DataColumn(ft.Text("Payment Method")),

            ft.DataColumn(ft.Text("Status"))

        ],

        rows=[

            ft.DataRow(

                cells=[

                    ft.DataCell(
                        ft.TextButton(
                            "P001",
                            on_click=open_payment
                        )
                    ),

                    ft.DataCell(ft.Text("TR001")),

                    ft.DataCell(ft.Text("C001")),

                    ft.DataCell(ft.Text("₹1000")),

                    ft.DataCell(ft.Text("15-07-2026")),

                    ft.DataCell(ft.Text("UPI")),

                    ft.DataCell(ft.Text("Paid"))

                ]

            ),

            ft.DataRow(

                cells=[

                    ft.DataCell(
                        ft.TextButton(
                            "P002",
                            on_click=open_payment
                        )
                    ),

                    ft.DataCell(ft.Text("TR002")),

                    ft.DataCell(ft.Text("C002")),

                    ft.DataCell(ft.Text("₹2500")),

                    ft.DataCell(ft.Text("16-07-2026")),

                    ft.DataCell(ft.Text("Cash")),

                    ft.DataCell(ft.Text("Pending"))

                ]

            )

        ]

    )


    # Page


    return ft.Column(

        scroll="auto",

        controls=[

            ft.Text(
                "Payments",
                size=25,
                weight=ft.FontWeight.BOLD
            ),

            ft.Divider(),

            payment_id,

            transaction_id,

            customer_id,

            payment_amount,

            payment_date,

            payment_method,

            reference_id,

            payment_status,

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
                "View All Payments",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            payment_table

        ]

    )