import flet as ft


def customers_page(page, open_dashboard=None):



    # Customer Form

    customer_id = ft.TextField(
        label="Customer ID",
        value="Auto",
        read_only=True
    )

    customer_name = ft.TextField(
        label="Customer Name"
    )

    phone = ft.TextField(
        label="Phone Number"
    )

    alternate_phone = ft.TextField(
        label="Alternate Number"
    )

    email = ft.TextField(
        label="Email"
    )

    address = ft.TextField(
        label="Address",
        multiline=True
    )

    created_date = ft.TextField(
        label="Created Date"
    )

    updated_date = ft.TextField(
        label="Updated Date"
    )

    # Buttons

    def save(e):
        print("Customer Saved")

    def clear(e):

        customer_name.value = ""
        phone.value = ""
        alternate_phone.value = ""
        email.value = ""
        address.value = ""
        created_date.value = ""
        updated_date.value = ""

        page.update()


    # Customer Details Dialog


    details_dialog = ft.AlertDialog(
        modal=True
    )

    def close_dialog(e):
        details_dialog.open = False
        page.update()

    def update_customer(e):
        print("Customer Updated")

    def delete_customer(e):
        print("Customer Deleted")

    def open_customer(e):

        details_dialog.title = ft.Text("Customer Details")

        details_dialog.content = ft.Column(

            tight=True,

            controls=[

                ft.Text("Customer ID : C001"),

                ft.Text("Customer Name : Rahul"),

                ft.Text("Phone Number : 9876543210"),

                ft.Text("Alternate Number : 9876543211"),

                ft.Text("Email : rahul@gmail.com"),

                ft.Text("Address : Mumbai"),

                ft.Text("Customer Performance : Excellent")

            ]

        )

        details_dialog.actions = [

            ft.ElevatedButton(
                "Update",
                on_click=update_customer
            ),

            ft.ElevatedButton(
                "Delete",
                color="white",
                bgcolor="red",
                on_click=delete_customer
            ),

            ft.ElevatedButton(
                "Close",
                on_click=close_dialog
            )

        ]

        page.dialog = details_dialog
        details_dialog.open = True
        page.update()


 # Customer Table

    customer_table = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("Customer ID")),

            ft.DataColumn(ft.Text("Customer Name")),

            ft.DataColumn(ft.Text("Phone Number")),

            ft.DataColumn(ft.Text("Email")),

            ft.DataColumn(ft.Text("Customer Performance"))

        ],

        rows=[

            ft.DataRow(

                cells=[

                    ft.DataCell(

                        ft.TextButton(

                            "C001",

                            on_click=open_customer

                        )

                    ),

                    ft.DataCell(ft.Text("Rahul")),

                    ft.DataCell(ft.Text("9876543210")),

                    ft.DataCell(ft.Text("rahul@gmail.com")),

                    ft.DataCell(ft.Text("Excellent"))

                ]

            ),

            ft.DataRow(

                cells=[

                    ft.DataCell(

                        ft.TextButton(

                            "C002",

                            on_click=open_customer

                        )

                    ),

                    ft.DataCell(ft.Text("Amit")),

                    ft.DataCell(ft.Text("9123456789")),

                    ft.DataCell(ft.Text("amit@gmail.com")),

                    ft.DataCell(ft.Text("Good"))

                ]

            )

        ]

    )

 # Page

    return ft.Column(

        scroll="auto",

        controls=[

            ft.Text(
                "Customers",
                size=25,
                weight=ft.FontWeight.BOLD
            ),

            ft.Divider(),

            ft.Text(
                "Add Customer",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            customer_id,

            customer_name,

            phone,

            alternate_phone,

            email,

            address,

            created_date,

            updated_date,

            ft.Row(

                controls=[

                    ft.ElevatedButton(
                        "Save",
                        on_click=save
                    ),

                    ft.ElevatedButton(
                        "Clear",
                        on_click=clear
                    )

                ]

            ),

            ft.Divider(),

            ft.Text(
                "View All Customers",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            customer_table

        ]

    )