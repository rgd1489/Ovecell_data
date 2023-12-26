# Ovecell Data Pipeline

## Project Structure

- data/: Contains game data in JSON and CSV formats.
- app/: Contains Python source code.
- tests/: Contains test cases.
- Dockerfile: Docker configuration for the application.
- docker-compose.yml: Docker configuration for the PostgreSQL database.
- requirements.txt: Python dependencies.
- README.md: Project documentation.

## Docker Setup

..bash

docker-compose build
docker-compose up -d

## Running Data Pipeline

docker-compose run ovepipe python app.py GameName Date

docker-compose run ovepipe python app.py wwc 2021-04-01
docker-compose run ovepipe python app.py hb 2021-04-28






