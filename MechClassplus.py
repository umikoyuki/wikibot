#at the moment these have been hand written, from the json files. plan to create a script to automate this process

class Mech_I(object):
    def __init__(self):
        self.PositiveQuirkCenterTorso=""
        self.HandHeldLeftArm="000Default_HandHeld_Slot"
        self.HandHeldRightArm="000Default_HandHeld_Slot"
        self.AddonLeftTorso="000Default_AddOn_Slot"
        self.AddonRightTorso="000Default_AddOn_Slot"
        self.LifeSupportAHead="000Default_Cockpit_LifeSupportA_Standard"
        self.CockpitFCSHead="001Default_FCS_Standard"
        self.CockpitHead="002Default_Cockpit_Standard"
        self.CockpitSensorsHead="003Default_Sensors_Standard"
        self.LifeSupportBHead="004Default_Cockpit_LifeSupportB_Standard"
        self.ArmorCenterTorso="001Default_Armor_Standard"
        self.StructureCenterTorso="002Default_Structure_Standard"
        self.CoolingCenterTorso="000Default_HeatSinkKit_Single"
        self.GyroCenterTorso="001Default_Gyro_Standard"
        self.EngineShieldCenterTorso="002Gear_Engine_Standard"
        self.EngineHeatBlockCenterTorso="003Default_EnginePart_Heatsinks"
        self.EngineCoreCenterTorso="004Gear_EngineCore_Dummy"
        self.LegHipLeftLeg="000Default_Actuator_Leg_Hip"
        self.LegUpperActuatorLeftLeg="001Default_Actuator_Leg_Upper"
        self.LegLowerActuatorLeftLeg="002Default_Actuator_Leg_Lower"
        self.LegFootActuatorLeftLeg="003Default_Actuator_Leg_Foot"
        self.LegHipRightLeg="000Default_Actuator_Leg_Hip"
        self.LegUpperActuatorRightLeg="001Default_Actuator_Leg_Upper"
        self.LegLowerActuatorRightLeg="002Default_Actuator_Leg_Lower"
        self.LegFootActuatorRightLeg="003Default_Actuator_Leg_Foot"
        self.ArmShoulderLeftArm="000Default_Actuator_Arm_Shoulder"
        self.ArmUpperActuatorLeftArm= "001Default_Actuator_Arm_Upper"
        self.ArmLowerActuatorLeftArm="002Default_Actuator_Arm_Lower"
        self.ArmHandActuatorLeftArm="003Default_Actuator_Arm_Hand"
        self.ArmShoulderRightArm="000Default_Actuator_Arm_Shoulder"
        self.ArmUpperActuatorRightArm= "001Default_Actuator_Arm_Upper"
        self.ArmLowerActuatorRightArm="002Default_Actuator_Arm_Lower"
        self.ArmHandActuatorRightArm="003Default_Actuator_Arm_Hand"
        self.SquadCockpitCenterTorso=""
        self.SquadSystemsCenterTorso=""
        self.SquadEngineCoreCenterTorso=""
        self.BAMotiveSystemCenterTorso=""
        self.ProtoMechActuatorsCenterTorso=""
        self.Head = []
        self.CenterTorso = []
        self.LeftTorso = []
        self.RightTorso = []
        self.LeftArm = []
        self.RightArm = []
        self.LeftLeg = []
        self.RightLeg = []
    def __str__(self):
        return f"{self.PositiveQuirk},{self.LifeSupportA}{self.CockpitFCS}{self.Cockpit}{self.CockpitSensors}{self.LifeSupportB}{self.Armor}{self.Structure}{self.Cooling}{self.Gyro}{self.EngineShield}{self.EngineHeatBlock}{self.EngineCore}{self.LegHip}{self.LegUpperActuator}{self.LegLowerActuator}{self.LegFootActuator}{self.ArmShoulder}{self.ArmUpperActuator}{self.ArmLowerActuator}{self.ArmHandActuator}{self.Chas}{self.Head}{self.CenterTorso}{self.LeftTorso}{self.RightTorso}{self.LeftArm}{self.RightArm}{self.LeftLeg}{self.RightLeg}{self.Chas}{self.Head}{self.CenterTorso}{self.LeftTorso}{self.RightTorso}{self.LeftArm}{self.RightArm}{self.LeftLeg}{self.RightLeg}"

