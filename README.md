## My first approach with Python automation framework

1. Install dependencies with `pip install -r requirements.txt`
2. Run tests with `py.test --alluredir=allure_result_folder src/test/tests`
3. You can generate:
    1. static HTML report with `allure generate allure_result_folder`
    2. or you can serve Allure report with `allure serve allure_result_folder`