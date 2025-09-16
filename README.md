# Toman Interview Task

# Testcases :
- **[Testcases - Persian](./testcases_fa.pdf)**

## 🧪 Login Test Cases

### ✅ Positive

```gherkin
Feature: User Login

  Scenario: Successful login with valid mobile number
    Given the user is on the Digikala login page
    When the user enters a valid mobile number "09332766613"
    And enter the verification code
    Then the user should be redirected to the dashboard
```


```gherkin
Feature: User Login

  Scenario: Successful login with valid email
    Given the user is on the Digikala login page
    When the user enters a valid email "erfanshafieeee@gmail.com"
    And enter the password "erfan1234"
    Then the user should be redirected to the dashboard
```

```gherkin
Feature: User Login

  Scenario: Successful login with valid mobile number and password
    Given the user is on the Digikala login page
    When the user enters a valid mobile number "09332766613"
    And enter the password "erfan1234".
    Then the user should be redirected to the dashboard
```

---

### ❌ Negative

```gherkin
Feature: User Login

  Scenario: Unsuccessful login with invalid mobile number
    Given the user is on the Digikala login page
    When the user enters an invalid mobile number "09332766"
    And submits the login form button
    Then an error message "Invalid email or mobile number" should be displayed
```

```gherkin
Feature: User Login

  Scenario: Unsuccessful login with invalid email
    Given the user is on the Digikala login page
    When the user enters an invalid email "Example.com"
    And submits the login form button
    Then an error message "Invalid email or mobile number" should be displayed
```

```gherkin
Feature: User Login

  Scenario: Unsuccessful login with mobile number and incorrect password
    Given the user is on the Digikala login page
    When the user enters a valid mobile number "09332766613"
    And enters an incorrect password
    Then an error message "Incorrect password" should be displayed
```

```gherkin
Feature: User Login

  Scenario: Unsuccessful login with mobile number and incorrect verification code
    Given the user is on the Digikala login page
    When the user enters a valid mobile number "09332766613"
    And enters an incorrect verification code
    Then an error message "Incorrect verification code" should be displayed
```



---

### 🧠 Edge Case

```gherkin
Feature: User Login

  Scenario: Login attempt with unregistered email
    Given the user is on the Digikala login page
    When the user enters a email "Example@gmail.com" that is not registered
    And submits the login form
    Then an error message "No account found with this email" should be displayed
```
```gherkin
Feature: User Login

  Scenario: Login attempt with unregistered mobile number
    Given the user is on the Digikala login page
    When the user enters a mobile number "09333333333" that is not registered
    And submits the login form
    Then the user should be redirected to the account creation page with verification code
```

---

## 🔄 Password Recovery Test Cases

### ✅ Positive

```gherkin
Feature: Password Recovery

  Scenario: Successful password recovery with valid mobile number
    Given the user is on the Digikala password recovery page
    When the user enters a valid mobile number "09332766613"
    And enter the verification code
    Then the user should be redirected to the password recovery page
```

```gherkin
Feature: Password Recovery

  Scenario: Successful password recovery with valid email
    Given the user is on the Digikala password recovery page
    When the user enters a valid email address "erfanshafieeee@gmail.com"
    And submits the recovery form button
    Then the user should receive a password reset link via email
```

---

### ❌ Negative


```gherkin
Feature: Password Recovery

  Scenario: Unsuccessful password recovery with valid mobile number and incorrect verification code
    Given the user is on the Digikala password recovery page
    When the user enters an valid mobile number "09332766613"
    And enter the incorrect verification code
    Then an error message "incorrect verification code" should be displayed
```

```gherkin
Feature: Password Recovery

  Scenario: Unsuccessful password recovery with invalid mobile number
    Given the user is on the Digikala password recovery page
    When the user enters an invalid mobile number "09332766"
    And submits the recovery form button
    Then an error message "Invalid email or mobile number" should be displayed
```

```gherkin
Feature: Password Recovery

  Scenario: Unsuccessful password recovery with invalid email
    Given the user is on the Digikala password recovery page
    When the user enters an invalid email "erfan.com"
    And submits the recovery form button
    Then an error message "Invalid email or mobile number" should be displayed
```

---
### 🧠 Edge Case

```gherkin
Feature: Password Recovery

  Scenario: Password Recovery attempt with unregistered email
    Given the user is on the Digikala password recovery page
    When the user enters a email "Example@gmail.com" that is not registered
    And submits the recovery form
    Then an error message "No account found with this email" should be displayed
```
```gherkin
Feature: User Login

  Scenario: Password Recovery attempt with unregistered mobile number
    Given the user is on the Digikala login page
    When the user enters a mobile number "09333333333" that is not registered
    And submits the recovery form
    Then an error message "No account found with this mobile number" should be displayed
```
---
# Digikala Login and Pay Test Automation 🚀

