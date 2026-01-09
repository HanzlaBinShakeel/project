"""
Authentication module with user management and security features.
"""

from typing import Optional, Dict
import hashlib
import secrets


class User:
    """User model for authentication."""
    
    def __init__(self, username: str, email: str, password_hash: str):
        """
        Initialize user.
        
        Args:
            username: User's username
            email: User's email
            password_hash: Hashed password
        """
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.is_active = True
        self.is_verified = False


class AuthManager:
    """Manages user authentication and authorization."""
    
    def __init__(self):
        """Initialize authentication manager."""
        self.users: Dict[str, User] = {}
        self.sessions: Dict[str, str] = {}
    
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password using SHA-256.
        
        Args:
            password: Plain text password
            
        Returns:
            Hashed password
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username: str, email: str, password: str) -> bool:
        """
        Register a new user.
        
        Args:
            username: User's username
            email: User's email
            password: Plain text password
            
        Returns:
            True if registration successful, False if user exists
        """
        if username in self.users:
            return False
        
        password_hash = self.hash_password(password)
        user = User(username, email, password_hash)
        self.users[username] = user
        return True
    
    def authenticate(self, username: str, password: str) -> Optional[str]:
        """
        Authenticate a user and create a session.
        
        Args:
            username: User's username
            password: Plain text password
            
        Returns:
            Session token if successful, None otherwise
        """
        if username not in self.users:
            return None
        
        user = self.users[username]
        password_hash = self.hash_password(password)
        
        if user.password_hash != password_hash:
            return None
        
        if not user.is_active:
            return None
        
        session_token = secrets.token_urlsafe(32)
        self.sessions[session_token] = username
        return session_token
    
    def verify_session(self, session_token: str) -> Optional[User]:
        """
        Verify a session token and return user.
        
        Args:
            session_token: Session token
            
        Returns:
            User object if valid, None otherwise
        """
        if session_token not in self.sessions:
            return None
        
        username = self.sessions[session_token]
        if username not in self.users:
            return None
        
        return self.users[username]
    
    def logout(self, session_token: str) -> bool:
        """
        Logout a user by invalidating session.
        
        Args:
            session_token: Session token
            
        Returns:
            True if logout successful, False otherwise
        """
        if session_token in self.sessions:
            del self.sessions[session_token]
            return True
        return False
    
    def deactivate_user(self, username: str) -> bool:
        """
        Deactivate a user account.
        
        Args:
            username: User's username
            
        Returns:
            True if deactivation successful, False otherwise
        """
        if username not in self.users:
            return False
        
        self.users[username].is_active = False
        # Invalidate all sessions for this user
        tokens_to_remove = [
            token for token, user in self.sessions.items()
            if user == username
        ]
        for token in tokens_to_remove:
            del self.sessions[token]
        
        return True
