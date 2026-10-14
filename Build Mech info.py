import pandas as pd

from Paths import *
from ExtraFunctions import *
from MechClassplus import *


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


##INVENTORY###


def getinventory_items(Mech_def,suffix,mech_item,appendlist,Mechtype):
    num = 0
    while suffix+ str(num) +".MountedLocation" in mech_def_df :
        component_id = mech_def_df.loc[Mech_def][suffix + str(num) +".ComponentDefID"]
        if isinstance(component_id, str):
            sorters=cat_sorter_search(component_id,components_df,color_keys,color_df)
            comp_num=(sorters).zfill(3)
            component_with_num=str(comp_num) + component_id
            appendlist.append(component_id)
            Cats = getcomp_categories(component_id,components_df)
            if set(Cats).intersection(set(squadrightwidget)):
                for i in squadrightwidget:
                    if i in Cats:
                        location = suffix + str(num) +"_MountedLocation"
                        comploc=i+location
                        setattr(mech_item, comploc, component_with_num)   
            else:
                if set(Cats).intersection(set(defaults)):
                    for i in defaults:
                        if i in Cats:
                            location = mech_def_df.loc[Mech_def][suffix + str(num) +".MountedLocation"]
                            comploc=i+location
                            setattr(mech_item, comploc, component_with_num)
                            dummylist= [item for item in defaults if item != i]
                            for di in dummylist:
                                if di in Cats:
                                    dcomploc=di+location
                                    setattr(mech_item, dcomploc, "000EMPTY")
                else:
                    location = mech_def_df.loc[Mech_def][suffix + str(num) +".MountedLocation"]
                    for loc in Locations:
                        if loc == location:
                            getattr(mech_item, loc).append(component_with_num)
        num = num+1
    return mech_item

def make_location_divs(locationlist,fixed,mech_def):
    locationdivs=[]
    locationlist=[x for x in locationlist if x != ""]
    for Comp_id in locationlist:
        if Comp_id != "EMPTY" or "":
            components_df.loc['Default_Armor_Standard']["UIName"]
            UI_name=components_df.loc[Comp_id]["UIName"]
            slots=components_df.loc[Comp_id]["InventorySize"]
            div_size=slots*24
            icon=components_df.loc[Comp_id]["Icon"]
            bg_color=cat_color_search(Comp_id,"Color",components_df,color_keys,color_df)
            text_color=cat_color_search(Comp_id,"tcolor",components_df,color_keys,color_df)
            text_size="12px"
            ui_length=len(UI_name)
            if ui_length > 20:
                text_size="10px"
            if Comp_id in fixed:
                div_class="component fixedcomp"
            else:
                div_class="component"
            # component_string=f'<div class="{div_class}" style="height:{str(div_size)}px;width:200px;color:{text_color};background-color:{bg_color};">[[File:{icon}.svg|25px|link=]][[{Comp_id}|{UI_name}]]</div>'
            ## link comp string ^^^^ no link comp string vvvv 
            component_string=f'<div class="{div_class}" style="font-size:{text_size};height:{str(div_size)}px;color:{text_color};background-color:{bg_color};"> [[File:{icon}.svg|21px|link=]] {UI_name}</div>\n'  
            locationdivs.append(component_string)         
    Locationdivstring=listtosting (locationdivs)
    Locationdiv=Locationdivstring+"</div>"
    return Locationdiv

def getinventory(Mech_def,mechtype,mechtags):     
    pre_mech = Mech_I()
    this_mech=adjust_defaults(pre_mech,mechtags)
    fixed_comps=[]
    not_fixed_comps=[]    
    m_this_mech=getinventory_items(Mech_def,"inventory.",this_mech,not_fixed_comps,mechtype)
    c_this_mech=getinventory_items(Mech_def,"FixedEquipment.",m_this_mech,fixed_comps,mechtype)
    #compile chassis list
    Chassis_Complist= Organise_inventory(c_this_mech,"Chassis")
    RightWidget_Complist= Organise_inventory(c_this_mech,"RightWidget")
    #init inventory dictionary with mechdef and add chassisdivs
    Inventory_dict={
        "Chassis": make_location_divs(Chassis_Complist,fixed_comps,Mech_def),
        "RightWidget":make_location_divs(RightWidget_Complist,fixed_comps,Mech_def)
        }    
    #compile and div all other locations
    for loc in Locations:
        Loc_Complist=Organise_inventory(c_this_mech,loc)
        Inventory_dict[loc]=make_location_divs(Loc_Complist,fixed_comps,Mech_def)
    #return the inventory_dict
    return Inventory_dict

