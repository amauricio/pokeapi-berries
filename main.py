from fastapi import FastAPI
import uvicorn
from app.config import settings
from app.api.endpoints.berry_stats import router as berry_stats_router

app = FastAPI()

app.include_router(berry_stats_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT or 8000, reload=settings.DEBUG)