class Mech_l(object):
    def __init__(self):
        self.Headslots =""
        self.Headmax_armor =""
        self.Headarmor = ""
        self.Headmax_rear_armor=""
        self.Headrear_armor =""
        self.Headstructure =""
        self.Headhp =[]
        self.CenterTorsoslots =""
        self.CenterTorsomax_armor =""
        self.CenterTorsoarmor = ""
        self.CenterTorsomax_rear_armor=""
        self.CenterTorsorear_armor =""
        self.CenterTorsostructure =""
        self.CenterTorsohp =[]
        self.LeftTorsoslots =""
        self.LeftTorsomax_armor =""
        self.LeftTorsoarmor = ""
        self.LeftTorsomax_rear_armor=""
        self.LeftTorsorear_armor =""
        self.LeftTorsostructure =""
        self.LeftTorsohp =[]
        self.RightTorsoslots =""
        self.RightTorsomax_armor =""
        self.RightTorsoarmor = ""
        self.RightTorsomax_rear_armor=""
        self.RightTorsorear_armor =""
        self.RightTorsostructure =""
        self.RightTorsohp =[]
        self.LeftArmslots =""
        self.LeftArmmax_armor =""
        self.LeftArmarmor = ""
        self.LeftArmmax_rear_armor=""
        self.LeftArmrear_armor =""
        self.LeftArmstructure =""
        self.LeftArmhp =[]
        self.RightArmslots =""
        self.RightArmmax_armor =""
        self.RightArmarmor = ""
        self.RightArmmax_rear_armor=""
        self.RightArmrear_armor =""
        self.RightArmstructure =""
        self.RightArmhp =[]
        self.LeftLegslots =""
        self.LeftLegmax_armor =""
        self.LeftLegarmor = ""
        self.LeftLegmax_rear_armor=""
        self.LeftLegrear_armor =""
        self.LeftLegstructure =""
        self.LeftLeghp =[]
        self.RightLegslots =""
        self.RightLegmax_armor =""
        self.RightLegarmor = ""
        self.RightLegmax_rear_armor=""
        self.RightLegrear_armor =""
        self.RightLegstructure =""
        self.RightLeghp =[]

def get_hp_list(mech_object,Location):
    if Location == "Head":
        hp_list=[]
        hp_list.extend(mech_object.Headhp)

    elif Location == "CenterTorso":
        hp_list=[]
        hp_list.extend(mech_object.CenterTorsohp)

    elif Location == "LeftTorso":
        hp_list=[]
        hp_list.extend(mech_object.LeftTorsohp)
    elif Location == "RightTorso":
        hp_list=[]
        hp_list.extend(mech_object.RightTorsohp)

    elif Location == "LeftArm":
        hp_list=[]
        hp_list.extend(mech_object.LeftArmhp)

    elif Location == "RightArm":
        hp_list=[]
        hp_list.extend(mech_object.RightArmhp)

    elif Location == "LeftLeg":
        hp_list=[]
        hp_list.extend(mech_object.LeftLeghp)

    elif Location == "RightLeg":
        hp_list=[]
        hp_list.extend(mech_object.RightLeghp)

    return hp_list
        
