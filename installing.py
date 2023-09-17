from selenium import webdriver
import time
driver= webdriver.Chrome()
url="https://github.com"
driver.get(url)
time.sleep(5)
driver.maximize_window()
time.sleep(2)
#driver.save_screenshot("github-homepage.png")
url="https://github.com/MuserrefOzturk"
driver.get(url)
if "MuserrefOzturk" in driver.title:
    driver.save_screenshot("github-page.png")
time.sleep(3)
driver.back()
#driver.forward()
print(driver.title)
time.sleep(5)
driver.close()