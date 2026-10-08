"""New tests added in Lab 7 to cover the gaps found in the baseline report."""
import auth
from unittest.mock import patch

# --- Experiment C: verify_reset_token tests ---
def test_verify_reset_token_accepts_valid_token():
    token = auth.generate_reset_token("student@uni.edu")
    result = auth.verify_reset_token(token)
    assert result["valid"] is True

def test_verify_reset_token_rejects_unknown_token():
    result = auth.verify_reset_token("no-such-token")
    assert result["valid"] is False

def test_verify_reset_token_rejects_expired_token():
    token = auth.generate_reset_token("student@uni.edu", hours_ago=2)
    result = auth.verify_reset_token(token)
    assert result["valid"] is False

def test_verify_reset_token_rejects_used_token():
    token = auth.generate_reset_token("student@uni.edu")
    auth.mark_token_used(token)
    result = auth.verify_reset_token(token)
    assert result["valid"] is False


# --- Experiment C: check_lockout tests ---
def test_check_lockout_blocks_already_locked_account():
    auth.lock_account("student@uni.edu")
    assert auth.check_lockout("student@uni.edu", attempt_count=0) is False

def test_check_lockout_allows_two_failed_attempts():
    assert auth.check_lockout("student@uni.edu", attempt_count=2) is True
    assert auth.is_locked("student@uni.edu") is False

def test_check_lockout_blocks_unknown_account_at_three_attempts():
    assert auth.check_lockout("nobody@uni.edu", attempt_count=3) is False


# --- Experiment C: validate_login tests ---
def test_validate_login_rejects_unregistered_email():
    result = auth.validate_login("ghost@uni.edu", "ValidPass1")
    assert result["success"] is False
    assert result["user_id"] is None
    assert result["error"] == "Invalid credentials"

def test_validate_login_refuses_locked_account():
    auth.lock_account("student@uni.edu")
    result = auth.validate_login("student@uni.edu", "ValidPass1")
    assert result["success"] is False
    assert result["error"] == "Account is locked"

def test_validate_login_locks_account_after_three_wrong_passwords():
    for _ in range(3):
        auth.validate_login("student@uni.edu", "WrongPass9")
    assert auth.is_locked("student@uni.edu") is True


# --- Experiment D: Session tests ---
def test_is_session_valid_no_session_exists():
    assert auth.is_session_valid("STU-001") is False

def test_is_session_valid_idle_29_minutes():
    auth.create_session("STU-001", idle_minutes=29)
    assert auth.is_session_valid("STU-001") is True

def test_is_session_valid_idle_30_minutes():
    auth.create_session("STU-001", idle_minutes=30)
    assert auth.is_session_valid("STU-001") is False

def test_handle_session_no_session_yet():
    assert auth.handle_session("STU-001", idle_minutes=0) is True
    assert auth.is_session_valid("STU-001") is True

def test_handle_session_session_idle_45_minutes():
    auth.create_session("STU-001", idle_minutes=45)
    assert auth.handle_session("STU-001") is False

def test_handle_session_valid_session_is_refreshed():
    auth.create_session("STU-001", idle_minutes=25)
    before_activity = auth.auth_store.sessions["STU-001"]["last_activity"]
    assert auth.handle_session("STU-001") is True
    after_activity = auth.auth_store.sessions["STU-001"]["last_activity"]
    assert after_activity >= before_activity


# --- Experiment D: Password reset email tests ---
def test_send_reset_email_not_registered():
    result = auth.send_reset_email("ghost@uni.edu")
    assert result["sent"] is False
    assert result["error"] == "Email address not found"

def test_send_reset_email_rate_limit_reached():
    for _ in range(3):
        auth.send_reset_email("student@uni.edu")
    result = auth.send_reset_email("student@uni.edu")
    assert result["sent"] is False
    assert result["error"] == "Rate limit exceeded"

def test_send_reset_email_token_generation_fails():
    with patch("auth.generate_reset_token", side_effect=RuntimeError("boom")):
        result = auth.send_reset_email("student@uni.edu")
        assert result["sent"] is False
        assert result["error"] == "Token generation failed: boom"

def test_send_reset_email_smtp_delivery_fails():
    with patch("auth._deliver_email", side_effect=ConnectionError("server down")):
        result = auth.send_reset_email("student@uni.edu")
        assert result["sent"] is False
        assert result["error"] == "SMTP error: server down"