This project includes automated tests for the Digikala login page using **Robot Framework** and **Selenium**. The test cases cover various login scenarios such as logging in with mobile and email, and a pay process for ordering products.


## 📂 Project Structure

```
Toman_interview_task
│
├── tests/
│   └── login_tests.robot        # Contains the main test cases for login scenarios (mobile & email).
│   └── pay_test.robot           # Contains the test case for successful product purchase after login.
│
└── resources/
    └── keywords/
        └── login_keywords.robot # Contains custom keywords for opening the login page, login with mobile/email, and verifying success/failure.
        └── pay_keywords.robot   # Contains custom keywords for interacting with the Digikala product page, cart, and checkout process.
│
└── results
    └── login_test
        └── report.html
        └── log.html
        └── output.xml
    └── pay_test
        └── report.html
        └── log.html
        └── output.xml


```

## ⚙️ Requirements

* **Robot Framework**: The main framework for writing and running the tests.
* **SeleniumLibrary**: The library used to interact with browsers in web tests.
* **ChromeDriver**: The browser driver for Chrome used to run the tests.

## 📥 Installing Dependencies

To install all the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Tests

To execute the tests, simply run the `start.sh` script:

```bash
bash ./start.sh
```

This will execute the tests and store the results in the `results` folder. 🎉

## 📊 Viewing Test Results

After running the tests, the reports will be saved in the `results` folder. To view the results:

1. Go to the `results` folder.
2. Open the `report.html` and `log.html` files in your browser to see the detailed execution results.
---
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
bash ./start_api_test.sh
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
# 📊 Load Testing Report for Digikala API

## 🧪 Test Overview

* **Test Duration:** 5 minutes
* **Virtual Users:** 3,000
* **Spawn Rate:** 10 users per second
* **Target Endpoint:** `https://api.digikala.com/v2/product/17833952/?_rch=db340a7f7c4f`
* **Test Tool:** [Locust](https://locust.io/)

## 🔧 Test Execution

To run the load test:

1. **Install Locust:**

   ```bash
   pip install locust
   ```
   OR
   ```
   pip install -r requirements.txt
   ```

2. **Execute the Test:**

   ```bash
   locust -f locustfile.py --headless --users 3000 --spawn-rate 10 --run-time 5m
   ```

   This command initiates the test with 3,000 virtual users, a spawn rate of 10 users per second, and a duration of 5 minutes. The results are saved in `load_test_result`.

## 📈 Results Analysis

### 1. Error Rates

* **HTTP 429 (Too Many Requests):** 52,277 occurrences
* **Connection Reset (Error 10054):** 1,122 occurrences

These errors indicate that the server's rate-limiting mechanisms were triggered, likely due to the high volume of requests.

### 2. Response Times

* **Median Response Time (p50):** 480 ms
* **Average Response Time:** 1,430.6 ms
* **95th Percentile Response Time (p95):** 55,003 ms
* **99th Percentile Response Time (p99):** 46,183 ms

The significant increase in response times, especially at higher percentiles, suggests that the server struggled to handle the load, leading to delays in processing requests.

### 3. Request Statistics

* **Total Requests:** 92,908
* **Successful Requests:** 53,999
* **Failure Rate:** 42.1%

The high failure rate underscores the server's inability to manage the traffic effectively, resulting in a substantial number of failed requests.

## 📄 Detailed Report

A comprehensive HTML report detailing the test results, including charts and statistics, is available in the `load_test_result` folder.
---

# Hypothetical Bug Reports for Digikala Website

This repository contains hypothetical bug reports for the Digikala website. These reports aim to address issues that were identified on both the user interface (UI) and functional aspects of the website.

## Contents

- **[Bug Reports - Persian](./Bug_report_fa.md)**: The bug reports are written in Persian and describe the issues encountered on the Digikala website.
- **[Bug Reports - English](./Bug_report_en.md)**: The bug reports are also written in English, detailing the same issues for international teams.

## Bug Descriptions

1. **Payment Failed But Order is Marked as Completed**  
   This bug involves the payment gateway not properly handling failed payments, yet the order is marked as "Completed" in the system.

2. **Price Filter in Category Page Works Incorrectly**  
   The price range filter on the category listing page does not display the expected results and shows products outside of the selected price range.

3. **Incorrect Similar Products Displayed on Product Details Page**  
   Similar products on the product details page are incorrectly shown based on product titles rather than categories, leading to irrelevant suggestions.
---

