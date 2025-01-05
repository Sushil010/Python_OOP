from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service=Service(executable_path="Selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)


# Search Portion
driver.get("https://www.google.com")

WebdriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

text_box=driver.find_element(By.CLASS_NAME,value="gLFyf")
text_box.clear()
text_box.send_keys("cookie clicker"+Keys.ENTER)


# Finding Link portion
Webdriver.wait(driver,5).until(
    EC.presence_of_element_located((BY.PARTIAL_LINK_TEXT,"Cookie Clicker"))
)

cookie_link=driver.find_element(BY.PARTIAL_LINK_TEXT,"Cookie Clicker")
cookie_link.click()






time.sleep(50)
time.quit()