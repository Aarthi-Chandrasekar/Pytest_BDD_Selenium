import pytest
import requests
from pytest_bdd import scenarios, given, when, then,parsers
import os

BASE_URL = "http://localhost:8088/employees/"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FEATURE_FILE_PATH = os.path.join(BASE_DIR, '..', 'features', 'api.feature')

# Sample Rest API To Test with Rest Assured
# Step 1. Clone the below repository to your local machine ->
# git clone https://github.com/onlyfullstack/rest-assured-tutorial.git
# Step 2. Run spring-boot mvn command in command prompt -> D:\Postman\rest-assured-tutorial>mvn spring-boot:run

# Automatically find all scenarios in the api.feature file
scenarios(FEATURE_FILE_PATH)

@pytest.fixture
def result():
    return {}

@pytest.fixture
def employee_data():
    return {
        "firstName": "Krishna",
        "lastName": "Radha",
        "salary": "10000",
        "email": "Krishna@abc.com"
    }

@pytest.fixture
def employee_update_data():
    return {
        "id": "2",
        "data": {
            "firstName": "Tom",
            "lastName": "Jerry",
            "salary": "10000",
            "email": "jerry2@abc.com"
        }
    }

@pytest.fixture
def employee_id_data():
    return {"id": "2"}

@given("A Get all employees service API endpoint is available")
def set_endpoint(result):
    result["url"] = BASE_URL

@when("I make the GET request to retrieve all employees")
def retrieve_all_employees(result):
    result["response"] = requests.get(result["url"])

@when('I create the employee')
def create_employee(result, employee_data):
    result["response"] = requests.post(BASE_URL, json=employee_data)

@when('I update the employee')
def update_employee(result, employee_update_data):
    result["response"] = requests.put(f"{BASE_URL}{employee_update_data['id']}", json=employee_update_data['data'])

@when('I delete the employee')
def delete_employee(result, employee_id_data):
    result["response"] = requests.delete(f"{BASE_URL}{employee_id_data['id']}")

@then(parsers.parse("The response status code should be {status_code}"))
def check_status_code(result, status_code):
    assert result["response"].status_code == int(status_code)
