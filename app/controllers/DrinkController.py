from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.drink import Drink as DrinkModel
from app.schemas.drink import DrinkBase, DrinkCreate, DrinkUpdate

'''
TODO:
- drink crud
- drink child relationships
    - businesstag
'''
# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# should it just be get_by_id
class DrinkController(BaseController[DrinkModel, DrinkCreate, DrinkUpdate]):

#! find a drink by id
    def get_drink_by_id(self, db: Session, * id: int):
        return db.query(DrinkModel).filter(DrinkModel.id == id).first()

#! find a drink by name
    def get_drink_by_name(self, db: Session, *, name: str):
        return db.query(DrinkModel).filter(DrinkModel.name == name).first()

#! find a drink business
    def get_drink_by_business(self, db: Session, *, business_id: id):
        return db.query(DrinkModel).filter(DrinkModel.business_id == business_id).first()

#! create drink
    def create_drink(self, db: Session, *, obj_in: DrinkBase) -> DrinkModel:
        db_obj = DrinkModel(
            business_id=obj_in.business_id, #?connect to business?
            name=obj_in.name,
            description=obj_in.description,
            price=obj_in.price,
            featured=obj_in.featured,
            ordered_list_number=obj_in.ordered_list_number,
            created_timestamp=obj_in.created_timestamp,
            updated_timestamp=obj_in.updated_timestamp
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

drink = DrinkController(DrinkModel)
