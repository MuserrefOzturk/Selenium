from githubUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.followers=[]
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element(By.NAME,"login").send_keys(self.username)
        self.browser.find_element(By.NAME,"password").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element(By.NAME,"commit").click()
        time.sleep(1)
    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
    
github=Github(username,password)
github.signIn()
github.getFollowers()


        
        