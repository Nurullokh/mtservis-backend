# MTSERVIS Project

## Outline
- Prerequisites
- Setup
    - Development
    - Production
- Documentation


## Prerequisites
This project has following prerequisites
- python 3.9.7
- docker 19.03.12
- docker-compose 1.25.0


## Setup

### Development

- Install virtual environment:
```
git clone git@github.com:Nurullokh/mtservis-backend.git
cd mtservis-backend
python3.9 -m venv --prompt="v" .env
```

- Load *local environment variables* to virtual environment:
```
cp ./deployments/development/env_example ./deployments/development/.env
change .env_local variable according to your settings
export ./deployments/development/.env
```

- If *pre commit* has not been installed please install by running following command:
```
pip install pre-commit
pre-commit install
```

- If *postgresql database* has not be started please start it by following command:
```
docker-compose -f deployments/development/docker-compose.yml up -d
```

- If *development packages* has not been installed please install by running following commit:
```
pip install -r requirements/development.txt
```

- If *migration* has not been applied please apply it first:
```
cd src
python manage.py migrate
```

- Start development server:
```
python runserver 0.0.0.0:8080
```
