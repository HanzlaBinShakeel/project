"""
Tests for the DataProcessor class.
"""

import pytest
from src.data_processor import DataProcessor


class TestDataProcessor:
    """Test suite for DataProcessor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.processor = DataProcessor()
        self.sample_data = [
            {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
            {"id": 2, "name": "Bob", "age": 25, "city": "London"},
            {"id": 3, "name": "Charlie", "age": 35, "city": "New York"},
            {"id": 4, "name": "David", "age": 28, "city": "Paris"},
        ]
    
    def test_filter_data_by_key_value(self):
        """Test filtering data by key-value pair."""
        result = self.processor.filter_data(self.sample_data, "city", "New York")
        assert len(result) == 2
        assert all(item["city"] == "New York" for item in result)
    
    def test_filter_data_no_matches(self):
        """Test filtering with no matches."""
        result = self.processor.filter_data(self.sample_data, "city", "Tokyo")
        assert len(result) == 0
    
    def test_sort_data_ascending(self):
        """Test sorting data in ascending order."""
        result = self.processor.sort_data(self.sample_data, "age")
        assert result[0]["age"] == 25
        assert result[-1]["age"] == 35
    
    def test_sort_data_descending(self):
        """Test sorting data in descending order."""
        result = self.processor.sort_data(self.sample_data, "age", reverse=True)
        assert result[0]["age"] == 35
        assert result[-1]["age"] == 25
    
    def test_aggregate_data(self):
        """Test aggregating data by key."""
        result = self.processor.aggregate_data(self.sample_data, "city")
        assert result["New York"] == 2
        assert result["London"] == 1
        assert result["Paris"] == 1
    
    def test_transform_data(self):
        """Test transforming data by renaming keys."""
        mapping = {"name": "full_name", "age": "years"}
        result = self.processor.transform_data(self.sample_data, mapping)
        assert "full_name" in result[0]
        assert "years" in result[0]
        assert "name" not in result[0]
    
    def test_merge_data(self):
        """Test merging two datasets."""
        data1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        data2 = [{"id": 1, "email": "alice@example.com"}, {"id": 2, "email": "bob@example.com"}]
        result = self.processor.merge_data(data1, data2, "id")
        assert len(result) == 2
        assert result[0]["email"] == "alice@example.com"
        assert result[1]["email"] == "bob@example.com"
    
    def test_calculate_statistics(self):
        """Test calculating statistics."""
        result = self.processor.calculate_statistics(self.sample_data, "age")
        assert result["count"] == 4
        assert result["sum"] == 118
        assert result["avg"] == 29.5
        assert result["min"] == 25
        assert result["max"] == 35
    
    def test_calculate_statistics_empty_data(self):
        """Test calculating statistics with empty data."""
        result = self.processor.calculate_statistics([], "age")
        assert result["count"] == 0
        assert result["sum"] == 0
