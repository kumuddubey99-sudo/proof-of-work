import flet as ft


class Sidebar(ft.Container):

    def __init__(
        self,
        page: ft.Page,
        on_menu_click,
    ):
        super().__init__()

        self.main_page = page
        self.on_menu_click = on_menu_click

        # -----------------------------
        # Expand / Collapse States
        # -----------------------------
        self.customer_open = False
        self.credit_item_open = False
        self.payment_open = False
        self.transaction_open = False

        # -----------------------------
        # Theme Colors
        # -----------------------------
        self.bg = "#1F2937"
        self.card = "#374151"
        self.hover = "#4B5563"
        self.text = "white"

        self.width = 270
        self.bgcolor = self.bg
        self.padding = 15

        self.content = self.build_sidebar()

    # =====================================================
    # BUTTON
    # =====================================================

    def menu_button (
        self,
        title,
        icon,
        page_name,
        indent=0,
    ):

        return ft.Container(
            padding=ft.padding.only(
                left=indent,
                right=10,
                top=5,
                bottom=5,
            ),
            border_radius=8,
            on_hover=lambda e: self.hover_effect(e),
            content=ft.TextButton(
                content=ft.Row(
                    [
                        ft.Icon(
                            icon,
                            color="white",
                            size=20,
                        ),
                        ft.Text(
                            title,
                            color="white",
                            size=15,
                        ),
                    ]
                ),
                on_click=lambda e: self.on_menu_click(
                    page_name
                ),
            ),
        )

    # =====================================================
    # EXPAND BUTTON
    # =====================================================

    def expand_button(
        self,
        title,
        icon,
        state_name,
    ):

        arrow = (
            ft.Icons.KEYBOARD_ARROW_DOWN
            if getattr(self, state_name)
            else ft.Icons.KEYBOARD_ARROW_RIGHT
        )

        return ft.Container(
            padding=8,
            border_radius=8,
            on_hover=lambda e: self.hover_effect(e),
            content=ft.Row(
                [
                    ft.Icon(icon, color="white"),
                    ft.Text(
                        title,
                        color="white",
                        expand=True,
                    ),
                    ft.Icon(
                        arrow,
                        color="white",
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            on_click=lambda e: self.toggle_menu(
                state_name
            ),
        )

    # =====================================================
    # Hover
    # =====================================================

    def hover_effect(self, e):
        e.control.bgcolor = (
            self.hover
            if e.data == "true"
            else None
        )
        e.control.update()

    # =====================================================
    # Toggle Menu
    # =====================================================

    def toggle_menu(self, state_name):

        current = getattr(
            self,
            state_name,
        )

        setattr(
            self,
            state_name,
            not current,
        )

        self.content = self.build_sidebar()

        self.update()

    # =====================================================
    # Build Sidebar
    # =====================================================

    def build_sidebar(self):

        controls = []

        # ---------------------------------
        # LOGO
        # ---------------------------------

        controls.append(
            ft.Container(
                padding=10,
                content=ft.Column(
                    [
                        ft.Icon(
                            ft.Icons.STORE,
                            size=50,
                            color="white",
                        ),
                        ft.Text(
                            "UDHAAR",
                            color="white",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Management System",
                            color="white70",
                            size=12,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )

        controls.append(
            ft.Divider(
                color="white24"
            )
        )

        # ---------------------------------
        # Dashboard
        # ---------------------------------

        controls.append(
            self.menu_button(
                "Dashboard",
                ft.Icons.DASHBOARD,
                "dashboard",
            )
        )

        # =====================================================
        # CUSTOMERS
        # =====================================================

        controls.append(
            self.expand_button(
                "Customers",
                ft.Icons.PEOPLE,
                "customer_open",
            )
        )

        if self.customer_open:

            controls.append(
                self.menu_button(
                    "Add Customer",
                    ft.Icons.PERSON_ADD,
                    "add_customer",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "View Customers",
                    ft.Icons.REMOVE_RED_EYE,
                    "view_customer",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "Update Customer",
                    ft.Icons.EDIT,
                    "update_customer",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "Customer Performance",
                    ft.Icons.STAR,
                    "customer_performance",
                    25,
                )
            )

        # =====================================================
        # CREDIT ITEMS
        # =====================================================

        controls.append(
            self.expand_button(
                "Credit Items",
                ft.Icons.SHOPPING_CART,
                "credit_item_open",
            )
        )

        if self.credit_item_open:

            controls.append(
                self.menu_button(
                    "Add Item",
                    ft.Icons.ADD_BOX,
                    "add_item",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "View Items",
                    ft.Icons.LIST,
                    "view_item",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "Update Item",
                    ft.Icons.EDIT_NOTE,
                    "update_item",
                    25,
                )
            )
        # =====================================================
        # PAYMENTS
        # =====================================================

        controls.append(
            self.expand_button(
                "Payments",
                ft.Icons.PAYMENTS,
                "payment_open",
            )
        )

        if self.payment_open:

            controls.append(
                self.menu_button(
                    "Add Payment",
                    ft.Icons.ADD_CARD,
                    "add_payment",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "View Payments",
                    ft.Icons.RECEIPT_LONG,
                    "view_payment",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "Update Payment",
                    ft.Icons.EDIT_DOCUMENT,
                    "update_payment",
                    25,
                )
            )

        # =====================================================
        # CREDIT TRANSACTIONS
        # =====================================================

        controls.append(
            self.expand_button(
                "Credit Transactions",
                ft.Icons.SWAP_HORIZ,
                "transaction_open",
            )
        )

        if self.transaction_open:

            controls.append(
                self.menu_button(
                    "Add Transaction",
                    ft.Icons.POST_ADD,
                    "add_transaction",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "View Transactions",
                    ft.Icons.RECEIPT,
                    "view_transaction",
                    25,
                )
            )

            controls.append(
                self.menu_button(
                    "Update Transaction",
                    ft.Icons.FACT_CHECK,
                    "update_transaction",
                    25,
                )
            )

        # =====================================================
        # OUTSTANDING BALANCE
        # =====================================================

        controls.append(
            self.menu_button(
                "Outstanding Balance",
                ft.Icons.ACCOUNT_BALANCE_WALLET,
                "outstanding_balance",
            )
        )

        # =====================================================
        # REPORTS
        # =====================================================

        controls.append(
            self.menu_button(
                "Generate Reports",
                ft.Icons.ANALYTICS,
                "reports",
            )
        )

        controls.append(
            ft.Container(expand=True)
        )

        controls.append(
            ft.Divider(
                color="white24",
            )
        )

        # =====================================================
        # LOGOUT
        # =====================================================

        controls.append(
            ft.Container(
                padding=5,
                border_radius=8,
                on_hover=lambda e: self.hover_effect(e),
                content=ft.TextButton(
                    content=ft.Row(
                        [
                            ft.Icon(
                                ft.Icons.LOGOUT,
                                color="red300",
                            ),
                            ft.Text(
                                "Logout",
                                color="red300",
                                size=15,
                            ),
                        ]
                    ),
                    on_click=lambda e: self.on_menu_click(
                        "logout"
                    ),
                ),
            )
        )
        # =====================================================
        # RETURN SIDEBAR LAYOUT
        # =====================================================

        return ft.Column(
            controls=controls,
            spacing=6,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        )


# ==========================================================
# OPTIONAL DEMO
# Remove this section when using the sidebar in your project.
# ==========================================================

if __name__ == "__main__":

    def menu_clicked(page_name):
        print(f"Selected: {page_name}")

    def main(page: ft.Page):
        page.title = "Sidebar Demo"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.spacing = 0
        page.window.width = 1200
        page.window.height = 700

        sidebar = Sidebar(
            page=page,
            on_menu_click=menu_clicked,
        )

        page.add(
            ft.Row(
                [
                    sidebar,
                    ft.VerticalDivider(width=1),
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            "Content Area",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ),
                ],
                expand=True,
            )
        )

    ft.app(target=main)