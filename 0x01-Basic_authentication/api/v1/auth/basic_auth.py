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
