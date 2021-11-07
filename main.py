from time import sleep
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

num = 0
phones = []

while num<=2:
    num+=1
    try:
        page = requests.get("https://www.skroutz.gr/c/40/kinhta-thlefwna/m/15053/Xiaomi.html?page="+str(num))
        soup = BeautifulSoup(page.text, "html.parser")
    except requests.exceptions.RequestException as error:
        break

    phone_data = soup.findAll('li', attrs= {'class': "cf card with-skus-slider"})

    for data in phone_data:
        phones.append(data.find("div", class_ = "card-content").h2.a.text) 

    print(phones)      
    sleep(5)
        
phones_df = pd.DataFrame({"Phone": phones})  
print(phones_df)





