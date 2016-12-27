from bs4 import BeautifulSoup
import requests
import os
import time

def check_page(c1,c2):
    if c1 == "DnsIsSuccess":
        print(c2+" success")
    else:
        print(c2+" fail")

list = []
url_get = "http://us.unidingcom.com/spac/a.txt"
req = requests.get(url_get)
soup = BeautifulSoup(req.text,"lxml")
texts = soup.p.text[:-2]
list = texts.split("\n")


for lists in list:
    link = "http://us."+lists+".top"
    try:
        recheck = requests.get(link)
        if recheck.status_code != 200:
            print("fail")
            continue
#        time.sleep(1)
        soups = BeautifulSoup(recheck.text,"lxml")
        textq = soups.div.text
        check_page(textq,link)
    except requests.exceptions.ConnectionError:
        print(link,'fail')
        continue
