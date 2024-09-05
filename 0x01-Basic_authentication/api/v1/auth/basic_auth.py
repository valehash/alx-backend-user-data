#!/usr/bin/env python3
"""
Basic Auth model for the api
"""
import base64
from .auth import Auth
from typing import List, TypeVar
from models.user import User
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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """function that returns the user email
        and password from the base64 decoded
        value """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if isinstance(decoded_base64_authorization_header, str):
            if ":" in decoded_base64_authorization_header:
                decb64 = decoded_base64_authorization_header
                return (decb64.split(":")[0], decb64.split(":")[1:][0])
            return (None, None)
        return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns the users instance based on thier credentials"""
         if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for u in users:
                if u.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns user Instances based on the requests"""
        if request:
            _auth_header = self.authorization_header(request)
            if _auth_header:
                extracted_auth = self.extract_base64_authorization_header(
                    _auth_header)
                if extracted_auth:
                    decoded_b64 = self.decode_base64_authorization_header(
                        extracted_auth)
                    if decoded_b64:
                        email, pword = self.extract_user_credentials(
                            decoded_b64)
                        if email:
                            return self.user_object_from_credentials(
                                email, pword)
        return None
