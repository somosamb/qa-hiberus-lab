# ---------------------------------------------------------------------------
# pages/inventory_page.py
#
# Page Object Model (POM) class for the SauceDemo inventory/products page.
# This is the page the user lands on after a successful login.
#
# PHASE: This class is built out in Phase 2 of the learning plan.
# For now it contains the skeleton structure with placeholder methods
# so the project runs cleanly from Phase 1 onwards.
# ---------------------------------------------------------------------------


class InventoryPage:
    # -----------------------------------------------------------------------
    # CLASS-LEVEL LOCATOR CONSTANTS
    #
    # Locators for elements on the inventory page.
    # Added as they are needed — start minimal, grow with the test suite.
    # -----------------------------------------------------------------------

    # The page title element showing "Products"
    PAGE_TITLE = ".title"

    # The container holding all product cards
    INVENTORY_LIST = ".inventory_list"

    # The dropdown that controls product sort order
    SORT_DROPDOWN = ".product_sort_container"

    # The "Add to cart" button on each product card (matches all of them)
    ADD_TO_CART_BUTTON = "button[data-test^='add-to-cart']"

    # The shopping cart icon in the top-right corner showing item count
    CART_BADGE = ".shopping_cart_badge"

    # -----------------------------------------------------------------------
    # __init__ (constructor)
    #
    # Receives and stores the Playwright page object.
    # Same pattern as LoginPage — consistent across all page classes.
    # -----------------------------------------------------------------------
    def __init__(self, page):
        self.page = page

    # -----------------------------------------------------------------------
    # is_on_inventory_page()
    #
    # Confirms the user has arrived on the inventory page after login.
    # Tests use this to assert a successful login redirect.
    # -----------------------------------------------------------------------
    def is_on_inventory_page(self) -> bool:
        # Check the page title element contains the expected text
        title_locator = self.page.locator(self.PAGE_TITLE)
        return title_locator.is_visible() and title_locator.inner_text() == "Products"

    # -----------------------------------------------------------------------
    # get_product_titles()
    #
    # Returns a list of all product name strings shown on the page.
    # Used to verify sort order and that the correct products are displayed.
    # Returns a Python list — demonstrates list usage (Data Collector Types).
    # -----------------------------------------------------------------------
    def get_product_titles(self) -> list:
        # all_inner_texts() returns a list of strings, one per matched element
        return self.page.locator(".inventory_item_name").all_inner_texts()

    # -----------------------------------------------------------------------
    # select_sort_option()
    #
    # Selects a sort option from the dropdown by its visible label value.
    # Valid values: "az", "za", "lohi", "hilo"
    # -----------------------------------------------------------------------
    def select_sort_option(self, value: str):
        # select_option() targets a <select> element and picks by value attribute
        self.page.select_option(self.SORT_DROPDOWN, value)

    # -----------------------------------------------------------------------
    # add_first_item_to_cart()
    #
    # Clicks the "Add to cart" button on the first product in the list.
    # Useful for quickly populating the cart in checkout/cart tests.
    # -----------------------------------------------------------------------
    def add_first_item_to_cart(self):
        # .first picks the first element matched by the locator
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    # -----------------------------------------------------------------------
    # get_cart_item_count()
    #
    # Returns the number shown on the cart badge icon.
    # Returns 0 if the badge is not visible (empty cart).
    # -----------------------------------------------------------------------
    def get_cart_item_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)

        # Only read the badge text if the badge element is visible
        if badge.is_visible():
            # inner_text() returns a string — cast to int for numeric comparison
            return int(badge.inner_text())

        # Badge is hidden when cart is empty
        return 0
