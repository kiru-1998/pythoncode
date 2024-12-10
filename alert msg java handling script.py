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

driver.find_element(By.ID,'name').send_keys('kiran')
driver.find_element(By.ID,'alertbtn').click()

alert = driver.switch_to.alert
alert_text=alert.text
print(alert_text)

alert.accept()
#alert.dismiss()
time.sleep(10)