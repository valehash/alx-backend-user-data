#!/usr/bin/env python3
"""
Basic Auth model for the api
"""
from .auth import Auth
from typing import List, TypeVar
from flask import request


class BasicAuth(Auth):
    """ The authentication class for all paths,
    Inherits from auth.py
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Function that encodes the autohrization header
        params:(self, auth_header: str)
        returns: str
        """
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str):
            if authorization_header.startswith("Basic "):
                return authorization_header.split(" ")[1:][0]
            return None
        return None
