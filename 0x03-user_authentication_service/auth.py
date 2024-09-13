#!/usr/bin/env python3
"""
Authorization file
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import Bool

def _hash_password(pwd: str) -> bytes:
    """Function to create a hashed password from a string"""
    pwd = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(pwd, salt)
    return hash_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """The unut method"""
        self._db = DB()

    def register_user(self, email: str, pwd: str) -> User:
        """
        Register user adds a new user if the email does not exist yet
        args:
            email: str - the users email
            pwd: str - regular password the user inputs
        returns:
            returns A user objext
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            passw = _hash_password(pwd)
            user = self._db.add_user(email, passw)
            return user
        raise ValueError(f"user {email} already exists")

    def valid_login(self, email: str, passw: str) -> bool:
        """Valid_login returns true if the the login exist"""
        try:
            # finding out if user exist and assigning if it does
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        # using bycrypt to check if the password matcheds the user in the db
        return bcrypt.checkpw(passw.encode("utf-8"), user.hashed_password)
