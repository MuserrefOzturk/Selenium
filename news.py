from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

driver= webdriver.Chrome()
url="https://www.hurriyet.com.tr/ekonomi/son-dakika-fed-faiz-kararini-acikladi-42333373"
driver.get(url)
time.sleep(2)
title=driver.find_element(By.CLASS_NAME,"container").find_element(By.TAG_NAME,"h1").text
image=driver.find_element(By.CLASS_NAME,"news-media").find_element(By.TAG_NAME,"img")
img=image.get_attribute("src")
description=driver.find_element(By.CLASS_NAME,"container").find_element(By.TAG_NAME,"h2").text
content=driver.find_element(By.CSS_SELECTOR,".news-content.readingTime").find_elements(By.TAG_NAME,"p")


t=driver.find_element(By.CLASS_NAME,"news-inf").find_element(By.CLASS_NAME,"news-date")
publishDate=t.text.replace("Oluşturulma Tarihi: ", "").split()
time.sleep(3)

month = publishDate[0]
day = publishDate[1][:-1]
year = publishDate[2]
time1 = publishDate[3]
month_dict = {"Ocak":"01" ,"Şubat":"02", "Mart":"03", "Nisan":"04", "Mayıs":"05", "Haziran":"06",
              "Temmuz":"07", "Ağustos":"08", "Eylül":"09", "Ekim":"10", "Kasım":"11", "Aralık":"12"}
formatted_date = f"{day}.{month_dict[month]}.{year} {time1}" 

json_data = {
"Title": title,
"Image": img,
"Description": description,
"Content": [p.text for p in content],
"Publish Date": formatted_date
}
with open("task.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)