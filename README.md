# AutomationExercise Playwright Tests

## Summary
This repository contains **end-to-end tests** for the [Automation Exercise](https://automationexercise.com) website, written in **Python** using **Playwright** and the **Page Object Model (POM)** pattern.  
The tests cover multiple flows including Home Page, Products, Product Details, Cart, Contact Us, Login, and Scroll functionality.

---

## Requirements  

Before running the tests, make sure you have the following installed:

- **Python 3.8+**
- **pipenv**
- **Git**
- **Playwright browsers** (Chromium, Firefox, WebKit)

---

## Installation Steps  

**Clone the repository:**
```bash
git clone https://github.com/alinapurtova/pytest_task9.git
cd pytest_task9
```

**Install dependencies:**
```bash
pip install pipenv
pipenv install --dev
pipenv run playwright install
```

## Running Tests

**Run all tests with Chromium or Firefox:**
```bash
pipenv run pytest --browser_name=chromium --alluredir=allure-results
pipenv run pytest --browser_name=firefox --alluredir=allure-results
```
or by scripts:
```bash
pipenv run test-chromium
pipenv run test-firefox
```

**Run tests in parallel (example with pytest-xdist, 2 workers):**
```bash
pipenv run pytest -n 2 --browser_name=chromium --alluredir=allure-results
```
or script:
```bash
pipenv run test-parallel
```

**Run specific test files:**
```bash
pipenv run pytest tests/test_products.py
```
or script:
```bash
pipenv run test-products
```
You can find other scripts in **Pipfile**.

## Generate Allure Report

**Generate report:**
```bash
pipenv run allure generate allure-results --clean -o allure-report
```
or
```bash
pipenv run allure-generate
```

**Open report locally:**
```bash
pipenv run allure open allure-report
```
or
```bash
pipenv run allure-open
```

## Test Summary

**Cart Tests**

| Test ID    | Description                      |
| ---------- | -------------------------------- |
| **TC-011** | Verify Subscription in Cart page |
| **TC-012** | Add Products in Cart             |
| **TC-013** | Verify Product quantity in Cart  |

**Contact Us Tests**

| Test ID    | Description     |
| ---------- | --------------- |
| **TC-006** | Contact Us Form |

**Scroll Tests**

| Test ID    | Description                                                         |
| ---------- | ------------------------------------------------------------------- |
| **TC-025** | Verify Scroll Up using 'Arrow' button and Scroll Down functionality |

**Login Tests**

| Test ID    | Description                                  |
| ---------- | -------------------------------------------- |
| **TC-003** | Login User with incorrect email and password |

**Products Tests**

| Test ID    | Description                                  |
| ---------- | -------------------------------------------- |
| **TC-008** | Verify All Products and Product Details page |
| **TC-009** | Search Product                               |
| **TC-018** | View Category Products                       |
| **TC-021** | Add Review on Product                        |

## CI/CD 
Tests are executed automatically via GitHub Actions with results reported to the branch allure-report and uploaded to Pages.
Also pipeline sends Slack notifications to channel with test results and report link.
