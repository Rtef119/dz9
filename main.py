from bs4 import BeautifulSoup
import requests



resource = requests.get("https://bank.gov.ua/")
if resource.status_code==200:
    soup = BeautifulSoup(resource.text,features="html.parser")
    Dolar = soup.find("p",'<span class="DFlfde SwHCTb" data-precision="2" data-value="35.942400000000006">35,94</span>')
    print(Dolar.text)
    Evro = soup.find("p","<span class='DFlfde SwHCTb' data-precision='2' data-value='39.2401152'>39,24</span>")
    print(Evro.text)