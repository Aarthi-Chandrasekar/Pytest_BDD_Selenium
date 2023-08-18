Feature: Employee Management

  Scenario: Retrieve all employees
    Given A Get all employees service API endpoint is available
    When I make the GET request to retrieve all employees
    Then The response status code should be 200

  Scenario: Create a new employee
    Given A Get all employees service API endpoint is available
    When I create the employee
    Then The response status code should be 201

  Scenario: Update an employee
    Given A Get all employees service API endpoint is available
    When I update the employee
    Then The response status code should be 200

  Scenario: Delete an employee
    Given A Get all employees service API endpoint is available
    When I delete the employee
    Then The response status code should be 200
