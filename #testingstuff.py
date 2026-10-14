#this file is just for testingstuff for fault finding
import pandas as pd
import json
from jsoncomment import JsonComment

from Paths import *
from ExtraFunctions import *

mech_def_df= pd.read_parquet(mech_def_table)
mech_def_list=mech_def_df.index.values.tolist()
mechcolums=mech_def_df.columns.tolist()
mech_tags_df= pd.read_parquet(mech_tags_table)
mod_df= pd.read_parquet(mod_info_table)
factions_df=pd.read_parquet(factions_table)
mech_variants_df=pd.read_parquet(mech_variants_table)
all_factions = factions_df.index.tolist()
components_df=pd.read_parquet(components_table)
color_df=pd.read_parquet(Color_table)
color_keys=table_index_list(Color_table)


# # mods_df.loc[modpath]["Name"]
# mechdef="mechdef_hunchback_HBK-4G"
# location = mech_def_df.loc[mechdef]["Locations.0.Location_chassis"]
# print(location)

# components_df.loc["Ammo_AmmunitionBox_AMS_960shots"]["UIName"]

print(components_df)