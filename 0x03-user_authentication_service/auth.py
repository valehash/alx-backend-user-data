#!/usr/bin/env python3
"""
Authorization file
"""

import bcrypt


def _hash_password(pwd:str) -> bytes:
    """Function to create a hashed password from a string"""
    pwd = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password =  bcrypt.hashpw(pwd, salt)
    return hash_password
