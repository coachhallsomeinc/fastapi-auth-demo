#import sqlalchemy as sa
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB
from typing import List

# from app.models.business import Business
# from app.models.user import User

from app.db.base_class import Base

#TAG MODEL - PARENT
class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # foreign key connecter to business
    title: Mapped[str] = Column(String, default="Title", nullable=False)
    description: Mapped[str] = Column(String, default="Description", nullable=False)
    color_hex: Mapped[str] = Column(String, default="Color Hex Code", nullable=False)
    icon_url: Mapped[str] = Column(String, default="Icon URL", nullable=False)
    created_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=True, server_default=text('now()'))

    # relationships - connect back to child businesstag under business.py

    business = relationship("BusinessTag", back_populates="tag")
    # Businesses has tag
    user = relationship("UserTag", back_populates="tag")
