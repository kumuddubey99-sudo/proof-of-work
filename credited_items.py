import flet as ft


def credited_items_page(page, open_dashboard=None):

    # -------------------------
    # Credited Item Form
    # -------------------------

    item_id = ft.TextField(
        label="Item ID",
        value="Auto",
        read_only=True
    )

    transaction_id = ft.TextField(
        label="Transaction ID"
    )

    item_name = ft.TextField(
        label="Item Name"
    )

    quantity = ft.TextField(
        label="Quantity"
    )

    unit_price = ft.TextField(
        label="Unit Price"
    )

    subtotal = ft.TextField(
        label="Subtotal"
    )

    credited_at = ft.TextField(
        label="Credited Date"
    )


    # -------------------------
    # Buttons
    # -------------------------

    def save(e):
        print("Item Saved")


    def update(e):
        print("Item Updated")


    def clear(e):

        transaction_id.value = ""
        item_name.value = ""
        quantity.value = ""
        unit_price.value = ""
        subtotal.value = ""
        credited_at.value = ""

        page.update()


    # -------------------------
    # Item Details Dialog
    # -------------------------

    details_dialog = ft.AlertDialog(
        modal=True
    )


    def close_dialog(e):

        details_dialog.open = False
        page.update()


    def update_item(e):

        print("Item Updated")


    def delete_item(e):

        print("Item Deleted")


    def open_item(e):

        details_dialog.title = ft.Text(
            "Credited Item Details"
        )


        details_dialog.content = ft.Column(
            tight=True,
            controls=[

                ft.Text("Item ID : I001"),

                ft.Text("Transaction ID : TR001"),

                ft.Text("Item Name : Rice"),

                ft.Text("Quantity : 5"),

                ft.Text("Unit Price : ₹50"),

                ft.Text("Subtotal : ₹250"),

                ft.Text("Credited Date : 15-07-2026")

            ]
        )


        details_dialog.actions = [

            ft.ElevatedButton(
                "Update",
                on_click=update_item
            ),


            ft.ElevatedButton(
                "Delete",
                bgcolor=ft.Colors.RED,
                color=ft.Colors.WHITE,
                on_click=delete_item
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
    # View All Credited Items
    # -------------------------

    items_table = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("Item ID")),

            ft.DataColumn(ft.Text("Transaction ID")),

            ft.DataColumn(ft.Text("Item Name")),

            ft.DataColumn(ft.Text("Quantity")),

            ft.DataColumn(ft.Text("Unit Price")),

            ft.DataColumn(ft.Text("Subtotal")),

            ft.DataColumn(ft.Text("Credited Date"))

        ],


        rows=[


            ft.DataRow(

                cells=[

                    ft.DataCell(

                        ft.TextButton(
                            "I001",
                            on_click=open_item
                        )

                    ),

                    ft.DataCell(
                        ft.Text("TR001")
                    ),

                    ft.DataCell(
                        ft.Text("Rice")
                    ),

                    ft.DataCell(
                        ft.Text("5")
                    ),

                    ft.DataCell(
                        ft.Text("₹50")
                    ),

                    ft.DataCell(
                        ft.Text("₹250")
                    ),

                    ft.DataCell(
                        ft.Text("15-07-2026")
                    )

                ]

            ),



            ft.DataRow(

                cells=[

                    ft.DataCell(

                        ft.TextButton(
                            "I002",
                            on_click=open_item
                        )

                    ),

                    ft.DataCell(
                        ft.Text("TR002")
                    ),

                    ft.DataCell(
                        ft.Text("Sugar")
                    ),

                    ft.DataCell(
                        ft.Text("2")
                    ),

                    ft.DataCell(
                        ft.Text("₹60")
                    ),

                    ft.DataCell(
                        ft.Text("₹120")
                    ),

                    ft.DataCell(
                        ft.Text("16-07-2026")
                    )

                ]

            )

        ]

    )



    # -------------------------
    # Page Layout
    # -------------------------

    return ft.Column(

        scroll="auto",

        controls=[


            ft.Text(

                "Credited Items",

                size=25,

                weight=ft.FontWeight.BOLD

            ),


            ft.Divider(),


            item_id,

            transaction_id,

            item_name,

            quantity,

            unit_price,

            subtotal,

            credited_at,



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

                "View All Credited Items",

                size=20,

                weight=ft.FontWeight.BOLD

            ),



            items_table

        ]

    )