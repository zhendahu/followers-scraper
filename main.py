from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

USERNAME = input("Please enter the username: \n")


driver = webdriver.Chrome()
driver.get(f"http://www.instagram.com/{USERNAME}/")


driver.close()