def getinventorylist(Mech_def,mechtype,mechtags):     
    pre_mech = Mech_I()
    this_mech=adjust_defaults(pre_mech,mechtags)
    fixed_comps=[]
    not_fixed_comps=[]    
    m_this_mech=getinventory_items(Mech_def,"inventory.",this_mech,not_fixed_comps,mechtype)
    c_this_mech=getinventory_items(Mech_def,"FixedEquipment.",m_this_mech,fixed_comps,mechtype)
    #compile chassis list
    Chassis_Complist= Organise_inventory(c_this_mech,"Chassis")
    RightWidget_Complist= Organise_inventory(c_this_mech,"RightWidget")
    #init inventory dictionary with mechdef and add chassisdivs
    #init inventory dictionary with mechdef and add chassisdivs\
    Inventory_list= Chassis_Complist
    #compile and div all other locations
    for loc in Locations:
        Loc_Complist=Organise_inventory(c_this_mech,loc)
        Inventory_list=Inventory_list+Loc_Complist
    return Inventory_list

def getlocationinfo(mechdef,Mechtype): 
    this_mech=Mech_l()
    c_num = 0
    while c_num < 8 :
        location = mech_def_df.loc[mechdef]["Locations."+str(c_num)+".Location_chassis"]
        setattr(this_mech,location+"slots", mech_def_df.loc[mechdef]["Locations."+str(c_num)+".InventorySlots"])
        setattr(this_mech,location+"max_armor", mech_def_df.loc[mechdef]["Locations."+str(c_num)+".MaxArmor"])
        setattr(this_mech, location + "max_rear_armor", mech_def_df.loc[mechdef]["Locations."+str(c_num)+".MaxRearArmor"])
        setattr(this_mech,location+"structure", mech_def_df.loc[mechdef]["Locations."+str(c_num)+".InternalStructure"])
        hp_num=0
        hp_list=[]
        while "Locations."+str(c_num)+".Hardpoints."+str(hp_num) + ".Omni" in mech_def_df:
            if mech_def_df.loc[mechdef]["Locations."+str(c_num)+".Hardpoints."+str(hp_num) + ".Omni"] is True:
                hp="Omni"
            else:
                try: 
                    hp=mech_def_df.loc[mechdef]["Locations."+str(c_num)+".Hardpoints."+str(hp_num) + ".WeaponMountID"]
                except:
                    hp=mech_def_df.loc[mechdef]["Locations."+str(c_num)+".Hardpoints."+str(hp_num) + ".WeaponMount"]
            hp_list.append(hp)
            hp_num=hp_num+1
        setattr(this_mech,location+"hp",hp_list)
        c_num = c_num+1 
    m_num = 0
    while m_num < 8 :
        location = mech_def_df.loc[mechdef]["Locations."+str(m_num)+".Location_mech"]
        setattr(this_mech,location+"armor", mech_def_df.loc[mechdef]["Locations."+str(m_num)+".CurrentArmor"])
        setattr(this_mech,location+"rear_armor", int(mech_def_df.loc[mechdef]["Locations."+str(m_num)+".CurrentRearArmor"]))
        m_num=m_num+1
    location_info_dict={}
    for loc in Locations:
        if Mechtype == "Squad":
            loc_header=Squadlocations_UI_Name[loc]
        else:
            loc_header=Locations_UI_Name[loc]
        loc_structure=getattr(this_mech,loc+"structure")
        loc_armor=getattr(this_mech,loc+"armor")
        loc_max_armor=getattr(this_mech,loc+"max_armor")
        loc_rear_armor=getattr(this_mech,loc+"rear_armor")
        loc_max_rear_armor=getattr(this_mech,loc+"max_rear_armor")
        try:
            armor_percent=str(int((loc_armor/loc_max_armor)*100))
        except:
            armor_percent=0
        try:
            rear_armor_percent=str(int((int(loc_rear_armor)/int(loc_max_rear_armor))*100))
        except:
            rear_armor_percent=0
        loc_hardpoints_list= get_hp_list(this_mech,loc)
        loc_slots=getattr(this_mech,loc+"slots")
        location_inventory_size=str(loc_slots*28)
        hp_total_string=""
        for hardp in Hardpointsnames:
            hp_count=loc_hardpoints_list.count(hardp)
            hp_image=Hardpoints_img_dict[hardp]
            if hp_count != 0:
                hp_string=str(hp_count)+' [[File:'+hp_image+'|25px|link=]]'
                hp_total_string=hp_total_string+" "+hp_string
        location_header_string=f'<div class="location_header">{loc_header}<div class="structure">S {loc_structure}/{loc_structure}</div></div>'
        location_armor_string=f'<div class="location_main"><div class="location_info"><div class="armor_box">F {loc_armor}/{loc_max_armor}<div class="armor_bar_container"><div class="armor_bar" style="width:{armor_percent}%;"></div></div></div>'
        location_rear_armor_string=f'<div class="armor_box">R {loc_rear_armor}/{loc_max_rear_armor}<div class="armor_bar_container"><div class="armor_bar" style="width:{rear_armor_percent}%;"></div></div></div>'
        location_hp_string=f'<div class="hardpoints">{hp_total_string}</div></div>'  
        location_info_dict[loc]=location_header_string+location_armor_string+location_hp_string +'<div class="location_inventory" style="height:'+location_inventory_size+'px;">'
        if Mechtype == "Mech":
            if loc == "RightTorso" or loc == "LeftTorso" or loc == "CenterTorso" :
                location_info_dict[loc]=location_header_string+location_armor_string+location_rear_armor_string+location_hp_string +'<div class="location_inventory" style="height:'+location_inventory_size+'px;">'
        if loc_max_armor == 0:
            location_info_dict[loc]="EMPTY"
    return location_info_dict



