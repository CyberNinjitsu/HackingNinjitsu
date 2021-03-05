# -*- coding: utf-8 -*-
"""
TWITTER SCRAPING BOT 2021

USE A SCRAPER ACCOUNT!
"""

# Block of Essential Python Modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome(executable_path='C:\scraping\chromedriver.exe')
target = "@YOUR TARGET" # hardcoded

def login ():
    driver.get('https://twitter.com/login')
    time.sleep(3)
    username = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    username.send_keys('YOUR ACCOUNT HERE')
    time.sleep(10)
    password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    password.send_keys('PASSWORD')
    password.send_keys(Keys.ENTER)


login()
time.sleep(8)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')))


def profile_finder():
    explore = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]')
    explore.click()
    time.sleep(4)
    search = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')
    search.send_keys(target)
    search.send_keys(Keys.ENTER)
    time.sleep(4)
    profilebtn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[3]/div/div/div/div[2]/div[1]/div[1]/a')
    profilebtn.click()



def extract_data():
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_='css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
    tweets = []
    while True:
        for post in postings:
            tweets.append(post.text)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)    
        soup = BeautifulSoup(driver.page_source, 'lxml')
        postings = soup.find_all('div', class_='css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
        tweets2 = list(set(tweets)) # Removes duplicates!
        if len(tweets2) > 100:
            break

profile_finder()
time.sleep(2)
extract_data()
     
# To search for specific keywords
#new_tweets = []
#for i in tweets2:    
#   if 'Gamer' in i:
#        new_tweets.append(i)