def Organise_inventory(mech_object,Location):
    if Location == 'Chassis':
        Inventory = [
            getattr(mech_object,'PositiveQuirkCenterTorso'),
            getattr(mech_object,'ArmorCenterTorso'),
            getattr(mech_object,'StructureCenterTorso')]
        
    if Location == 'RightWidget':
        Inventory = [
            getattr(mech_object,'SquadCockpitCenterTorso'),
            getattr(mech_object,'SquadSystemsCenterTorso'),
            getattr(mech_object,'SquadEngineCoreCenterTorso'),
            getattr(mech_object,'BAMotiveSystemCenterTorso'),
            getattr(mech_object,'ProtoMechActuatorsCenterTorso')]
        
    elif Location == "Head":
        Inventory = [
            getattr(mech_object,'LifeSupportAHead'),
            getattr(mech_object,'CockpitFCSHead'),
            getattr(mech_object,'CockpitHead'),
            getattr(mech_object,'CockpitSensorsHead'),
            getattr(mech_object,'LifeSupportBHead')]
        Inventory.extend(mech_object.Head)

    elif Location == "CenterTorso":
        Inventory = [
            getattr(mech_object,'CoolingCenterTorso'),
            getattr(mech_object,'GyroCenterTorso'),
            getattr(mech_object,'EngineShieldCenterTorso'),
            getattr(mech_object,'EngineHeatBlockCenterTorso'),
            getattr(mech_object,'EngineCoreCenterTorso')]
        Inventory.extend(mech_object.CenterTorso)

    elif Location == "LeftTorso":
        Inventory = [  
        getattr(mech_object,"AddonLeftTorso")]
        Inventory.extend(mech_object.LeftTorso)

    elif Location == "RightTorso":
        Inventory = [  
        getattr(mech_object,"AddonRightTorso")]
        Inventory.extend(mech_object.RightTorso)

    elif Location == "LeftArm":
        Inventory = [
        getattr(mech_object,'ArmShoulderLeftArm'),
        getattr(mech_object,'ArmUpperActuatorLeftArm'),
        getattr(mech_object,'ArmLowerActuatorLeftArm'),
        getattr(mech_object,'ArmHandActuatorLeftArm'),]
        Inventory.extend(mech_object.LeftArm)

    elif Location == "RightArm":
        Inventory = [
        getattr(mech_object,'ArmShoulderRightArm'),
        getattr(mech_object,'ArmUpperActuatorRightArm'),
        getattr(mech_object,'ArmLowerActuatorRightArm'),
        getattr(mech_object,'ArmHandActuatorRightArm'),]    
        Inventory.extend(mech_object.RightArm)

    elif Location == "LeftLeg":
        Inventory = [
        getattr(mech_object,'LegHipLeftLeg'),
        getattr(mech_object,'LegUpperActuatorLeftLeg'),
        getattr(mech_object,'LegLowerActuatorLeftLeg'),
        getattr(mech_object,'LegFootActuatorLeftLeg')]     
        Inventory.extend(mech_object.LeftLeg)

    elif Location == "RightLeg":
        Inventory = [
        getattr(mech_object,'LegHipRightLeg'),
        getattr(mech_object,'LegUpperActuatorRightLeg'),
        getattr(mech_object,'LegLowerActuatorRightLeg'),
        getattr(mech_object,'LegFootActuatorRightLeg'),]  
        Inventory.extend(mech_object.RightLeg)

    sorted_inventory_nums=sorted(Inventory)
    sorted_inventory=[]
    for sitem in sorted_inventory_nums:
        item=sitem[3:]
        sorted_inventory.append(item)

    return sorted_inventory

