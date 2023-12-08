#import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.expression import text
from typing import List
#from datetime import datetime
#from app.schemas import UserInDB
from app.models.tag import Tag

from app.db.base_class import Base

#BUSINESS MODEL - PARENT
class Business(Base):
    __tablename__ = "businesses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name", nullable=False)
    address: Mapped[str] = Column(String, default="Address", nullable=False)
    city: Mapped[str] = Column(String, default="City", nullable=False)
    state: Mapped[str] = Column(String(), default="State", nullable=False)
    postal_code: Mapped[str] = Column(String(), default="Postal Code", nullable=False)
# add to given user model...
    latitude: Mapped[float] = Column(Float, nullable=False)
    longitude: Mapped[float] = Column(Float, nullable=False)
    created_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=False, server_default=text('now()')) #change to DateTime?
    updated_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=True, server_default=text('now()')) #change to DateTime?
# where a business pic would be added ---> logo_pic = Column()

# relationships? do i need anything here or is that only in my child/pivots?
    tags = relationship("BusinessTag", back_populates="business")
    #BusinessTag refers to child class
    #businesses refers to businesses relationship under child
    reviews = relationship("Review", back_populates="business")
    drinks = relationship("Drink", back_populates="business")

#! pivot/child
class BusinessTag (Base):
    __tablename__ = "business_tags"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    business_id: Mapped[int] = mapped_column(ForeignKey("businesses.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))

# relationship
    business = relationship("Business", back_populates="tags")
    tag = relationship("Tag", back_populates="business")
    #tag has businesses relationship
