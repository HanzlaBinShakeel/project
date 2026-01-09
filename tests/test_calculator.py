"""
Tests for the Calculator class.
"""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(-10, 5) == -5
    
    def test_add_zero(self):
        """Test addition with zero."""
        assert self.calc.add(5, 0) == 5
        assert self.calc.add(0, 10) == 10
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert self.calc.subtract(10, 3) == 7
        assert self.calc.subtract(20, 5) == 15
    
    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        assert self.calc.subtract(5, -3) == 8
        assert self.calc.subtract(-10, -5) == -5
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert self.calc.multiply(5, 3) == 15
        assert self.calc.multiply(10, 4) == 40
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 10) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        assert self.calc.multiply(-5, 3) == -15
        assert self.calc.multiply(-5, -3) == 15
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert self.calc.divide(10, 2) == 5.0
        assert self.calc.divide(15, 3) == 5.0
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_divide_negative_numbers(self):
        """Test division of negative numbers."""
        assert self.calc.divide(-10, 2) == -5.0
        assert self.calc.divide(10, -2) == -5.0
        assert self.calc.divide(-10, -2) == 5.0
    
    def test_history_tracking(self):
        """Test that calculations are tracked in history."""
        self.calc.add(5, 3)
        self.calc.multiply(2, 4)
        history = self.calc.get_history()
        assert len(history) == 2
        assert "5 + 3 = 8" in history
        assert "2 * 4 = 8" in history
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(5, 3)
        self.calc.multiply(2, 4)
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0
    
    def test_float_operations(self):
        """Test operations with floating point numbers."""
        assert self.calc.add(1.5, 2.5) == 4.0
        assert self.calc.multiply(2.5, 4.0) == 10.0
        assert self.calc.divide(7.5, 2.5) == 3.0