def adjust_defaults(mech_object,mech_tags):
    if "RISCBattleMech" in mech_tags:
        mech_object.CockpitFCSHead="001Gear_FCS_RISC"
        mech_object.CockpitHead="002Gear_Cockpit_RISC"
        mech_object.CockpitSensorsHead="003Gear_Sensors_RISC"
        mech_object.CoolingCenterTorso="000Gear_HeatSinkKit_Radical_RISC"
        mech_object.EngineHeatBlockCenterTorso="003Gear_EngineCooling_EmergencyCoolant_RISC"
        mech_object.EngineCoreCenterTorso="004Gear_EngineCore_Dummy"

    if "ClanMech" in mech_tags:
        mech_object.CockpitFCSHead="001Default_FCS_Clan"
        mech_object.CockpitHead="002Default_Cockpit_Clan"
        mech_object.CockpitSensorsHead="003Default_Sensors_Clan"
        mech_object.ArmorCenterTorso="001Default_Armor_Standard_Clan"

    if "SocietyMech" in mech_tags:
        mech_object.CockpitFCSHead="001Default_FCS_Society"
        mech_object.CockpitHead="002Default_Cockpit_Clan"
        mech_object.CockpitSensorsHead="003Default_Sensors_Society"
        mech_object.ArmorCenterTorso="001Default_Armor_Standard_Clan"

    if "TribeMech" in mech_tags:
        mech_object.CockpitSensorsHead="003Default_Sensors_Tribe"

    if "SLDFMech" in mech_tags:
        mech_object.CockpitFCSHead="001Default_FCS_SLDF"
        mech_object.CockpitHead="002Default_Cockpit_SLDF"
        mech_object.CockpitSensorsHead="003Default_Sensors_SLDF"
        mech_object.CoolingCenterTorso="000Unique_Gear_HeatSinkKit_Double_Royal"

    if "IndustrialMech" in mech_tags:
        mech_object.CockpitFCSHead="001Default_FCS_Primitive"
        mech_object.CockpitHead="002Default_Cockpit_Primitive"
        mech_object.CockpitSensorsHead="003Default_Sensors_Primitive"
        mech_object.ArmorCenterTorso="001Default_Armor_Industrial"
        mech_object.StructureCenterTorso="002Default_Structure_Industrial"
        mech_object.EngineShieldCenterTorso="002Gear_Engine_ICE"

    if "PrimitiveMech" in mech_tags:
        mech_object.CockpitFCSHead="001Default_FCS_Primitive"
        mech_object.CockpitHead="002Default_Cockpit_Primitive"
        mech_object.CockpitSensorsHead="003Default_Sensors_Primitive"
        mech_object.ArmorCenterTorso="001Default_Armor_Industrial"
        mech_object.EngineShieldCenterTorso="002Gear_Engine_Primitive"

    if "LandAirMech" in mech_tags:
        mech_object.ArmorCenterTorso="001Default_Armor_LAM_Aluminium"
        mech_object.StructureCenterTorso="002Default_Structure_LAM_Standard"
        mech_object.EngineShieldCenterTorso="002Gear_Engine_Standard_LAM"

    if "SuperheavyMech" in mech_tags:
        mech_object.StructureCenterTorso="002Default_Structure_Standard_Superheavy"
        mech_object.GyroCenterTorso="001Gear_Gyro_Superheavy"

    if "QuadMech" in mech_tags:
        mech_object.ArmShoulderLeftArm="000Default_Actuator_Leg_Hip"
        mech_object.ArmUpperActuatorLeftArm= "001Default_Actuator_Leg_Upper"
        mech_object.ArmLowerActuatorLeftArm="002Default_Actuator_Leg_Lower"
        mech_object.ArmHandActuatorLeftArm="003Default_Actuator_Leg_Foot"
        mech_object.ArmShoulderRightArm="000Default_Actuator_Leg_Hip"
        mech_object.ArmUpperActuatorRightArm= "001Default_Actuator_Leg_Upper"
        mech_object.ArmLowerActuatorRightArm="002Default_Actuator_Leg_Lower"
        mech_object.ArmHandActuatorRightArm="003Default_Actuator_Leg_Foot"

    if "ArmLimitUpperLeft" in mech_tags:
        mech_object.ArmLowerActuatorLeftArm="000EMPTY"
        mech_object.ArmHandActuatorLeftArm="000EMPTY"

    if "ArmLimitUpperRight" in mech_tags:
        mech_object.ArmLowerActuatorRightArm="000EMPTY"
        mech_object.ArmHandActuatorRightArm="000EMPTY"

    if "ArmLimitLowerLeft" in mech_tags:
        mech_object.ArmHandActuatorLeftArm="000EMPTY"

    if "ArmLimitLowerRight" in mech_tags:
        mech_object.ArmHandActuatorRightArm="000EMPTY"

    if "OmniMech" in mech_tags:
        mech_object.ArmLowerActuatorLeftArm="000EMPTY"
        mech_object.ArmHandActuatorLeftArm="000EMPTY"
        mech_object.ArmLowerActuatorRightArm="000EMPTY"
        mech_object.ArmHandActuatorRightArm="000EMPTY"
    
    if "Squad" in mech_tags:
        mech_object.ArmUpperActuatorLeftArm="000EMPTY"
        mech_object.ArmUpperActuatorRightArm="000EMPTY"
        mech_object.ArmShoulderLeftArm="000EMPTY"
        mech_object.ArmLowerActuatorLeftArm="000EMPTY"
        mech_object.ArmHandActuatorLeftArm="000EMPTY"
        mech_object.ArmShoulderRightArm="000EMPTY"
        mech_object.ArmLowerActuatorRightArm="000EMPTY"
        mech_object.ArmHandActuatorRightArm="000EMPTY"
        mech_object.HandHeldLeftArm="000EMPTY"
        mech_object.HandHeldRightArm="000EMPTY"
        mech_object.AddonLeftTorso="000EMPTY"
        mech_object.AddonRightTorso="000EMPTY"
        mech_object.LifeSupportAHead="000EMPTY"
        mech_object.CockpitFCSHead="000EMPTY"
        mech_object.CockpitHead="000EMPTY"
        mech_object.CockpitSensorsHead="000EMPTY"
        mech_object.LifeSupportBHead="000EMPTY"
        mech_object.ArmorCenterTorso="000EMPTY"
        mech_object.StructureCenterTorso="000EMPTY"
        mech_object.CoolingCenterTorso="000EMPTY"
        mech_object.GyroCenterTorso="000EMPTY"
        mech_object.EngineShieldCenterTorso="000EMPTY"
        mech_object.EngineHeatBlockCenterTorso="000EMPTY"
        mech_object.EngineCoreCenterTorso="000EMPTY"
        mech_object.LegHipLeftLeg="000EMPTY"
        mech_object.LegUpperActuatorLeftLeg="000EMPTY"
        mech_object.LegLowerActuatorLeftLeg="000EMPTY"
        mech_object.LegFootActuatorLeftLeg="000EMPTY"
        mech_object.LegHipRightLeg="000EMPTY"
        mech_object.LegUpperActuatorRightLeg="000EMPTY"
        mech_object.LegLowerActuatorRightLeg="000EMPTY"
        mech_object.LegFootActuatorRightLeg="000EMPTY"
    return mech_object

