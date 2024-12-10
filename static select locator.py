import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(service = Service(r"C:/Users/Kiran/Downloads/chrome-win64/chromedriver.exe"))
driver =webdriver.Chrome(service=service)

# driver= webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

Drop_down = Select(driver.find_element(By.ID,'dropdown-class-example'))

Drop_down.select_by_index(2)
# Drop_down.select_by_value()

time.sleep(3)