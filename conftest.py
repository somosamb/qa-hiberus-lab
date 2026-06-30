# ---------------------------------------------------------------------------
# conftest.py
#
# pytest configuration file. Loaded automatically by pytest before any test.
# Defines shared fixtures (reusable setup/teardown) available to all tests.
#
# BROWSER NOTE:
# Locally (Ubuntu 26.04): Playwright's bundled binaries are not yet supported.
# We work around this by setting the PLAYWRIGHT_BROWSER_PATH environment variable
# to point to the system-installed Brave browser, which is Chromium-based and
# fully compatible with Playwright's Chromium driver.
#
# In CI (GitHub Actions): PLAYWRIGHT_BROWSER_PATH is not set, so BROWSER_PATH
# falls back to None and Playwright uses its own bundled Chromium as normal.
# The Brave workaround is local-only and has no effect on the pipeline.
# ---------------------------------------------------------------------------

# os is a built-in Python module (no install needed) that lets your code talk to the
# operating system. Here we use it to read environment variables — system-level
# settings stored outside the code, like PLAYWRIGHT_BROWSER_PATH.
import os

# json is a built-in Python module for reading and writing JSON files.
# JSON is a common format for storing structured data (like test users).
# json.load() converts a .json file into a Python dict or list automatically.
import json

# pytest is the test framework that discovers, runs, and reports your tests.
# It also provides @pytest.fixture — a way to define reusable setup/teardown
# logic that tests can request just by naming it as a parameter.
import pytest

# sync_playwright is the entry point to the Playwright library.
# It starts the Playwright engine and gives access to browser types
# (Chromium, Firefox, WebKit). "sync" means it runs synchronously —
# one action at a time, which is simpler to read and debug than async code.
from playwright.sync_api import sync_playwright

# None means Playwright uses its own bundled Chromium (CI default).
# Set PLAYWRIGHT_BROWSER_PATH=/usr/bin/brave-browser locally to use Brave.
BROWSER_PATH = os.environ.get("PLAYWRIGHT_BROWSER_PATH") or None


# ---------------------------------------------------------------------------
# FIXTURE: browser (override)
#
# pytest-playwright provides a built-in `browser` fixture, but it tries to
# use Playwright's bundled binaries. We override it here to launch Brave
# instead via `executable_path`.
#
# Scope "session" — one browser instance shared across the whole test run.
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def browser(pytestconfig):
    # pytestconfig gives access to all CLI options passed to pytest.
    # getoption("headed") returns True if --headed was passed, False otherwise.
    # We invert it: headed=True means headless=False (visible window).
    headed = pytestconfig.getoption("headed", default=False)
    headless = not headed

    # slowmo adds a delay (in ms) between every Playwright action.
    # Useful for watching tests run in slow motion with --headed.
    # Defaults to 0 (no delay) if --slowmo is not passed.
    slowmo = pytestconfig.getoption("slowmo", default=0)

    # sync_playwright() starts the Playwright engine as a context manager
    with sync_playwright() as pw:
        # launch() starts the browser process
        # executable_path is None in CI (uses bundled Chromium) or set via
        # PLAYWRIGHT_BROWSER_PATH env var locally to use Brave
        # headless is now dynamic: False when --headed is passed, True otherwise
        # slow_mo applies a delay in ms between every action
        browser = pw.chromium.launch(
            executable_path=BROWSER_PATH,
            headless=headless,
            slow_mo=slowmo,
        )

        # yield hands the browser object to tests that request this fixture
        yield browser

        # Teardown: close the browser after the full session ends
        browser.close()


# ---------------------------------------------------------------------------
# FIXTURE: page (override)
#
# We override pytest-playwright's built-in `page` fixture so it uses our
# Brave-backed `browser` fixture above instead of the bundled one.
#
# Scope "function" (default) — a fresh tab is created for each test,
# guaranteeing full isolation: cookies, storage, and state are reset.
# ---------------------------------------------------------------------------
@pytest.fixture
def page(browser):
    # new_page() opens a new browser tab inside the existing browser instance
    page = browser.new_page()

    # yield the page to the test function
    yield page

    # Teardown: close the tab after each test to free resources
    page.close()


# ---------------------------------------------------------------------------
# FIXTURE: base_url
#
# Provides the root URL of the application under test (SauceDemo).
# Scope "session" — created once and shared across all tests.
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"


# ---------------------------------------------------------------------------
# FIXTURE: users
#
# Loads test user data from data/users.json and returns it as a Python dict.
# Demonstrates "Data Collector Types" from JobPost: dicts and lists used
# to organise structured test data.
#
# Scope "session" — the file is read once and reused across all tests.
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def users():
    # Open the JSON file holding all test user categories
    with open("data/users.json", encoding="utf-8") as file:
        # json.load() parses the file into a Python dict:
        # { "valid_users": [...], "invalid_users": [...], ... }
        return json.load(file)


# ---------------------------------------------------------------------------
# FIXTURE: valid_user
#
# Returns the first valid user from users.json.
# Saves tests from indexing into the full users dict themselves.
# ---------------------------------------------------------------------------
@pytest.fixture
def valid_user(users):
    # users["valid_users"] is a list — take the first entry (index 0)
    return users["valid_users"][0]
