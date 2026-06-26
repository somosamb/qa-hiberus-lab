# ---------------------------------------------------------------------------
# tests/test_api.py
#
# REST API test suite using the `requests` library against reqres.in.
# reqres.in is a hosted fake API that simulates real REST endpoints
# (GET users, POST login, POST register, etc.) — perfect for learning.
#
# API testing is a key requirement in JobPostFull alongside UI automation.
# These tests demonstrate:
#   - HTTP GET / POST requests
#   - Status code assertions
#   - JSON response body validation
#   - Data-driven API testing
#
# PHASE 2 of the learning plan.
# ---------------------------------------------------------------------------

import pytest

# requests is the standard Python HTTP client library
# Documentation: https://docs.python-requests.org/
import requests


# ---------------------------------------------------------------------------
# MODULE-LEVEL CONSTANT: API base URL
#
# We define the API base URL once at the top of the file.
# All test functions build their endpoint URLs from this constant.
# ---------------------------------------------------------------------------
API_BASE = "https://reqres.in/api"


# ---------------------------------------------------------------------------
# TEST: test_get_users_returns_200
#
# SCENARIO: Fetch the list of users from page 2 of the API.
# EXPECTED: Status code 200 and the response body contains a "data" list.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_get_users_returns_200():
    # Send a GET request to /users?page=2
    response = requests.get(f"{API_BASE}/users", params={"page": 2})

    # Assert the HTTP status code is 200 OK
    assert response.status_code == 200, (
        f"Expected status 200 but got {response.status_code}"
    )

    # Parse the response JSON into a Python dict
    body = response.json()

    # Assert the response body contains a "data" key with a non-empty list
    assert "data" in body, "Response body should contain a 'data' key."
    assert isinstance(body["data"], list), "'data' should be a list."
    assert len(body["data"]) > 0, "'data' list should not be empty."


# ---------------------------------------------------------------------------
# TEST: test_get_single_user
#
# SCENARIO: Fetch a single user by ID.
# EXPECTED: Status 200 and the user object has an "email" field.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_get_single_user():
    # User ID 2 is a known stable user in reqres.in
    user_id = 2
    response = requests.get(f"{API_BASE}/users/{user_id}")

    assert response.status_code == 200

    body = response.json()

    # The single-user endpoint wraps the user object under a "data" key
    assert "data" in body
    assert body["data"]["id"] == user_id
    assert "email" in body["data"], "User object should contain an email field."


# ---------------------------------------------------------------------------
# TEST: test_get_nonexistent_user_returns_404
#
# SCENARIO: Request a user ID that does not exist.
# EXPECTED: Status code 404.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_get_nonexistent_user_returns_404():
    response = requests.get(f"{API_BASE}/users/9999")

    assert response.status_code == 404, (
        f"Expected 404 for unknown user, got {response.status_code}"
    )


# ---------------------------------------------------------------------------
# TEST: test_post_login_valid_credentials
#
# SCENARIO: POST login with valid credentials to the API.
# EXPECTED: Status 200 and a token is returned in the response.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_post_login_valid_credentials():
    # reqres.in expects these specific credentials for a successful login
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    # Send a POST request with JSON body
    response = requests.post(f"{API_BASE}/login", json=payload)

    assert response.status_code == 200

    body = response.json()

    # A successful login returns a token string
    assert "token" in body, "Successful login response should contain a token."
    assert isinstance(body["token"], str), "Token should be a string."


# ---------------------------------------------------------------------------
# TEST: test_post_login_missing_password
#
# SCENARIO: POST login without a password field.
# EXPECTED: Status 400 and an error message explaining what is missing.
# ---------------------------------------------------------------------------
@pytest.mark.skip(reason="Phase 2 — not yet implemented")
def test_post_login_missing_password():
    # Send only the email, omit the password
    payload = {"email": "eve.holt@reqres.in"}

    response = requests.post(f"{API_BASE}/login", json=payload)

    assert response.status_code == 400, (
        f"Expected 400 for missing password, got {response.status_code}"
    )

    body = response.json()
    assert "error" in body, "Error response should contain an 'error' key."
