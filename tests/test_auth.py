"""
Tests for the authentication module.
"""

import pytest
from src.auth import AuthManager, User


class TestAuthManager:
    """Test suite for AuthManager class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.auth = AuthManager()
    
    def test_hash_password(self):
        """Test password hashing."""
        hash1 = AuthManager.hash_password("password123")
        hash2 = AuthManager.hash_password("password123")
        assert hash1 == hash2
        assert hash1 != AuthManager.hash_password("different")
    
    def test_register_user_success(self):
        """Test successful user registration."""
        result = self.auth.register_user("testuser", "test@example.com", "password123")
        assert result is True
        assert "testuser" in self.auth.users
    
    def test_register_user_duplicate(self):
        """Test registration with duplicate username."""
        self.auth.register_user("testuser", "test@example.com", "password123")
        result = self.auth.register_user("testuser", "test2@example.com", "password456")
        assert result is False
    
    def test_authenticate_success(self):
        """Test successful authentication."""
        self.auth.register_user("testuser", "test@example.com", "password123")
        token = self.auth.authenticate("testuser", "password123")
        assert token is not None
        assert isinstance(token, str)
    
    def test_authenticate_wrong_password(self):
        """Test authentication with wrong password."""
        self.auth.register_user("testuser", "test@example.com", "password123")
        token = self.auth.authenticate("testuser", "wrongpassword")
        assert token is None
    
    def test_authenticate_nonexistent_user(self):
        """Test authentication with non-existent user."""
        token = self.auth.authenticate("nonexistent", "password123")
        assert token is None
    
    def test_verify_session_valid(self):
        """Test verifying a valid session."""
        self.auth.register_user("testuser", "test@example.com", "password123")
        token = self.auth.authenticate("testuser", "password123")
        user = self.auth.verify_session(token)
        assert user is not None
        assert user.username == "testuser"
    
    def test_verify_session_invalid(self):
        """Test verifying an invalid session."""
        user = self.auth.verify_session("invalid_token")
        assert user is None
    
    def test_logout_success(self):
        """Test successful logout."""
        self.auth.register_user("testuser", "test@example.com", "password123")
        token = self.auth.authenticate("testuser", "password123")
        result = self.auth.logout(token)
        assert result is True
        assert self.auth.verify_session(token) is None
    
    def test_logout_invalid_token(self):
        """Test logout with invalid token."""
        result = self.auth.logout("invalid_token")
        assert result is False
    
    def test_deactivate_user(self):
        """Test deactivating a user."""
        self.auth.register_user("testuser", "test@example.com", "password123")
        token = self.auth.authenticate("testuser", "password123")
        result = self.auth.deactivate_user("testuser")
        assert result is True
        assert not self.auth.users["testuser"].is_active
        assert self.auth.authenticate("testuser", "password123") is None
