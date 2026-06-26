# ---------------------------------------------------------------------------
# pages/cart_page.py
#
# Page Object Model (POM) class for the SauceDemo shopping cart page.
# Reached by clicking the cart icon after adding items on the inventory page.
#
# PHASE: Built out in Phase 2 alongside the cart E2E test suite.
# ---------------------------------------------------------------------------


class CartPage:
    # -----------------------------------------------------------------------
    # CLASS-LEVEL LOCATOR CONSTANTS
    # -----------------------------------------------------------------------

    # Each item row in the cart
    CART_ITEM = ".cart_item"

    # The name label inside each cart item row
    CART_ITEM_NAME = ".inventory_item_name"

    # The "Continue Shopping" button that returns to inventory
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"

    # The "Checkout" button that starts the checkout flow
    CHECKOUT_BUTTON = "#checkout"

    # -----------------------------------------------------------------------
    # __init__
    # -----------------------------------------------------------------------
    def __init__(self, page):
        self.page = page

    # -----------------------------------------------------------------------
    # get_cart_item_names()
    #
    # Returns a list of the names of all items currently in the cart.
    # Used to assert that the correct items were added from the inventory page.
    # -----------------------------------------------------------------------
    def get_cart_item_names(self) -> list:
        # all_inner_texts() collects text from every matching element into a list
        return self.page.locator(self.CART_ITEM_NAME).all_inner_texts()

    # -----------------------------------------------------------------------
    # get_cart_item_count()
    #
    # Returns the number of item rows displayed in the cart.
    # -----------------------------------------------------------------------
    def get_cart_item_count(self) -> int:
        # count() returns the number of elements matched by the locator
        return self.page.locator(self.CART_ITEM).count()

    # -----------------------------------------------------------------------
    # click_checkout()
    #
    # Proceeds to the checkout step from the cart page.
    # -----------------------------------------------------------------------
    def click_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)

    # -----------------------------------------------------------------------
    # click_continue_shopping()
    #
    # Returns to the inventory page without checking out.
    # -----------------------------------------------------------------------
    def click_continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING_BUTTON)
