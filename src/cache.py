"""
Caching module with TTL support.
"""

from typing import Any, Optional, Dict
from datetime import datetime, timedelta


class Cache:
    """Simple in-memory cache with TTL support."""
    
    def __init__(self, default_ttl: int = 3600):
        """
        Initialize cache.
        
        Args:
            default_ttl: Default time-to-live in seconds
        """
        self._cache: Dict[str, tuple] = {}
        self.default_ttl = default_ttl
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """
        Set a value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (uses default if None)
        """
        ttl = ttl or self.default_ttl
        expires_at = datetime.now() + timedelta(seconds=ttl)
        self._cache[key] = (value, expires_at)
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value from cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None if not found or expired
        """
        if key not in self._cache:
            return None
        
        value, expires_at = self._cache[key]
        if datetime.now() > expires_at:
            del self._cache[key]
            return None
        
        return value
    
    def delete(self, key: str) -> bool:
        """
        Delete a key from cache.
        
        Args:
            key: Cache key
            
        Returns:
            True if key was deleted, False if not found
        """
        if key in self._cache:
            del self._cache[key]
            return True
        return False
    
    def clear(self):
        """Clear all cache entries."""
        self._cache.clear()
    
    def size(self) -> int:
        """
        Get number of cache entries.
        
        Returns:
            Number of entries in cache
        """
        # Clean expired entries
        now = datetime.now()
        expired_keys = [
            key for key, (_, expires_at) in self._cache.items()
            if now > expires_at
        ]
        for key in expired_keys:
            del self._cache[key]
        
        return len(self._cache)
    
    def has(self, key: str) -> bool:
        """
        Check if key exists and is not expired.
        
        Args:
            key: Cache key
            
        Returns:
            True if key exists and is valid, False otherwise
        """
        return self.get(key) is not None
