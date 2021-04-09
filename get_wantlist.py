import discogs_client
from bs4 import BeautifulSoup as bs
from typing import List
import sys
import pandas as pd


def identify(token:str):
    return discogs_client.Client("Get Wantlist",user_token=token)

def get_wantlist(user):
    wantlist = user.identity().wantlist
    result = []
    for i in range(wantlist.pages):
        result.extend(wantlist.page(i))
    return result

def clean_names(wantlist):
    result = []
    for record in wantlist:
        result.append([record.release.id,record.release.artists[0].name,record.release.title,record.release.year,record.release.labels[0].name])
    return result

def write_csv(wantlist):
    dfToFlush = pd.DataFrame.from_records(wantlist,columns=["Reference","Artist","Title","Year","Label"]).drop_duplicates()
    dfToFlush.to_csv("wantlist.csv",index=False,sep=";")

if __name__ == "__main__":

    token = sys.argv[1]

    user = identify(token)
    wantlist = clean_names(get_wantlist(user))
    try:
        write_csv(wantlist)
        print("Congratulations ! Everything went perfectly. You're ready to find your references.")
    except:
        print("There was an error while writing the file :( \nPlease verify that you're allowed to write a file.")

