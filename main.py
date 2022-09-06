from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
from pynput.mouse import Button, Controller

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
    followers_list = driver.find_elements(By.CLASS_NAME, "_ab8y")

    for i in followers_list:
        innerText = i.get_attribute("innerText")
        if(innerText != '.' and innerText != '·') :
            followers.add(innerText)

    print("done!")
    return followers


if __name__ == "__main__":
    USERNAME = input("Please enter your username: \n")
    PASSWORD = input("Please enter your password: \n")
    SCROLL_BUFFER = 0.5

    followers = set()
    driver = webdriver.Chrome()
    driver.set_window_size(1080, 800)
    driver.set_window_position(0,0)
    driver.get(f"http://www.instagram.com")

    login(driver)

    time.sleep(2)


    driver.get("http://www.instagram.com/zhendawho/followers")

    time.sleep(2)
    mouse = Controller()
    mouse.position = (525, 573)
    #525, 573
    while True:
        mouse.scroll(0, -40)
        time.sleep(SCROLL_BUFFER)

        followers_prev = followers
        followers.update(find_followers(driver))

        if followers_prev == followers:
            print("Breaking")
            break


    with open('followers.txt', 'a') as file:
        file.write('\n'.join(followers) + "\n")