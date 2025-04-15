# Description

Simple CRUD application which enable to create, read, update and delete users. Using Django and Djangorestframework to write and API. Postgres as a database. Postman as a client which makes a requests.

TechStack:

- Python
- Django
- Postgres
- Postman

# Packages to install

- pip install django
- pip install djangorestframwork
- pip install psycopg2

# Starting project

// make sure that Django is installed

- django-admin --version

// create a new Django project which is called config

- django-admin startproject config .

// create a new app wihch is called myusers

- python manage.py startapp myusers

// run the serwer using that command

- python manage.py runserver

# Other handy commands

- python manage.py makemigrations
- python manage.py migrate
