from githubUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


browser=webdriver.Chrome()

def loadFollowers():
    followers=[]
    items=browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
    for i in items:
        followers.append(i.find_element(By.CSS_SELECTOR, ".Link--secondary").text)
    print(followers)

def getFollowers(username):
    browser.get(f"https://github.com/{username}?tab=followers")
    time.sleep(2)
    loadFollowers()

    while True:
        links= browser.find_element(By.CLASS_NAME,"pagination").find_elements(By.TAG_NAME, "a")

        if len(links) ==1:
            if links[0].text == "Next":
                links[0].click()
                time.sleep(1)
            else:
                break
        else:
            for link in links:
                if link.text == "Next":
                    link.click()
                    time.sleep(1)
                    loadFollowers()
                else:
                    continue   

getFollowers("sadikturan")
