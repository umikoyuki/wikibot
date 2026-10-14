# Extra Reused Functions
import json
import pandas as pd
import glob
from jsoncomment import JsonComment
import numpy

from Paths import*


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

def table_index_list(table_path):
    df = pd.read_parquet(table_path)
    index_list=df.index.values.tolist()
    return index_list

def getmechmod (Mech_def_path,mods_df):
    modpath=Mech_def_path.replace("\\","/")
    modpath=modpath.removeprefix(rt_path)
    last_delimiter_index = modpath.rfind("/")
    if last_delimiter_index != -1:
        modpath=modpath[:last_delimiter_index]
    else:
        modpath=modpath
    modpath=modpath[:-5]
    try:
        modname=mods_df.loc[modpath]["Name"]
    except:
        print("getmechmod"+modpath)
        modname="DUMMY"
    return modname

def listtosting(divlist):
    string=""
    for item in divlist:
        string=string+item
    return string

#get list of component catagories from comp table
def getcomp_categories(component_id,components_df):
    Catagories=[]
    num=0
    while "catagory"+ str(num) in components_df:
        try:
            Catagories.append(components_df.loc[component_id]["catagory"+str(num)])
        except KeyError as e:
            print ("getcomp_categories",e,component_id,num) 
        num=num+1
    return Catagories


def get_factionlist(mechtags, factions_df):
    all_factions = factions_df.index.tolist()
    Faction_name_list=[]
    for tag in mechtags:
        tag=str(tag)
        lowertag=tag.lower()
        if lowertag in all_factions:
            try:
                faction_name = factions_df.loc[lowertag]["name"]
                faction_link = f"[[{lowertag}|{faction_name}]]<br>"
                Faction_name_list.append(faction_link)
            except:
                print(lowertag)
    Factions_list=listtosting(Faction_name_list)
    return Factions_list

def cat_sorter_search(Comp_id,components_df,color_keys,color_df):
    cat_num=0
    sorters=str(999)
    while "catagory"+str(cat_num) in components_df:
        try:
            categorycolumn="catagory"+str(cat_num)
            cat=components_df.loc[Comp_id][categorycolumn]
            if cat in color_keys:
                sorter=color_df.loc[cat]["Sorter"]
                if numpy.isnan(sorter):
                    pass
                else:       
                    sorters=str(int(sorter))
        except KeyError:
            pass
        cat_num= cat_num +1 
    return sorters


def cat_color_search(Comp_id,color_type,components_df,color_keys,color_df):
    if color_type == 'Color':
        color="#464c54"
    else:
        color="#ffffff"
    cat_num=0
    while "catagory"+str(cat_num) in components_df:
        categorycolumn="catagory"+str(cat_num)
        cat=components_df.loc[Comp_id][categorycolumn]
        if cat in color_keys:
            if color_df.loc[cat][color_type] is not None:
                color=color_df.loc[cat][color_type]
        cat_num= cat_num +1
    return color

