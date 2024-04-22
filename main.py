from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
Price =[]
Product_name =[]
Reviews=[]
url = 'https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy,4io'

page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')
# box = soup.find_all("div",class_="DOjaWF gdgoEp")
names = soup.find_all("div",class_="KzDlHZ")
# print(names)
for i in names:
  name =i.text
  Product_name.append(name)
  np.unique(Product_name)
  
print(len(Product_name))
prices =soup.find_all("div",class_="Nx9bqj _4b5DiR")
for i in prices:
  name =i.text
  Price.append(name)
  np.unique(Price)
  
print(len(Price))

df = pd.DataFrame({"Product Name":Product_name,"Prices":Price})
df.to_csv("flipkart_mobiles_under_50000.csv")