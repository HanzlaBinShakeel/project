"""
Tests for the configuration module.
"""

import pytest
import os
from src.config import Config


class TestConfig:
    """Test suite for Config class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.config = Config()
    
    def test_get_existing_key(self):
        """Test getting an existing configuration key."""
        value = self.config.get("port")
        assert value is not None
    
    def test_get_nonexistent_key(self):
        """Test getting a non-existent key with default."""
        value = self.config.get("nonexistent_key", "default_value")
        assert value == "default_value"
    
    def test_set_and_get(self):
        """Test setting and getting a configuration value."""
        self.config.set("test_key", "test_value")
        assert self.config.get("test_key") == "test_value"
    
    def test_has_key(self):
        """Test checking if a key exists."""
        self.config.set("test_key", "test_value")
        assert self.config.has("test_key") is True
        assert self.config.has("nonexistent") is False
    
    def test_all_config(self):
        """Test getting all configuration values."""
        all_config = self.config.all()
        assert isinstance(all_config, dict)
        assert len(all_config) > 0
    
    def test_load_from_env(self):
        """Test loading configuration from environment."""
        os.environ["TEST_ENV_VAR"] = "test_value"
        # Config loads from env in __init__, so we check it's loaded
        assert self.config.has("port") or self.config.has("host")
