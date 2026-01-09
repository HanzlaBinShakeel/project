"""
API client module for making HTTP requests.
"""

from typing import Dict, Optional, Any
import json


class APIClient:
    """Client for making API requests."""
    
    def __init__(self, base_url: str):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for API requests
        """
        self.base_url = base_url.rstrip('/')
        self.headers = {"Content-Type": "application/json"}
    
    def set_header(self, key: str, value: str):
        """
        Set a custom header.
        
        Args:
            key: Header key
            value: Header value
        """
        self.headers[key] = value
    
    def build_url(self, endpoint: str) -> str:
        """
        Build full URL from endpoint.
        
        Args:
            endpoint: API endpoint
            
        Returns:
            Full URL
        """
        endpoint = endpoint.lstrip('/')
        return f"{self.base_url}/{endpoint}"
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make GET request.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            
        Returns:
            Response data as dictionary
        """
        url = self.build_url(endpoint)
        # Simulated response for demonstration
        return {"status": "success", "url": url, "method": "GET", "params": params or {}}
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make POST request.
        
        Args:
            endpoint: API endpoint
            data: Request body data
            
        Returns:
            Response data as dictionary
        """
        url = self.build_url(endpoint)
        # Simulated response for demonstration
        return {"status": "success", "url": url, "method": "POST", "data": data or {}}
    
    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make PUT request.
        
        Args:
            endpoint: API endpoint
            data: Request body data
            
        Returns:
            Response data as dictionary
        """
        url = self.build_url(endpoint)
        # Simulated response for demonstration
        return {"status": "success", "url": url, "method": "PUT", "data": data or {}}
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """
        Make DELETE request.
        
        Args:
            endpoint: API endpoint
            
        Returns:
            Response data as dictionary
        """
        url = self.build_url(endpoint)
        # Simulated response for demonstration
        return {"status": "success", "url": url, "method": "DELETE"}
