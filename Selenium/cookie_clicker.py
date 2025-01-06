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

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

text_box=driver.find_element(By.CLASS_NAME,value="gLFyf")
text_box.clear()
text_box.send_keys("cookie clicker"+Keys.ENTER)


# Finding Link portion
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Cookie Clicker"))
)

cookie_link=driver.find_element(By.PARTIAL_LINK_TEXT,"Cookie Clicker")
cookie_link.click()


# selecting_language from pop up
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"langSelect-EN"))
)
lang=driver.find_element(By.ID,value="langSelect-EN")
lang.click()



# Clicking on the cookie
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"bigCookie"))
)
for cookie in range(100):
    cookie_id=driver.find_element(By.ID,value="bigCookie")
    cookie_id.click()
    # time.sleep(0.1)
    
# cookie_id=driver.find_element(By.ID,value="bigCookie")
# cookie_id.click()

# check no of cookies
cookie_count=driver.find_element(By.ID,value="cookies")
print(cookie_count.text())

# buy items
cursor=driver.find_element(By.ID,value="product0")
cursor_price=driver.find_element(By.ID,value="productPrice0")
cursor_number=driver.find_element(By.ID,value="productOwned0")

# while(cookie_count<5):
#     # if(cookie_count > cursor_price):
#     #     cursor.click()
#     cursor.click()






time.sleep(50)
time.quit()