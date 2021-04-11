from fastapi import FastAPI


from app.api import router as main_router
from app.core.config import SECRET_KEY
app = FastAPI()

app.include_router(main_router, prefix="/api")

print(SECRET_KEY)
