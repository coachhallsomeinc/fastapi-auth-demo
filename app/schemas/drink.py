from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

#! from perspective of dev/admin - info needed to create/update/delete a drink
#! from perspective of a user - info given back to read a drink
# consider CRUD

#from app.schemas.business import Business

'''
TODO:
- base schema
- create schema
- update schema
- endpoint
- add to schema init file
- add router to api file
'''

class DrinkBase(BaseModel):
    business_id: int #?connect to business?
    name: str
    description: str
    price: float
    featured: bool
    ordered_list_number: int
    created_timestamp: Optional[datetime] = None
    updated_timestamp: Optional[datetime] = None

#!CREATE - dev
class DrinkCreate(DrinkBase):
    pass

#!UPDATE - dev
class DrinkUpdate(DrinkBase):
    pass

#!IN DB - dev
class DrinkInDBBase(DrinkBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

# business that inherits from business in db base to include EVERYTHING
#! DRINK
class Drink(DrinkInDBBase):
    #businesses: List["Business"]
    pass
