#!/usr/bin/env python3
"""
Basic Auth model for the api
"""
import base64
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """"Function that decodes the  base64 string
        params(self, base64_aurization heaser : str)
        returns: str
        """
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str):
            try:
                decoded_mess = base64.b64decode(base64_authorization_header)
                return decoded_mess.decode("utf-8")
            except (base64.binascii.Error, UnicodeDecodeError):
                return None
        return None
