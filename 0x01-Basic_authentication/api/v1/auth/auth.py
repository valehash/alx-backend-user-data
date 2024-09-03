#!/usr/bin/env python3
"""
Auth model for the api
"""
from typing import *
from flask import request


class Auth:
    """
    The authentication class for all paths,
    it handles which paths need authtication
    and which ones do not
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns path that requre auth
        input: path:str excluded_paths:List[str]
        returns:bool
        """
        if path is None:
            return True
        if excluded_paths is None:
            return True

    def authorization_header(self, request=None) -> str:
        """returns the flask object
        input:request
        returns:str
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user
        input:request
        returns:TypeVar
        """
        return None
