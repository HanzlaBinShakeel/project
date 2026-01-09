"""
Main application module.
"""

from .calculator import Calculator
from .utils import validate_input


def main():
    """Main application entry point."""
    calc = Calculator()
    print("Calculator Application")
    print("=" * 30)
    
    # Example operations
    result1 = calc.add(10, 5)
    result2 = calc.multiply(4, 7)
    result3 = calc.divide(20, 4)
    
    print(f"10 + 5 = {result1}")
    print(f"4 * 7 = {result2}")
    print(f"20 / 4 = {result3}")


if __name__ == "__main__":
    main()
