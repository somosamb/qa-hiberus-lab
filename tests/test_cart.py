# ---------------------------------------------------------------------------
# tests/test_cart.py
#
# End-to-end test suite for the SauceDemo shopping cart.
# Validates the full flow: login → add item → view cart → assert contents.
#
# PHASE 2 of the learning plan.
# ---------------------------------------------------------------------------

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


# ---------------------------------------------------------------------------
# TEST: test_added_item_appears_in_cart
#
# SCENARIO: User adds a product and navigates to the cart.
# EXPECTED: The product appears in the cart item list.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_added_item_appears_in_cart(page, base_url, valid_user):
    # Step 1: Log in
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login(valid_user["username"], valid_user["password"])

    # Step 2: Add the first item from the inventory page
    inventory = InventoryPage(page)
    titles = inventory.get_product_titles()

    # Save the name of the first product so we can verify it in the cart
    first_product_name = titles[0]
    inventory.add_first_item_to_cart()

    # Step 3: Navigate to the cart page
    page.click(".shopping_cart_link")

    # Step 4: Assert the correct item is in the cart
    cart = CartPage(page)
    cart_items = cart.get_cart_item_names()

    assert first_product_name in cart_items, (
        f"Expected '{first_product_name}' in cart but found: {cart_items}"
    )
