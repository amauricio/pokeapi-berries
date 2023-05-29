import requests
from typing import List
from app.models.berry import Berry
from statistics import mean, median, variance
from collections import Counter
from functools import lru_cache
import io
import seaborn as sns
import matplotlib
matplotlib.use('agg')
import pandas as pd
import base64

@lru_cache(maxsize=10)
def fetch_berry_data() -> List[Berry]:
    """
    Fetch all the berry list from PokeAPI
    """
    pokeapi_url = "https://pokeapi.co/api/v2/berry"
    berries = []
    #based on the pokeapi i am getting the next url and validate if the key exists in the next fetch. 
    #So in that way i will be able to know in what moment stops the fetching :)
    while pokeapi_url:
        response = requests.get(pokeapi_url, timeout=2000)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            for result in results:
                name = result["name"]
                berry = fetch_berry_details(name)
                if berry:
                    berries.append(berry)
            pokeapi_url = data.get("next")
        else:
            # Handle error cases
            raise Exception("Failed to fetch data from the PokeAPI :(")

    return berries

@lru_cache(maxsize=10)
def fetch_berry_details(name: str) -> Berry:
    """
    Fetch berry data detail from the PokeAPI.
    """
    url = f"https://pokeapi.co/api/v2/berry/{name}"
    response = requests.get(url, timeout=2000)
    if response.status_code == 200:
        data = response.json()
        growth_time = data.get("growth_time", 0)
        return Berry(name=name, growth_time=growth_time)
    else:
        raise Exception("Failed to fetch data details from the PokeAPI :(")

def generate_histogram(berries: List[Berry]) -> str:
    """
    Generate histogram in base64 using matplotlib
    """
    if not berries:
        raise ValueError("List of berries is empty")

    data = [str(berry.growth_time) for berry in berries]

    # generate the plot using seaborn
    sns.set(style="darkgrid")
    plot = sns.histplot(  data=data,  kde=True)
    plot.set(xlabel='Growth Time', ylabel='Count', title="PokeAPI-Berries Histogram")

    # save the plot to a byte buffer
    buf = io.BytesIO()
    plot.figure.savefig(buf, format='png')
    buf.seek(0)

    # create the html string
    return base64.b64encode(buf.getvalue()).decode('utf8')

def calculate_berry_statistics(berries: List[Berry]) -> dict:
    """
    Calculate all the statistics required
    """

    if not berries:
        raise ValueError("List of berries is empty")

    growth_times = [berry.growth_time for berry in berries]

    min_growth_time = min(growth_times)
    max_growth_time = max(growth_times)
    median_growth_time = median(growth_times)
    variance_growth_time = variance(growth_times)
    mean_growth_time = mean(growth_times)

    statistics_data = {
        "berries_names": [berry.name for berry in berries],
        "min_growth_time": round(min_growth_time, 2),
        "max_growth_time": round(max_growth_time, 2),
        "median_growth_time": round(median_growth_time, 2),
        "variance_growth_time": round(variance_growth_time, 2),
        "mean_growth_time": round(mean_growth_time, 2),
        "frequency_growth_time": Counter(growth_times)
    }

    return statistics_data