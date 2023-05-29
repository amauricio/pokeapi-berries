from fastapi import FastAPI
import uvicorn
from app.config import settings
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi.responses import JSONResponse


from app.api.endpoints.berry_stats import router as berry_stats_router

app = FastAPI()

@app.exception_handler(Exception)
async def pokeapi_exception_handler(request, err):
    error_message = f"Error: {request.method}: {request.url}"
    return JSONResponse(status_code=500, content={"message": f"{error_message}. Detail: {err}"})

#caching the data fetch from PokeAPI 
@app.on_event("startup")
async def startup():
    #by default in memory
    adapter_cache = InMemoryBackend()
    if settings.CACHE_TYPE == "InMemory":
        adaptar_cache = InMemoryBackend()
    elif settings.CACHE_TYPE == "Redis":
        #add redis
        pass
    elif settings.CACHE_TYPE == "Memcached":
        #add memcached
        pass
    FastAPICache.init(adapter_cache)

app.include_router(berry_stats_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT or 8000, reload=settings.DEBUG)