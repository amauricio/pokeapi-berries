# Poke-berries statistics API
[![Deploy to Heroku](https://github.com/amauricio/pokeapi-berries/actions/workflows/heroku.yml/badge.svg?branch=main)](https://github.com/amauricio/pokeapi-berries/actions/workflows/heroku.yml)

Demo PokeAPI: http://poketest.herokuapp.com/allBerryStats

Demo PokePlot: http://poketest.herokuapp.com/plots
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
  

## With Makefile
- Setup the project installing the requirements.
  ```shell
  make install
  ```
  - If you want to update the dependencies: 
    ```shell
      make update-deps
    ```
- Serve the API.
  ```shell
  make start
  ```
- Run test with the following command.
  ```shell
  make test
  ```
- Run coverage with the following command.
  ```shell
  make coverage
  ```
- Clean project.
  ```shell
  make clean
  ```
## With Docker compose
Deploy the project using docker & docker compose

- Run the following command to start everithing.
```shell
docker-compose up -d
```
- To stop and remove the containers, run the following command:
```shell
docker-compose down
```

## Endpoints
PokeAPI: http://localhost:8000/allBerryStats

PokePlot: http://localhost:8000/plots