# Poke-berries statistics API
[![Deploy to Heroku](https://github.com/amauricio/pokeapi-berries/actions/workflows/heroku.yml/badge.svg)](https://github.com/amauricio/pokeapi-berries/actions/workflows/heroku.yml)
## Overview

The Poke-Berries Statistics API provides statistical information about various berries in the Pokemon universe. It retrieves data from the PokeAPI and calculates metrics such as minimum growth time, median growth time, maximum growth time, variance of growth time, mean growth time, and frequency distribution of growth time.

## Setup  &nbsp; [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python)

First create the `.env` file and set the environment variables.
```shell
cp .env.example .env
```

| Environment Variable | Description |
|----------------------|-------------|
| `DEBUG`      | Enable live reloading (fastapi)|
| `PORT`      | Define the expose port |
| `CACHE`      | Enable caching system |
| `CACHE_TYPE`      | `InMemory`, `Redis`, `Memcached` (only supports `InMemory`) |

- Install the requirements.
  ```shell
  pip3 install -r requirements.txt
  ```
- Serve the project.
  ```shell
  python3 main.py
  ```
