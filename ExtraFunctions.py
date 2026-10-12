# Extra Reused Functions
import json
import pandas as pd
import glob
from jsoncomment import JsonComment

def flatten_json(y):
    out = {}
    def flatten(x, name=""):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + ".")
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + ".")
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

def append_row(df, row):
    return pd.concat([
                df, 
                pd.DataFrame([row], columns=row.index)]
    ).reset_index(drop=True)

def jsonglob_to_df (pathglob):
    df = pd.DataFrame()   
    for path in pathglob: 
        with open(path,encoding="utf8") as file:
            data = json.load(file)
        details=flatten_json(data)
        details["def_path"]= path
        details["def"]= details["Description.Id"]
        new_row = pd.Series(details)
        df = append_row(df, new_row)
        print("done"+ path)
    return df

def parse_components (jpath):
    componet_dict={}     
    with open(jpath,encoding="utf8") as file:
        parser = JsonComment(json)
        data = parser.load(file)
    if "Description" in data:
        if "Id" in data["Description"]:
            componet_dict["ID"] = data["Description"]["Id"]        
        if "UIName" in data["Description"]:
            componet_dict["UIName"] = data["Description"]["UIName"]          
        if "Icon" in data["Description"]:
            componet_dict["Icon"] = data["Description"]["Icon"] 
    if "Type" in data:
        componet_dict["Type"] = data["Type"] 
    if "InventorySize" in data:
        componet_dict["InventorySize"] = data["InventorySize"]
    if "Category" in data:
        componet_dict["Category"] = data["Category"]
    if "Custom" in data:
        if "Category" in data["Custom"]:
            catlength= len(data["Custom"]["Category"])
            catnum=0
            while catnum < catlength:
                catagory_num="catagory"+str(catnum)
                catid=data["Custom"]["Category"][catnum]["CategoryID"]
                componet_dict[catagory_num]=catid
                catnum = catnum+1     
        if "BonusDescriptions" in data["Custom"]:
            componet_dict["Bonusdesc"] = str(data["Custom"]["BonusDescriptions"]) 
    return componet_dict    

#get unique list from column of dataframe
def unique_from_column_df(df,column):  
    columnlist=df[column].tolist()
    unique_columnlist=[]
    for item in columnlist:
        if item not in unique_columnlist:
            unique_columnlist.append(item)
    return unique_columnlist