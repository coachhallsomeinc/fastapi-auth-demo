from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

#! from perspective of dev/admin - info needed to create/update/delete a review
#! from perspective of authorized user - info needed to create/update/delete a review
#! from perspective of a user/dev - info given back to read a business
# consider CRUD
#? do i need class config anywhere?
#from app.schemas.user import User
from app.schemas.business import Business

'''
TODO:
- base schema
- create schema
- update schema
'''
#? check on how foreign keys are written in schema
class ReviewBase(BaseModel):
    user_id: int
    business_id: int
    body: str
    star_rating: int
    created_timestamp: datetime
    updated_timestamp: datetime

#!CREATE - dev
class ReviewCreate(ReviewBase):
    pass

#!UPDATE - dev
class ReviewUpdate(ReviewBase):
    pass

#!IN DB - dev
class ReviewInDBBase(ReviewBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

# Review that inherits from Review in db base to include EVERYTHING
#! Review
class Review(ReviewInDBBase):

    user: List["User"]
    business: List["Business"]
