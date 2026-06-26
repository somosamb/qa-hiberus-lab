# ---------------------------------------------------------------------------
# pages/login_page.py
#
# Page Object Model (POM) class for the SauceDemo login page.
#
# WHAT IS POM?
# Instead of writing browser interactions directly in tests, we encapsulate
# all locators and actions for a specific page inside a dedicated class.
# Tests then call methods on this class — they never touch Playwright directly.
#
# ADVANTAGES:
#   - If a locator changes, we fix it in ONE place, not in every test
#   - Tests read like business scenarios ("login_page.login(user, pass)")
#   - Actions are reusable across multiple test files
#
# DISADVANTAGES (know these for interviews):
#   - More files to maintain as the application grows
#   - Requires discipline to keep page classes focused and not bloated
# ---------------------------------------------------------------------------


class LoginPage:
    # -----------------------------------------------------------------------
    # CLASS-LEVEL LOCATOR CONSTANTS
    #
    # We define locators as class attributes at the top.
    # This makes them easy to find and update without reading the whole class.
    # Using CSS selectors here — Playwright supports CSS, XPath, text, role.
    # -----------------------------------------------------------------------

    # The input field where the user types their username
    USERNAME_INPUT = "#user-name"

    # The input field where the user types their password
    PASSWORD_INPUT = "#password"

    # The button that submits the login form
    LOGIN_BUTTON = "#login-button"

    # The error message container that appears on failed login attempts
    ERROR_MESSAGE = "[data-test='error']"

    # -----------------------------------------------------------------------
    # __init__ (constructor)
    #
    # Called automatically when we create a LoginPage instance.
    # We receive the Playwright `page` object and store it as an instance
    # attribute so every method in this class can use it.
    #
    # `page` is the Playwright Page object — it represents a browser tab
    # and provides all methods to interact with the DOM.
    # -----------------------------------------------------------------------
    def __init__(self, page):
        # Store the Playwright page object for use in all instance methods
        self.page = page

    # -----------------------------------------------------------------------
    # navigate()
    #
    # Opens the login page in the browser.
    # We pass the URL here (not hardcoded to the class) so the method
    # can be reused if the base URL changes between environments.
    # -----------------------------------------------------------------------
    def navigate(self, url: str):
        # page.goto() navigates the browser tab to the given URL
        # and waits for the page to reach "load" state by default
        self.page.goto(url)

    # -----------------------------------------------------------------------
    # fill_username()
    #
    # Types a value into the username input field.
    # Separating each field interaction into its own method keeps actions
    # small, readable, and independently reusable.
    # -----------------------------------------------------------------------
    def fill_username(self, username: str):
        # page.fill() clears the field first, then types the given value
        # This is safer than page.type() which appends to existing content
        self.page.fill(self.USERNAME_INPUT, username)

    # -----------------------------------------------------------------------
    # fill_password()
    #
    # Types a value into the password input field.
    # Same pattern as fill_username() for consistency.
    # -----------------------------------------------------------------------
    def fill_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)

    # -----------------------------------------------------------------------
    # click_login()
    #
    # Clicks the login submit button.
    # By isolating this action we can easily test button state (enabled,
    # disabled) or add a wait before/after the click if needed.
    # -----------------------------------------------------------------------
    def click_login(self):
        # page.click() simulates a mouse click on the matched element
        self.page.click(self.LOGIN_BUTTON)

    # -----------------------------------------------------------------------
    # login()
    #
    # High-level composite action: fills credentials and clicks login.
    # This is the method most tests will call — it chains the lower-level
    # methods into a single readable action.
    #
    # Having both low-level methods (fill_username) and a high-level
    # composite (login) gives tests flexibility:
    #   - Use login() for the happy path
    #   - Use fill_username() alone to test field-level behaviour
    # -----------------------------------------------------------------------
    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

    # -----------------------------------------------------------------------
    # get_error_message()
    #
    # Reads and returns the text content of the error message element.
    # Returns an empty string if the element is not visible.
    #
    # Tests use this to assert what error was shown after a failed login,
    # without needing to know the CSS selector for the error element.
    # -----------------------------------------------------------------------
    def get_error_message(self) -> str:
        # inner_text() returns the visible text content of the element
        # We check visibility first to avoid errors if no message is shown
        error_locator = self.page.locator(self.ERROR_MESSAGE)

        # is_visible() returns True/False without throwing if element is absent
        if error_locator.is_visible():
            return error_locator.inner_text()

        # Return empty string when no error is displayed
        return ""

    # -----------------------------------------------------------------------
    # is_login_page_visible()
    #
    # Checks whether the login page is currently displayed.
    # Useful for asserting that a failed login kept the user on the login page
    # rather than redirecting them elsewhere.
    # -----------------------------------------------------------------------
    def is_login_page_visible(self) -> bool:
        # We verify the login button is present as a proxy for "login page is shown"
        return self.page.locator(self.LOGIN_BUTTON).is_visible()
