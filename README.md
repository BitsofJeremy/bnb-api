# bnb-api

The API backend for bikesandbids.com

### Get it

Clone the repo

Setup you virtualenv and activate it

    virtualenv -p python3 venv
    source venv/bin/activate

Install requirements

    pip install -r requirements.txt

Create you SQLite DB

    python manage.py migrate

Create an admin

    python manage.py createsuperuser

Run the server

  python manage.py runserver

Open http://127.0.0.1:8000



### API

Basic routes setup in the API

http://127.0.0.1:8000/api
