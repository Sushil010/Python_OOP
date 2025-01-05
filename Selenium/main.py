from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service=Service(executable_path="Selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("https://www.google.com")


# to check first if the element is present or not
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

text_box=driver.find_element(By.CLASS_NAME,value="gLFyf")


# to clear the input box
text_box.clear()


# Below command will append what's written in input box
text_box.send_keys("chatgpt"+Keys.ENTER)




WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"chatgpt"))
)
#find the links and clicks on the link provided 
link=driver.find_element(By.PARTIAL_LINK_TEXT,"chatgpt")
link.click()


# texter=driver.find_element(By.ID,"prompt-textarea")
# texter.clear()
# texter.send_keys("Hello, how are you?"+Keys.ENTER)

time.sleep(90)

driver.quit()