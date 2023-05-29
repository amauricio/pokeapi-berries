from urllib import response
from fastapi import APIRouter
from typing import List
from app.models.berry import Berry
from app.api.core.poke_stats_response import PokeStatsResponse
from app.services.berry_service import fetch_berry_data, calculate_berry_statistics
from app.config import settings

router = APIRouter()

@router.get("/allBerryStats",status_code=200, response_class=PokeStatsResponse)
def get_all_berry_stats():
    berries: List[Berry] = fetch_berry_data()
    statistics_data: dict = calculate_berry_statistics(berries)
    return statistics_data
