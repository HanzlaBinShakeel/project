"""
Tests for the validators module.
"""

import pytest
from src.validators import Validator


class TestValidator:
    """Test suite for Validator class."""
    
    def test_validate_email_valid(self):
        """Test validating valid email addresses."""
        assert Validator.validate_email("test@example.com") is True
        assert Validator.validate_email("user.name@domain.co.uk") is True
        assert Validator.validate_email("user+tag@example.com") is True
    
    def test_validate_email_invalid(self):
        """Test validating invalid email addresses."""
        assert Validator.validate_email("invalid") is False
        assert Validator.validate_email("invalid@") is False
        assert Validator.validate_email("@example.com") is False
        assert Validator.validate_email("test@") is False
    
    def test_validate_username_valid(self):
        """Test validating valid usernames."""
        assert Validator.validate_username("user123") is True
        assert Validator.validate_username("test_user") is True
        assert Validator.validate_username("User123") is True
    
    def test_validate_username_invalid(self):
        """Test validating invalid usernames."""
        assert Validator.validate_username("ab") is False  # Too short
        assert Validator.validate_username("a" * 21) is False  # Too long
        assert Validator.validate_username("user-name") is False  # Invalid character
        assert Validator.validate_username("") is False
    
    def test_validate_username_custom_length(self):
        """Test validating username with custom length requirements."""
        assert Validator.validate_username("ab", min_length=2) is True
        assert Validator.validate_username("a", min_length=2) is False
    
    def test_validate_password_valid(self):
        """Test validating valid passwords."""
        assert Validator.validate_password("password123") is True
        assert Validator.validate_password("SecurePass1") is True
        assert Validator.validate_password("test1234") is True
    
    def test_validate_password_invalid(self):
        """Test validating invalid passwords."""
        assert Validator.validate_password("short") is False  # Too short
        assert Validator.validate_password("password") is False  # No number
        assert Validator.validate_password("12345678") is False  # No letter
        assert Validator.validate_password("") is False
    
    def test_validate_password_custom_length(self):
        """Test validating password with custom length requirement."""
        assert Validator.validate_password("test12", min_length=6) is True
        assert Validator.validate_password("test1", min_length=6) is False
    
    def test_validate_url_valid(self):
        """Test validating valid URLs."""
        assert Validator.validate_url("https://example.com") is True
        assert Validator.validate_url("http://example.com/path") is True
        assert Validator.validate_url("https://example.com:8080/path?query=value") is True
    
    def test_validate_url_invalid(self):
        """Test validating invalid URLs."""
        assert Validator.validate_url("not-a-url") is False
        assert Validator.validate_url("example.com") is False  # Missing protocol
    
    def test_validate_phone_valid(self):
        """Test validating valid phone numbers."""
        assert Validator.validate_phone("1234567890") is True
        assert Validator.validate_phone("+1234567890") is True
        assert Validator.validate_phone("(123) 456-7890") is True
    
    def test_validate_phone_invalid(self):
        """Test validating invalid phone numbers."""
        assert Validator.validate_phone("123") is False  # Too short
        assert Validator.validate_phone("abc1234567") is False  # Contains letters
    
    def test_validate_custom_pattern(self):
        """Test validating with custom regex pattern."""
        assert Validator.validate_custom("12345", r'^\d+$') is True
        assert Validator.validate_custom("abc", r'^\d+$') is False
        assert Validator.validate_custom("test", r'^[a-z]+$') is True
