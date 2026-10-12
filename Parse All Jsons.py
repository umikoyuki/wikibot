import json
import pandas as pd
import glob
from jsoncomment import JsonComment

from Paths import *
from ExtraFunctions import *

# ## parse mech_defs jsons
# mech_def_path = rt_path + "**/mechdef_*.json"
# mech_def_glob = glob.glob(mech_def_path, recursive=True)
# mech_def_glob = list(set(mech_def_glob)-set(exclusionglob))
# mech_def_df = jsonglob_to_df (mech_def_glob)

# ## parse chassis_defs jsons
# chassis_def_path = rt_path +"**/chassisdef_*.json"
# chassis_def_glob = glob.glob(chassis_def_path, recursive=True)
# chassis_def_df=jsonglob_to_df (chassis_def_glob)

# ## merge chassis_defs to mech df 
# mech_df=pd.merge(mech_def_df,chassis_def_df,left_on='ChassisID',right_on='Description.Id',suffixes=('_mech', '_chassis'))
# mech_df= mech_df.set_index("def_mech")
# mech_df.to_parquet(mech_def_table, engine='pyarrow', compression='snappy')

# ## parse component_defs jsons
# components_df = pd.DataFrame()
# for prefix in prefixes:
#     paths = rt_path +"**/" + prefix + "*.json"
#     components_glob = glob.glob(paths, recursive=True)
#     components_glob = list(set(components_glob)-set(exclusionglob))
#     for jsons in components_glob:
#         current_componet_dict=parse_components(jsons)
#         new_row = pd.Series(current_componet_dict)
#         components_df = append_row(components_df, new_row)
#     print("done" + prefix)

# components_df.to_parquet(components_table, engine='pyarrow', compression='snappy')


factionjson= rt_path +"Core/RogueTechCore/Faction.json"
factionjsons= rt_path + "Core/RogueTechCore/Factions/"
##Create Factions Dictionary

df = pd.DataFrame()   

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
            df = append_row(df, new_row)  
    except Exception as e:
        print(e)
    f=f+1

finaldf= df.set_index("id")  
# Write the Faction DataFrame to a Parquet file
finaldf.to_parquet(factions_table, engine='pyarrow', compression='snappy')
print("done")









