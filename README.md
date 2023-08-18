**About**: 

The Pytest_BDD_Selenium framework is designed for web and API test automation, using 'pytest' together with the Page Object Model design pattern and 'Selenium'.

**Overview**:

Focused on both web and API test automation.
Adopts a BDD style approach, enhancing test readability and maintainability.
Integrated with Allure for detailed and visually appealing test reports.

**Setup and Execution:**

1. Prerequisites: Install Python, pip, and PyCharm IDE.
2. Allure Setup: Follow instructions from Allure's official site (https://docs.qameta.io/allure/)
3. Pipenv Setup: Initialize pipenv using the command: pipenv --python [path_to_python.exe]
4. Test Execution: Use the following command: pipenv run pytest
   (to run api test only run the following command : pipenv run pytest tests/step_defs/test_api.py
    to run web test only run the following command : pipenv run pytest tests/step_defs/test_web.py)
6. Report Generation: Post test execution, generate and view comprehensive reports with: allure serve report
