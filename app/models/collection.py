#import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB
from typing import List

# from app.models.drink import Drink
# from app.models.badge import Badge
# from app.models.user import User

from app.db.base_class import Base

#TRACKER/COLLECTION MODEL - PARENT
class Collection(Base):
    __tablename__ = "collection_trackers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#? foreign key AND relationship
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    title: Mapped[str] = Column(String, default="Name", index=True)
# where a list image would be added ---> logo_pic = Column()
    ordered_list_number: Mapped[int] = Column(Integer, nullable=True)
    contact_info: Mapped[str] = Column(String, default="Contact Info", nullable=True)
    website_url: Mapped[str] = Column(String, default="Website URL", nullable=True)
    instagram_handle: Mapped[str] = Column(String, default="Insta Handle", nullable=True)
    event_promotion_time_start: Mapped[DateTime] = Column(DateTime(timezone=True), default="Event Start Date", nullable=True, server_default=text('now()'))
    event_promotion_time_stop: Mapped[DateTime] = Column(DateTime(timezone=True), default="Event End Date", nullable=True, server_default=text('now()'))
    event_promotion_banner: Mapped[str] = Column(String, nullable=True)
    favorite: Mapped[bool] = Column(Boolean(), nullable=False) #compare to is superuser?
    created_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=True, server_default=text('now()'))

#*PARENT relationship to child table CollectionTrackerDrink
    #drinks = relationship("CollectionTrackerDrink", back_populates="collection_tracker")
    #badges = relationship("CollectionTrackerBadge", back_populates="collection_tracker")

#*PARENT relationship to PARENT
    #user = relationship("User", back_populates="collection_trackers")


#! pivot/child Collection drinks
class CollectionTrackerDrink (Base):
    __tablename__ = "collection_tracker_drinks"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    collection_tracker_id: Mapped[int] = mapped_column(ForeignKey("collection_trackers.id"))
    drink_id: Mapped[int] = mapped_column(ForeignKey("drinks.id"))

# relationships to parents
    #collection_tracker = relationship("Collection" , back_populates="drinks")
    #drink = relationship("Drink", back_populates="collection_trackers")


#! pivot/child Collection drinks
class CollectionTrackerBadge (Base):
    __tablename__ = "collection_tracker_badges"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    collection_tracker_id: Mapped[int] = mapped_column(ForeignKey("collection_trackers.id"))
    badge_id: Mapped[int] = mapped_column(ForeignKey("badges.id"))

# relationship to parents
    #collection_tracker = relationship("Collection", back_populates="badges")
    #badge = relationship("Badge", back_populates="collection_trackers")
