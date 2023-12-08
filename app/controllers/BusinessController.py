from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.business import Business as BusinessModel, BusinessTag as BusinessTagModel
from app.schemas.business import BusinessBase, BusinessCreate, BusinessUpdate, BusinessInDBBase, Business as BusinessSchema

'''
TODO:
- business crud
- business child relationships
    - businesstag
    queries deal with models
    parameters and passing deal with schemas
'''
# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# this class def inherits from BaseController with model, create schema, and update schema
class BusinessController(BaseController[BusinessModel, BusinessCreate, BusinessUpdate]):
    def get_business_by_id(self, db: Session, *, id: int):
        return db.query(BusinessModel).filter(BusinessModel.id == id).first()

# example code from docs -----
    # def get_business_by_id(db: Session, business_id: int):
    #     return db.query(models.Business).filter(models.Business.id == business_id).first()

    def get_business_by_name(self, db: Session, *, name: str):
        return db.query(BusinessModel).filter(BusinessModel.name == name).first()

#*doc ex get by name
    # def get_business_by_name(db: Session, name: str):
    #     return db.query(models.Business).filter(models.Business.name == name).first()

    # def get_businesses(self, db: Session, skip: int = 0, limit: int = 100):
    #     return db.query(models.Business).offset(skip).limit(limit).all()

#* doc ex get all
    # def get_businesses(db: Session, skip: int = 0, limit: int = 100):
    #     return db.query(models.Business).offset(skip).limit(limit).all()

# --------

    def create(self, db: Session, *, obj_in: BusinessBase) -> BusinessModel:
        db_obj = BusinessModel(
            name=obj_in.name,
            address=obj_in.address,
            city=obj_in.city,
            state=obj_in.state,
            postal_code=obj_in.postal_code,
            latitude=obj_in.latitude,
            longitude=obj_in.longitude,
            created_timestamp=obj_in.created_timestamp,
            updated_timestamp=obj_in.updated_timestamp
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

business = BusinessController(BusinessModel)

    #* code searching keyword and getting back nearby cafes to user location
    # def get_nearby_cafes(db: Session, keyword: str, latitude: float, longitude: float):
    #     user_location = f'POINT({longitude} {latitude})'
    #     return db.query(Business).filter(
    #         BusinessModel. ____ .contains([keyword]),
    #         BusinessModel.locations.ST_DWithin(user_location, 0.1)).all()
