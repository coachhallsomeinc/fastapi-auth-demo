#import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.expression import text
#
from typing import List

from app.db.base_class import Base
#

#BADGE MODEL - PARENT
class Badge(Base):
    __tablename__ = "badges"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
# foreign key connecter to business
    title: Mapped[str] = Column(String, index=True, nullable=False)
    description: Mapped[str] = Column(String, default="Description", nullable=False)
    color_hex: Mapped[str] = Column(String, default="Color Hex Code", nullable=False)
    icon_url: Mapped[str] = Column(String, default="Icon URL", nullable=False)
    created_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=True, server_default=text('now()'))

# relationship
    #from app.models.user import UserBadge
    #users  = relationship("UserBadge", back_populates="badge")
    #collection_trackers = relationship("CollectionTrackerBadge", back_populates="badge")
