#!/usr/bin/python3
""" user class module """


from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self):
        super().__init__()
