
pytest --html=Api_test_report/api_test_report.html --self-contained-html api_test.py

robot --outputdir ./results/login_tests tests/login_tests.robot

robot --outputdir ./results/pay_test tests/pay_test.robot

