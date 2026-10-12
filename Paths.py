#testing json to pandas
import pandas as pd
import glob

###RoguetechPath###
rtpathinput="S:/RogueTech-Mini/"
rt_path =rtpathinput.replace("\\","/")

exclusion_path=rt_path+"**/ExperimentalGear/**/*.json"
exclusionglob=glob.glob(exclusion_path, recursive=True)


mech_variants_table="Umiscripts/Json_Tables/mech_variants_table.parquet"
mech_tags_table="Umiscripts/Json_Tables/mech_tags_table.parquet"
mech_def_table="Umiscripts/Json_Tables/mech_def_table.parquet"
mechstuff_table="Umiscripts/Json_Tables/mechstuff_table.parquet"
components_table="Umiscripts/Json_Tables/componets_table.parquet"
factions_table="Umiscripts/Json_Tables/factions_table.parquet"


###Component paths
prefixes = [
"Ammo_",
"BoltOn_",
"Gear_",
"Linked_",
"Special_",
"Weapon_",
"Quirk_",
"Default_",
"HandHeld_",
"Lootable_",
"Unique_"
]
