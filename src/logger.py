"""
Logging module with different log levels and formatting.
"""

from enum import Enum
from datetime import datetime
from typing import Optional


class LogLevel(Enum):
    """Log level enumeration."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Logger:
    """Simple logging utility."""
    
    def __init__(self, name: str, level: LogLevel = LogLevel.INFO):
        """
        Initialize logger.
        
        Args:
            name: Logger name
            level: Minimum log level
        """
        self.name = name
        self.level = level
        self.logs = []
    
    def _log(self, level: LogLevel, message: str, **kwargs):
        """
        Internal logging method.
        
        Args:
            level: Log level
            message: Log message
            **kwargs: Additional context
        """
        if level.value >= self.level.value:
            timestamp = datetime.now().isoformat()
            log_entry = {
                "timestamp": timestamp,
                "level": level.value,
                "logger": self.name,
                "message": message,
                **kwargs
            }
            self.logs.append(log_entry)
            print(f"[{timestamp}] {level.value} [{self.name}] {message}")
    
    def debug(self, message: str, **kwargs):
        """Log debug message."""
        self._log(LogLevel.DEBUG, message, **kwargs)
    
    def info(self, message: str, **kwargs):
        """Log info message."""
        self._log(LogLevel.INFO, message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message."""
        self._log(LogLevel.WARNING, message, **kwargs)
    
    def error(self, message: str, **kwargs):
        """Log error message."""
        self._log(LogLevel.ERROR, message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        """Log critical message."""
        self._log(LogLevel.CRITICAL, message, **kwargs)
    
    def get_logs(self, level: Optional[LogLevel] = None) -> list:
        """
        Get log entries, optionally filtered by level.
        
        Args:
            level: Optional log level filter
            
        Returns:
            List of log entries
        """
        if level:
            return [log for log in self.logs if log["level"] == level.value]
        return self.logs.copy()
    
    def clear_logs(self):
        """Clear all log entries."""
        self.logs.clear()
