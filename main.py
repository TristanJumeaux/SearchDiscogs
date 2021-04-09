import discogs_client
from bs4 import BeautifulSoup as bs
from typing import List
import requests
import sys

def identify(token):
    return discogs_client.Client("Get common sellers",user_token=token)

def get_wantlist(d):
    return d.identity().wantlist

def get_release_dict(d,refs):
    releases = {}
    for ref in refs:
        release_request = d.release(ref)
        releases[ref] = ref + " - " + release_request.artists[0].name + " - " + release_request.title
    return releases

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
    return list(set(names))

def generate_link(ref:str) -> str :
    return "https://discogs.com/fr/sell/release/{}?ev=rb".format(ref)

def find_most_common_seller(list_seller_ref,ref_tab):
    sellers = {}
    index=0
    for ref in list_seller_ref:
         for seller in ref:
             if seller not in sellers:
                 sellers[seller]=[ref_tab[index]]
             else:
                 sellers[seller].append(ref_tab[index])
         index+=1
    return dict(sorted(sellers.items(), key=lambda item: len(item[1]), reverse=True))

def transform_results(seller_ref,release_dict):
    for key in seller_ref:
        new_value = []
        for value in seller_ref[key]:
            new_value.append(release_dict[value])
        seller_ref[key]=new_value
    return seller_ref

def display_result(tab_result):

    top_results = [[k] + tab_result[k] for k in list(tab_result.keys())[:10]]
    index=0
    for result in top_results:
        index+=1
        print("\n--- " + str(index)+": "+result[0]+" is selling "+str(len(result[1:]))+" of the records : \n"+ '\n'.join(result[1:]))

if __name__ == "__main__":

    token = sys.argv[1]

    d = identify(token)

    refs = sys.argv[2:]

    # Get information about release numbers, faire un dictionnaire pour quand on aura un tab pouvoir inclure les infos
    release_dict = get_release_dict(d,refs)

    # Generate links to scrap for releases
    links = [generate_link(ref) for ref in refs]

    # Scrap the links
    results = [scrap_web_page(link) for link in links]

    # Find common vendors between links
    sellers = find_most_common_seller(results,refs)

    # Add release informations like artists or title
    release_results = transform_results(sellers,release_dict)

    # Display results
    display_result(release_results)
    

