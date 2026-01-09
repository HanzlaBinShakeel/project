"""
Tests for the logger module.
"""

import pytest
from src.logger import Logger, LogLevel


class TestLogger:
    """Test suite for Logger class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.logger = Logger("test_logger", LogLevel.DEBUG)
    
    def test_log_info(self):
        """Test logging info message."""
        self.logger.info("Test info message")
        logs = self.logger.get_logs()
        assert len(logs) == 1
        assert logs[0]["level"] == "INFO"
        assert logs[0]["message"] == "Test info message"
    
    def test_log_debug(self):
        """Test logging debug message."""
        self.logger.debug("Test debug message")
        logs = self.logger.get_logs()
        assert len(logs) == 1
        assert logs[0]["level"] == "DEBUG"
    
    def test_log_warning(self):
        """Test logging warning message."""
        self.logger.warning("Test warning message")
        logs = self.logger.get_logs()
        assert len(logs) == 1
        assert logs[0]["level"] == "WARNING"
    
    def test_log_error(self):
        """Test logging error message."""
        self.logger.error("Test error message")
        logs = self.logger.get_logs()
        assert len(logs) == 1
        assert logs[0]["level"] == "ERROR"
    
    def test_log_critical(self):
        """Test logging critical message."""
        self.logger.critical("Test critical message")
        logs = self.logger.get_logs()
        assert len(logs) == 1
        assert logs[0]["level"] == "CRITICAL"
    
    def test_log_with_context(self):
        """Test logging with additional context."""
        self.logger.info("Test message", user_id=123, action="login")
        logs = self.logger.get_logs()
        assert logs[0]["user_id"] == 123
        assert logs[0]["action"] == "login"
    
    def test_log_level_filtering(self):
        """Test filtering logs by level."""
        self.logger.info("Info message")
        self.logger.error("Error message")
        self.logger.warning("Warning message")
        
        error_logs = self.logger.get_logs(LogLevel.ERROR)
        assert len(error_logs) == 1
        assert error_logs[0]["level"] == "ERROR"
    
    def test_clear_logs(self):
        """Test clearing logs."""
        self.logger.info("Message 1")
        self.logger.info("Message 2")
        self.logger.clear_logs()
        assert len(self.logger.get_logs()) == 0
    
    def test_log_level_threshold(self):
        """Test log level threshold filtering."""
        logger = Logger("test", LogLevel.WARNING)
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        
        logs = logger.get_logs()
        assert len(logs) == 1
        assert logs[0]["level"] == "WARNING"
