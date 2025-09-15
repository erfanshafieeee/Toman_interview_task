# Toman Interview Task

# Testcases :

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
# Digikala Login Test Automation 🚀

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
=======



