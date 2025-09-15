from locust import HttpUser, task, between, events
import json
import csv
import time

class DigiKalaUser(HttpUser):
    wait_time = between(1, 5)
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.digikala.com',
        'referer': 'https://www.digikala.com/',
        'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        'x-web-client': 'desktop',
        'x-web-optimize-response': '1',
    }

    report_file = 'load_test_report.csv'
    fieldnames = ['timestamp', 'task', 'response_time_s', 'status_code']

    @classmethod
    def on_start(cls):
        with open(cls.report_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cls.fieldnames)
            writer.writeheader()

    @task(1)
    def add_product_to_cart(self):
        payload = {
            "variant_ids": [70672040],
            "pass": True
        }
        
        start_time = time.time()
        response = self.client.post(
            "/v2/cart/add/", 
            headers=self.headers, 
            data=json.dumps(payload)
        )
        end_time = time.time() 
        
        response_time = end_time - start_time
        
        self.log_to_csv('add_product_to_cart', response_time, response.status_code)

    @task(2)
    def view_cart(self):
        start_time = time.time()
        response = self.client.get(
            "/v2/cart", 
            headers=self.headers
        )
        end_time = time.time()
        
        response_time = end_time - start_time
    
        self.log_to_csv('view_cart', response_time, response.status_code)

    def log_to_csv(self, task_name, response_time, status_code):
        """Function to log results into CSV file."""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        with open(self.report_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow({
                'timestamp': timestamp,
                'task': task_name,
                'response_time_s': response_time,
                'status_code': status_code
            })

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print(f"Load Test Finished. Results saved to {DigiKalaUser.report_file}")
