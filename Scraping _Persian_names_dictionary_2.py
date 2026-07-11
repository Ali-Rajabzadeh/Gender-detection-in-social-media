import numpy as np
import pandas as pd
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pickle

name_dict = {}

# =================================================================================================
# scarping data

names = []
for i in range(1, 53): # I found maximum pages in website and it was 53
    BoyName_url_2 = f"https://abadis.ir/name/boy/?sort=asc&pn={i}"
    page = requests.get(BoyName_url_2)
    soup = BeautifulSoup(page.text, 'html.parser')
    list_name = soup.select("span.boxName")

    for name in list_name:
        if name.find("i").get_text(strip=True) == 'پسر':
            names.append(name.find("a").get_text(strip=True))

name_dict["Boy"] = names


names = []
for i in range(1, 53):
    BoyName_url_2 = f"https://abadis.ir/name/girl/?sort=asc&pn={i}"
    page = requests.get(BoyName_url_2)
    soup = BeautifulSoup(page.text, 'html.parser')
    list_name = soup.select("span.boxName")

    for name in list_name:
        if name.find("i").get_text(strip=True) == 'دختر':
            names.append(name.find("a").get_text(strip=True))

name_dict["Girl"] = names

# =================================================================================================
## saving dictionary

with open('name_dict_website_2.pkl', "wb") as file:
    pickle.dump(name_dict, file)