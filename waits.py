import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Set up the ChromeDriver service
# service = Service(r"C:/Users/Kiran/Downloads/chrome-win64/chromedriver.exe")
driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()

search_box = driver.find_element(By.XPATH, "//input[@type='search']")
search_box.send_keys('ber')
time.sleep(3)


results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:
    result.find_element(By.XPATH,"div/button").click()
    time.sleep(3)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,".promoInfo"))
print(driver.find_element(By.CLASS_NAME,'.promoInfo').text)










