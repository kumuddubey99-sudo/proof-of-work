import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import flet as ft

from language import language_page
from login import login_page
from sidebar import Sidebar

from pages.dashboard import dashboard_page
from pages.customers import customers_page
from pages.credit_transactions import credit_transactions_page
from pages.payments import payments_page
from pages.credited_items import credited_items_page
from pages.outstanding_balance import outstanding_balance_page
from pages.reports import reports_page


def main(page: ft.Page):

    # =====================================================
    # WINDOW SETTINGS
    # =====================================================

    page.title = "Udhaar Management System"
    page.window.width = 1400
    page.window.height = 800
    page.padding = 0
    page.spacing = 0

    selected_language = "English"

    # =====================================================
    # THEME COLORS
    # =====================================================

    LIGHT = {
        "bg": "#F5F7FA",
        "header": "#1565C0",
        "sidebar": "#1F2937",
        "footer": "#ECEFF1",
    }

    DARK = {
        "bg": "#121212",
        "header": "#1F1F1F",
        "sidebar": "#111827",
        "footer": "#1A1A1A",
    }

    current_theme = LIGHT

    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = current_theme["bg"]

    # =====================================================
    # SEARCH BOX
    # =====================================================

    search_box = ft.TextField(
        hint_text="Search Customer, Payment, Transaction...",
        width=360,
        border_radius=10,
        prefix_icon=ft.Icons.SEARCH,
        filled=True,
    )

    def search(e):
        print("Searching:", search_box.value)

    # =====================================================
    # CONTENT
    # =====================================================

    content = ft.Container(
        expand=True,
        padding=20,
        bgcolor=current_theme["bg"],
    )

    # =====================================================
    # DARK MODE
    # =====================================================

    dark_mode = ft.Switch(
        label="🌙 Dark Mode",
        value=False,
    )

    header = None
    sidebar = None
    footer = None

    def change_theme(e):
        nonlocal current_theme
        nonlocal header
        nonlocal sidebar
        nonlocal footer

        if dark_mode.value:
            current_theme = DARK
            page.theme_mode = ft.ThemeMode.DARK
        else:
            current_theme = LIGHT
            page.theme_mode = ft.ThemeMode.LIGHT

        page.bgcolor = current_theme["bg"]
        content.bgcolor = current_theme["bg"]

        if header:
            header.bgcolor = current_theme["header"]

        if sidebar:
            sidebar.bgcolor = current_theme["sidebar"]

        if footer:
            footer.bgcolor = current_theme["footer"]

        page.update()

    dark_mode.on_change = change_theme

    # =====================================================
    # PAGE NAVIGATION
    # =====================================================

    def change_page(page_name):

        if page_name == "dashboard":
            content.content = dashboard_page(page, selected_language)

        elif page_name in (
            "add_customer",
            "view_customer",
            "update_customer",
            "customer_performance",
        ):
            content.content = customers_page(page, selected_language)

        elif page_name in (
            "add_item",
            "view_item",
            "update_item",
        ):
            content.content = credited_items_page(page, selected_language)

        elif page_name in (
            "add_payment",
            "view_payment",
            "update_payment",
        ):
            content.content = payments_page(page, selected_language)

        elif page_name in (
            "add_transaction",
            "view_transaction",
            "update_transaction",
        ):
            content.content = credit_transactions_page(page, selected_language)

        elif page_name == "outstanding_balance":
            content.content = outstanding_balance_page(page, selected_language)

        elif page_name == "reports":
            content.content = reports_page(page, selected_language)

        elif page_name == "logout":
            page.controls.clear()
            page.add(
                login_page(
                    page,
                    selected_language,
                    login_success,
                )
            )
            page.update()
            return

        page.update()

    # =====================================================
    # HEADER
    # =====================================================

    header = ft.Container(
        bgcolor=current_theme["header"],
        padding=20,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.ACCOUNT_BALANCE_WALLET,
                            color="white",
                            size=40,
                        ),
                        ft.Text(
                            "Udhaar Management System",
                            color="white",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ]
                ),
                ft.Row(
                    spacing=15,
                    controls=[
                        search_box,
                        ft.IconButton(
                            icon=ft.Icons.SEARCH,
                            icon_color="white",
                            on_click=search,
                        ),
                        dark_mode,
                    ],
                ),
            ],
        ),
    )
    # =====================================================
    # SIDEBAR
    # =====================================================

    sidebar = Sidebar(
        page=page,
        on_menu_click=change_page,
    )

    sidebar.bgcolor = current_theme["sidebar"]

    # =====================================================
    # DEFAULT PAGE
    # =====================================================

    content.content = dashboard_page(
        page,
        selected_language,
    )

    # =====================================================
    # BODY
    # =====================================================

    body = ft.Row(
        controls=[
            sidebar,
            ft.VerticalDivider(width=1),
            content,
        ],
        expand=True,
    )

    # =====================================================
    # FOOTER
    # =====================================================

    footer = ft.Container(
        bgcolor=current_theme["footer"],
        padding=10,
        alignment=ft.alignment.center,
        content=ft.Text(
            "© 2026 Udhaar Management System",
            size=14,
            color=ft.Colors.GREY_700,
        ),
    )

    # =====================================================
    # MAIN APPLICATION LAYOUT
    # =====================================================

    app_layout = ft.Column(
        controls=[
            header,
            body,
            footer,
        ],
        spacing=0,
        expand=True,
    )

    # =====================================================
    # LOGIN SUCCESS
    # =====================================================

    def login_success():

        page.controls.clear()

        page.add(app_layout)

        page.update()

    # =====================================================
    # LANGUAGE SELECTED
    # =====================================================

    def language_selected(language):

        nonlocal selected_language

        selected_language = language

        page.controls.clear()

        page.add(
            login_page(
                page,
                selected_language,
                login_success,
            )
        )

        page.update()

    # =====================================================
    # START APPLICATION
    # =====================================================

    page.add(
        language_page(
            page,
            language_selected,
        )
    )


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":
    ft.app(target=main)