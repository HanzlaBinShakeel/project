"""
Utility functions for the application.
"""


def validate_input(value: str) -> float:
    """
    Validate and convert input to float.
    
    Args:
        value: String value to validate
        
    Returns:
        Float value
        
    Raises:
        ValueError: If value cannot be converted to float
    """
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid input: {value} is not a number")


def format_result(value: float, precision: int = 2) -> str:
    """
    Format a float result with specified precision.
    
    Args:
        value: Float value to format
        precision: Number of decimal places
        
    Returns:
        Formatted string
    """
    return f"{value:.{precision}f}"
