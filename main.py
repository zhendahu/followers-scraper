from datetime import datetime
from turtle import update
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from pynput.mouse import Controller
import re

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

def update_followers(driver):
    followers = set()
    followers_list = driver.find_elements(By.CLASS_NAME, "_ab8y")

    for i in followers_list:
        innerText = i.get_attribute("innerText")
        if(innerText != '.' and innerText != '·' and innerText != 'Verified') :
            followers.add(innerText)

    return followers

def update_following(driver):
    following = set()
    following_list = driver.find_elements(By.CLASS_NAME, "_ab8y")

    for i in following_list:
        innerText = i.get_attribute("innerText")
        if (innerText != '.' and innerText != '.' and innerText != 'Verified'):
            following.add(innerText)
    
    return following

# type parameter will either be "following" or "followers"
def get_names(driver, type: str):

    driver.get(f"http://www.instagram.com/zhendawho/{type}")

    time.sleep(2)
    mouse = Controller()
    mouse.position = (525, 573)

    update_counter = 0

    if type == "followers":
        while not len(followers) >= NUM_FOLLOWERS - 10:
            mouse.scroll(0, -40)
            time.sleep(SCROLL_BUFFER)
            update_counter += 1

            if update_counter % 500 == 0:
                followers.update(update_followers(driver))
                with open('followers.txt', 'w') as file:
                    file.write('\n'.join(followers) + "\n")
                print(len(followers))
    
    else:
        while not len(following) >= NUM_FOLLOWING - 10:
            mouse.scroll(0, -40)
            time.sleep(SCROLL_BUFFER)
            update_counter += 1

            if update_counter % 500 == 0:
                following.update(update_following(driver))
                with open('following.txt', 'w') as file:
                    file.write('\n'.join(following) + "\n")
                print(len(following))

def find_diff():
    with open("followers.txt") as followers:
        contents = followers.read()
        with open("following.txt") as following:
            following_lines = following.readlines()
            print("Listed below are users who do not follow you back.")
            for i in range(len(following_lines)):
                if following_lines[i] not in contents:
                    print(following_lines[i])

            following.close()
    followers.close()


if __name__ == "__main__":
    USERNAME = input("Please enter your username: \n")
    PASSWORD = input("Please enter your password: \n")
    SCROLL_BUFFER = 0.4

    followers = set()
    following = set()
    driver = webdriver.Chrome()
    driver.set_window_size(1080, 800)
    driver.set_window_position(0,0)
    driver.get(f"http://www.instagram.com")
    

    login(driver)

    time.sleep(2)

    driver.get("http://www.instagram.com/zhendawho/")

    time.sleep(1)
    num_followers_string = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span').text

    num_following_string = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/div/span').text

    NUM_FOLLOWERS = int(re.sub('[^0-9]', '', num_followers_string))
    print("num followers: ")
    print(NUM_FOLLOWERS)

    NUM_FOLLOWING = int(re.sub('[^0-9]', '', num_following_string))
    print("num following: ")
    print(NUM_FOLLOWING)

    get_names(driver, followers)
    print("got followers")
    
    get_names(driver, following)
    print("got following")

    find_diff()


    