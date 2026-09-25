import flet as ft

def reports_page(page, open_dashboard=None):

    report_type = ft.Dropdown(
        label="Select Report",
        options=[
            ft.dropdown.Option("Customer Report"),
            ft.dropdown.Option("Credit Transaction Report"),
            ft.dropdown.Option("Payment Report"),
            ft.dropdown.Option("Credited Items Report"),
            ft.dropdown.Option("Outstanding Balance Report"),
            ft.dropdown.Option("Customer Performance Report")
        ]
    )

    from_date = ft.TextField(
        label="From Date"
    )

    to_date = ft.TextField(
        label="To Date"
    )

    report = ft.Text(
        "Report will be displayed here."
    )

    def generate(e):

        report.value = "Report Generated Successfully"

        page.update()

    return ft.Column(

        controls=[

            ft.Text(
                "Reports",
                size=25,
                weight="bold"
            ),

            ft.Divider(),

            report_type,

            from_date,

            to_date,

            ft.ElevatedButton(
                "Generate Report",
                on_click=generate
            ),

            ft.Divider(),

            report

        ]

    )