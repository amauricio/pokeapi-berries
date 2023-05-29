from urllib import response
from fastapi import APIRouter
from typing import List
from fastapi_cache.decorator import cache
from fastapi.responses import HTMLResponse
from app.models.berry import Berry
from app.api.core.poke_stats_response import PokeStatsResponse
from app.services.berry_service import fetch_berry_data, calculate_berry_statistics, generate_histogram
from app.config import settings
import json

router = APIRouter()

@router.get("/allBerryStats",status_code=200, response_class=PokeStatsResponse)
@cache(expire=settings.CACHE_TIME)
def get_all_berry_stats():
    berries: List[Berry] = fetch_berry_data()
    statistics_data: dict = calculate_berry_statistics(berries)
    return statistics_data

@router.get("/plots",response_class=HTMLResponse)
def generate_plots():
    berries: List[Berry] = fetch_berry_data()
    image_histogram = generate_histogram(berries)

    html_content = f"""
    <html>
        <head>
            <title>Poke Stats // Graphs</title>
        </head>
        <body>
            <img src='data:image/png;base64,{image_histogram}'>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)