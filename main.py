from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("You need to type anything for this search")

time.sleep(5)

driver.quit()