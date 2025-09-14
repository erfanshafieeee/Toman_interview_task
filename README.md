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
