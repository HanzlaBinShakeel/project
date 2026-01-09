"""
Data processing module with various data manipulation functions.
"""

from typing import List, Dict, Any, Optional
import json


class DataProcessor:
    """Process and manipulate data structures."""
    
    def __init__(self):
        """Initialize the data processor."""
        self.processed_items = []
    
    def filter_data(self, data: List[Dict], key: str, value: Any) -> List[Dict]:
        """
        Filter data by key-value pair.
        
        Args:
            data: List of dictionaries to filter
            key: Key to filter by
            value: Value to match
            
        Returns:
            Filtered list of dictionaries
        """
        return [item for item in data if item.get(key) == value]
    
    def sort_data(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        """
        Sort data by a key.
        
        Args:
            data: List of dictionaries to sort
            key: Key to sort by
            reverse: Whether to sort in reverse order
            
        Returns:
            Sorted list of dictionaries
        """
        return sorted(data, key=lambda x: x.get(key, 0), reverse=reverse)
    
    def aggregate_data(self, data: List[Dict], key: str) -> Dict[Any, int]:
        """
        Aggregate data by counting occurrences of a key.
        
        Args:
            data: List of dictionaries
            key: Key to aggregate by
            
        Returns:
            Dictionary with counts
        """
        result = {}
        for item in data:
            value = item.get(key)
            result[value] = result.get(value, 0) + 1
        return result
    
    def transform_data(self, data: List[Dict], mapping: Dict[str, str]) -> List[Dict]:
        """
        Transform data by renaming keys.
        
        Args:
            data: List of dictionaries
            mapping: Dictionary mapping old keys to new keys
            
        Returns:
            Transformed list of dictionaries
        """
        result = []
        for item in data:
            transformed = {}
            for old_key, new_key in mapping.items():
                if old_key in item:
                    transformed[new_key] = item[old_key]
            result.append(transformed)
        return result
    
    def merge_data(self, data1: List[Dict], data2: List[Dict], key: str) -> List[Dict]:
        """
        Merge two datasets on a common key.
        
        Args:
            data1: First list of dictionaries
            data2: Second list of dictionaries
            key: Key to merge on
            
        Returns:
            Merged list of dictionaries
        """
        lookup = {item[key]: item for item in data2}
        result = []
        for item in data1:
            if item.get(key) in lookup:
                merged = {**item, **lookup[item[key]]}
                result.append(merged)
        return result
    
    def calculate_statistics(self, data: List[Dict], key: str) -> Dict[str, float]:
        """
        Calculate statistics for a numeric key.
        
        Args:
            data: List of dictionaries
            key: Numeric key to calculate statistics for
            
        Returns:
            Dictionary with statistics
        """
        values = [item.get(key, 0) for item in data if isinstance(item.get(key), (int, float))]
        if not values:
            return {"count": 0, "sum": 0, "avg": 0, "min": 0, "max": 0}
        
        return {
            "count": len(values),
            "sum": sum(values),
            "avg": sum(values) / len(values),
            "min": min(values),
            "max": max(values)
        }
