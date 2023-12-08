from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

#! from perspective of dev/admin - info needed to create/update/delete a tag
#! from perspective of a user - info given back to read a tag
# consider CRUD
#? do i need class config anywhere?
#from app.schemas.business import Business
#from app.schemas.user import User

'''
TODO:
- base schema
- create schema
- update schema
'''

class TagBase(BaseModel):
    title: str
    description: str
    color_hex: str
    icon_url: str
    created_timestamp: datetime
    updated_timestamp: datetime

#!CREATE - dev
class TagCreate(TagBase):
    pass

#!UPDATE - dev
class TagUpdate(TagBase):
    pass

#!IN DB - dev
class TagInDBBase(TagBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

# Tag that inherits from Tag in db base to include EVERYTHING
#! Tag
class Tag(TagInDBBase):
    pass
    #businesses: List["Business"]
    #users: List["User"]
