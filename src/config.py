"""
Configuration management module.
"""

import os
from typing import Optional, Dict, Any


class Config:
    """Application configuration manager."""
    
    def __init__(self):
        """Initialize configuration."""
        self._config: Dict[str, Any] = {}
        self._load_from_env()
    
    def _load_from_env(self):
        """Load configuration from environment variables."""
        self._config = {
            "debug": os.getenv("DEBUG", "False").lower() == "true",
            "port": int(os.getenv("PORT", "8000")),
            "host": os.getenv("HOST", "localhost"),
            "database_url": os.getenv("DATABASE_URL", ""),
            "secret_key": os.getenv("SECRET_KEY", ""),
            "log_level": os.getenv("LOG_LEVEL", "INFO"),
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """
        Set configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self._config[key] = value
    
    def has(self, key: str) -> bool:
        """
        Check if configuration key exists.
        
        Args:
            key: Configuration key
            
        Returns:
            True if key exists, False otherwise
        """
        return key in self._config
    
    def all(self) -> Dict[str, Any]:
        """
        Get all configuration values.
        
        Returns:
            Dictionary of all configuration values
        """
        return self._config.copy()
