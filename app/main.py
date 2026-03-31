from fastapi import FastAPI
from app.api.product_routes import router as product_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_router)