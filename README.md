### Python Backend Developer Coding Tasks

#### Description
This repository contains coding tasks for the position of Python Backend Developer. Candidates are expected to complete the tasks as per the instructions provided and submit their solutions via a pull request.

---

#### Tasks

---

#### Task 1: Design and Implement a FastAPI/Django Backend System

##### Description
Design, develop, and implement a backend system using FastAPI or Django.

##### Requirements
- Create RESTful APIs for data access and manipulation.
- Implement CRUD operations.
- Use an open-source database (e.g., SQLite, PostgreSQL).
- Write unit tests for your code.

##### Feature List
- CRUD operations for tasks
- Fetch and display weather data from OpenWeatherMap API
- Calculate and display the average temperature for a location
  - Endpoint to get weather data for a city: `GET /weather/{city}`
  - Endpoint to calculate average temperature for a list of cities: `GET /average_temperature/{city_list}`
  - Additional endpoints for CRUD operations for tasks as mentioned above

##### Sample Database: SQLite
You can use SQLite, a C library that provides a lightweight disk-based database, to store and retrieve data for this task.

##### Sample API: OpenWeatherMap API
Integrate the OpenWeatherMap API to fetch and display weather data.

- **API Documentation**: [OpenWeatherMap API](https://openweathermap.org/api)

---

#### Task 2: Unit Testing and Performance Optimization

##### Description
Perform unit testing, integration testing, and performance optimization of backend code.

##### Requirements
- Write unit tests to cover the implemented functionalities.
- Optimize the backend code for performance.

---

#### Guidelines for Submission
1. Fork this repository.
2. Create a new branch for each task.
3. Complete the tasks as per the requirements.
4. Write a README.md file explaining your solution and any additional information.
5. Commit and push your changes to your forked repository.
6. Create a pull request to submit your solutions.

---

#### Sample Project
A sample project is provided to help candidates understand the expectations and requirements for the tasks.

##### Sample Project Setup
- **Database**: SQLite
- **API**: OpenWeatherMap API

---

#### Additional Notes
- Candidates are encouraged to follow best practices for code quality, security, and performance optimization.
- Candidates are expected to provide well-documented and readable code.
- Any questions or clarifications regarding the tasks should be raised via GitHub issues.
