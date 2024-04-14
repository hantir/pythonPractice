import argparse
import time
import json
import csv
import re
import sys
import os

import pyautogui
from random import randint
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

loopNumber=10
#my_email=sys.argv[2]
#my_password=sys.argv[3]

fburl = "https://www.facebook.com/"
chrome_driver=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

htmlfile=str(os.path.basename(sys.argv[1]))
outputfile=htmlfile+"_output"+".txt"

firsttag="x9f619 x1n2onr6 x1ja2u2z x1jx94hy x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld"
firsttaglist=["xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs","xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"]
htmlurl="https://www.facebook.com/groups/"+htmlfile

def extract_text(item):
    final = ""
    bs_data1 = bs(str(item), 'html.parser')
    k1 = bs_data1.find_all("div", {"class":firsttaglist})
    for item1 in k1:
        one=re.sub(r"\s+$", "", item1.text, 0, re.MULTILINE)
        two=re.sub(r"^\s+", "", one, 0, re.MULTILINE)
        final += two+"~"
    return final
    
def extract_first_level(htmlfile):
    fp = open(htmlfile, "r", encoding="utf8")
    bs_data = bs(fp, 'html.parser')
    k = bs_data.find_all("div", {"class":firsttag})
    i=0
    
    for item in k:
        postdata=extract_text(item)
        with open(outputfile, 'a', encoding='utf8') as file1:
            if len(postdata)!=0:
                i=i+1
                file1.write(str(i)+":"+postdata+"\n")

#extract_first_level(htmlfile)           

def extract_first_level_url(htmlurl, driver):
    driver.get(htmlurl)
    bs_data = bs(driver.page_source, 'html.parser')
    k = bs_data.find_all("div", {"class":firsttag})
    i=0
    
    for item in k:
        postdata=extract_text(item)
        with open(outputfile, 'a', encoding='utf8') as file1:
            if len(postdata)!=0:
                i=i+1
                file1.write(str(i)+":"+postdata+"\n")

def random_scroll(pages, driver):
    for i in range(0, pages):
        scrollDownPixel = -randint(200, 500)
        scroolTime1 = randint(10, 20)
        scroolTime2 = randint(10, 50)
        print(i)
        time.sleep(scroolTime1)
        pyautogui.scroll(scrollDownPixel)
        #time.sleep(scroolTime2)

def random_scroll_selenium(ln, driver):
    for i in range(0, ln):
        scroolTime1 = randint(10, 20)
        scroolTime2 = randint(10, 50)
        #print(i)
        #print(scroolTime1)
        #time.sleep(scroolTime1)
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, firsttag)))
        #time.sleep(scroolTime2)
        print(element)

#chrome_options = Options()
#chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#driver.get(htmlurl)
#print(driver.title)
#random_scroll(loopNumber, driver)
#element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, firsttag)))
#print(element)
#driver.quit()

extract_first_level(htmlfile)