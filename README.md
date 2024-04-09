#### Task 3: Enhanced Security

##### Details

API Documentation
https://documenter.getpostman.com/view/22085405/2sA3BgAFKF

Implemented API Key authentication using Django's built-in authentication capabilities.
1. model for APIKey
2. APIView for GenerateAPIKey
3. impelented custom APIKeyAuthentication using BaseAuthentication

Generate an API key
POST generate-api-key/

Usage: the API key should be sent in the request header
Authorization: ApiKey <api_key>

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
