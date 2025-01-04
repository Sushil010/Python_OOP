from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service=Service(executable_path="Selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("https://www.google.com")


text_box=driver.find_element(By.CLASS_NAME,value="gLFyf")
text_box.send_keys("Selenium"+Keys.ENTER)

time.sleep(5)

driver.quit()