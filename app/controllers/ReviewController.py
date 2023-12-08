from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.review import Review as ReviewModel
from app.schemas.review import ReviewBase, ReviewCreate, ReviewUpdate

'''
TODO:
- drink crud
- drink child relationships
    - businesstag
'''
# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# should it just be get_by_id
class ReviewController(BaseController[ReviewModel, ReviewCreate, ReviewUpdate]):
    def create_review(self, db: Session, *, obj_in: ReviewBase) -> ReviewModel:
        db_obj = ReviewModel(
            business_id=obj_in.business_id, #?connect to business?
    
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

review = ReviewController(ReviewModel)
