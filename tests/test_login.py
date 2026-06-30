# ---------------------------------------------------------------------------
# tests/test_login.py
#
# Test suite for the SauceDemo login page.
# Covers the "Login Flows" requirement from JobPost and demonstrates:
#   - Page Object Model usage (OOP)
#   - Data-driven testing with pytest.mark.parametrize
#   - Fixture injection from conftest.py
#   - Assertions with clear failure messages
#
# PHASE 1 of the learning plan.
# ---------------------------------------------------------------------------

import pytest

# Import the LoginPage POM class we built in pages/login_page.py
from pages.login_page import LoginPage

# Import InventoryPage to assert successful login redirects
from pages.inventory_page import InventoryPage


# ---------------------------------------------------------------------------
# TEST: test_valid_login
#
# SCENARIO: A user with correct credentials logs in successfully.
# EXPECTED: The browser redirects to the inventory page showing "Products".
#
# Fixtures injected by pytest:
#   - page: provided by pytest-playwright, a fresh browser tab per test
#   - base_url: defined in conftest.py, returns "https://www.saucedemo.com"
#   - valid_user: defined in conftest.py, returns the first user from users.json
# ---------------------------------------------------------------------------
@pytest.mark.smoke
def test_valid_login(page, base_url, valid_user):
    # Instantiate the LoginPage POM — we pass the Playwright page object
    login_page = LoginPage(page)

    # Navigate to the login URL
    login_page.navigate(base_url)

    # Use the composite login() method to fill credentials and submit
    login_page.login(valid_user["username"], valid_user["password"])

    # After successful login, SauceDemo redirects to /inventory.html
    # We use InventoryPage to assert we arrived on the right page
    inventory_page = InventoryPage(page)

    # Assert with a descriptive message so failures are easy to understand
    assert inventory_page.is_on_inventory_page(), (
        f"Expected to land on the inventory page after logging in as "
        f"'{valid_user['username']}', but the Products title was not found."
    )


# ---------------------------------------------------------------------------
# TEST: test_invalid_login (data-driven)
#
# SCENARIO: A user with wrong credentials attempts to log in.
# EXPECTED: An error message is displayed and the user stays on the login page.
#
# pytest.mark.parametrize runs this test once for each tuple in the list.
# Each tuple is unpacked into (username, password, expected_error).
# This is the "Data Collector Types" and parametrize concept from JobPost.
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("username, password, expected_error", [
    # Wrong username AND wrong password
    (
        "wrong_user",
        "wrong_pass",
        "Epic sadface: Username and password do not match any user in this service"
    ),
    # Correct username but wrong password
    (
        "standard_user",
        "wrong_pass",
        "Epic sadface: Username and password do not match any user in this service"
    ),
    # Empty username — submitting a blank form
    (
        "",
        "secret_sauce",
        "Epic sadface: Username is required"
    ),
    # Empty password — username filled but no password
    (
        "standard_user",
        "",
        "Epic sadface: Password is required"
    ),
])
@pytest.mark.smoke
def test_invalid_login(page, base_url, username, password, expected_error):
    login_page = LoginPage(page)
    login_page.navigate(base_url)

    # Attempt login with the parametrized credentials
    login_page.login(username, password)

    # Read the error message text from the page via the POM method
    actual_error = login_page.get_error_message()

    # Assert the error message matches what we expect for this combination
    assert actual_error == expected_error, (
        f"Login with username='{username}' password='{password}': "
        f"expected error '{expected_error}' but got '{actual_error}'"
    )

    # Also assert the user is still on the login page (not redirected)
    assert login_page.is_login_page_visible(), (
        "After a failed login, the login form should still be visible."
    )


# ---------------------------------------------------------------------------
# TEST: test_locked_out_user
#
# SCENARIO: A locked-out user attempts to log in.
# EXPECTED: A specific "locked out" error message is displayed.
#
# This is a separate test (not parametrized with invalid_login) because
# it represents a distinct business scenario: account locked by admin.
# ---------------------------------------------------------------------------
@pytest.mark.smoke
def test_locked_out_user(page, base_url, users):
    # We use the 'users' fixture (full dict) to access locked_users
    locked_user = users["locked_users"][0]

    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login(locked_user["username"], locked_user["password"])

    actual_error = login_page.get_error_message()

    # The exact error message SauceDemo returns for a locked account
    expected_error = "Epic sadface: Sorry, this user has been locked out."

    assert actual_error == expected_error, (
        f"Locked user login: expected '{expected_error}' but got '{actual_error}'"
    )
