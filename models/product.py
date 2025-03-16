from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Product(BaseModel, Base):
    """user table model"""

    name = Column(String(128), nullable=False)
    description = Column(String(500), nullable=False)
    product_image = Column(String(128), nullable=False)
    price = Column(String(64), nullable=False)

    # more to be implemantted
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
