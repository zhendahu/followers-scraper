from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time

def login(driver):
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


def find_followers(driver):
    followers = set()
    print("finding followers")
    followers_list = driver.find_elements(By.CLASS_NAME, "_ab8y")

    for i in followers_list:
        innerText = i.get_attribute("innerText")

        print(innerText)
        if(innerText != '.' and innerText != '·') :
            followers.add(innerText)

    print("writing followers")
    with open('followers.txt', 'a') as file:
        file.write('\n'.join(followers) + "\n")

    print("done!")
    return followers


if __name__ == "__main__":
    USERNAME = input("Please enter your username: \n")
    PASSWORD = input("Please enter your password: \n")

    followers = set()
    driver = webdriver.Chrome()
    driver.get(f"http://www.instagram.com")

    login(driver)

    time.sleep(2)

    driver.get("http://www.instagram.com/zhendawho/followers")

    time.sleep(2)

    followers = find_followers(driver)
    
    # <div class=" _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm">anuj.the.manuj</div>

