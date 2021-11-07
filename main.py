from time import sleep
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

phones = []

for page in range(5):
    try:
        page = requests.get("https://www.skroutz.gr/c/40/kinhta-thlefwna/m/15053/Xiaomi.html?page="+str(page))
        soup = BeautifulSoup(page.text, "html.parser")
    except requests.exceptions.RequestException as error:
        print(error)


    phone_data = soup.findAll('li', attrs= {'class': "cf card with-skus-slider"})

    for data in phone_data:
        phones.append(data.find("div", class_ = "card-content").h2.a.text) 

    print(phones)      
    sleep(5)
        
phones_df = pd.DataFrame({"Phone": phones})  
print(phones_df)





