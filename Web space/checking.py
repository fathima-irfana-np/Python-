from selenium import webdriver
import time 


# create a new Chrome driver
driver = webdriver.Chrome()

# navigate to a website
driver.get("https://freebitco.in/")

time.sleep(200)
driver.quit()
