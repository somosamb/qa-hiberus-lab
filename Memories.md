# Memories — AI Agent Instructions for qa-hiberus-lab

This file records the user's preferences and project decisions so that any AI agent
reading this file in a future context can continue the work consistently.

---

## User Profile

- Name: Erwin Andrei Hortua Cortes
- Email: andreihortua@gmail.com
- Role: QA Engineer, ISTQB CTFL certified
- Background: 10+ years manual QA, UI testing, POM support in C#/Selenium
- Learning goal: Bridge toward Python + Playwright automation at senior level
- Location: Bogotá, Colombia
- LinkedIn: linkedin.com/in/hortua

---

## Project

- Name: qa-hiberus-lab
- Path: /home/drei/MEGA/CV/Hiberus/qa-hiberus-lab
- Purpose: Hands-on automation framework targeting the Hiberus Automation Engineer Senior role
- App under test (UI): https://www.saucedemo.com
- App under test (API): https://reqres.in

---

## Environment

- OS: Ubuntu 26.04 LTS
- Python: 3.14.4 (path: /usr/bin/python3)
- Virtual environment: .venv (created with python3 -m venv .venv)
- Browser: Brave (/usr/bin/brave-browser) — used instead of Playwright bundled binaries
  because Ubuntu 26.04 is not yet supported by Playwright's binary distribution
- Playwright is configured to use Brave via `executable_path` in the `browser` fixture
  inside conftest.py — no CLI flags needed, it works automatically

---

## Language Preferences

- Conversation: Spanish
- Code comments: English
- File content (docs, markdown): English

---

## Code Comment Style — STRICT RULES

These rules must be followed on every line of code written:

1. Comments must be ABOVE the line or block they describe, never on the same line.
   CORRECT:
     # Navigate to the login page
     self.page.goto(url)

   WRONG:
     self.page.goto(url)  # Navigate to the login page

2. Every function/method must have a block comment above its definition explaining:
   - What the function does
   - Why it exists (context or design decision)
   - Parameters and return value if non-obvious

3. Every class must have a block comment explaining:
   - What the class represents
   - Design pattern used (e.g. POM)
   - Advantages and disadvantages if relevant (useful for interviews)

4. Every file must have a header block comment explaining:
   - What the file is
   - What concepts it covers
   - Which learning section it belongs to

5. Module-level constants must have a comment explaining what they are and why
   they are defined at module level instead of inline.

6. Comments must be detailed and educational — this is a learning project.
   Assume the reader is learning Python and Playwright for the first time.

---

## Code Style

- Minimal code: write only what is needed to address the requirement
- No unused imports, no placeholder pass blocks without explanation
- Type hints on all function signatures (e.g. def login(self, username: str) -> None)
- Locators defined as class-level constants in POM classes, not inline in methods
- Fixtures in conftest.py, not duplicated inside test files
- Local fixtures (needed only in one test file) defined at the top of that file

---

## Project Structure Preferences

- POM classes in pages/
- Test files in tests/
- Test data in data/ as JSON
- CI/CD in .github/workflows/
- Virtual environment in .venv/ (gitignored)
- HTML reports in reports/ (gitignored)
- No src/ wrapper — flat structure at root level
- pages/__init__.py and tests/__init__.py must exist to mark them as Python packages
- pytest.ini at root with: testpaths=tests, addopts=-v --tb=short --html --self-contained-html, markers declared

---

## Documentation Preferences

- Do NOT distinguish between source documents when they describe the same role
- Do NOT organise learning plans by weeks or time estimates — use sections only
- The user sets their own pace; sections are logical groupings, not schedules
- README.md must always include: prerequisites, installation, how to run tests,
  project structure, architecture explanation, and resources
- Plan.md must always include: gap analysis, project structure, and learning sections

---

## Git Preferences

- Default branch: main
- Commit message format: "feat: <short description of what was done>"
- One commit per meaningful milestone, not per file
- .gitignore must exclude: .venv/, __pycache__/, reports/, .pytest_cache/

---

## Interaction Preferences

- Ask clarifying questions before creating files or writing code
- Group all questions in one message, not one at a time
- Do not apologise for errors — just fix them silently and retry
- Do not add tests unless explicitly requested
- Do not remove existing code unless explicitly requested
- Always confirm before running git commit
- Keep responses concise — no flattery, no filler phrases
