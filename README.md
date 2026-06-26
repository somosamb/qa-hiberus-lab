# qa-hiberus-lab

A Python + Playwright automation framework built from scratch as a hands-on learning
project, targeting the Hiberus Automation Engineer Senior role requirements.

---

## Prerequisites

- Python 3.12+ (project developed on 3.14.4)
- Git
- A terminal (Linux/macOS) or WSL (Windows)
- A GitHub account (for CI/CD in Section 3)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/qa-hiberus-lab.git
cd qa-hiberus-lab
```

### 2. Create and activate the virtual environment

```bash
# Create the virtual environment in the .venv folder
python3 -m venv .venv

# Activate it (Linux/macOS)
source .venv/bin/activate

# Activate it (Windows)
.venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
# Downloads Chromium, Firefox, and WebKit binaries
playwright install
```

> **Note:** On Ubuntu 26.04, Playwright's bundled binaries are not yet supported.
> The project is configured to use the system-installed Brave browser as a drop-in
> replacement. No extra steps needed — `conftest.py` handles this automatically.

---

## Running the Tests

### Run the full test suite

```bash
pytest
```

### Run a specific test file

```bash
pytest tests/test_login.py
```

### Run a specific test by name

```bash
pytest tests/test_login.py::test_valid_login
```

### Run with verbose output

```bash
pytest -v
```

### Run and generate an HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

### Run tests in headed mode (see the browser)

```bash
pytest --headed
```

---

## Project Structure

```
qa-hiberus-lab/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD pipeline
├── pages/                      # Page Object Model (POM) layer
│   ├── login_page.py           # Encapsulates login page actions and locators
│   ├── inventory_page.py       # Encapsulates inventory/product page behaviour
│   └── cart_page.py            # Encapsulates shopping cart page behaviour
├── tests/
│   ├── test_login.py           # Login flow scenarios
│   ├── test_inventory.py       # Product listing, sorting, add-to-cart
│   ├── test_cart.py            # End-to-end cart and checkout validation
│   └── test_api.py             # REST API tests using requests library
├── data/
│   └── users.json              # Test user data for data-driven tests
├── conftest.py                 # Shared pytest fixtures (browser, page, base_url)
├── requirements.txt            # All Python dependencies with pinned versions
├── Plan.md                     # Full learning plan and gap analysis
└── README.md                   # This file
```

---

## Architecture: Page Object Model (POM)

Each page of the application under test is represented by a Python class.
The class owns all locators and all interactions for that page.
Tests never interact with the browser directly — they always go through a page class.

```
tests/test_login.py
    └── calls → pages/login_page.py (LoginPage class)
                    └── uses → Playwright page object (browser interaction)
```

**Why POM?**
- Locator changes require updates in one place only
- Tests read like business scenarios, not like CSS selectors
- Reusable actions across multiple test files

---

## Key Concepts Practiced

| Concept                    | Where applied                          |
|----------------------------|----------------------------------------|
| OOP (classes, inheritance) | All `pages/*.py` classes               |
| Page Object Model          | `pages/` layer                         |
| Login Flows                | `tests/test_login.py`                  |
| UI Testing                 | `tests/test_inventory.py`              |
| Data structures (list/dict)| `data/users.json` + parametrize        |
| Git (branches, commits)    | Full project version control           |
| Playwright                 | All UI tests                           |
| Python scripting           | All test and page files                |
| API Testing                | `tests/test_api.py`                    |
| CI/CD pipeline             | `.github/workflows/ci.yml`             |
| HTML test reports          | `pytest-html` output                   |

---

## Test Data

Test users are stored in `data/users.json` and loaded in `conftest.py`.
This demonstrates use of Python data structures (dicts, lists) applied to
test automation.

```json
{
  "valid_users": [
    { "username": "standard_user", "password": "secret_sauce" }
  ],
  "invalid_users": [
    { "username": "wrong_user", "password": "wrong_pass" }
  ],
  "locked_users": [
    { "username": "locked_out_user", "password": "secret_sauce" }
  ]
}
```

---

## CI/CD Pipeline (Section 3)

The GitHub Actions pipeline in `.github/workflows/ci.yml` runs automatically
on every push and pull request to `main`.

**Pipeline steps:**
1. Checkout code
2. Set up Python 3.12
3. Install dependencies
4. Install Playwright browsers
5. Run pytest
6. Upload HTML report as a downloadable artifact

---

## Learning Sections

| Section | Focus                        | Key output                              |
|---------|------------------------------|-----------------------------------------|
| 1       | Foundation                   | POM skeleton + login tests passing      |
| 2       | Coverage + API               | Full suite + data-driven + API tests    |
| 3       | CI/CD                        | Green pipeline on GitHub Actions        |
| 4       | Advanced (mobile + TS)       | Mobile emulation + TypeScript tests     |

See `Plan.md` for the full detailed breakdown.

---

## Dependencies

| Package          | Purpose                                      |
|------------------|----------------------------------------------|
| pytest           | Test runner and assertion framework          |
| playwright       | Browser automation (Chromium/Firefox/WebKit) |
| pytest-playwright| Playwright fixtures for pytest               |
| requests         | HTTP client for API testing                  |
| pytest-html      | HTML test report generation                  |

---

## Git Workflow

```bash
# Start a new feature branch (one branch per section or feature)
git checkout -b feature/section-1-login-tests

# Stage and commit your work
git add .
git commit -m "feat: add LoginPage POM class and login test suite"

# Push to remote
git push origin feature/section-1-login-tests

# Merge via pull request on GitHub
```

---

## Resources

- [Playwright Python Docs](https://playwright.dev/python/docs/intro)
- [pytest Docs](https://docs.pytest.org/)
- [SauceDemo (app under test)](https://www.saucedemo.com)
- [reqres.in (API under test)](https://reqres.in)
- [ISTQB Glossary](https://glossary.istqb.org/)
