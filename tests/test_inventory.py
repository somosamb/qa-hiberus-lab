# ---------------------------------------------------------------------------
# tests/test_inventory.py
#
# Test suite for the SauceDemo inventory/products page.
# Covers UI testing, sorting behaviour, and add-to-cart interactions.
#
# PHASE 2 of the learning plan.
# These tests are marked with pytest.mark.skip until Phase 2 begins,
# so the test suite runs cleanly in Phase 1 without failures.
# ---------------------------------------------------------------------------

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


# ---------------------------------------------------------------------------
# FIXTURE: logged_in_inventory_page (local to this module)
#
# A module-level fixture that handles login and returns an InventoryPage.
# Any test in this file that needs to start from the inventory page
# can request this fixture instead of repeating the login steps.
# ---------------------------------------------------------------------------
@pytest.fixture
def logged_in_inventory_page(page, base_url, valid_user):
    # Log in first — every inventory test requires an authenticated session
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login(valid_user["username"], valid_user["password"])

    # Return the InventoryPage instance ready for the test to use
    return InventoryPage(page)


# ---------------------------------------------------------------------------
# TEST: test_inventory_page_loads
#
# SCENARIO: After login, the inventory page displays the product list.
# EXPECTED: The page title is "Products" and at least one product is shown.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_inventory_page_loads(logged_in_inventory_page):
    inventory = logged_in_inventory_page

    assert inventory.is_on_inventory_page(), "Inventory page title not found."

    # get_product_titles() returns a list — assert it is not empty
    products = inventory.get_product_titles()
    assert len(products) > 0, "No products found on the inventory page."


# ---------------------------------------------------------------------------
# TEST: test_sort_products_a_to_z
#
# SCENARIO: User selects sort "A to Z".
# EXPECTED: Product titles are in ascending alphabetical order.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_sort_products_a_to_z(logged_in_inventory_page):
    inventory = logged_in_inventory_page
    inventory.select_sort_option("az")

    titles = inventory.get_product_titles()

    # sorted() returns a new sorted list — compare to the actual order
    assert titles == sorted(titles), (
        f"Products are not sorted A→Z. Actual order: {titles}"
    )


# ---------------------------------------------------------------------------
# TEST: test_add_item_to_cart_updates_badge
#
# SCENARIO: User adds the first product to the cart.
# EXPECTED: The cart badge counter increments to 1.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_add_item_to_cart_updates_badge(logged_in_inventory_page):
    inventory = logged_in_inventory_page

    # Confirm cart starts empty
    assert inventory.get_cart_item_count() == 0, "Cart should be empty before adding items."

    inventory.add_first_item_to_cart()

    # After adding one item the badge should show 1
    assert inventory.get_cart_item_count() == 1, (
        "Cart badge should show 1 after adding one item."
    )
