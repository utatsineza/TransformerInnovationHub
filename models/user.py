from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """user table model"""

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    phonenumber = Column(String(128), nullable=False)
    username = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
