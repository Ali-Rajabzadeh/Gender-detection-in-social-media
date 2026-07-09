import numpy as np
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pickle

BoyName_url = "https://nameniko.com/names/gender-boy/category-music?category=irani&category=international&category=bird&category=imam&category=history&category=shahname&category=luxury&category=nature&category=quran&category=flower&category=religious&category=sky&order=firstname_acs"
GirlName_url = "https://nameniko.com/names/gender-girl/category-music?category=irani&category=international&category=bird&category=imam&category=history&category=shahname&category=luxury&category=nature&category=quran&category=flower&category=religious&category=sky&order=firstname_acs"

websites = {
    "Boy": BoyName_url,
    "Girl": GirlName_url,
}

name_dict = {}

# =================================================================================================
# scarping data

driver = webdriver.Chrome()

for gender, url in websites.items():

    driver.get(url)

    last_height = 0

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")

    name_list = []
    for a in soup.select("a.name-value"):
        href = a.get("href")
        if href:
            name_list.append(href.rstrip("/").split("/")[-1])

    name_dict[gender] = name_list

driver.quit()

# =================================================================================================
## saving dictionary

with open('name_dict_website_1.pkl', "wb") as file:
    pickle.dump(name_dict, file)
