from selenium import webdriver

user_data_dirs = "/tmp/u1"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={user_data_dirs}')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Remote(command_executor='http://localhost:4444',options=chrome_options)

