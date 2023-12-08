from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.tag import Tag as TagModel
from app.schemas.tag import TagBase, TagCreate, TagUpdate

'''
TODO:
- drink crud
- drink child relationships
    - businesstag
'''
# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# should it just be get_by_id
class TagController(BaseController[TagModel, TagCreate, TagUpdate]):
    def create_review(self, db: Session, *, obj_in: TagBase) -> TagModel:
        db_obj = TagModel(
            business_id=obj_in.business_id, #?connect to business?
    
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

tag = TagController(TagModel)