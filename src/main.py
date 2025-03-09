from fastapi import FastAPI

from src.api import router as router_api


app = FastAPI()
app.include_router(router_api)
