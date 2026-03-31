from app.repositories.product_repo import ProductRepository

class ProductService:

    @staticmethod
    def create_product(db, product):
        return ProductRepository.create(db, product)

    @staticmethod
    def get_products(db):
        return ProductRepository.get_all(db)

    @staticmethod
    def get_product(db, product_id):
        return ProductRepository.get_by_id(db, product_id)

    @staticmethod
    def update_product(db, product_id, data):
        return ProductRepository.update(db, product_id, data)

    @staticmethod
    def delete_product(db, product_id):
        return ProductRepository.delete(db, product_id)