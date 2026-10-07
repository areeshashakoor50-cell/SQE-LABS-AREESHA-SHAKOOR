"""Additional tests for improving authentication coverage."""

import auth


# TC-008: valid reset token
def test_verify_reset_token_valid():
    result = auth.verify_reset_token("student@uni.edu")
    assert result["valid"] is True


# TC-009: expired reset token
def test_verify_reset_token_expired():
    result = auth.verify_reset_token("student@uni.edu", expired=True)
    assert result["valid"] is False


# TC-010: invalid reset token
def test_verify_reset_token_invalid():
    result = auth.verify_reset_token("invalid-token")
    assert result["valid"] is False


# TC-011: reset token for unknown user
def test_verify_reset_token_unknown_user():
    result = auth.verify_reset_token("unknown@uni.edu")
    assert result["valid"] is False