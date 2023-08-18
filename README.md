**About**: 

The Pytest_BDD_Selenium framework is designed for web and API test automation, using 'pytest' together with the Page Object Model design pattern and 'Selenium'.

**Overview**:

1. Focused on both web and API test automation.
2. Adopts a BDD style approach, enhancing test readability and maintainability.
3. Integrated with Allure for detailed and visually appealing test reports.

**Setup and Execution:**

1. Prerequisites: Install Python 3.11.4, pip, and PyCharm IDE.
2. Allure Setup: Follow instructions from Allure's official site (https://docs.qameta.io/allure/)
3. Pipenv Setup: Initialize pipenv using the command: pipenv --python [path_to_python.exe]
4. Configure your DRIVER_PATH in the environment.py file.
5. Test Execution: Use the following command: pipenv run pytest.
   (To execute only the API tests, use the command: pipenv run pytest tests/step_defs/test_api.py)
   (To execute only the web tests, use the command: pipenv run pytest tests/step_defs/test_web.py)
6. Report Generation: Post test execution, generate and view comprehensive reports with: allure serve report.
