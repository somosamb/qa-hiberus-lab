# qa-hiberus-lab — Learning Plan & Project Roadmap

## Context

This project is a hands-on learning path for a QA Engineer with manual testing
expertise and basic automation knowledge, targeting the Hiberus Automation Engineer
Senior role. The requirements were gathered from two complementary documents
describing the same position.

---

## Role Requirements Summary

- Python as primary automation language
- Playwright and Selenium for UI automation
- Page Object Model (POM) and OOP design
- Login flows and UI testing
- Data-driven testing (arrays, lists, maps)
- Git and version control
- REST API testing
- CI/CD pipeline integration
- TypeScript / JavaScript as secondary language
- Mobile automation (Appium / XCUI)
- Technical leadership of a framework

---

## Gap Analysis

| Requirement                            | Current Profile          | Gap         |
|----------------------------------------|--------------------------|-------------|
| Python as primary automation language  | Basic exposure           | Medium      |
| Playwright (owned framework)           | Exposure, no own project | Medium      |
| Appium / mobile automation             | None                     | High        |
| CI/CD pipeline (active)                | Azure DevOps support     | Medium      |
| TypeScript / JavaScript                | Basic                    | Medium      |
| Technical leadership of framework      | C# POM support role      | Medium      |

---

## Target Applications

- **UI:** [SauceDemo](https://www.saucedemo.com) — login flows, inventory, cart (E2E)
- **API:** [reqres.in](https://reqres.in) — REST API validation, data-driven scenarios

---

## Project Structure

```
qa-hiberus-lab/
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD pipeline — GitHub Actions
├── pages/                      # Page Object Model (POM) layer
│   ├── __init__.py
│   ├── login_page.py           # Login page interactions
│   ├── inventory_page.py       # Product inventory page
│   └── cart_page.py            # Shopping cart page
├── tests/
│   ├── __init__.py
│   ├── test_login.py           # Login flow tests (valid, invalid, locked user)
│   ├── test_inventory.py       # UI, sorting, add-to-cart tests
│   ├── test_cart.py            # End-to-end cart validation
│   └── test_api.py             # API tests using requests library
├── data/
│   └── users.json              # Data-driven test users (arrays, maps)
├── Quiz/
│   └── Phase1.html             # Interactive HTML quiz for Phase 1 concepts
├── conftest.py                 # pytest fixtures: browser, page, base_url
├── pytest.ini                  # pytest configuration
├── requirements.txt            # Python dependencies
├── Plan.md                     # This file
└── README.md                   # Setup, usage, and learning guide
```

---

## Learning Sections

### Section 1 — Foundation
**Goal:** Set up the framework skeleton, write the first Page Object and login tests.

- Install Python, Playwright, pytest
- Understand fixtures in `conftest.py`
- Build `LoginPage` POM class in Python (vs prior C# Selenium experience)
- Write login flow tests: valid credentials, invalid credentials, locked user
- Git: feature branches, commits, push

**Covers:** OOP, POM, UI Testing, Login Flows, Git, Python basics, Playwright basics

---

### Section 2 — Real Coverage
**Goal:** Expand test coverage with data-driven tests and API validation.

- Data-driven tests using `pytest.mark.parametrize` + `users.json`
- Python data structures: lists, dicts applied to test data
- API testing with `requests` library against reqres.in
- Build `InventoryPage` and `CartPage` POM classes
- E2E flow: login → add item → cart → assert

**Covers:** Data structures, Python depth, Playwright intermediate, API testing

---

### Section 3 — CI/CD Integration
**Goal:** Automate test execution on every push via GitHub Actions.

- Write `.github/workflows/ci.yml`
- Configure pytest HTML reports as pipeline artifacts
- Understand pipeline stages: install → test → report

**Covers:** CI/CD pipelines, DevOps collaboration

---

### Section 4 — Advanced
**Goal:** Close remaining gaps toward the Senior profile.

- Playwright mobile device emulation (conceptual bridge to Appium)
- Rewrite 1–2 tests in TypeScript using Playwright JS
- Cross-browser execution: Chromium, Firefox, WebKit

**Covers:** Appium (conceptual), TypeScript/JS, cross-browser testing

---

## Milestones

| Milestone | Deliverable                                    | Section |
|-----------|------------------------------------------------|---------|
| M1        | Project structure + Git + first passing test   | 1       |
| M2        | Full login suite (6 scenarios) with POM        | 1       |
| M3        | Data-driven tests + users.json                 | 2       |
| M4        | API test suite against reqres.in               | 2       |
| M5        | CI/CD pipeline running on GitHub Actions       | 3       |
| M6        | HTML test report as pipeline artifact          | 3       |
| M7        | Mobile emulation test                          | 4       |
| M8        | 2 tests rewritten in TypeScript                | 4       |
