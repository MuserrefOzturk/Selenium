from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
url="http://www.python.org"
driver.get(url)
searchInput = driver.find_element(By.NAME,"q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)

time.sleep(2)
driver.close()
