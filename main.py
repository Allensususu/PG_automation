from ctypes.wintypes import WORD
from email import message
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as Soup
import os
import random, string
import requests
import PC
from webdriver_manager.chrome import ChromeDriverManager




url = 'https://www.bsportstest.com/'  

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)


if __name__ == '__main__' :
        PC.login("coreycny2","1qaz2wsx",browser)


