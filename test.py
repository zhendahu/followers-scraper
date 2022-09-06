import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
  
driver = webdriver.Chrome()
  
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
  
pop_up_window = driver.find_elements(By.CLASS_NAME, "_aano")
  
# Scroll till Followers list is there
while True:
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
      pop_up_window)
    time.sleep(1)
  
driver.quit()

 