from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

#! from perspective of dev/admin - info needed to create/update/delete an event collection
#! from perspective of an anonymous/authorized user - info given back to read an event collection
#! from perspective of an authorized user - create/update/delete their own collections
# consider CRUD

from app.schemas.drink import Drink
from app.schemas.user import User

'''
TODO:
- base schema
- create schema
- update schema
- endpoint
- add to schema init file
- add router to api file
'''

class CollectionBase(BaseModel):
    user_id: int #? foreign keyconnect to user?
    title: str
    ordered_list_number: int
    contact_info: Optional[str] = None
    website_url: Optional[str] = None
    instagram_handle: Optional[str] = None
    event_promotion_time_start: Optional[datetime] = None
    event_promotion_time_stop: Optional[datetime] = None
    favorite: Optional[bool] = None
    created_timestamp: Optional[datetime] = None
    updated_timestamp: Optional[datetime] = None

#!CREATE - dev
class CollectionCreate(CollectionBase):
    pass

#!UPDATE - dev
class CollectionUpdate(CollectionBase):
    pass

#!IN DB - dev
class CollectionInDBBase(CollectionBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

# business that inherits from business in db base to include EVERYTHING
#! Collection
class Collection(CollectionInDBBase):
    
    drinks: List["Drink"]
    user: List["User"]
