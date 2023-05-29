import pytest
from requests_mock import Mocker
from typing import List
from app.models.berry import Berry
from collections import Counter
from app.services.berry_service import fetch_berry_data, fetch_berry_details, calculate_berry_statistics


@pytest.fixture
def mocked_responses():
    with Mocker() as m:
        yield m


def test_fetch_berry_data(mocked_responses):
  #set initial data and mock requests
  berries_json = {
      "results": [
          {"name": "berry1"},
          {"name": "berry2"},
          {"name": "berry3"}
      ],
  }
      
  berry1_json = {"growth_time": 5}
  berry2_json = {"growth_time": 10}
  berry3_json = {"growth_time": 8}

  mocked_responses.get("https://pokeapi.co/api/v2/berry", json=berries_json)

  mocked_responses.get("https://pokeapi.co/api/v2/berry/berry1", json=berry1_json)
  mocked_responses.get("https://pokeapi.co/api/v2/berry/berry2", json=berry2_json)
  mocked_responses.get("https://pokeapi.co/api/v2/berry/berry3", json=berry3_json)

  berries = fetch_berry_data()

  assert len(berries) == 3
  assert berries[0].name == "berry1"
  assert berries[0].growth_time == 5
  assert berries[1].name == "berry2"
  assert berries[1].growth_time == 10
  assert berries[2].name == "berry3"
  assert berries[2].growth_time == 8

def test_fetch_berry_details(mocked_responses):
  berry_name = "berry1"
  berry_json = {"growth_time": 5}

  url = f"https://pokeapi.co/api/v2/berry/{berry_name}"
  mocked_responses.get(url, json=berry_json)

  berry = fetch_berry_details(berry_name)

  assert berry.name == "berry1"
  assert berry.growth_time == 5


def test_calculate_berry_statistics():
  #test calculations
  berries = [
      Berry(name="berry1", growth_time=5),
      Berry(name="berry2", growth_time=10),
      Berry(name="berry3", growth_time=8)
  ]

  statistics_data = calculate_berry_statistics(berries)

  assert statistics_data["berries_names"] == ["berry1", "berry2", "berry3"]
  assert statistics_data["min_growth_time"] == 5
  assert statistics_data["max_growth_time"] == 10
  assert statistics_data["median_growth_time"] == 8
  assert statistics_data["variance_growth_time"] == pytest.approx(6.33, abs=0.01)
  assert statistics_data["mean_growth_time"] == pytest.approx(7.67, abs=0.01)
  assert statistics_data["frequency_growth_time"] == Counter({5: 1, 10: 1, 8: 1})
