from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# create an instance of the Chrome driver
driver = webdriver.Chrome()

# navigate to the website login page
driver.get("https://freebitco.in/?op=home")

# find the email input field and enter the email
email_field = driver.find_element_by_id("login_form_btc_address")
email_field.send_keys("your_email@example.com")

# find the password input field and enter the password
password_field = driver.find_element_by_id("password")
password_field.send_keys("your_password")

# submit the form by pressing Enter on the password field
password_field.send_keys(Keys.RETURN)

# wait for the login to complete and the user dashboard to load
driver.implicitly_wait(10)

# do some actions on the user dashboard
# ...
time.sleep(20)
# close the browser
driver.quit()
