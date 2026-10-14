import json
import pandas as pd
import glob
from jsoncomment import JsonComment

from Paths import *
from ExtraFunctions import *

## parse mech_defs jsons
mech_def_path = rt_path + "**/mechdef_*.json"
mech_def_glob = glob.glob(mech_def_path, recursive=True)
mech_def_glob = list(set(mech_def_glob)-set(exclusionglob))
mech_def_df = jsonglob_to_df (mech_def_glob)

## parse chassis_defs jsons
chassis_def_path = rt_path +"**/chassisdef_*.json"
chassis_def_glob = glob.glob(chassis_def_path, recursive=True)
chassis_def_df=jsonglob_to_df (chassis_def_glob)

## merge chassis_defs to mech df 
mech_df=pd.merge(mech_def_df,chassis_def_df,left_on='ChassisID',right_on='Description.Id',suffixes=('_mech', '_chassis'))
mech_df= mech_df.set_index("def_mech")
mech_df.to_parquet(mech_def_table, engine='pyarrow', compression='snappy')

## parse component_defs jsons
components_df = pd.DataFrame()
for prefix in prefixes:
    paths = rt_path +"**/" + prefix + "*.json"
    components_glob = glob.glob(paths, recursive=True)
    components_glob = list(set(components_glob)-set(exclusionglob))
    for jsons in components_glob:
        current_componet_dict=parse_components(jsons)
        new_row = pd.Series(current_componet_dict)
        components_df = append_row(components_df, new_row)
    print("done" + prefix)
components_df = components_df .set_index("ID")  
components_df.to_parquet(components_table, engine='pyarrow', compression='snappy')

##parse factions jsons
factionjson= rt_path +"Core/RogueTechCore/Faction.json"
factionjsons= rt_path + "Core/RogueTechCore/Factions/"
faction_df = pd.DataFrame()   
with open(factionjson,encoding="utf8") as file:
        parser = JsonComment(json)
        data1 = parser.load(file)
factionslist=data1["enumerationValueList"]
flistsize=len(factionslist)
f=0
while f < flistsize:
    faction_dict={}
    FactionDefID=factionslist[f]["FactionDefID"]
    try:
        factionjsonpath=factionjsons + FactionDefID + '.json'
        with open(factionjsonpath,encoding="utf8") as file:
            parser = JsonComment(json)
            data2 = parser.load(file)
        faction_id_c=data2["factionID"]
        faction_id=faction_id_c.lower()
        faction_name=data2["Name"]
        if "3150" in faction_id:
            faction_name=faction_name+" (3150)"
        if faction_id != "invalid_unset":
            faction_dict["id"] =faction_id
            faction_dict["name"] =faction_name 
            faction_dict["description"]=data2["Description"]
            if 'factionMapColor'in data2:
                faction_dict["factionMapColor"]=data2['factionMapColor']
            faction_dict["icon"]=data2["icon"]
            faction_dict["IsGreatHouse"]=factionslist[f]["IsGreatHouse"]
            faction_dict["IsClan"]=factionslist[f]["IsClan"]
            faction_dict["IsPirate"]=factionslist[f]["IsPirate"]
            faction_dict["DoesGainReputation"]=factionslist[f]["DoesGainReputation"]
            faction_dict["CanAlly"]=factionslist[f]["CanAlly"]
            print(faction_id) 
            new_row = pd.Series(faction_dict)
            faction_df  = append_row(faction_df , new_row)  
    except Exception as e:
        print(e)
    f=f+1
faction_df = faction_df .set_index("id")  
# Write the Faction DataFrame to a Parquet file
faction_df .to_parquet(factions_table, engine='pyarrow', compression='snappy')
print("done fation table")

# ##parse mod info jsons
mod_path= rt_path + "**/mod.json"
mod_glob=glob.glob(mod_path,recursive=True)
modinfo=(
    "Name",
    "Version",
    "Description",
    "Author"
)
mod_df=pd.DataFrame()
for path in mod_glob:
    pathstr=path.replace("\\","/")
    modfilepath=pathstr.removeprefix(rt_path)
    modpath=modfilepath.removesuffix("/mod.json")
    print(modpath)
    with open(path,encoding="utf-8-sig") as file:
        parser = JsonComment(json)
        data = parser.load(file)
    moddict={
        "modpath":modpath
    }
    for i in modinfo:
        if i in data:
            moddict[i]=data[i]
    new_row = pd.Series(moddict)
    mod_df = append_row( mod_df, new_row)
mod_df=  mod_df.set_index("modpath")  
mod_df.to_parquet(mod_info_table, engine='pyarrow', compression='snappy')
print("done mod info table") 

##parse color components info jsons
Custom_Components_json=rt_path +"Core/CustomComponents/mod.json"
cat_paths=rt_path +"/Core/RogueTechCore/categories/*.json"
cat_jsonData = glob.glob(cat_paths, recursive=True)
color_df = pd.DataFrame()
with open(Custom_Components_json,encoding="utf8") as file:
        parser = JsonComment(json)
        data = parser.load(file)
colortagslist = data["Settings"]["ColorTags"]
colortags={}
for item in colortagslist:
    tag=item["Tag"]
    color=item["Color"]
    colortags[tag] = color
def build_setting_dict(settingnum,data):
    category={}
    category["Name"]=data["Settings"][settingnum]["Name"]
    if "DefaultCustoms" in data["Settings"][settingnum]:
        if "ColorTag" in data["Settings"][settingnum]["DefaultCustoms"]:
            categorycolor=data["Settings"][settingnum]["DefaultCustoms"]["ColorTag"]
            category["Colortag"]=categorycolor
            if categorycolor in colortags:
                category["Color"]=colortags[categorycolor]
        if "RGBColor" in data["Settings"][settingnum]["DefaultCustoms"]:
            rgbbcolor=data["Settings"][settingnum]["DefaultCustoms"]["RGBColor"]
            category["Color"]=rgbbcolor
        if "TRGBColor" in data["Settings"][settingnum]["DefaultCustoms"]:
            trgbcolor=data["Settings"][settingnum]["DefaultCustoms"]["TRGBColor"]["Color"]
            category["tcolor"]=trgbcolor
        if "Sorter" in data["Settings"][settingnum]["DefaultCustoms"]:
            category["Sorter"]=data["Settings"][settingnum]["DefaultCustoms"]["Sorter"]
        if "InventorySorter" in data["Settings"][settingnum]["DefaultCustoms"]:
            category["Inventory_Sorter"]=data["Settings"][settingnum]["DefaultCustoms"]["InventorySorter"]
    return category     
def getsettings(path):
    color_df = pd.DataFrame()
    with open(path,encoding="utf8") as file:
        parser = JsonComment(json)
        data = parser.load(file)
    settings = data["Settings"]
    setting_length = len(settings)
    settingnum  = 0
    while settingnum < setting_length:
        current_setting_dict=build_setting_dict(settingnum,data)
        new_row = pd.Series(current_setting_dict)
        color_df = append_row(color_df, new_row)
        settingnum = settingnum+1
    return color_df
for path in cat_jsonData:
    path_color_df=getsettings(path)
    color_df = pd.concat([color_df, path_color_df], ignore_index=True)
newcolor_df= color_df.set_index("Name")  
newcolor_df.to_parquet(Color_table, engine='pyarrow', compression='snappy')
print("Done Color and Sort Table")








