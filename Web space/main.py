import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener,KeyCode
from selenium import webdriver

# create a new Chrome driver
driver = webdriver.Chrome()
# create a new Chrome driver
driver = webdriver.Chrome()
# navigate to a website
driver.get("https://www.youtube.com/")

TOGGLE_KEY = KeyCode(char="q")
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 2)
        time.sleep(5.0)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking= not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event)as listener:
    listener.join()
    clicker.quit()