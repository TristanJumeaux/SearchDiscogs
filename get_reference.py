from typing import List
import requests
import sys
import csv
import pandas as pd
from difflib import SequenceMatcher

def read_wantlist():
    return pd.read_csv("wantlist.csv",sep=";")

def compare_names(df:pd.DataFrame, col1:str, col2:str, ref_to_check:str) -> SequenceMatcher:
    return SequenceMatcher(None, df[col1].upper()+" "+df[col2].upper(),ref_to_check.upper()).ratio()

def find_closest_record(ref_to_check:str, df_wantlist:pd.DataFrame) -> pd.DataFrame:
    df_wantlist["comp"] = df_wantlist.apply(compare_names,args=("Artist","Title",ref_to_check),axis=1)
    return df_wantlist.loc[df_wantlist["comp"]>0.85]

def forall_refs(refs):
    df_result = pd.DataFrame(columns=["Reference","Artist","Title","Year","Label"])
    for ref in refs:
        df_result = df_result.append(find_closest_record(ref,df_wantlist).drop(columns="comp"))
    return df_result


if __name__ == "__main__":

    refs_to_check = sys.argv[1:]
    df_wantlist = read_wantlist()
    df_result=forall_refs(refs_to_check)
    if len(df_result)>0:
        print("Here are the refs you need : \n",df_result.head())
    else:
        print("There might be an error in your input. Or the record might not be in your wantlist. \nPlease make sure to put artist then title.")