def full_mech_atlas(Mech_def,mechtype,mechtags):
    inventory_dict=getinventory(Mech_def,mechtype,mechtags)
    location_dict=getlocationinfo(Mech_def,mechtype)
    Chassis_div=f'<div class="chassis_div"><div class="location_header">Chassis</div><div class="location_main">{inventory_dict["Chassis"]}</div></div></div></div>'
    if mechtype =="Squad":
        Squad_div=f'<div class="chassis_div"><div class="location_header">Internals</div><div class="location_main">{inventory_dict["RightWidget"]}</div></div></div></div>'
    else:
        Squad_div=f'<div class="chassis_div"></div>'    
    divtag_dict={}
    for loc in Locations:
        divtype=Divtype[loc]
        if location_dict[loc] == "EMPTY":
            divtag_dict[loc]=""
        else:
            divtag_dict[loc]=f'<div class="{divtype}">{location_dict[loc]}{inventory_dict[loc]}</div></div></div></div>'
    mech_atlas="{{{{{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}}}}}".format("Mechatlas", "Chassis_div="+Chassis_div, "RightArm="+divtag_dict["RightArm"],"RightTorso="+divtag_dict["RightTorso"],"RightLeg="+divtag_dict["RightLeg"],"Head="+divtag_dict["Head"],"CenterTorso="+divtag_dict["CenterTorso"],"LeftTorso="+divtag_dict["LeftTorso"],"LeftLeg="+divtag_dict["LeftLeg"],"Squad_div="+Squad_div,"LeftArm="+divtag_dict["LeftArm"])
    return mech_atlas


def get_mech_details(Mech_def):
    print("-----------------"+Mech_def)
    chassisdef=mech_def_df.loc[Mech_def]["ChassisID"]
    mech_path=mech_def_df.loc[Mech_def]["def_path_mech"]
    mechtags=[]
    for col in mech_tags_df:
        mechtags.append(mech_tags_df.loc[chassisdef][col])
    if "unit_squad" in mechtags:
        mechtype="Squad"
    else:
        mechtype="Mech"
    mech_dict = {
        'mech_def' : Mech_def,
        "mech_webid" : Mech_def[8:],        
        "Details" : mech_def_df.loc[Mech_def]["Description.Details_mech"],
        "Icon" : mech_def_df.loc[Mech_def]["Description.Icon_mech"],
        "mech_UIname" : mech_def_df.loc[Mech_def]["Description.UIName_mech"],
        "mech_cost" : int(mech_def_df.loc[Mech_def]["Description.Cost_mech"]),
        "mech_atlas":full_mech_atlas(Mech_def,mechtype,mechtags),
        "mechcomplist":getinventorylist(Mech_def,mechtype,mechtags),
        "weightClass": mech_def_df.loc[Mech_def]["weightClass"],
        "Tonnage":float(mech_def_df.loc[Mech_def]["Tonnage"],),
        "MaxJumpjets":int(mech_def_df.loc[Mech_def]["MaxJumpjets"],),
        "drop_modifer":int(mech_def_df.loc[Mech_def]["Custom.DropCostFactor.DropModifier"]),
        "MeleeDamage":int(mech_def_df.loc[Mech_def]["MeleeDamage"]),
        "TopSpeed":int(mech_def_df.loc[Mech_def]["TopSpeed"]),
        "chassis_cost":int(mech_def_df.loc[Mech_def]["Description.Cost_chassis"]),
        "BattleValue":int(mech_def_df.loc[Mech_def]["BattleValue"]),
        "mod":getmechmod(mech_path,mod_df),
        "factions":get_factionlist(mechtags, factions_df)
        }
    # mechtotalsdict=getmechtotals(Mech_def,mechtype)
    # mech_dict.update(mechtotalsdict)
    if mech_def_df.loc[Mech_def]["Custom.AssemblyVariant.Include"] == "True" or "true":
        variant=mech_def_df.loc[Mech_def]["Custom.AssemblyVariant.PrefabID"]
        mech_dict["Variants_list"]=mech_variants_df.loc[variant][0]
    else:
        mech_dict["Variants_list"]=""
    if mech_dict["Tonnage"] == int(mech_dict["Tonnage"]):
        mech_dict["Tonnage"]=int(mech_dict["Tonnage"])
    return mech_dict

print(get_mech_details("mechdef_hunchback_HBK-4G"))
