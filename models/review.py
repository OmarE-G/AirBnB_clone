#!/usr/bin/python3
""" review class module """


from models.base_model import BaseModel


class Review(BaseModel):
    """review Class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init():
        super().__init__()
