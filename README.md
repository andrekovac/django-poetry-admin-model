# A basic Django Model to view in the Admin panel

A basic Django Model

## Run

1. Clone the repo.
2. Make sure you have [poetry](https://python-poetry.org/) (python environment and dependency manager) installed.
3. In the project folder run `poetry install` to install dependencies.
4. Run `poetry shell` to open a new shell with all dependencies available.
5. Run `python manage.py runserver`

## Concepts

### Migrations

- `makemigrations` is responsible for packaging up your model changes into individual migration files
- `migrate` is responsible for applying those to your database.
