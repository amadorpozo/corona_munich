import requests
from bs4 import BeautifulSoup
import re

# if no using some headers, wikiloc answers HTML error 503, probably they protect their servers against scrapping
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',}


def main():
    print("##############################")
    response=requests.get("http://www.muenchen.de/rathaus/Serviceangebote/familie/kinderbetreuung/corona.html#geschlossene-kitas-oder-kitagruppen-_6", headers=headers)
    soup=BeautifulSoup(response.text, "lxml")
    p = soup.find("p", text =re.compile("geschlossen"))
    if p != None:
        kitaUl = p.findNext("ul")
        kitaList = kitaUl.find_all("li")
        # for kita in kitaList:
        #     print("KITA: " + kita.text)
        print("TOTAL closed Kitas=", len(kitaList))
    else: 
        print("Error, Kita list not found")
        
    print("##############################")
    response=requests.get("http://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/", headers=headers)
    soup2=BeautifulSoup(response.text, "lxml")
    munich = soup2.find("td", text =re.compile("München Stadt"))
    if munich != None:
        change = munich.findNext("td").findNext("td")
        average=change.findNext("td").findNext("td").findNext("td")
        print("Munich 7-day average %s, today´s increase %s" %(re.sub(r"\s+", "", average.text), re.sub(r"\s+", "", change.text)))
    else: 
        print("Error, Munich row not found")
    print("##############################")
    exit


if __name__ == "__main__":
    main()