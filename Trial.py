from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
url="https://www.youtube.com/"
driver.get(url)
searchInput = driver.find_element(By.NAME,"search_query")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()