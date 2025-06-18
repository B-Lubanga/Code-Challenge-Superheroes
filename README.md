# Code-Challenge-Superheroes

# Superheroes API

## Description

A RESTful API built with Flask to manage superheroes and their powers.

## Features

- Hero and Power Models with Many-to-Many Relationship
- CRUD routes using Flask + SQLAlchemy
- Validations and error handling

## ERD

<img src="./server/static/images/Superheroes ERD.png"alt="Hero Image" width="500" height="600">

## Setup Instructions

```bash
git clone <repo>
cd Code-Challenge-superheroes
pipenv install && pipenv shell
python seed.py
export FLASK_RUN_PORT=5555
flask db init
flask db migrate -m "initial migrate"
flask db upgrade head
flask shell
flask run
```
