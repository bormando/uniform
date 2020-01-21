# Uniform
This project is a part of my portfolio. Here you can find API tests, developed using stack:
- Python (programming language)
- PyTest (test framework for Python)
- Allure (post-test reporting tool)

### How to run these tests?
You'll need to install Python 3.7+ and all packages from "requirements.txt" file:
> pip install -r requirements.txt

Also you'll need to install **Allure-CLI** (and **Java**) if you'd like to generate Allure report.

Run this command inside project's root directory:
> pytest -v -s -m="smoke" --alluredir="allure-results"
