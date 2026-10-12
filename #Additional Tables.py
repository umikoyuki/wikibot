#Additional Tables

#testing json to pandas
import json
import pandas as pd
import glob
from Paths import *
from ExtraFunctions import *


##create mech tags dataframe ####

mech_df=pd.read_parquet(mech_def_table)
mech_tags_df=mech_df[mech_df.columns[mech_df.columns.str.contains("MechTags|ChassisTags")]]
mech_tags_df.to_parquet(mech_tags_table, engine='pyarrow', compression='snappy')

####create mech variants lists#####

#remove prefabs thats are listed "false" for inclusion
mech_df_filtered = mech_df[mech_df['Custom.AssemblyVariant.Include'] != False]
#get list of all prefabs
prefablist=unique_from_column_df(mech_df,'Custom.AssemblyVariant.PrefabID')
#get dictionary of all mechs for each prefabid
prefabs={}
for prefab in prefablist:
    df_filter = mech_df_filtered [mech_df_filtered['Custom.AssemblyVariant.PrefabID'] == prefab]
    prefabslist=unique_from_column_df(df_filter,"Description.Id_mech")
    prefabslist.sort()
    prefabstring=""
    for i in prefabslist:
        mech_web_id = i[8:]
        Uiname=mech_df.loc[i,"Description.UIName_mech"]
        mech_link=f"[[{mech_web_id}|{Uiname}]]<br>"
        prefabstring=prefabstring+mech_link
    prefabs[prefab]=prefabstring

prefabs_df = pd.DataFrame.from_dict(prefabs, orient='index')
prefabs_df.index.name = 'prefab'
prefabs_df.to_parquet(mech_variants_table, engine='pyarrow', compression='snappy')
print("Done Prefabsvariants Table")

