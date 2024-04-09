#### Task 1: Django Backend System

##### Details

API Documentation
https://documenter.getpostman.com/view/22085405/2sA3BgAFKF

RESTful APIs with CRUD Operations
1. GET tasks/
2. POST tasks/
3. GET tasks/<int:pk>/
4. PUT tasks/<int:pk>/
5. DELETE tasks/<int:pk>/

Two Additional APIs with OpenWeatherMap
1. GET weather/<str:city>/
2. GET average_temperature/<str:city_list>/

Database: SQLite3

##### Environment Setup
1.  "python3 -m venv venv"
2.  "source venv/bin/activate"
3.  "pip install -r requirements.txt"

##### Prerequisites
1. local redis server
2. (FOR TASK 2 AND 3 ONLY) celery worker: "celery -A project worker --loglevel=info"

##### Project Setup
1. "python3 manage.py makemigrations"
2. "python3 manage.py migrate"
3. "python3 manage.py runserver"
4. the server is reachable at http://127.0.0.1:8000/

##### Running Tests
1. "pytest"
