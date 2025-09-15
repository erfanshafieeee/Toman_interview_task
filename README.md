
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
