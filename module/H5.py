from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as Soup
import os
import json
import re

def login(account,password,browser):
    #點擊右上角登入
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'login')))
    browser.find_element(By.CLASS_NAME,'login').click()
    time.sleep(0.5)

    #點選帳號密碼登入
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"text-blue")))
    browser.find_element(By.CLASS_NAME,"text-blue").click()
    time.sleep(0.5)

    #輸入帳號密碼
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'van-field__control')))
    browser.find_elements(By.CLASS_NAME,"van-field__control")[0].send_keys(account)
    browser.find_elements(By.CLASS_NAME,"van-field__control")[1].send_keys(password)
    time.sleep(0.5)
    #點擊登入
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"van-button--primary")))
    browser.find_elements(By.CLASS_NAME,"van-button--primary")[0].click()
    time.sleep(0.5)
    
    #跳轉PG電子
    browser.get("https://m.bsportstest.com/digital?gameId=38001&channelId=38&gameType=3&platFormId=38003&gameName=PG%E7%94%B5%E5%AD%90")
    

    #計算場館數量
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'game-item')))
    game_count = len(browser.find_elements(By.CLASS_NAME,"game-item"))
    #進入各場館
    for i in range(0,game_count):
        #調整網頁進入遊戲場館
        browser.find_elements(By.CLASS_NAME,"game-item")[i].click()
        browser.find_elements(By.CLASS_NAME,"play-btn")[i].click()

        #調整畫面，並選擇遊戲場館頁面
        browser.switch_to.window(browser.window_handles[1])
        browser.set_window_size(1024, 768)

        #等待開始按鈕並點擊
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME,"start-button-inner")))
        browser.get_screenshot_as_file("2330.png")
        browser.find_element(By.CLASS_NAME,"start-button-inner").click()

        #獲得canvas
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"gameCanvas")))
        canvas = browser.find_element(By.CLASS_NAME,"gameCanvas")
        #獲取帳戶餘額
        ActionChains(browser).move_to_element_with_offset(canvas,100,608).click().perform()
        time.sleep(2)
        balance = browser.find_elements(By.CLASS_NAME,"sc-breuTD")[1].text
        balance  = int(''.join(re.findall(r'\d+', balance.split('.')[0])))

        ActionChains(browser).move_to_element_with_offset(canvas,100,100).click().perform()
        #點擊按鈕
        ActionChains(browser).move_to_element_with_offset(canvas,180,560).click().perform()

        #再次獲取帳戶餘額
        ActionChains(browser).move_to_element_with_offset(canvas,100,608).click().perform()
        balance2 = browser.find_elements(By.CLASS_NAME,"sc-breuTD")[1].text
        balance2  = int(''.join(re.findall(r'\d+', balance.split('.')[0])))

        if (balance2 - balance)/balance > 0.1 :
            print("error")

