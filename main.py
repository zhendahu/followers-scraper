from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time

USERNAME = input("Please enter your username: \n")
PASSWORD = input("Please enter your password: \n")

followers = set()

driver = webdriver.Chrome()
driver.get(f"http://www.instagram.com")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[name='password']")))

username.clear()
username.send_keys(USERNAME)

password.clear()
password.send_keys(PASSWORD)

Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(2)
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

time.sleep(2)
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

time.sleep(2)

driver.get("http://www.instagram.com/zhendawho/followers")

time.sleep(2)

print("finding followers")
followers_list = driver.find_elements(By.CLASS_NAME, "_ab8y")

for i in followers_list:
    print(i.get_attribute("innerText"))
    followers.add(i.get_attribute("innerText"))
# //*[@id="f30e37da85e3ac"]/div/div/span/a/span/div
# //*[@id="f2f05aa2d262fd8"]/div/div/span/a/span/div

# #f2f05aa2d262fd8 > div > div > span > a > span > div
#f15a1cfac096eec > div > div > span > a > span > div

print("parsing followers")
for i in followers_list:
    if i.get_attribute('href'):
        followers.add(i.get_attribute('href').split("/")[3])
    else:
        continue

print("writing followers")
with open('followers.txt', 'a') as file:
    file.write('\n'.join(followers) + "\n")

print("done!")
# <div class=" _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm">anuj.the.manuj</div>

# for i in followers_list:
#     print(i)

