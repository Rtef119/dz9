from bs4 import BeautifulSoup
import requests



resource = requests.get("https://bank.gov.ua/")
if resource.status_code==200:
    soup = BeautifulSoup(resource.text,features="html.parser")
    Dolar = soup.find("p","<div class='col-xs-4'><div class='left'><div class='value index-page'>39<small>,3054</small>")
    print(Dolar.text)