"""
Tests for the APIClient class.
"""

import pytest
from src.api_client import APIClient


class TestAPIClient:
    """Test suite for APIClient class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.client = APIClient("https://api.example.com")
    
    def test_initialization(self):
        """Test client initialization."""
        assert self.client.base_url == "https://api.example.com"
        assert "Content-Type" in self.client.headers
    
    def test_set_header(self):
        """Test setting custom header."""
        self.client.set_header("Authorization", "Bearer token123")
        assert self.client.headers["Authorization"] == "Bearer token123"
    
    def test_build_url(self):
        """Test building full URL."""
        url = self.client.build_url("users")
        assert url == "https://api.example.com/users"
    
    def test_build_url_with_slash(self):
        """Test building URL with leading slash."""
        url = self.client.build_url("/users")
        assert url == "https://api.example.com/users"
    
    def test_get_request(self):
        """Test GET request."""
        response = self.client.get("users", params={"page": 1})
        assert response["method"] == "GET"
        assert response["params"] == {"page": 1}
    
    def test_post_request(self):
        """Test POST request."""
        data = {"name": "John", "email": "john@example.com"}
        response = self.client.post("users", data=data)
        assert response["method"] == "POST"
        assert response["data"] == data
    
    def test_put_request(self):
        """Test PUT request."""
        data = {"name": "Jane"}
        response = self.client.put("users/1", data=data)
        assert response["method"] == "PUT"
        assert response["data"] == data
    
    def test_delete_request(self):
        """Test DELETE request."""
        response = self.client.delete("users/1")
        assert response["method"] == "DELETE"
    
    def test_base_url_trailing_slash(self):
        """Test base URL with trailing slash."""
        client = APIClient("https://api.example.com/")
        assert client.base_url == "https://api.example.com"
