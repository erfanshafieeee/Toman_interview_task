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

2. **Execute the Test:**

   ```bash
   locust -f locustfile.py --headless --users 3000 --spawn-rate 10 --run-time 5m
   ```

   This command initiates the test with 3,000 virtual users, a spawn rate of 10 users per second, and a duration of 5 minutes. The results are saved in `results/report.html`.

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

