from fastapi import FastAPI
from router import admin, user

app = FastAPI()
app.include_router(admin.router)
app.include_router(user.router)
