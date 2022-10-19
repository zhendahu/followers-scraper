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

# This function logs the user in based on the username and password credentials passed in through stdin.
def login(driver):

    # Corresponding username and password HTML fields
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[name='password']")))

    # Enter credentials and click log in
    username.clear()
    username.send_keys(USERNAME)

    password.clear()
    password.send_keys(PASSWORD)

    Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    # Click the "save password" and "manage preferences" popups
    time.sleep(2)
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

    time.sleep(2)
    not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# Returns a set of the usernames of followers.
def update_followers(driver):
    followers = set()
    followers_list = driver.find_elements(By.CLASS_NAME, "_ab8y")

    # Removes junk elements (non-usernames)
    for i in followers_list:
        innerText = i.get_attribute("innerText")
        if(innerText != '.' and innerText != '·' and innerText != 'Verified') :
            followers.add(innerText)

    return followers

# Returns a set of the usernames of following.
def update_following(driver):
    following = set()
    following_list = driver.find_elements(By.CLASS_NAME, "_ab8y")

    # Removes junk elements (non-usernames)
    for i in following_list:
        innerText = i.get_attribute("innerText")
        if (innerText != '.' and innerText != '.' and innerText != 'Verified'):
            following.add(innerText)
    
    return following

# This will get the full list of usernames for either followers and following, and will write them into either "followers.txt" or "following.txt"
# the "type" parameter will either be "following" or "followers"
def get_names(driver, type: str, username: str):
    update_buffer = 500

    if type == "followers" and NUM_FOLLOWERS < 700:
        update_buffer = 250
    elif type == "following" and NUM_FOLLOWING < 700:
        update_buffer = 250

    driver.get(f"http://www.instagram.com/{username}/{type}")

    time.sleep(2)
    mouse = Controller()

    # Set mouse position for scrolling through list
    mouse.position = (525, 573)

    update_counter = 0

    if type == "followers":
        # Because instagram sometimes leaves out users when scrolling, we will break as long as the list contains more than 85% of total followers.
        while not len(followers) >= NUM_FOLLOWERS*0.95:
            mouse.scroll(0, -40)
            time.sleep(SCROLL_BUFFER)
            update_counter += 1

            # Every 500 iterations, update the followers set once. We do this in order to speed up the process, as updating the set every iteration will drastically slow the program down.
            if update_counter % update_buffer == 0:
                followers.update(update_followers(driver))
                with open('followers.txt', 'w') as file:
                    file.write('\n'.join(followers) + "\n")
                print(len(followers))
                update_buffer = ((NUM_FOLLOWERS - len(followers))/NUM_FOLLOWERS)*500
    
    else:
        while not len(following) >= NUM_FOLLOWING*0.95:
            mouse.scroll(0, -40)
            time.sleep(SCROLL_BUFFER)
            update_counter += 1

            if update_counter % update_buffer == 0:
                following.update(update_following(driver))
                with open('following.txt', 'w') as file:
                    file.write('\n'.join(following) + "\n")
                print(len(following))
                update_buffer = ((NUM_FOLLOWING - len(followers))/NUM_FOLLOWING)*500

# Prints out the names of users you follow but don't follow you back.
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
    # Prompt username for login credentials.
    USERNAME = input("Please enter your username: \n")
    PASSWORD = input("Please enter your password: \n")

    # Will scroll once every 0.4 seconds.
    SCROLL_BUFFER = 0.4

    followers = set()
    following = set()
    driver = webdriver.Chrome()

    # Set window size and position for future scrolling. 
    driver.set_window_size(1080, 800)
    driver.set_window_position(0,0)
    driver.get(f"http://www.instagram.com")
    
    login(driver)

    time.sleep(2)

    driver.get(f"http://www.instagram.com/{USERNAME}/")

    time.sleep(1)
    
    # Gets the number of followers the user has and the number of other users the user is following.
    num_followers_string = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div').text

    num_following_string = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a/div').text

    NUM_FOLLOWERS = int(re.sub('[^0-9]', '', num_followers_string))
    print("num followers: ")
    print(NUM_FOLLOWERS)

    NUM_FOLLOWING = int(re.sub('[^0-9]', '', num_following_string))
    print("num following: ")
    print(NUM_FOLLOWING)

    get_names(driver, "followers", USERNAME)
    print("got followers")

    get_names(driver, "following", USERNAME)
    print("got following")

    find_diff()


    