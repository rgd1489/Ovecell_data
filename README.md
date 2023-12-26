# Ovecell Data Pipeline

## Project Structure

- data/: Contains game data in JSON and CSV formats.
- app/: Contains Python code.
- Dockerfile: Docker configuration for the application.
- docker-compose.yml: Docker configuration for the PostgreSQL database.
- requirements.txt: Python dependencies.

## Docker Setup

..bash

docker-compose build

docker-compose up -d

## Running Data Pipeline

docker-compose run ovicell python app.py GameName Date

docker-compose run ovicell python app.py wwc 2021-04-01
docker-compose run ovicell python app.py hb 2021-04-28






