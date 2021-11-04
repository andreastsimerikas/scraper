import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

phone = []

page = requests.get("https://www.skroutz.gr/c/40/kinhta-thlefwna.html?page=1")
soup = BeautifulSoup(page.text, "html.parser")
phone_data = soup.findAll('li', attrs= {'class': "cf card with-skus-slider"})

for data in phone_data:
    phone.append(data.find("div", class_ = "card-content").h2.a.text)   
    
phone_df = pd.DataFrame({"Phone": phone})  

print(phone_df)




