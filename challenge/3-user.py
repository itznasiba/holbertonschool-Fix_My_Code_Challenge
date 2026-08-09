#!/usr/bin/python3
"""
User class
"""
import hashlib
import uuid


class User:
    """ User class representation """

    def __init__(self):
        """ Constructor """
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        """ Password getter """
        return self.__password

    @password.setter
    def password(self, password):
        """ Password setter """
        if password is None or type(password) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(password.encode()).hexdigest().lower()

    def is_valid_password(self, password):
        """ Check if password is valid """
        if password is None or type(password) is not str:
            return False
        if self.__password is None:
            return False
        return self.__password == hashlib.md5(password.encode()).hexdigest().lower()


if __name__ == "__main__":
    print("Test User")
    user_1 = User()
    user_1.password = "Documentation"
    if user_1.is_valid_password("Documentation"):
        print("is_valid_password should return True if it's the right password")
    else:
        print("is_valid_password returning False on valid password")
