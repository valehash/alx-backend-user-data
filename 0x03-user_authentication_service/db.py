#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, insert, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """New user object creation"""
        new_user = User(
            email=email,
            hashed_password=hashed_password
        )
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        for k, v in kwargs.items():
            key_word = k
            value = v
        if hasattr(User, key_word):
            users = self._session.query(User)
            for user in users:
                if getattr(user, key_word) == value:
                    return user
                raise NoResultFound
        raise InvalidRequestError

    
    def update_user(self, user_id: int, **kwargs) -> None:
        try:
            user = self.find_user_by(id = user_id)
        except NoResultFound:
            raise ValueError
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)
            self._session.commit()

