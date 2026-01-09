"""
Tests for utility functions.
"""

import pytest
from src.utils import validate_input, format_result


class TestValidateInput:
    """Test suite for validate_input function."""
    
    def test_valid_integer_string(self):
        """Test validation of integer string."""
        assert validate_input("5") == 5.0
        assert validate_input("10") == 10.0
    
    def test_valid_float_string(self):
        """Test validation of float string."""
        assert validate_input("5.5") == 5.5
        assert validate_input("10.25") == 10.25
    
    def test_invalid_string(self):
        """Test validation of invalid string."""
        with pytest.raises(ValueError, match="Invalid input"):
            validate_input("abc")
        with pytest.raises(ValueError, match="Invalid input"):
            validate_input("not a number")
    
    def test_empty_string(self):
        """Test validation of empty string."""
        with pytest.raises(ValueError):
            validate_input("")


class TestFormatResult:
    """Test suite for format_result function."""
    
    def test_default_precision(self):
        """Test formatting with default precision."""
        assert format_result(5.123456) == "5.12"
        assert format_result(10.999) == "11.00"
    
    def test_custom_precision(self):
        """Test formatting with custom precision."""
        assert format_result(5.123456, precision=4) == "5.1235"
        assert format_result(10.999, precision=0) == "11"
    
    def test_zero_precision(self):
        """Test formatting with zero precision."""
        assert format_result(5.7, precision=0) == "6"
        assert format_result(10.3, precision=0) == "10"
    
    def test_negative_numbers(self):
        """Test formatting of negative numbers."""
        assert format_result(-5.123) == "-5.12"
        assert format_result(-10.999) == "-11.00"
