from argparse import Action
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

driver = webdriver.Chrome()
driver.get("http://www.instagram.com/zhendawho")
scroll = ActionChains(driver)
scroll.scroll_by_amount(0, -100)
scroll.perform()

