### Python Backend Developer Coding Tasks' Solutions

#### NOTE
#### When at Branch 3 (mentioned below by name) 
####   &nbsp;  PLEASE ADD ?api_key={api_key_from_env_file} to the urls when making requests to the endpoints

This branch has an API Key Authentication Middleware implemented and so will return 401 if not passed a valid api key. The test cases written will run OK in other branches as they test the endpoints without the api key but they will fail on branch 3. It has been done on purpose so you can verify that the endpoints are blocked when the middleware is in place.
<br>

#### Example Request URLs for Branch 3
`http://localhost:8000/weather/paris?api_key=d5478237dac7aa890c813beb9e3cc206`<br>
`http://localhost:8000/average_temperature/lahore,karachi?api_key=d5478237dac7aa890c813beb9e3cc206`<br>
`http://localhost:8000/tasks?api_key=d5478237dac7aa890c813beb9e3cc206`<br>
`http://localhost:8000/tasks/1?api_key=d5478237dac7aa890c813beb9e3cc206`

for the other branches, you can remove the ?api_key={api_key} part.

---
#### Description
This repository contains solutions for the coding tasks given  for the position of Python Backend Developer.
There are mainly 3 branches for the given 3 tasks. The branches are

- backend-system &nbsp; &nbsp;  (Branch 1)
- backend-system-with-unit-testing-and-optimization  &nbsp; &nbsp;  (Branch 2) 
- backend-system-with-unit-testing-and-optimization-and-api-key-authentication &nbsp; &nbsp;  (Branch 3)

---

#### Project Setup 

Please note that for this django project the backendDeveloper root directory is being used for project's root directory.

##### Steps
- Switch to branch 3 using<br>
`git checkout backend-system-with-unit-testing-and-optimization-and-api-key-authentication`

- Install the required dependencies using<br>
`pip install -r requirements.txt`
- Run the server using<br>
`python manage.py runserver`

---
#### Solutions

---

#### Solution 1: Developing a Django Backend System 
#### Branch: backend-system

##### Description
This solution involves three parts<br>
- Implementing a model for Tasks, the model's serializer as well as the
class based view set for performing CRUD operations on the tasks. The view set provides predefined functions for all the CRUD operations.
Moreover, the APIView or ViewSet of rest framework makes the CRUD endpoints browsable.
- Integration with OpenWeather API.
- Developing two browsable class based views inheriting from rest APIView. The first one for getting the weather data for a given city. The second one for calculating the average temperature for given number of cities.

---

#### Solution 2: Test Cases Implementation & Code Optimization 
####  Branch: backend-system-with-unit-testing-and-optimization

##### Description
This solution involves two parts<br>
- Removing unnecessary imports, variables, following PEP-8 Standards, converting some instance methods to static methods which did not require interaction with instance/self, abstracting the sensitive information e.g., api key using a .env file, handling bad requests.
- Writing & executing test cases for verifying successful responses from the endpoints implemented without the api key (valid for branch 1 and 2).

---

#### Solution 3: Implementation of API-KEY Authentication Middleware
####  Branch: backend-system-with-unit-testing-and-optimization-and-api-key-authentication
##### Description
This solution involves developing a custom authentication middleware which basically checks every request url for a query parameter 'api_key' and compares it with the valid 
api key set in the .env file of the project. It returns 401/unauthorized in case of a mismatch.

---