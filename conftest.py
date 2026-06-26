# ---------------------------------------------------------------------------
# conftest.py
#
# pytest configuration file. Loaded automatically by pytest before any test.
# Defines shared fixtures (reusable setup/teardown) available to all tests.
#
# BROWSER NOTE:
# Playwright bundles its own browser binaries, but on Ubuntu 26.04 those
# binaries are not yet supported. We work around this by pointing Playwright
# to the system-installed Brave browser, which is Chromium-based and fully
# compatible with Playwright's Chromium driver.
# ---------------------------------------------------------------------------

import json
import pytest
from playwright.sync_api import sync_playwright

# ---------------------------------------------------------------------------
# PATH TO BRAVE BROWSER
#
# Module-level constant — easy to update if Brave moves to a different path.
# ---------------------------------------------------------------------------
BRAVE_PATH = "/usr/bin/brave-browser"


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
def browser():
    # sync_playwright() starts the Playwright engine as a context manager
    with sync_playwright() as pw:
        # launch() starts the browser process
        # executable_path overrides the default bundled binary with Brave
        # headless=True runs without a visible window (standard for CI)
        browser = pw.chromium.launch(
            executable_path=BRAVE_PATH,
            headless=True,
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