defaults=[
    'LifeSupportA', 
    'CockpitFCS', 
    'Cockpit', 
    'CockpitSensors', 
    'LifeSupportB', 
    'Armor', 
    'Structure', 
    'Cooling', 
    'Gyro', 
    'EngineShield',
    'EngineHeatBlock',
    'EngineCore', 
    'PositiveQuirk',
    'HandHeld',
    'AddOn',
    'LegHip', 
    'LegUpperActuator', 
    'LegLowerActuator', 
    'LegFootActuator', 
    'ArmShoulder', 
    'ArmUpperActuator', 
    'ArmLowerActuator', 
    'ArmHandActuator',
    ]

squadrightwidget=[
    "SquadCockpit",
    "SquadSystems",
    "SquadEngineCore",
    "BAMotiveSystem",
]

Locations = [
    "Head",
    "CenterTorso",
    "LeftTorso",
    "RightTorso",
    "LeftArm",
    "RightArm",
    "LeftLeg",
    "RightLeg"    
    ]

Locations_UI_Name={
    "Head":"Head",
    "CenterTorso":"Center Torso",
    "LeftTorso":"Left Torso",
    "RightTorso":"Right Torso",
    "LeftArm":"Left Arm",
    "RightArm":"Right Arm",
    "LeftLeg":"Left Leg",
    "RightLeg":"Right Leg"
}

Divtype={
    "Head":"head_div",
    "CenterTorso":"torso_div",
    "LeftTorso":"torso_div",
    "RightTorso":"torso_div",
    "LeftArm":"arm_leg_div",
    "RightArm":"arm_leg_div",
    "LeftLeg":"arm_leg_div",
    "RightLeg":"arm_leg_div"
}


Squadlocations_UI_Name={
    "Head":"Trooper 1",
    "CenterTorso":"Trooper 2",
    "LeftTorso":"Trooper 3",
    "RightTorso":"Trooper 4",
    "LeftArm":"Trooper 5",
    "RightArm":"Trooper 6",
    "LeftLeg":"",
    "RightLeg":""
}

mech_tags = [
    "RISCBattleMech",
    "SocietyMech",
    "ClanMech",
    "SLDFMech",
    "TribeMech",
    "IndustrialMech",
    "PrimitiveMech",
    "LandAirMech",
    "SuperheavyMech",
    "Quad",
    "Squad",
    "Omni",
    "OmniMechQS",
    "ArmLimitUpperLeft",
    "ArmLimitUpperRight",
    "ArmLimitLowerRight",
    "ArmLimitLowerLeft"
]

Hardpoints_img_dict={
    'Ballistic':"Hardpoint_Ballistic.svg", 
    'Energy':"Hardpoint_Energy.svg", 
    'Special':"", 
    'AntiPersonnel':"Hardpoint_Support.svg",
    'BattleArmor':"Hardpoint_Support.svg",
    'Missile':"Hardpoint_Missile.svg", 
    'SpecialHandHeld':"",
    'InternalBombBay':"Hardpoint_Bomb.svg",
    'WingMountedWeapon':"Hardpoint_Wing.svg",
    'Omni':"Hardpoint_Omni.svg"   
}
Hardpointsnames =[
    'Ballistic', 
    'Energy', 
    'AntiPersonnel',
    'Missile', 
    'InternalBombBay',
    'WingMountedWeapon',
    'Omni'   
]
