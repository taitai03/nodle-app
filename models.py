from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

db = SQLAlchemy()

class Shop(db.Model):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    cashless = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Shop(name='{self.name}', address='{self.address}')>"