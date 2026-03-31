from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:

    @staticmethod
    def create(db: Session, product):
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def get_all(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_by_id(db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def update(db: Session, product_id: int, data):
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None
        for key, value in data.dict().items():
            setattr(product, key, value)
        db.commit()
        return product

    @staticmethod
    def delete(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            db.delete(product)
            db.commit()
        return product