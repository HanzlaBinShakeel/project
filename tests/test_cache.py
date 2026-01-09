"""
Tests for the Cache class.
"""

import pytest
import time
from src.cache import Cache


class TestCache:
    """Test suite for Cache class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.cache = Cache(default_ttl=1)
    
    def test_set_and_get(self):
        """Test setting and getting values."""
        self.cache.set("key1", "value1")
        assert self.cache.get("key1") == "value1"
    
    def test_get_nonexistent_key(self):
        """Test getting non-existent key."""
        assert self.cache.get("nonexistent") is None
    
    def test_set_with_custom_ttl(self):
        """Test setting value with custom TTL."""
        self.cache.set("key1", "value1", ttl=2)
        assert self.cache.get("key1") == "value1"
        time.sleep(2.1)
        assert self.cache.get("key1") is None
    
    def test_expiration(self):
        """Test cache expiration."""
        self.cache.set("key1", "value1", ttl=1)
        assert self.cache.get("key1") == "value1"
        time.sleep(1.1)
        assert self.cache.get("key1") is None
    
    def test_delete(self):
        """Test deleting a key."""
        self.cache.set("key1", "value1")
        assert self.cache.delete("key1") is True
        assert self.cache.get("key1") is None
        assert self.cache.delete("nonexistent") is False
    
    def test_clear(self):
        """Test clearing all cache."""
        self.cache.set("key1", "value1")
        self.cache.set("key2", "value2")
        self.cache.clear()
        assert self.cache.get("key1") is None
        assert self.cache.get("key2") is None
    
    def test_size(self):
        """Test getting cache size."""
        assert self.cache.size() == 0
        self.cache.set("key1", "value1")
        assert self.cache.size() == 1
        self.cache.set("key2", "value2")
        assert self.cache.size() == 2
    
    def test_has(self):
        """Test checking if key exists."""
        assert self.cache.has("key1") is False
        self.cache.set("key1", "value1")
        assert self.cache.has("key1") is True
        time.sleep(1.1)
        assert self.cache.has("key1") is False
    
    def test_size_with_expired_entries(self):
        """Test size calculation with expired entries."""
        self.cache.set("key1", "value1", ttl=1)
        self.cache.set("key2", "value2", ttl=1)
        assert self.cache.size() == 2
        time.sleep(1.1)
        assert self.cache.size() == 0
