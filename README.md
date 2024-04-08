# Employee CRUD
This repository contains the source code for a Django REST API that manages employee data. It provides endpoints for retrieving, creating, updating, and deleting employee records.

#### Features
- GET Endpoint: Retrieve employee details by regid or retrieve all employees.
- POST Endpoint: Create a new employee record.
- PUT Endpoint: Update an existing employee record.
- DELETE Endpoint: Delete an employee record by regid.
#### Installation
Clone the repository:
```
git clone <repository-url>
```
Install dependencies:
```
pip install -r requirements.txt
```
Apply migrations:
```
python manage.py migrate
```
Start the development server:
```
python manage.py runserver
```
#### Usage
###### GET Endpoint:
- To retrieve details of a specific employee: /employees/<regid>/
- To retrieve details of all employees: /employees/
###### POST Endpoint:
- Create a new employee record by sending a POST request to /employees/ with JSON data containing employee details.
###### PUT Endpoint:
- Update an existing employee record by sending a PUT request to /employees/ with JSON data containing updated employee details.
###### DELETE Endpoint:
- Delete an employee record by sending a DELETE request to /employees/<regid>/.
#### Error Handling
If an error occurs during processing, the API will return an appropriate error response with details in JSON format.
#### Logging
The API logs errors and important events to the log/error.log file.
