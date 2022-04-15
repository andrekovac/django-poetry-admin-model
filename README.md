# A basic Django Model to view in the Admin panel

Create and view books in the Django Admin panel

## Run

1. Clone the repo.
2. Make sure you have [poetry](https://python-poetry.org/) (python environment and dependency manager) installed.
3. In the project folder run `poetry install` to install dependencies.
4. Run `poetry shell` to open a new shell with all dependencies available.
5. Run `python manage.py runserver`

## Concepts

### Data Models

See `books/models.py`

### Migrations

- `python manage.py makemigrations` is responsible for packaging up your model changes into individual migration files
- `python manage.py migrate` is responsible for applying those to your database.

## Re-create this project

- [BASIC_POETRY_DJANGO_SETUP.md](./docs/BASIC_POETRY_DJANGO_SETUP.md) contains instructions to set up the basics of this project
- [HOW_TO.md](./docs/HOW_TO.md) contains a step-by-step instruction to recreate this project.