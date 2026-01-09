"""
Input validation module with various validation functions.
"""

import re
from typing import Optional, List, Callable


class Validator:
    """Input validation utility class."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email address format.
        
        Args:
            email: Email address to validate
            
        Returns:
            True if valid, False otherwise
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_username(username: str, min_length: int = 3, max_length: int = 20) -> bool:
        """
        Validate username format.
        
        Args:
            username: Username to validate
            min_length: Minimum length
            max_length: Maximum length
            
        Returns:
            True if valid, False otherwise
        """
        if not username:
            return False
        if len(username) < min_length or len(username) > max_length:
            return False
        # Only alphanumeric and underscore
        pattern = r'^[a-zA-Z0-9_]+$'
        return bool(re.match(pattern, username))
    
    @staticmethod
    def validate_password(password: str, min_length: int = 8) -> bool:
        """
        Validate password strength.
        
        Args:
            password: Password to validate
            min_length: Minimum length
            
        Returns:
            True if valid, False otherwise
        """
        if not password:
            return False
        if len(password) < min_length:
            return False
        # At least one letter and one number
        has_letter = bool(re.search(r'[a-zA-Z]', password))
        has_number = bool(re.search(r'[0-9]', password))
        return has_letter and has_number
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """
        Validate URL format.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid, False otherwise
        """
        pattern = r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$'
        return bool(re.match(pattern, url))
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validate phone number format.
        
        Args:
            phone: Phone number to validate
            
        Returns:
            True if valid, False otherwise
        """
        # Remove common separators
        cleaned = re.sub(r'[\s\-\(\)]', '', phone)
        # Check if it's all digits and reasonable length
        pattern = r'^\+?[1-9]\d{9,14}$'
        return bool(re.match(pattern, cleaned))
    
    @staticmethod
    def validate_custom(value: str, pattern: str) -> bool:
        """
        Validate using custom regex pattern.
        
        Args:
            value: Value to validate
            pattern: Regex pattern
            
        Returns:
            True if valid, False otherwise
        """
        try:
            return bool(re.match(pattern, value))
        except re.error:
            return False
