# AutoQA — REST API Test Automation Framework



![CI](https://github.com/DHARSHINIPRIYA510/AutoQA/actions/workflows/ci.yml/badge.svg)



A professional test automation framework built with Python, pytest, and Selenium that automatically validates REST APIs and browser behavior.

## 🚀 Features

- ✅ REST API testing with `requests` + `pytest`
- ✅ Browser automation with `Selenium`
- ✅ Parametrized tests across multiple inputs
- ✅ Negative testing (404, invalid inputs)
- ✅ Response time validation
- ✅ HTML test reports via `pytest-html`
- ✅ Automated CI/CD pipeline via GitHub Actions

## 🧪 Test Coverage

| Test File | Tests | Coverage |
|-----------|-------|----------|
| test_users.py | 9 tests | GET all, GET single, parametrized, 404, response time |
| test_posts.py | 9 tests | GET, POST, parametrized, 404, smoke & regression markers |
| test_browser.py | 3 tests | Page title, URL, heading validation |

**Total: 21 automated tests**

## 🛠 Tech Stack

- Python 3.13
- pytest + pytest-html
- Selenium WebDriver
- requests
- GitHub Actions CI/CD

## ▶️ How to Run

### Install dependencies
pip install pytest requests pytest-html selenium webdriver-manager
### Run all tests
pytest tests/ -v
### Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html
### Run only smoke tests
pytest tests/ -m smoke -v
### Run only regression tests
pytest tests/ -m regression -v
## 📊 Sample Report

21 tests | 0 failed | Runs automatically on every push via GitHub Actions