#!/usr/bin/env python3
"""
Auth model for the api
"""
from typing import *
from flask import request


class Auth:
    """ The authentication class for all paths
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns path that requre auth"""
        if path == None:
            return True

        if excluded_paths == None:
            return True
    def authorization_header(self, request=None) -> str:
        """returns the flask object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user"""
        return None
