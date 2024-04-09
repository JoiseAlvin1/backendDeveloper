#### Task 2: Test Cases and Performance Optimization

##### Details

API Documentation
https://documenter.getpostman.com/view/22085405/2sA3BgAFKF

Performance Optimizations
1. Database Indexing (indexed the title field in Task model to improve query performance)
2. Serial Optimization (serialized only the necessary data fields to minimize the payload size, instead of using __all__)
3. Caching (impelemented API response caching with Redis, reducing the need to fetch data from the database or external APIs repeatedly)
4. Celery (implemented background tasks with Celery, to handle heavy and time taking processes asyncronously)

Unit and Integration Test Cases
1. Test cases for CRUD operations
2. Test cases for model
3. Two addition test cases for APIs with OpenWeatherMap

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
