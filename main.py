import discogs_client
from bs4 import BeautifulSoup as bs
from typing import List
import requests

def identify():
    return discogs_client.Client("TestRequests",user_token="urhZlLQUyxkJEEigCxyTzvfIyIhWufqurtodSgwJ")

def get_wantlist(d):
    return d.identity().wantlist

def get_release(d,release):
    return d.release(release)

def scrap_web_page(link: str):
    r = requests.get(link)
    soup = bs(r.content,features="html.parser")
    parsed_sellers = soup.find_all("td",attrs={"class":"seller_info"}) # Get all sellers
    parsed_sellers_attributes = [seller.find_all("a") for seller in parsed_sellers] # Create a list of list of fighter first names, last names and surname
    return get_sellers(parsed_sellers_attributes)

def get_sellers(parsed_sellers):
    names=[]
    for seller in parsed_sellers:
        index=0
        for attribute in seller:
            if index == 0:
                names.append(attribute.get_text())
                index+=1
    return names

def generate_link(ref:str) -> str : 
    print("https://discogs.com/fr/sell/release/{}?ev=rb".format(ref))
    return "https://discogs.com/fr/sell/release/{}?ev=rb".format(ref)


def main(ref1="",ref2="",ref3=""):

    d = identify()

    refs = [ref1,ref2,ref3]
    links = [generate_link(ref) for ref in refs]
    results = [scrap_web_page(link) for link in links]
    print(results)
    return results

main("4485099","10949522","4468030")

