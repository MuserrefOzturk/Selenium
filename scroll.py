
last_heigth=driver.execute_script("return dokument.dokumentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0,dokument.dokumentElement.scrollHeight);")
    time.sleep(2)
    new_height= driver.execute_script("return dokument.dokumentElement.scrollHeight")
    if last_heigth==new_height:
        break
    last_heigth=new_height