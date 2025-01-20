import time
import requests
from bs4 import BeautifulSoup

url1='https://www.google.com/finance/quote/NIFTY_50:INDEXNSE'
url2='https://www.google.com/finance/quote/SENSEX:INDEXBOM'

response1=requests.get(url1)
response2=requests.get(url2)

soup1=BeautifulSoup(response1.text,"html.parser")
soup2=BeautifulSoup(response2.text,"html.parser")

nif=soup1.find(class_="YMlKec fxKbKc").text
sen=soup2.find(class_="YMlKec fxKbKc").text

print("nifty: " + nif )
print("sensex: " + sen )