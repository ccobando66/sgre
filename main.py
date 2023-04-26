from fastapi import FastAPI
from .models.admin import Base
from .config.database import engine
from .routers import (
    user,personal,admin
)
from fastapi.middleware.cors import CORSMiddleware
 
Base.metadata.create_all(engine)

app = FastAPI()

#cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*']
)

#routers
app.include_router(user.router)
app.include_router(personal.router)
app.include_router(admin.router)

@app.get('/')
async def root():
    return {'sms':'hello_word'}