import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.mouse import Button, Controller
  
driver = webdriver.Chrome()
driver.set_window_size(1080, 800)
driver.set_window_position(0,0)

mouse = Controller()


  
# open the webpage
driver.get("http://www.instagram.com")
  
# target username
username = WebDriverWait(
    driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='username']")))
  
# target Password
password = WebDriverWait(
    driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='password']")))
  
# enter username and password
username.clear()
username.send_keys("zhendawho")
password.clear()
password.send_keys("HoshiLoshi21!")
  
# target the login button and click it
button = WebDriverWait(
    driver, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']"))).click()
  
time.sleep(5)
  
driver.get("https://www.instagram.com/zhendawho/followers/")
  
mouse.position = (525, 573)
  
# Scroll till Followers list is there
while True:
    mouse.scroll(0, -2)
    time.sleep(1)
  
driver.quit()

 