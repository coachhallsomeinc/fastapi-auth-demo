
#import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.expression import text

from app.schemas.user import User
from app.schemas.business import Business

from app.db.base_class import Base

#REVIEW MODEL - PARENT
class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#? foreign key connecter to user
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

#? foreign key connector to business
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("businesses.id"))

    body: Mapped[str] = Column(String, default="Body Text", nullable=True)
    star_rating: Mapped[int] = Column(Integer, nullable=True)
    created_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=True, server_default=text('now()'))

#? foreign key relationships
    
    user = relationship("User", back_populates="reviews", uselist=False)
    business = relationship("Business", back_populates="reviews", uselist=False)
