from fastapi import FastAPI


from app.api import router as main_router

app = FastAPI()

app.include_router(main_router, prefix="/api")
