## View/Create data model in Django Admin Panel 

1. Create a poetry project and delete the default folders.
2. Make a Django project called "backend": (`django-admin startproject backend .`)

### New Django App `books`

3. Create a new app `books` via `django-admin startapp books`
4. Tell Django about the new app
   
   In `backend/settings.py` -> `INSTALLED_APPS` add `'books'`

5. Create a `Book` model (see `books/models.py`)

### Migrations

6. Make a new migration `python manage.py makemigrations`

   This will create the `0001_initial.py` migration

7. Apply migration (aka "migrate"): `python manage.py migrate`

   - **Note**: A new file has appeared -> `db.sqlite3` -> A simpler txt database that works like our SQL database for now.

8. Get the VSCode SQLite extension

   <img width="538" alt="image" src="https://user-images.githubusercontent.com/1945462/163561438-678195cb-4245-4388-8e87-badb10e3f47e.png">

   and observe the structure of the newly created `books` table:

   <img width="449" alt="image" src="https://user-images.githubusercontent.com/1945462/163561574-f0c87ca5-b135-490e-bc1d-277bbe25df02.png">

### Django Admin Panel

9.  Register the model so the admin site is aware of it: import model in `albums/admin.py`

   1. In `albums/admin.py` add the line `admin.site.register(Book)`
   2. Hover over `Book` with your cursor and hit `Cmd + .` -> pick the import from `books.models` -> This should create `from books.models import Book`

10. Create an admin user via `python manage.py createsuperuser`. Just use `admin` as username and password. Yes, let's bypass password validation 🙈
11.  Run the server (`python manage.py runserver`) and login to the admin panel on `http://127.0.0.1:8000/admin/`.
12. Add a **book** (note the POST request showing in terminal)

### View SQLite DB

Check out the data in your `sqlite3` database

- ... via the VSCode SQLite extension

  <img width="1037" alt="image" src="https://user-images.githubusercontent.com/1945462/163562599-3826aa87-4c25-4ed0-910e-a631d9a21919.png">

- ... via [this sqlite-viewer](https://inloop.github.io/sqlite-viewer/).