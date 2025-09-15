# 📦 API Test Documentation

Welcome to the **API Test Suite** for the **Digikala Cart API**! This repository includes a series of automated tests to ensure the functionality, schema compliance, and correct response content of the API. Below you will find details on how to run the tests and access the results.

## 🗂️ Project Structure

```bash
├── api_test.py           # Contains the test functions
├── requirements.txt      # List of dependencies
├── reports/              # Folder for HTML reports
└── start.sh              # script for run test
```

## 🔍 Tests Overview

The tests are designed to validate:

1. **Status Code**: Ensure the API returns the correct status code (200 OK).
2. **API Schema**: Validate that the API response matches the expected JSON schema.

### 🧑‍💻 Test Breakdown:

* **test\_api\_status\_code**:

  * **Purpose**: Verify that the API returns a `200 OK` status code on a successful request.
  * **Test Logic**: Sends a POST request with product data and asserts that the status code is `200`.

* **test\_api\_schema**:

  * **Purpose**: Ensure the API response matches the predefined JSON schema.
  * **Test Logic**: Validates the response body using the `jsonschema` library.

---

## 🏃‍♂️ How to Run the Tests

### Step 1: Set Up the Environment

First, make sure to install the dependencies:

```bash
pip install -r requirements.txt
```

### Step 2: Run the Tests

To run the tests and generate an HTML report, use this command:

```bash
pytest --html=reports/test_report.html --self-contained-html
```
Or

```bash
bash ./start.sh
```

This will run all tests and create a complete HTML report in the `Api_test_report` directory.

### Step 3: View the Test Report

Once the tests are complete, you can open the generated `api_test_report.html` file in any browser to see a detailed breakdown of:

* **Test results**: Pass or Fail status for each test.
* **Detailed error messages**: If any test fails, it will provide insights into the cause.
* **Overall test summary**: Summary of all tests with the count of passed and failed tests.

---

## 📄 Example Test Output

Here’s an example of how the test output may look in the HTML report:

### Status Code Test:

* **Test Name**: `test_api_status_code`
* **Result**: ✅ Passed
* **Details**: `The API returned a status code of 200, indicating success.`

### Schema Validation Test:

* **Test Name**: `test_api_schema`
* **Result**: ✅ Passed
* **Details**: `The API response matched the predefined JSON schema.`

---

## 🛠️ Dependencies

You can find all required dependencies in the `requirements.txt` file.

---
