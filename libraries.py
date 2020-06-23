from powers4th import *

LIGHTARMOR=feat([ft("light armor",["light armor",lambda x:max(x.mod("dex"),x.mod("int"))])])

def atWillAsEncounter(pickList, title, often="encounter",keyword=""):
    if pickList!="WarlockSpecial": 
        newList=[x.copy() for x in pickList]
        if keyword != "":
            remIt=[]
            for x in newList:
                if keyword not in x.keys:
                    remIt.append(x)
            for x in remIt:
                newList.remove(x)
        for g in xrange(len(newList)):
            newList[g].often=often
        if len(newList)>1:
            return ft("powerpick",PowerPick(newList, 0, 31, title))
        else: return ft("power",newList)
    else:
        newList=[feat([powerList["warlockat-will1"][warlockPacts[x]].copy(),ft("feat",[feat([],x)])]) for x in sorted(warlockPacts.keys())]
        for g in xrange(len(newList)): newList[g].what()[0].resolve[0].often=often
        return specialMenu(["Dark Pact","Fae Pact","Infernal Pact","Star Pact", "Vestige Pact"],newList,"Training in one warlock skill, "," at-will power as an encounter power, can use warlock implements")

EquipmentLists={}

weapons=[Weapon("club",["simple","melee","one-handed"],2,(1,6),3,["mace"])
        ,Weapon("dagger",["simple","melee","one-handed","off-hand","light thrown"],3,(1,4),1,["light blade"],(5,10))
        ,Weapon("javelin",["simple","melee","one-handed","heavy thrown"],2,(1,6),2,["spear"],(10,20))
        ,Weapon("mace",["simple","melee","one-handed","versatile"],2,(1,8),6,["mace"])
        ,Weapon("sickle",["simple","melee","one-handed","off-hand"],2,(1,6),2,["light blade"])
        ,Weapon("spear",["simple","melee","one-handed","versatile"],2,(1,8),6,["spear"])
        ,Weapon("spiked gauntlet",["simple","melee","one-handed","off-hand"],2,(1,6),1,["unarmed"])

        ,Weapon("greatclub",["simple","melee","two-handed"],2,(2,4),10,["mace"])
        ,Weapon("morningstar",["simple","melee","two-handed"],2,(1,10),8,["mace"])
        ,Weapon("quarterstaff",["simple","melee","two-handed"],2,(1,8),4,["staff"])
        ,Weapon("scythe",["simple","melee","two-handed"],2,(2,4),10,["heavy blade"])

        ,Weapon("battleaxe",["military","melee","one-handed","versatile"],2,(1,10),6,["axe"])
        ,Weapon("flail",["military","melee","one-handed","versatile"],2,(1,10),5,["flail"])
        ,Weapon("handaxe",["military","melee","one-handed","off-hand","heavy thrown"],2,(1,6),3,["axe"],(5,10))
        ,Weapon("longsword",["military","melee","one-handed","versatile"],3,(1,8),4,["heavy blade"])
        ,Weapon("scimitar",["military","melee","one-handed","high crit"],2,(1,8),4,["heavy blade"])
        ,Weapon("short sword",["military","melee","one-handed","off-hand"],3,(1,6),2,["light blade"])
        ,Weapon("throwing hammer",["military","melee","one-handed","off-hand","heavy thrown"],2,(1,6),2,["hammer"],(5,10))
        ,Weapon("warhammer",["military","melee","one-handed","versatile"],2,(1,10),5,["hammer"])
        ,Weapon("war pick",["military","melee","one-handed","high crit","versatile"],2,(1,8),6,["pick"])
        ,Weapon("broadsword",["military","melee","one-handed","versatile"],2,(1,10),5,["heavy blade"])
        ,Weapon("kopesh",["military","melee","one-handed","versatile","brutal 1"],2,(1,10),6,["axe","heavy blade"])
        ,Weapon("light war pick",["military","melee","one-handed","high crit","off-hand"],2,(1,6),4,["pick"])
        ,Weapon("scourge",["military","melee","one-handed","off-hand"],2,(1,8),3,["flail"])
        ,Weapon("trident",["military","melee","one-handed","heavy thrown","versatile"],2,(1,8),4,["spear"],(3,6))

        ,Weapon("falchion",["military","melee","two-handed","high crit"],3,(2,4),7,["heavy blade"])
        ,Weapon("glaive",["military","melee","two-handed","reach"],2,(2,4),10,["heavy blade","polearm"])
        ,Weapon("greataxe",["military","melee","two-handed","high crit"],2,(1,12),12,["axe"])
        ,Weapon("greatsword",["military","melee","two-handed"],3,(1,10),8,["heavy blade"])
        ,Weapon("halberd",["military","melee","two-handed","reach"],2,(1,10),12,["axe","polearm"])
        ,Weapon("heavy flail",["military","melee","two-handed"],2,(2,6),10,["flail"])
        ,Weapon("longspear",["military","melee","two-handed","reach"],2,(1,10),9,["polearm","spear"])
        ,Weapon("maul",["military","melee","two-handed"],2,(2,6),12,["hammer"])
        ,Weapon("heavy war pick",["military","melee","two-handed","high crit"],2,(1,12),8,["pick"])

        ,Weapon("bastard sword",["superior","melee","one-handed","versatile"],3,(1,10),6,["heavy blade"])
        ,Weapon("katar",["superior","melee","one-handed","off-hand","high crit"],3,(1,6),1,["light blade"])
        ,Weapon("rapier",["superior","melee","one-handed"],3,(1,8),2,["light blade"])
        ,Weapon("craghammer",["superior","melee","one-handed", "brutal 2","versatile"],2,(1,10),6,["hammer"])
        ,Weapon("kukri",["superior","melee","one-handed", "brutal 1", "off-hand"],2,(1,6),2,["light blade"])
        ,Weapon("parrying dagger",["superior","melee","one-handed", "defensive", "off-hand"],2,(1,4),1,["light blade"])
        ,Weapon("spiked shield",["superior","melee","one-handed", "off-hand"],2,(1,6),7,["light blade"])
        ,Weapon("tratnyr",["superior","melee","one-handed","heavy thrown", "versatile"],2,(1,8),5,["spear"],(10,20))
        ,Weapon("triple-headed flail",["superior","melee","one-handed","versatile"],3,(1,10),6,["flail"])
        ,Weapon("waraxe",["superior","melee","one-handed","versatile"],2,(1,12),10,["axe"])
        ,Weapon("double axe",["superior","melee","two-handed", "defensive", "double weapon"],2,(1,10,1,10),15,["axe"])
        ,Weapon("double flail",["superior","melee","two-handed", "defensive", "double weapon"],2,(1,10,1,10),11,["flail"])
        ,Weapon("double sword",["superior","melee","two-handed", "defensive", "double weapon"],3,(1,8,1,8),9,["heavy blade","light blade"])
        ,Weapon("urgrosh",["superior","melee","two-handed", "defensive", "double weapon"],2,(1,12,1,6),12,["axe","spear"])

        ,Weapon("spiked chain",["superior","melee","two-handed","reach"],3,(2,4),10,["flail"])
        ,Weapon("execution axe",["superior","melee","two-handed","brutal 2", "high crit"],2,(1,12),14,["axe"])
        ,Weapon("fullblade",["superior","melee","two-handed","high crit"],3,(1,12),10,["heavy blade"])
        ,Weapon("greatspear",["superior","melee","two-handed","reach"],3,(1,10),8,["polearm","spear"])
        ,Weapon("mordenkrad",["superior","melee","two-handed", "brutal 1"],2,(2,6),12,["hammer"])

        ,Weapon("improvised one-handed",["improvised","melee","one-handed"],0,(1,4),0,[])
        ,Weapon("unarmed attack",["improvised","melee","one-handed"],0,(1,4),0,["unarmed"])
        ,Weapon("improvised two-handed",["improvised","melee","two-handed"],0,(1,8),0,[])
        ,Weapon("battlefist",["melee","one-handed"],3,(1,8),0,["mace"])

        ,Weapon("hand crossbow",["simple","ranged","one-handed","load free"],2,(1,6),2,["crossbow"],(10,20))
        ,Weapon("sling",["simple","ranged","one-handed","load free"],2,(1,6),0,["sling"],(10,20))

        ,Weapon("crossbow",["simple","ranged","two-handed","load minor"],2,(1,8),6,["crossbow"],(15,30))
        ,Weapon("repeating crossbow",["simple","ranged","two-handed","load free"],2,(1,8),4,["crossbow"],(10,20))

        ,Weapon("longbow",["military","ranged","two-handed","load free"],2,(1,10),3,["bow"],(20,40))
        ,Weapon("shortbow",["military","ranged","two-handed","load free","small"],2,(1,8),2,["bow"],(15,30))

        ,Weapon("shuriken",["superior","ranged","one-handed","light thrown"],3,(1,4),0.1,["light blade"],(6,12))
        ,Weapon("greatbow",["superior","ranged","two-handed","load free"],2,(1,12),5,["bow"],(20,40))
        ,Weapon("superior crossbow",["superior","ranged","two-handed","load minor"],3,(1,10),6,["crossbow"],(20,40))

        ,Weapon("improvised ranged",["improvised","ranged","one-handed"],0,(1,4),0,[],(5,10))]
EquipmentLists["Weapons"]={"Military Melee":{},
                           "Military Ranged":{},
                           "Simple Melee":{},
                           "Simple Ranged":{},
                           "Superior Melee":{},
                           "Superior Ranged":{},
                           "Improvised":{}}
weaponList={}
for weapon in weapons:
    weaponList[weapon.name]=weapon
    if "military" in weapon.keys: 
        if "melee" in weapon.keys: EquipmentLists["Weapons"]["Military Melee"][weapon.name]=weapon
        if "ranged" in weapon.keys: EquipmentLists["Weapons"]["Military Ranged"][weapon.name]=weapon
    elif "simple" in weapon.keys: 
        if "melee" in weapon.keys: EquipmentLists["Weapons"]["Simple Melee"][weapon.name]=weapon
        if "ranged" in weapon.keys: EquipmentLists["Weapons"]["Simple Ranged"][weapon.name]=weapon
    elif "superior" in weapon.keys:
        if "melee" in weapon.keys: EquipmentLists["Weapons"]["Superior Melee"][weapon.name]=weapon
        if "ranged" in weapon.keys: EquipmentLists["Weapons"]["Superior Ranged"][weapon.name]=weapon
    else:
        EquipmentLists["Weapons"]["Improvised"][weapon.name]=weapon

armorList=[Item("cloth armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("armortype","light"),ft("armortype","cloth")])],[feat([ft("ac",["enhancement",0])],"magic")],4),
           Item("feyweave armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("ac",("armor",1)),ft("armortype","light"),ft("armortype","cloth")])],[feat([ft("ac",["enhancement",0])],"magic")],5),
           Item("starweave armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("ac",("armor",2)),ft("armortype","light"),ft("armortype","cloth")])],[feat([ft("ac",["enhancement",0])],"magic")],3),
           Item("githweave armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("will",("armor",1)),ft("armortype","light"),ft("armortype","cloth")])],[feat([ft("ac",["enhancement",0])],"magic")],4),
           Item("mindweave armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("will",("armor",2)),ft("armortype","light"),ft("armortype","cloth")])],[feat([ft("ac",["enhancement",0])],"magic")],4),
           Item("efreetweave armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("ac",("armor",1)),ft("will",("armor",1)),ft("armortype","light"),ft("armortype","cloth")])],[feat([ft("ac",["enhancement",0])],"magic")],4),
           Item("mindpatterned armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","cloth")))),ft("ac",("armor",2)),ft("will",("armor",2)),ft("armortype","light"),ft("armortype","cloth")])],[feat([ft("ac",["enhancement",0])],"magic")],4),

           Item("leather armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("ac",("armor",2)),ft("armortype","light"),ft("armortype","leather")])],[feat([ft("ac",["enhancement",0])],"magic")],15),
           Item("feyleather armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("ac",("armor",3)),ft("armortype","light"),ft("armortype","leather")])],[feat([ft("ac",["enhancement",0])],"magic")],15),
           Item("starleather armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("ac",("armor",4)),ft("armortype","light"),ft("armortype","leather")])],[feat([ft("ac",["enhancement",0])],"magic")],15),
           Item("drowmesh armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("ac",("armor",2)),ft("ref",("armor",1)),ft("armortype","light"),ft("armortype","leather")])],[feat([ft("ac",["enhancement",0])],"magic")],15),
           Item("snakeskin armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("ac",("armor",2)),ft("ref",("armor",2)),ft("armortype","light"),ft("armortype","leather")])],[feat([ft("ac",["enhancement",0])],"magic")],15),
           Item("anathema armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("ac",("armor",3)),ft("ref",("armor",1)),ft("armortype","light"),ft("armortype","leather")])],[feat([ft("ac",["enhancement",0])],"magic")],15),
           Item("swordwing armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","leather")))),ft("ac",("armor",3)),ft("ref",("armor",2)),ft("armortype","light"),ft("armortype","leather")])],[feat([ft("ac",["enhancement",0])],"magic")],15),


           Item("hide armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("ac",("armor",3)),ft("acheck",("armor",-1)),ft("armortype","light"),ft("armortype","hide")])],[feat([ft("ac",["enhancement",0])],"magic")],25),
           Item("darkhide armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("ac",("armor",4)),ft("acheck",("armor",-1)),ft("armortype","light"),ft("armortype","hide")])],[feat([ft("ac",["enhancement",0])],"magic")],25),
           Item("elderhide armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("ac",("armor",5)),ft("acheck",("armor",-1)),ft("armortype","light"),ft("armortype","hide")])],[feat([ft("ac",["enhancement",0])],"magic")],25),
           Item("earthhide armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("ac",("armor",3)),ft("fort",("armor",1)),ft("acheck",("armor",-1)),ft("armortype","light"),ft("armortype","hide")])],[feat([ft("ac",["enhancement",0])],"magic")],25),
           Item("feyhide armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("ac",("armor",3)),ft("fort",("armor",2)),ft("acheck",("armor",-1)),ft("armortype","light"),ft("armortype","hide")])],[feat([ft("ac",["enhancement",0])],"magic")],25),
           Item("stalkerhide armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("ac",("armor",4)),ft("fort",("armor",1)),ft("acheck",("armor",-1)),ft("armortype","light"),ft("armortype","hide")])],[feat([ft("ac",["enhancement",0])],"magic")],25),
           Item("voidhide armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","hide")))),ft("ac",("armor",4)),ft("fort",("armor",2)),ft("acheck",("armor",-1)),ft("armortype","light"),ft("armortype","hide")])],[feat([ft("ac",["enhancement",0])],"magic")],25),
           
           Item("chainmail armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("ac",("armor",lambda x:6-x.statret("light armor"))),ft(["acheck","speed"],("armor",-1)),ft("armortype","heavy"),ft("armortype","chainmail")])],[feat([ft("ac",["enhancement",0])],"magic")],40),
           Item("forgemail armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("ac",("armor",lambda x:9-x.statret("light armor"))),ft(["acheck","speed"],("armor",-1)),ft("armortype","heavy"),ft("armortype","chainmail")])],[feat([ft("ac",["enhancement",0])],"magic")],40),
           Item("spiritmail armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("ac",("armor",lambda x:12-x.statret("light armor"))),ft(["acheck","speed"],("armor",-1)),ft("armortype","heavy"),ft("armortype","chainmail")])],[feat([ft("ac",["enhancement",0])],"magic")],40),
           Item("finemail armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("ac",("armor",lambda x:7-x.statret("light armor"))),ft(["acheck","speed"],("armor",-1)),ft("armortype","heavy"),ft("armortype","chainmail")])],[feat([ft("ac",["enhancement",0])],"magic")],40),
           Item("braidmail armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("ac",("armor",lambda x:8-x.statret("light armor"))),ft(["acheck","speed"],("armor",-1)),ft("armortype","heavy"),ft("armortype","chainmail")])],[feat([ft("ac",["enhancement",0])],"magic")],40),
           Item("crysteel armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("ac",("armor",lambda x:8-x.statret("light armor"))),ft("will",("armor",2)),ft(["acheck","speed"],("armor",-1)),ft("armortype","heavy"),ft("armortype","chainmail")])],[feat([ft("ac",["enhancement",0])],"magic")],40),
           Item("weavemail armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("ac",("armor",lambda x:10-x.statret("light armor"))),ft("will",("armor",1)),ft(["acheck","speed"],("armor",-1)),ft("armortype","heavy"),ft("armortype","chainmail")])],[feat([ft("ac",["enhancement",0])],"magic")],40),
           Item("pitmail armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","chainmail")))),ft("ac",("armor",lambda x:11-x.statret("light armor"))),ft("will",("armor",2)),ft(["acheck","speed"],("armor",-1)),ft("armortype","heavy"),ft("armortype","chainmail")])],[feat([ft("ac",["enhancement",0])],"magic")],40),
           
           Item("scale armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("ac",("armor",lambda x:7-x.statret("light armor"))),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","scale")])],[feat([ft("ac",["enhancement",0])],"magic")],45),
           Item("wyrmscale armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("ac",("armor",lambda x:10-x.statret("light armor"))),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","scale")])],[feat([ft("ac",["enhancement",0])],"magic")],45),
           Item("elderscale armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("ac",("armor",lambda x:13-x.statret("light armor"))),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","scale")])],[feat([ft("ac",["enhancement",0])],"magic")],45),
           Item("drakescale armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("ac",("armor",lambda x:8-x.statret("light armor"))),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","scale")])],[feat([ft("ac",["enhancement",0])],"magic")],45),
           Item("wyvernscale armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("ac",("armor",lambda x:9-x.statret("light armor"))),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","scale")])],[feat([ft("ac",["enhancement",0])],"magic")],45),
           Item("stormscale armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("ac",("armor",lambda x:9-x.statret("light armor"))),ft("fort",("armor",2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","scale")])],[feat([ft("ac",["enhancement",0])],"magic")],45),
           Item("nagascale armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("ac",("armor",lambda x:11-x.statret("light armor"))),ft("fort",("armor",1)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","scale")])],[feat([ft("ac",["enhancement",0])],"magic")],45),
           Item("titanscale armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","scale")))),ft("ac",("armor",lambda x:12-x.statret("light armor"))),ft("fort",("armor",2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","scale")])],[feat([ft("ac",["enhancement",0])],"magic")],45),
           
           Item("plate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:8-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           Item("warplate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:11-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           Item("godplate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:14-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           Item("rimefire plate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:8-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           Item("layered plate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:9-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           Item("gith plate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:10-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           Item("specter plate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:10-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           Item("specter plate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:12-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           Item("tarrasque plate armor",["armor"],[feat([ft("ref",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("attack",("armor",lambda x:-2*(1-x.check("proficiency","plate")))),ft("ac",("armor",lambda x:12-x.statret("light armor"))),ft("acheck",("armor",-2)),ft("speed",("armor",-1)),ft("armortype","heavy"),ft("armortype","plate")])],[feat([ft("ac",["enhancement",0])],"magic")],50),
           
           Item("light shield",["off hand"],[feat([ft(["ac","ref"],("shield",lambda x:x.check("proficiency","light"))),ft("armortype","shield"),ft("armortype","light shield")])],[],6),
           Item("heavy shield",["off hand"],[feat([ft(["ac","ref"],("shield",lambda x:2*x.check("proficiency","heavy"))),ft("acheck",("shield",-2)),ft("armortype","shield"),ft("armortype","heavy shield")])],[],15)
           ]
EquipmentLists["Armor"]={"Cloth":{},"Leather":{},"Hide":{},"Chainmail":{},"Scale":{},"Plate":{},"Shields":{}}

for armor in armorList:
    if armor.armorType()=="cloth": EquipmentLists["Armor"]["Cloth"][armor.name()]=armor
    if armor.armorType()=="leather": EquipmentLists["Armor"]["Leather"][armor.name()]=armor
    if armor.armorType()=="hide":EquipmentLists["Armor"]["Hide"][armor.name()]=armor
    if armor.armorType()=="chainmail":EquipmentLists["Armor"]["Chainmail"][armor.name()]=armor
    if armor.armorType()=="scale": EquipmentLists["Armor"]["Scale"][armor.name()]=armor
    if armor.armorType()=="plate":EquipmentLists["Armor"]["Plate"][armor.name()]=armor
    if armor.armorType() in ["heavy shield","light shield"]:EquipmentLists["Armor"]["Shields"][armor.name()]=armor 

EquipmentLists["Implements"]={"orb":Item("orb",["1hand"],[],[feat([ft("orbimplement",["enhancement",0])],"magic")],2),
               "wand":Item("wand",["1hand"],[],[feat([ft("wandimplement",["enhancement",0])],"magic")]),
               "rod":Item("rod",["1hand"],[],[feat([ft("rodimplement",["enhancement",0])],"magic")],2),
               "staff":Item(EquipmentLists["Weapons"]["Simple Melee"]["quarterstaff"]),
               "dagger":Item(EquipmentLists["Weapons"]["Simple Melee"]["dagger"]),
               "tome":Item("tome",["1hand"],[],[feat([ft("tomeimplement",["enhancement",0])],"magic")]),
               "holy symbol":Item("holy symbol",["holy symbol"],[],[feat([ft("holy symbol",["enhancement",0])],"magic")],1),
               "totem":Item("totem",["1hand"],[],[feat([ft("totemimplement",["enhancement",0])],"magic")],2),
               "ki focus":Item("ki focus",["ki focus"],[],[feat([ft("ki focusimplement",["enhancement",0])],"magic")])}

EquipmentLists["Beasts"]={
           "bear":Item("bear",["beast"],[feat([ft("beaststr",["",16]),ft("beastcon",["",14]),ft("beastdex",["",12]),ft("beastint",["",6]),ft("beastwis",["",12]),ft("beastcha",["",6]),ft("beastspeed",["",5]),ft("beastac",["",lambda x:x.statret("level")+12]),ft("beastfort",["",lambda x:x.statret("level")+14]),ft("beastref",["",lambda x:x.statret("level")+10]),ft("beastwill",["",lambda x:x.statret("level")+12]),ft("beasthp",["",lambda x:x.statret("level")*10+16]),ft("beastatk",["",lambda x:x.statret("level")-x.statret("level")/2+2]),ft("beastdiesize",["",12]),ft("beastdmg",["",lambda x:x.mod("beaststr")]),ft("beastsize","medium"),ft(["beastathletics","beastendurance"],["training",5])])],[])
           ,"boar":Item("boar",["beast"],[feat([ft("beaststr",["",16]),ft("beastcon",["",16]),ft("beastdex",["",14]),ft("beastint",["",6]),ft("beastwis",["",12]),ft("beastcha",["",6]),ft("beastspeed",["",6]),ft("beastac",["",lambda x:x.statret("level")+14]),ft("beastfort",["",lambda x:x.statret("level")+12]),ft("beastref",["",lambda x:x.statret("level")+10]),ft("beastwill",["",lambda x:x.statret("level")+12]),ft("beasthp",["",lambda x:x.statret("level")*8+14]),ft("beastatk",["",lambda x:x.statret("level")-x.statret("level")/2+4]),ft("beastdiesize",["",8]),ft("beastdmg",["",lambda x:x.mod("beaststr")]),ft("beastsize","medium"),ft("beastendurance",["training",5])])],[])
           ,"cat":Item("cat",["beast"],[feat([ft("beaststr",["",14]),ft("beastcon",["",12]),ft("beastdex",["",16]),ft("beastint",["",6]),ft("beastwis",["",14]),ft("beastcha",["",6]),ft("beastspeed",["",7]),ft("beastac",["",lambda x:x.statret("level")+14]),ft("beastfort",["",lambda x:x.statret("level")+11]),ft("beastref",["",lambda x:x.statret("level")+13]),ft("beastwill",["",lambda x:x.statret("level")+12]),ft("beasthp",["",lambda x:x.statret("level")*8+14]),ft("beastatk",["",lambda x:x.statret("level")-x.statret("level")/2+4]),ft("beastdiesize",["",8]),ft("beastdmg",["",lambda x:x.mod("beastdex")]),ft("beastsize","medium"),ft(["beastathletics","beaststealth"],["training",5])])],[])
           ,"lizard":Item("lizard",["beast"],[feat([ft("beaststr",["",16]),ft("beastcon",["",14]),ft("beastdex",["",16]),ft("beastint",["",6]),ft("beastwis",["",12]),ft("beastcha",["",6]),ft("beastspeed",["",6]),ft("beastac",["",lambda x:x.statret("level")+15]),ft("beastfort",["",lambda x:x.statret("level")+12]),ft("beastref",["",lambda x:x.statret("level")+12]),ft("beastwill",["",lambda x:x.statret("level")+10]),ft("beasthp",["",lambda x:x.statret("level")*8+14]),ft("beastatk",["",lambda x:x.statret("level")-x.statret("level")/2+4]),ft("beastdiesize",["",8]),ft("beastdmg",["",lambda x:x.mod("beaststr")]),ft("beastsize","medium"),ft(["beastathletics","beastendurance"],["training",5])])],[])
           ,"raptor":Item("raptor",["beast"],[feat([ft("beaststr",["",12]),ft("beastcon",["",12]),ft("beastdex",["",18]),ft("beastint",["",6]),ft("beastwis",["",12]),ft("beastcha",["",6]),ft("beastspeed",["",2]),ft("beastac",["",lambda x:x.statret("level")+14]),ft("beastfort",["",lambda x:x.statret("level")+10]),ft("beastref",["",lambda x:x.statret("level")+14]),ft("beastwill",["",lambda x:x.statret("level")+12]),ft("beasthp",["",lambda x:x.statret("level")*6+12]),ft("beastatk",["",lambda x:x.statret("level")-x.statret("level")/2+5]),ft("beastdiesize",["",6]),ft("beastdmg",["",lambda x:x.mod("beastdex")]),ft("beastsize","small"),ft("beastperception",["training",5])])],[])
           ,"serpent":Item("serpent",["beast"],[feat([ft("beaststr",["",14]),ft("beastcon",["",14]),ft("beastdex",["",16]),ft("beastint",["",6]),ft("beastwis",["",12]),ft("beastcha",["",6]),ft("beastspeed",["",5]),ft("beastac",["",lambda x:x.statret("level")+14]),ft("beastfort",["",lambda x:x.statret("level")+12]),ft("beastref",["",lambda x:x.statret("level")+13]),ft("beastwill",["",lambda x:x.statret("level")+12]),ft("beasthp",["",lambda x:x.statret("level")*8+14]),ft("beastatk",["",lambda x:x.statret("level")-x.statret("level")/2+4]),ft("beastdiesize",["",8]),ft("beastdmg",["",lambda x:x.mod("beastdex")]),ft("beastsize","medium"),ft("beaststealth",["training",5])])],[])
           ,"spider":Item("spider",["beast"],[feat([ft("beaststr",["",14]),ft("beastcon",["",12]),ft("beastdex",["",16]),ft("beastint",["",6]),ft("beastwis",["",12]),ft("beastcha",["",6]),ft("beastspeed",["",6]),ft("beastac",["",lambda x:x.statret("level")+14]),ft("beastfort",["",lambda x:x.statret("level")+11]),ft("beastref",["",lambda x:x.statret("level")+12]),ft("beastwill",["",lambda x:x.statret("level")+12]),ft("beasthp",["",lambda x:x.statret("level")*8+14]),ft("beastatk",["",lambda x:x.statret("level")-x.statret("level")/2+4]),ft("beastdiesize",["",8]),ft("beastdmg",["",lambda x:x.mod("beastdex")]),ft("beastsize","medium"),ft(["beastathletics","beaststealth"],["training",5])])],[])
           ,"wolf":Item("wolf",["beast"],[feat([ft("beaststr",["",14]),ft("beastcon",["",14]),ft("beastdex",["",14]),ft("beastint",["",6]),ft("beastwis",["",14]),ft("beastcha",["",6]),ft("beastspeed",["",7]),ft("beastac",["",lambda x:x.statret("level")+14]),ft("beastfort",["",lambda x:x.statret("level")+12]),ft("beastref",["",lambda x:x.statret("level")+12]),ft("beastwill",["",lambda x:x.statret("level")+13]),ft("beasthp",["",lambda x:x.statret("level")*8+14]),ft("beastatk",["",lambda x:x.statret("level")-x.statret("level")/2+4]),ft("beastdiesize",["",8]),ft("beastdmg",["",lambda x:x.mod("beaststr")]),ft("beastsize","medium"),ft(["beastperception","beastendurance"],["training",5])])],[])
           }
EquipmentLists["Misc"]={
         "bracers":Item("bracers",["arm"],[],[]),
         "hat":Item("hat",["head"],[],[]),
        "gloves":Item("gloves",["hands"],[],[]),
        "amulet":Item("amulet",["neck"],[],[feat([ft(["fort","ref","will"],["enhancement",0])],"magic")]),
        "cloak":Item("cloak",["neck"],[],[feat([ft(["fort","ref","will"],["enhancement",0])],"magic")]),
        "boots":Item("boots",["feet"],[],[]),
        "ring":Item("ring",["ring"],[],[])
         }

EquipmentLists["Gear"]={
         "backpack":Item("backpack",[],[],[],2),
         "bedroll":Item("bedroll",[],[],[],5),
         "flint and steel":Item("flint and steel",[],[],[]),
         "belt pouch":Item("belt pouch",[],[],[],0.5),
         "trail rations (day)":Item("trail rations (day)",[],[],[],1),
         "hempen rope (ft.)":Item("feet hempen rope",[],[],[],0.2),
         "sunrod":Item("sunrod",[],[],[],2),
         "waterskin":Item("waterskin",[],[],[],4),
         "arrows":Item("arrows",[],[],[],0.1),
         "crossbow bolts":Item("crossbow bolts",[],[],[],0.1),
         "sling bullets":Item("sling bullets",[],[],[],0.25),
         "candle":Item("candle",[],[],[]),
         "chain (ft.)":Item("chain",[],[],[],2),
         "chest":Item("chest",[],[],[],25),
         "grappling hook":Item("grappling hook",[],[],[],4),
         "hammer":Item("hammer",[],[],[],2),
         "pitons":Item("pitons",[],[],[],0.5),
         "everburning torch":Item("everburning torch",[],[],[],1),
         "fine clothing":Item("fine clothing",[],[],[],6),
         "flask":Item("flask",[],[],[],1),
         "journeybread":Item("journeybread",[],[],[],0.1),
         "lantern":Item("lantern",[],[],[],2),
         "lamp oil (pt.)":Item("lamp oil",[],[],[],1),
         "ritual book":Item("ritual book",[],[],[],3),
         "silk rope (ft.)":Item("feet silk rope",[],[],[],5),
         "spellbook":Item("spellbook",[],[],[],3),
         "tent":Item("tent",[],[],[],20),
         "thieves' tools":Item("thieve's tools",[],[],[],1),
         "torch":Item("torch",[],[],[],1),
          }
EquipmentLists["Instruments"]={}
Instruments=[Item("drum",[],[],[],1),
              Item("flute",[],[],[],1),
              Item("harp",[],[],[],4),
              Item("horn",[],[],[],3),
              Item("lute",[],[],[],2),
              Item("lyre",[],[],[],2),
              Item("woodwind",[],[],[],1)]
for x in Instruments:
    EquipmentLists["Instruments"][x.name()]=x
EquipmentLists["Wondrous Items"]={}
Wondrous=[Item("bag of holding",[],[],[],1),
          Item("dimensional shackles",[],[],[],0),
          Item("dust of appearance",[],[],[],0),
          Item("everlasting provisions",[],[],[],0),
          Item("feather boat",[],[],[],0),
          Item("flying carpet",[],[],[],0),
          Item("handy haversack",[],[],[],1),
          Item("keoghtom's ointment",[],[],[],0),
          Item("portable hole",[],[],[],0)]
for x in Wondrous:
    EquipmentLists["Wondrous Items"][x.name()]=x
EquipmentLists["Potions"]={}
Potions=[Item("potion of healing",[],[],[],0),
         Item("potion of life",[],[],[],0),
         Item("potion of recovery",[],[],[],0),
         Item("potion of vitality",[],[],[],0)]
for x in Potions:
    EquipmentLists["Potions"][x.name()]=x
propertyList={}

def addProperties(properties):
    for x in properties:
        name=x.name.replace("#","").strip()
        propertyList[name]=x
def PHBproperties():
    return [
       Property("angelsteel #",[4,"chainmail"],[feat([Power("Angelsteel Armor",[],"daily","immediate reaction",[Trigger("You are hit by an attack"),Effect("Gain a +2 power bonus to the defense that attack targetted until the end of the encounter.")],"","item")])]),
       Property("barkskin #",[1,"scale","hide"],[feat([ft("barkskin #",["item",0])],"magic"),feat([Power("Barkskin Armor",[],"daily","minor",[Effect(["Gain a +",lambda x:(x.statret("barkskin #")+3)/2," power bonus to AC until the end of the encounter.  Each time an attack hits your AC, reduce this bonus by 1 (minimum 0)."])],"","item")])]),
       Property("battleforged #",[1,"plate"],[feat([ft("battleforged #",["item",0])],"magic"),feat([],"Battleforged Armor",["Using second wind while bloodied restores ",lambda x:(x.statret("battleforged #")+1)/2,"d10 extra hit points."])]),
       Property("black iron #",[1,"scale","plate"],[feat([ft("black iron #",["item",0])],"magic"),feat([],"Black Iron Armor",["Resist ",lambda x:((x.statret("black ironlevel")+1)/2)*5," fire and resist ",lambda x:((x.statret("black iron #")+1)/2)*5," necrotic."])]),
       Property("bloodcut #",[1,"leather","hide"],[feat([ft("bloodcut #",["item",0])],"magic"),feat([Power("Barkskin Armor",["(healing surge)"],"daily","minor",[Effect(["While you are bloodied, use this armor to gain resist",lambda x:((x.statret("bloodcut #")+3)/2)*5," to all damage until the end of your next turn."])],"","item")])]),
       Property("bloodthread #",[1,"cloth"],[feat([],"Bloodthread Armor","When you are bloodied, you gain a +2 item bonus to AC and saving throws")]),
       Property("curseforged #",[1,"scale","chainmail"],[feat([ft("curseforged #",["item",0])],"magic"),feat([Power("Curseforged Armor",[],"daily","immediate reaction",[Trigger("An enemy hits you with an attack"),Effect(["The triggering enemy takes a -",lambda x:(x.statret("curseforged #")+3)/2," penalty to attack rolls (save ends).  When the enemy saves against the penalty, the enemy takes a -1 penalty on attack rolls (save ends)."])],"","item")])]),
       Property("darkleaf #",[1,"cloth","leather","hide"],[feat([],"Darkleaf Armor","Gain a +2 item bonus to AC against the first attack made against you in each encounter")]),
       Property("deathcut #",[1,"leather","hide"],[feat([ft("deathcut #",["item",0])],"magic"),feat([Power("Deathcut Armor",["necrotic"],"daily","minor",[Trigger("An enemy hits you with an attack"),Effect(["Deal ",dmg(CHAMOD,lambda x:(x.statret("deathcut #")+1)/2,10)," to that enemy."])],"","item")],"Deathcut Armor","Resist 5 necrotic and resist 5 poison")]),
       Property("delver's #",[1,"armor"],[feat([Power("Delver's Armor",[],"daily","no",[Effect("Gain a +2 power bonus to a saving throw you just rolled; use the new result.")],"","item")])]),
       Property("dwarven #",[1,"chainmail","scale","plate"],[feat([ft(["dwarven #","endurance"],["item",0])],"magic"),feat([Power("Dwarven Armor",["healing"],"daily","free",[Effect("Regain hit points as if you had spent a healing surge.")],"","item")],"Dwarven Armor",["Gain a +",lambda x:x.statret("dwarven #")," item bonus to Endurance checks."])]),
       Property("eladrin #",[1,"chainmail"],[feat([ft("eladrin #",["item",0])],"magic"),feat([ft(["acheck","speed"],("armor",0))],"Eladrin Armor",["Add ",lambda x:(x.statret("eladrin #")+1)/2," square(s) to the maximum distance of any teleport you make"])]),
       Property("elven battle #",[2,"leather","hide"],[feat([Power("Elven Battle Armor",[],"encounter","minor",[Effect("Gain a +2 power bonus to speed until the end of your next turn.")],"","item")],"Elven Battle Armor","Gain a +5 item bonus to saving throws against being slowed or immobilized")]),
       Property("exalted #",[1,"chainmail"],[feat([Power("Exalted Armor",["healing"],"daily","minor",[Effect(["Until the end of your turn, each character healed by one of your encounter powers or daily powers regains 1d10",plus(CHAMOD)," additional hit points."])],"","item")])]),
       Property("fireburst #",[1,"cloth"],[feat([ft("fireburst #",["item",0])],"magic"),feat([Power("Fireburst Armor",["fire"],"daily","minor",[Effect(["Until the end of your next turn, any creature that hits you with a melee attack takes ",dmg(CHAMOD,lambda x:(x.statret("fireburst #")+1)/2,8),"."])],"","item")],"Fireburst Armor","You automatically succeed on saving throws against ongoing fire damage")]),
       Property("flamedrinker #",[3,"plate"],[feat([ft("flamedrinker #",["item",0])],"magic"),feat([Power("Flamedrinker Armor",[],"daily","immediate interrupt",[Trigger("You are hit by a power that has the fire keyword"),Effect(["You and each ally within 5 squares of you gain resist ",lambda x:((x.statret("flamedrinker #")+1)/2)*10," fire until the end of your next turn."])],"","item")],"Flamedrinker Armor",["Resist ",lambda x:((x.statret("flamedrinker #")+1)/2)*5," fire"])]),
       Property("ghostphase #",["2,cloth"],[feat([ft("ghostphase #",["item",0])],"magic"),feat([Power("Ghostphase Armor",[],"daily","minor",[Effect(["Become insubstantial ",orfeat("","and gain phasing ",["ghostphase #",5])," until the end of your next turn."])],"","item")],"Ghostphase Armor",[orfeat("",["Resist ",lambda x:(x.statret("ghostphase #")/2)*5," necrotic"],["ghostphase #",3])])]),
       Property("hydra #",[3,"scale"],[feat([ft("hydra #",["item",0])],"magic"),feat([],"Hydra Armor",["When an enemy scores a critical hit against you, gain regeneration ",lambda x:(x.statret("hydra #")-1)/2*5," until the end of the encounter."])]),
       Property("mantle of the seventh wind",[5,"cloth"],[feat([],"Mantle of the Seventh Wind","You have a fly speed equal to your speed, but you must end each turn on a solid surface or you fall.")]),
       Property("mountain #",[2,"plate"],[feat([ft("mountain #",["item",0])],"magic"),feat([Power("Mountain Armor",[],"encounter","immediate interrupt",[Trigger("You are subjected to a push, pull, or slide effect"),Effect(["Reduce the forced movement by ",lambda x:((x.statret("mountain #"))/2)," square(s)."])],"","item")])]),
       Property("razor #",[1,"scale"],[feat([ft("razor #",["item",0])],"magic"),feat([],"Razor Armor",["When an enemy scores a melee critical against you, that enemy takes ",damage(DEXMOD,lambda x:(x.statret("razor #")+1)/2,10),"."])]),
       Property("shadowflow #",[3,"cloth","leather"],[feat([ft(["shadowflow #","stealth"],["item",0])],"magic"),feat([Power("Shadowflow Armor",[],"encounter","minor",[Effect(["Gain ",orfeat("concealment","invisibility",["shadowflow #",5])," until the start of your next turn."])],"","item")],"Shadowflow Armor",["Gain a +",lambda x:x.statret("shadowflow #")," item bonus to Stealth checks."])]),
       Property("soulforged #",[4,"plate"],[feat([],"Soulforged Armor","Remain concious at 0 or fewer until end of your next turn.  If still at or below 0 at end of turn, effected as normal.")]),
       Property("sunleaf #",[2,"cloth","leather","hide"],[feat([ft("sunleaf #",["item",0])],"magic"),feat([Power("Sunleaf Armor",["radiant"],"daily","free",[Trigger("You are hit by an opportunity attack"),Effect(["Deal ",damage(DEXMOD,lambda x:((x.statret("sunleaf #")+1)/2),10)," to triggering enemy."])],"","item")],"Sunleaf Armor",["Resist ",lambda x:((x.statret("sunleaf #")+1)/2)*5," radiant"])]),
       Property("sylvan #",[3,"chainmail","leather","hide"],[feat([ft(["sylvan #","athletics","stealth"],["item",0])],"magic"),feat([],"Sylvan Armor",["Gain a +",lambda x:x.statret("sylvan #")," item bonus to Athletics check and Stealth checks."])]),
       Property("tombforged #",[3,"chainmail"],[feat([ft("tombforged #",["item",0])],"magic"),feat([Power("Tombforged Armor",["healing"],"daily","immediate interrupt",[Trigger(["An ally within ",lambda x:(x.statret("tombforged #")-1)/2*5," squares of you takes damage"]),Effect("You spend a healing surge but regain no hit points.  Instead, the ally regains hit points as if her or she had spent a healing surge.")],"","item")],"Tombforged Armor",["Resist ",lambda x:((x.statret("tombforged #")+1)/2)*5," necrotic"])]),
       Property("trollskin #",[3,"hide","scale"],[feat([ft("trollskin #",["item",0])],"magic"),feat([Power("Trollskin Armor",["healing"],"daily","standard",[Effect(["Gain regeneration ",lambda x:(x.statret("trollskin #")-1)/2*5," until the end of the encounter or until you drop to 0 hit points or fewer.  If you take acid or fire damage, the regeneration is surpressed until the end of your next turn."])],"","item")])]),
#Weapon Properties
       Property("berserker #",[2,"axe","heavy blade"],[feat([ft("berserker #",["item",0])],"magic"),feat([Power("Berserker Weapon",[],"daily","minor",[Effect(["Gain a +2 power bonus to all attack rolls and damage rolls with this weapon and take a -5 penalty to all defenses.  You also gain resist ",lambda x:x.statret("berserker #")/2*5," to all damage.  the effects last until the end of the encounter or until you fall unconscious."])],"","item")])]),
       Property("dancing #",[4,"heavy blade","light blade"],[feat([Power("Dancing Weapon",[],"daily","minor",[Effect("You release the dancing weapon, and it hovers near you until the end of your next turn or until you drop to 0 hit points or fewer."),Line("You can deliver basic attacks and attack powers through the dancing weapon as if you were holding it yourself (including all attack and damage modifiers you'd normally apply)."),Line("If you do not attack with a dancing weapon before the end of your turn, it makes a melee basic attack against an enemy of your choice within 2 squares of you as if you were wielding it.  A dancing weapon cannot make opportunity attacks."),Line("Except during brief moments when it is attacking, a dancing weapon remains in your space, even if you move away or are teleported.  It automatically resists any attempts by other creatures to take hold of it."),Line("At any time during the encounter, you can take hold of the weapon again.  This ends the effect."),Sustain("minor","The sword continues to hover and fight near you until the end of your next turn.")],"","item")])]),
       Property("dragonslayer #",[2,"weapon"],[feat([ft("dragonslayer #",["item",0])],"magic"),feat([Power("Dragonslayer Weapon",[],"daily","minor",[Effect("Your next attack made with this weapon against a dragon, if made before the end of your next turn, gains a +5 power bonus to the attack roll and automatically ignores any resistance the dragon has.")],"","item")],"Dragonslayer Weapon",["Gain resist ",lambda x:(x.statret("dragonslayer #")+1)/2*5," against dragon breath attacks."])]),
       Property("deulist's #",[1,"light blade"],[feat([Power("Duelist's Weapon",[],"daily","minor",[Effect("You have combat advantage against the next creature you attack with this weapon on this turn.")],"","item")])]),
       Property("flameburst #",[1,"ranged"],[feat([ft("flameburst #",["item",0])],"magic"),feat([Power("Flameburst Weapon",["fire"],"daily","standard",[Effect(["The next ranged basic attack you make with this weapon before the end of your turn becomes a burst 1 centered on the target.  Use your normal attack bonus for the basic attack, but against Reflex.  Instead of normal damage, each target takes ongoing ",lambda x:(x.statret("flameburst #")+1)/2*5," fire damage (save ends)."])],"","item")])]),
       Property("flaming #",[1,"weapon"],[feat([ft("flaming #",["item",0])],"magic"),feat([Power("Flaming Weapon",["fire"],"at-will","free",[Effect("All damage dealt by this weapon is fire damage.  Another free action returns the damage to normal.")],"","item"),Power("Fire Weapon Daily",["fire"],"daily","free",[Trigger("You hit with the weapon"),Effect(["The target takes an extra ",dmg(0,lambda x:(x.statret("flaming #")+1)/2,6)," and ",lambda x:(x.statret("flaming #")+1)/2*5," ongoing fire damage (save ends)"])],"","item")])]),
       Property("frost #",[1,"weapon"],[feat([ft("frost #",["item",0])],"magic"),feat([Power("Frost Weapon",["cold"],"at-will","free",[Effect("All damage dealt by this weapon is cold damage.  Another free action returns the damage to normal.")],"","item"),Power("Frost Weapon Daily",["cold"],"daily","free",[Trigger("You hit with the weapon"),Effect(["The target takes an extra ",dmg(0,lambda x:(x.statret("frost #")+1)/2,8)," and is slowed until the end of your next turn."])],"","item")])]),
       Property("holy avenger #",[5,"axe","hammer","heavy blade"],[feat([ft(["holy avenger"],["enhancement",0])],"magic"),feat([Power("Holy Avenger",[],"daily","minor",[Effect("You and each ally within 10 squares of you gain a +5 power bonus to Fortitude, Reflex, and Will defenses until the end of your next turn.")],"","item")],"Holy Avenger","This weapon deals an extra 1d10 radiant damage when used with an attack that has the Radiant keyword.")]),
       Property("lifedrinker #",[1,"melee"],[feat([ft("lifedrinker #",["item",0])],"magic"),feat([],"Lifedrinker Weapon",["When you drop an enemy to 0 hit points or fewer with a melee attack made with this weapon, gain ",lambda x:(x.statret("lifedrinker #")+1)/2*5," temporary hit points."])]),
       Property("lightning #",[1,"weapon"],[feat([ft("lightning #",["item",0])],"magic"),feat([Power("Lightning Weapon",["lightning"],"at-will","free",[Effect("All damage dealt by this weapon is lightning damage.  Another free action returns the damage to normal.")],"","item"),Power("Lightning Weapon Daily",["lightning"],"daily","free",[Trigger("You hit with the weapon"),Effect(["The target and each enemy within 2 squares of the target takes ",dmg(0,lambda x:(x.statret("lightning #")+1)/2,6)," ."])],"","item")])]),
       Property("pact #",[1,"light blade"],[feat([ft(["pact blade #"],["item",0]),ft(["pact blade"],["enhancement",0])],"magic"),feat([],"Pact Blade",["When a creature you have cursed makes a melee attack against you, deal ",lambda x:x.statret("pact blade #")," damage to the creature."])]),
       Property("perfect hunter's #",[6,"ranged"],[feat([Power("Perfect Hunter's Weapon",[],"daily","standard",[Effect("When you use this power, you automatically pinpoint the location of all creatures within 10 squares of you, even if line of sight or line of effect to those creatures would normally be blocked.  This pinpointing lasts until the end of your turn.  You can target any one of those creatures as if it did not have cover or concealment.  You can then make a ranged basic attack with this weapon with a +5 bonus to the attack roll.")],"","item")])]),
       Property("phasing #",[3,"ranged"],[feat([],"Phasing Weapon","Your ranged attacks with this weapon ignore the penalty to attack rolls for cover or superior cover.")]),
       Property("resounding #",[1,"hammer","flail","mace","sling","staff"],[feat([Power("Resounding Weapon",[],"daily","free",[Trigger("You hit with the weapon"),Effect("The target is dazed until the end of your next turn.")],"","item")])]),
       Property("terror #",[1,"axe","hammer","heavy blade"],[feat([Power("Terror Weapon",["fear"],"daily","free",[Trigger("You hit with the weapon"),Effect("The target takes a -2 penalty to all defenses (save ends).")],"","item")])]),
       Property("thunderburst #",[1,"ranged"],[feat([ft("thunderburst #",["item",0])],"magic"),feat([Power("Thunderburst Weapon",["thunder"],"daily","standard",[Effect(["The next ranged basic attack you make with this weapon before the end of your turn becomes a burst ",lambda x:(x.statret("thunderburst #")+1)/2," centered on the target.  Use your normal attack bonus for the basic attack, but against Fortitude.  Each target hit takes thunder damage equal to the normal damage you would deal with a ranged basic attack with this weapon."])],"","item")])]),
       Property("thundering #",[1,"weapon"],[feat([ft("thundering #",["item",0])],"magic"),feat([Power("Thundering Weapon",["thunder"],"daily","free",[Trigger("You hit with the weapon"),Effect(["Deal an extra ",lambda x:(x.statret("thundering #")+1)/2,"d8 thunder damage and push the target 1 square."])],"","item")])]),
       Property("vicious #",[1,"weapon"],[]),
       Property("vorpal #",[6,"axe","heavy blade"],[feat([Power("Vorpal Weapon",[],"daily","free",[Trigger("You hit with the weapon"),Effect(["Deal an extra 3d12 damage with the attack."])],"","item")],"Vorpal Weapon","Whenever you roll maximum on a damage die with this weapon, add another die of damage.")]),
#Implement properties
       Property("symbol of battle",[1,"holy symbol"],[feat([ft("symbol of battle #",["item",0])],"magic"),feat([Power("Symbol of Battle",[],"daily","free",[Trigger("You hit with a power using this symbol"),Effect(["Deal an extra ",lambda x:(x.statret("symbol of battle #")+1)/2,"d10 damage."])],"","item")])]),
       Property("symbol of hope",[1,"holy symbol"],[feat([Power("Symbol of Hope",[],"daily","immediate reaction",[Trigger("You or an ally within 5 squares is hit by an effect that a save can end"),Effect("You or the ally gain a +5 power bonus to saving throws against the effect.")],"","item")])]),
       Property("symbol of life",[1,"holy symbol"],[feat([ft("symbol of life #",["item",0])],"magic"),feat([Power("Symbol of Life",["healing"],"daily","minor",[Effect(["Until the end of your turn, any character healed by one of your encounter or daily powers regains an additional ",lambda x:(x.statret("symbol of life #")+1)/2,"d6 hit points."])],"","item")])]),
       Property("symbol of power",[2,"holy symbol"],[feat([],"Symbol of Power","Targets are at -2 to the first saving throw against effects delivered by this symbol")]),
       Property("symbol of radiance",[5,"holy symbol"],[feat([Power("Symbol of Radiance",["healing"],"daily","free",[Trigger("You use the symbol to attack with a power that has the Radiant keyword"),Target("one ally",("ranged",10)),Effect("The target can spend a healing surge.")],"","item")])]),
       Property("symbol of victory",[2,"holy symbol"],[feat([Power("Symbol of Victory",[],"daily","free",[Trigger("You or an ally within 5 squares scores a critical hit"),Effect("That character gains an action point.")],"","item")])]),
       Property("orb of drastic resolutions",[3,"orb"],[feat([Power("Orb of Drastic Resolutions",[],"daily","free",[Trigger("An enemy within 10 squares of you drops to 0 hit points or fewer."),Effect("Immobilize (save ends) or Weaken (save ends) a different enemy within 10 squares of you.")],"","item")])]),
       Property("orb of indisputable gravity",[2,"orb"],[feat([Power("Orb of Indisputable Gravity",[],"daily","minor",[Effect("Until the end of your next turn, any attack that hist a flying creature within 10 squares of you also forces that creature to gently fall 10 squares.  If a descent that distance would bring the creature to the ground, it lands prone but takes no damage from the fall.")],"","item")])]),
       Property("orb of inevitable continuance",[1,"orb"],[feat([Power("Orb of Inevitable Continuance",[],"daily","minor",[Effect("One of your powers that is due to end at the end of this turn instead lasts until the end of your next turn.")],"","item")])]),
       Property("orb of invasive fortune",[4,"orb"],[feat([Power("Orb of Invasive Fortune",[],"daily","immediate interrupt",[Trigger("An enemy within 10 squares of you successfully recharges a power."),Effect("The recharge fails and you regain the use of an expended encounter power.")],"","item")])]),
       Property("orb of reversed polarities",[2,"orb"],[feat([ft("orb of reversed polarities #",["item",0])],"magic"),feat([Power("Orb of Reversed Polarities",[],"daily","minor",[Effect(["Until the end of your next turn, your attacks treat any resistance possessed by a target as vulnerable ",lambda x:(x.statret("orb of reversed polarities #")+1)/2*5," to the same damage type."])],"","item")])]),
       Property("orb of sanguinary repercussions",[1,"orb"],[feat([ft("orb of sanguinary repercussions #",["item",0])],"magic"),feat([Power("Orb of Sanguinary Repercussions",[],"daily","minor",[Effect(["Deal ",dmg(INTMOD,lambda x:(x.statret("orb of sanguinary repercussions #")+1)/2,6)," to each bloodied creature within 5 squares of you."])],"","item")])]),
       Property("rod of corruption",[1,"rod"],[feat([],"Rod of Corruption","May curse enemies within 5 squares of target instead ot taking pact boon")]),
       Property("rod of dark reward",[1,"rod"],[feat([],"Rod of Dark Reward","+1 power bonus to AC until start of next turn whenever you curse an enemy")]),
       Property("rod of death's grasp",[5,"rod"],[feat([ft("rod of death's grasp #",["item",0])],"magic"),feat([Power("Rod of Death's Grasp",["necrotic"],"daily","free",[Trigger("You place your Warlock's Curse on a target"),Effect(["The target takes ongoing ",lambda x: x.statret("rod of death's grasp #")*5-15," necrotic damage (save ends).  Each time this damage is dealt, you gain ",lambda x: x.statret("rod of death's grasp #")*5-15," temporary hit points"])],"","item")])]),
       Property("rod of first blood",[2,"rod"],[feat([ft("rod of first blood #",["item",0])],"magic"),feat([],"Rod of First Blood",["When you hit a creature with maximum hit points with this rod, deal an extra ",lambda x:(x.statret("rod of first blood #")+1)/2,"d8 damage"])]),
       Property("rod of harvest",[3,"rod"],[feat([Power("Rod of Harvest",[],"encounter","miner",[Effect("Use the pact boon effect stored within your rod")],"","item")],"Rod of Harvest","When your pact boon is triggered, you can store it in your rod.")]),
       Property("rod of reaving",[1,"rod"],[feat([ft("rod of reaving #",["item",0])],"magic"),feat([],"Rod of Reaving",["When you place your warlocks curse on a nonminion target, it takes ",lambda x:x.statret("rod of reaving #")," damage."])]),
       Property("rod of the pyre",[2,"rod"],[feat([ft("rod of the pyre #",["item",0])],"magic"),feat([Power("Rod of the Pyre",[],"daily","free",[Trigger("You place your Warlock's Curse on a target"),Effect(["The target gains vulnerability ",lambda x:x.statret("rod of the pyre #")," fire until the end of your next turn."])],"","item")])]),
       Property("staff of fiery might",[1,"staff"],[feat([ft("staff of fiery might #",["item",0])],"magic"),feat([Power("Staff of Fiery Might",[],"daily","free",[Trigger("You use a power that has the Fire keyword"),Effect(["After rolling damage, you can reroll up to ",lambda x:x.statret("staff of fiery might #")," dice.  You must keep the new results, and can't reroll any dice more than once."])],"","item")]),
       Property("staff of power",[4,"staff"],[feat([Power("Staff of Power",[],"daily","free",[Trigger("You score a critical hit using an encounter power or a daily power"),Effect("That power is not expended")],"","item")])]),
       Property("staff of storms",[1,"staff"],[ft("staff of storms #",["item",0])],"magic"),feat([Power("Staff of Storms",["lightning","thunder"],"daily","free",[Trigger("You use a power that has the lightning or the thunder keyword"),Effect(["After resolving the power, deal ",dmg(0,lambda x: (x.statret("staff of storms #")+1)/2,8)," to every creature in a close blast 3"])],"","item")])]),
       Property("staff of the war mage",[1,"staff"],[feat([Power("Staff of the War Mage",[],"daily","free",[Trigger("You use a power that has a blast or burst effect"),Effect("Increase the size of the blast or burst by 1")],"","item")])]),
       Property("staff of winter",[1,"staff"],[feat([Power("Staff of Winter",[],"daily","free",[Trigger("You use a power that has the cold keyword"),Effect("After you resolve the power, all enemies within 3 squares of you are immobilized (save ends).")],"","item")])]),
       Property("thunderwave staff",[2,"staff"],[feat([ft("thunderwave staff #",["item",0])],"magic"),feat([Power("Thunderwave Staff",["thunder"],"daily","free",[Trigger("You would push one or more creatures with one of your powers"),Effect(["Instead of pushing those creatures, knock them prone and deal ",lambda x:(x.statret("thunderwave staff #")+1)/2*2+4," thunder damage to each one, where x equals the number of squares you would normally push each one."])],"","item")])]),
       Property("wand of eldritch rain",[2,"wand"],[feat([atWillAsEncounter([powerList["warlockencounter3"]["Eldritch Rain"]],"","daily")])]),
       Property("wand of fiery bolt",[2,"wand"],[feat([atWillAsEncounter([powerList["warlockencounter3"]["Fiery Bolt"]],"","daily")])]),
       Property("wand of fire burst",[3,"wand"],[feat([atWillAsEncounter([powerList["wizardencounter7"]["Fire Burst"]],"","daily")])]),
       Property("wand of icy rays",[2,"wand"],[feat([atWillAsEncounter([powerList["wizardencounter3"]["Icy Rays"]],"","daily")])]),
       Property("wand of ray of enfeeblement",[1,"wand"],[feat([atWillAsEncounter([powerList["wizardencounter1"]["Ray of Enfeeblement"]],"","daily")])]),
       Property("wand of shield",[2,"wand"],[feat([atWillAsEncounter([powerList["wizardutility2"]["Shield"]],"","daily")])]),
       Property("wand of soul flaying",[4,"wand"],[feat([atWillAsEncounter([powerList["warlockencounter13"]["Soul Flaying"]],"","daily")])]),
       Property("wand of witchfire",[1,"wand"],[feat([atWillAsEncounter([powerList["warlockencounter1"]["Witchfire"]],"","daily")])]),
#Arm slot properties
       Property("bashing shield (Heroic)",["shield"],[feat([Power("Bashing Shield",[],"daily","free",[Trigger("You hit an enemy with a melee attack"),Effect("Push the enemy 1d4 squares after applying the attack's effects.")],"","item")],"","")],["off hand","arm"]),
       Property("bashing shield (Paragon)",["shield"],[feat([Power("Bashing Shield",[],"daily","free",[Trigger("You hit an enemy with a melee attack"),Effect("Push the enemy 2d4 squares after applying the attack's effects.")],"","item")],"","")],["off hand","arm"]),
       Property("bashing shield (Epic)",["shield"],[feat([Power("Bashing Shield",[],"daily","free",[Trigger("You hit an enemy with a melee attack"),Effect("Push the enemy 3d4 squares after applying the attack's effects.")],"","item")],"","")],["off hand","arm"]),
       Property("bracers of defense (Heroic)",["shield"],[feat([Power("Bracers of Defense",[],"daily","immediate interrupt",[Trigger("You are hit by a melee attack"),Effect("Reduce the damage dealt to you by the attack by 10.")],"","item")],"","")]),
       Property("bracers of defense (Paragon)",["shield"],[feat([Power("Bracers of Defense",[],"daily","immediate interrupt",[Trigger("You are hit by a melee attack"),Effect("Reduce the damage dealt to you by the attack by 20.")],"","item")],"","")]),
       Property("bracers of defense (Epic)",["shield"],[feat([Power("Bracers of Defense",[],"daily","immediate interrupt",[Trigger("You are hit by a melee attack"),Effect("Reduce the damage dealt to you by the attack by 30.")],"","item")],"","")]),
       Property("bracers of mighty striking",["arm"],[feat([ft(["bracers of mighty striking #","basicmeleedamage"],["item",0])],"magic"),feat([ft(["and","basic attackdamage","meleedamage"],["item",0])],"magic"),feat([],"Bracers of Mighty Striking",["+",lambda x:x.statret("bracers of mighty striking #")," damage on a melee basic attack"])]),
       Property("bracers of the perfect shot",["arm"],[feat([ft(["bracers of the perfect shot #","basicrangeddamage"],["item",0])],"magic"),feat([ft(["and","basic attackdamage","rangeddamage"],["item",0])],"magic"),feat([],"Bracers of the Perfect Shot",["+",lambda x:x.statret("bracers of the perfect shot #")," damage on a ranged basic attack"])]),
       Property("dragondaunt shield (Paragon)",["shield"],[feat([Power("Dragondaunt Shield",[],"daily","immediate interrupt",[Trigger("You are hit by an area or close attack."),Effect("Reduce the damage dealt by the attack to you and each ally by 10.")],"","item")],"Dragondaunt Shield","Resist 5 to all attacks of dragons")],["off hand","arm"]),
       Property("dragondaunt shield (Epic)",["shield"],[feat([Power("Dragondaunt Shield",[],"daily","immediate interrupt",[Trigger("You are hit by an area or close attack."),Effect("Reduce the damage dealt by the attack to you and each ally by 15.")],"","item")],"Dragondaunt Shield","Resist 10 to all attacks of dragons")],["off hand","arm"]),
       Property("guardian shield (Heroic)",["shield"],[feat([Power("Guardian Shield",[],"daily","immediate interrupt",[Trigger("An adjacent ally is hit by an attack."),Effect("You are hit by the attack instead.  You then gain resistance to all damage equal to half the damage dealt by the attack (if any) until the start of your next turn.")],"","item")],"","")],["off hand","arm"]),
       Property("guardian shield (Paragon)",["shield"],[feat([Power("Guardian Shield",[],"daily","immediate interrupt",[Trigger("An ally within 5 squares of you is hit by an attack."),Effect("You are hit by the attack instead.  You then gain resistance to all damage equal to half the damage dealt by the attack (if any) until the start of your next turn.")],"","item")],"","")],["off hand","arm"]),
       Property("guardian shield (Epic)",["shield"],[feat([Power("Guardian Shield",[],"daily","immediate interrupt",[Trigger("An ally within 10 squares of you is hit by an attack."),Effect("You are hit by the attack instead.  You then gain resistance to all damage equal to half the damage dealt by the attack (if any) until the start of your next turn.")],"","item")],"","")],["off hand","arm"]),
       Property("sheild of defiance (Heroic)",["shield"],[feat([Power("Shield of Defiance",["healing"],"daily","immediate reaction",[Trigger("A critical hit is scored on you."),Effect("You can spend a healing surge")],"","item")])],["off hand","arm"]),
       Property("sheild of defiance (Paragon)",["shield"],[feat([Power("Shield of Defiance",["healing"],"daily","immediate reaction",[Trigger("A critical hit is scored on you."),Effect("You can spend a healing surge and regain an additional 2d6 hit points")],"","item")])],["off hand","arm"]),
       Property("sheild of defiance (Epic)",["shield"],[feat([Power("Shield of Defiance",["healing"],"daily","immediate reaction",[Trigger("A critical hit is scored on you."),Effect("You can spend a healing surge and regain an additional 4d6 hit points")],"","item")])],["off hand","arm"]),
       Property("shield of deflection (Paragon)",["shield"],[feat([],"Shield of Deflection","Resist 5 to damage from all ranged attacks")],["off hand","arm"]),
       Property("shield of deflection (Epic)",["shield"],[feat([],"Shield of Deflection","Resist 10 to damage from all ranged attacks")],["off hand","arm"]),
       Property("shield of protection (Heroic)",["shield"],[feat([Power("Shield of Protection",[],"daily","standard",[Effect("You and an adjacent ally gain resist 10 to all damage until the end of your next turn")],"","item")])],["off hand","arm"]),
       Property("shield of protection (Paragon)",["shield"],[feat([Power("Shield of Protection",[],"daily","standard",[Effect("You and an adjacent ally gain resist 15 to all damage until the end of your next turn")],"","item")])],["off hand","arm"]),
       Property("shield of protection (Epic)",["shield"],[feat([Power("Shield of Protection",[],"daily","standard",[Effect("You and an adjacent ally gain resist 20 to all damage until the end of your next turn")],"","item")])],["off hand","arm"]),
       Property("shield of warding (Paragon)",["shield"],[feat([Power("Shield of Warding",[],"daily","immediate interrupt",[Trigger("An adjacent ally is hit by an attack"),Effect("That ally gains resist 15 to any damage from the attack")],"","item")])],["off hand","arm"]),
       Property("shield of warding (Epic)",["shield"],[feat([Power("Shield of Warding",[],"daily","immediate interrupt",[Trigger("An adjacent ally is hit by an attack"),Effect("That ally gains resist 20 to any damage from the attack")],"","item")])],["off hand","arm"]),
#Feet slot properties
       Property("acrobat boots",["feet"],[feat([ft("acrobatics",["item",1]),Power("Acrobat Boots",[],"at-will","minor",[Effect("Stand up from prone")],"","item")],"Acrobat Boots","+1 item bonus to Acrobatics checks")]),
       Property("battlestrider greaves",["feet"],[feat([ft("speed",["item",CHECK("armortype","heavy")])],"Battlestrider Greaves","+1 item bonus to speed while wearing heavy armor")]),
       Property("boots of balance",["feet"],[feat([Power("Boots of Balance",[],"daily","free",[Effect("Reroll an Acrobatics check you just made.  Use the new results.")],"","item"),ft("acrobatics",["item",5])],"Boots of Balance","+5 item bonus to Acrobatics checks")]),
       Property("boots of the infinite stride",["feet"],[feat([Power("Boots of the Infinite Stride",["teleportation"],"daily","move",[Effect("Teleport up to 1 mile (line of sight and line of effect to the destination are required.)")],"","item"),ft("speed",["item",1])],"Boots of the Infinite Stride","+1 item bonus to speed")]),
       Property("boots of spider climbing",["feet"],[feat([Power("Boots of Spider Climbing",[],"daily","move",[Effect("On this move action, you move with a climb speed equal to your speed")],"","item")],"Boots of Spider Climbing","When you make an athletics check to climb, you can climb at your normal speed instead of one-half your speed.")]),
       Property("boots of striding",["feet"],[feat([ft("speed",["item",NOTCHECK("armortype","heavy")])],"Boots of Striding","+1 item bonus to speed when wearing light or no armor.")]),
       Property("boots of striding and springing",["feet"],[feat([ft("speed",["item",not(CHECK("armortype","heavy"))])],"Boots of Striding","+1 item bonus to speed when wearing light or no armor, and gain a +2 bonus to Athletics checks made to jump")]),
       Property("catstep boots",["feet"],[feat([Power("Catstep Boots",[],"daily","free",[Effect("Gain a +5 power bonus to your next Acrobatics or Athletics check.")],"","item")],"When you fall or jump down, you take only half normal falling damage and always land on your feet.")]),
       Property("dwarven greaves",["feet"],[feat([Power("Dwarven Greaves",[],"daily","immediate interrupt",[Trigger("You are hit by a power that has a pull, push, or slide effect"),Effect("You negate the forced movement.")],"","item")])]),
       Property("eladrin boots",["feet"],[feat([Power("Eladrin Boots",["teleportation"],"daily","move",[Effect(["Teleport up to ",lambda x:5+5*(x.check("checkrace","eladrin"))," squares."])],"","item")],"Eladrin Boots","Add 2 to the maximum range of any teleport you make (other than that provided by these boots)")]),
       Property("elven boots",["feet"],[feat([Power("Elven Boots",[],"encounter","minor",[Effect("Gain a +2 power bonus to speed and stealth checks until the end of your turn.")],"","item")])]),
       Property("wavestrider boots",["feet"],[feat([Power("Wavestrider Boots",[],"daily","minor",[Effect("You can move across liquid surfaces as if they were normal terrain until the end of the encounter.")],"","item")],"Wavestrider Boots","If you begin your turn standing on a solid surface, you can move across liquid as if it were normal terrain until the end of your turn.")]),
       Property("winged boots",["feet"],[feat([Power("Winged Boots",[],"daily","move",[Effect("Fly a number of squares equal to your speed.  At the end of your turn, you float down to the ground if you aren't already there.")],"","item")],"Winged Boots","You take no damage from a fall and always land on your feet.")]),
#Hand slot properties
       Property("burglar's gloves",["hands"],[feat([ft("thievery",["item",1])],"Burglar's Gloves","+1 item bonus to Thievery checks")]),
       Property("gauntlets of destruction",["hands"],[feat([],"Gauntlets of Destruction","When rolling damage on melee attacks, reroll 1's until the ycome up as something other than a 1")]),
       Property("gauntlets of ogre power",["hands"],[feat([Power("Gauntlets of Ogre Power",[],"daily","free",[Trigger("You hit with a melee attack"),Effect("Add a +5 power bonus to the damage roll.")],"","item"),ft("athletics",["item",1])],"Gauntlets of Ogre Power","+1 item bonus to Athletic checks and Strength ability checks")]),
       Property("gauntlets of the ram",["hands"],[feat([],"Gauntlets of the Ram","Add 1 to the distance of any push effect you create")]),
       Property("gloves of piercing",["hands"],[feat([Power("Gloves of Piercing",[],"daily","minor",[Effect("Until the end of the encounter, your attacks ignore any resistance of 10 or lower.")],"","item")])]),
       Property("guildmaster's gloves",["hands"],[feat([Power("Guildmaster's Gloves",[],"daily","minor",[Effect("Each time you make a thievery check during this encounter, roll twice and take the higher result")],"","item"),ft("thievery",["item",5])],"Guildmaster's Gloves","+5 item bonus to Thievery checks")]),
       Property("rogue's gloves",["hands"],[feat([Power("Rogue's Gloves",[],"daily","minor",[Effect("Each time you make a thievery check during this turn, roll twice and take the higher result")],"","item"),ft("thievery",["item",3])],"Rogue's Gloves","+3 item bonus to Thievery checks")]),
       Property("shadowfell gloves (Heroic)",["hands"],[feat([Power("Shadowfell Gloves",["necrotic"],"daily","minor",[Effect("Change the damage type dealt by the next arcane power you use to necrotic.  Add 1d6 to the damage dealt by that power (if any).")],"","item")])]),
       Property("shadowfell gloves (Paragon)",["hands"],[feat([Power("Shadowfell Gloves",["necrotic"],"daily","minor",[Effect("Change the damage type dealt by the next arcane power you use to necrotic.  Add 2d6 to the damage dealt by that power (if any).")],"","item")])]),
       Property("shadowfell gloves (Epic)",["hands"],[feat([Power("Shadowfell Gloves",["necrotic"],"daily","minor",[Effect("Change the damage type dealt by the next arcane power you use to necrotic.  Add 3d6 to the damage dealt by that power (if any).")],"","item")])]),
#Head slot properties
       Property("basilisk helm",["head"],[feat([Power("Basilisk Helm",[],"daily","immediate reaction",[Trigger("An enemy within 5 squares of you makes a melee or ranged attack against you"),Target("The trriggering enemy"),Effect("That enemy is immobilized (save ends).")],"","item")])]),
       Property("circlet of authority",["head"],[feat([ft(["diplomacy","intimidate"],["item",2])],"Circlet of Authority","+2 item bonus to Diplomacy and Intimidate checks.")]),
       Property("crown of command",["head"],[feat([ft(["diplomacy","intimidate"],["item",4]),Power("Crown of Command",[],"daily","free",[Trigger("You or an ally within 5 squares of you rolls a poor Diplomacy or Intimidate check"),Effect("You or the ally rerolls the check and uses the new result.")],"","item")],"Crown of Command","+4 item bonus to Diplomacy and Intimidate checks.")]),
       Property("diadem of acuity",["head"],[feat([ft(["insight","perception"],["item",2])],"Circlet of Authority","+2 item bonus to Insight and Perception checks.")]),
       Property("goggles of night",["head"],[feat([ft("vision","darkvision")],"Goggles of Night","Gain darkvision")]),
       Property("halo of fallen stars",["head"],[feat([ft(["heal","nature","religion"],["item",5]),Power("Halo of Fallen Stars",["radiant"],"daily","immediate interrupt",[Trigger("An enemy makes a melee attack or a ranged attack against you"),Effect(["That enemy takes ",dmg(CHAMOD,5,6)," and is blinded (save ends)."])],"","item")],"Halo of Fallen Stars","+5 item bonus to Heal, Nature, and Religion checks.")]),
       Property("helm of battle (heroic)",["head"],[feat([ft("initiative",["item",1])],"Helm of Battle","You and each ally within 5 squares of you gain a +1 item bonus to initiative checks.")]),
       Property("helm of battle (paragon)",["head"],[feat([ft("initiative",["item",2])],"Helm of Battle","You and each ally within 5 squares of you gain a +2 item bonus to initiative checks.")]),
       Property("helm of battle (epic)",["head"],[feat([ft("initiative",["item",3])],"Helm of Battle","You and each ally within 5 squares of you gain a +3 item bonus to initiative checks.")]),
       Property("helm of the eagle",["head"],[feat([ft("perception",["item",3]),Power("Helm of the Eagle",[],"daily","minor",[Effect("Gain a +2 power bonus to your next ranged attack roll this turn.")],"","item")],"Helm of the Eagle","+3 item bonus to Perception checks.")]),
       Property("helm of ghostly defense",["head"],[feat([Power("Helm of Ghostly Defense",[],"encounter","immediate interrupt",[Trigger("You are hit by an attack"),Effect("You become insubstantial until the start of your next turn.")],"","item")],"Helm of Ghostly Defense","Resist 10 necrotic")]),
       Property("helm of heroes (heroic)",["head"],[feat([Power("Helm of Heroes",[],"daily","free",[Trigger("You grant an ally a basic attack"),Effect("The ally can take a standard action instead.  The ally gains a +2 power bonus to any damage rolls made during that standard action.")],"","item")],"Helm of Heroes","You and each ally in 10 squares gain a +2 item bonus to saves vs. fear effects.")]),
       Property("helm of heroes (paragon)",["head"],[feat([Power("Helm of Heroes",[],"daily","free",[Trigger("You grant an ally a basic attack"),Effect("The ally can take a standard action instead.  The ally gains a +5 power bonus to any damage rolls made during that standard action.")],"","item")],"Helm of Heroes","You and each ally in 10 squares gain a +2 item bonus to saves vs. fear effects.")]),
       Property("helm of heroes (epic)",["head"],[feat([Power("Helm of Heroes",[],"daily","free",[Trigger("You grant an ally a basic attack"),Effect("The ally can take a standard action instead.  The ally gains a +10 power bonus to any damage rolls made during that standard action.")],"","item")],"Helm of Heroes","You and each ally in 10 squares gain a +5 item bonus to saves vs. fear effects.")]),
       Property("horned helm (heroic)",["head"],[feat([],"Horned Helm","Your charge attacks deal an extra 1d6 damage.")]),
       Property("horned helm (paragon)",["head"],[feat([],"Horned Helm","Your charge attacks deal an extra 2d6 damage.")]),
       Property("horned helm (epic)",["head"],[feat([],"Horned Helm","Your charge attacks deal an extra 3d6 damage.")]),
       Property("ioun stone of true sight",["head"],[feat([ft("vision","darkvision"),ft(["perception","insight"],["item",6]),Power("Ioun Stone of True Sight",[],"daily","minor",[Effect("You can see invisible creatures as if they were visible"),Sustain("minor","The power remains in effect.")],"","item")],"Ioun Stone of True Sight","Gain darkvision and a +6 item bonus to Insight and Perception cheks.")]),
       Property("iron of spite",["head"],[feat([ft(["arcana","intimidate"],["item",6])],"Iron of Spite","+6 item bonus to Arcana and Intimidate checks, and any enemy that hits you with a melee attack takes 1d10 necrotic damage.")]),
       Property("phoenix helm",["head"],[feat([ft(["perception"],["item",5]),Power("Phoenix Helm",["fire"],"daily","minor",[Effect("Gain a +2 power bonus to your next ranged attack roll this turn.  If that attack hits, it deals an extra 2d8 fire damage.")],"","item")],"Phoenix Helm","+5 item bonus to Perception checks.")]),
#Neck slot properties
       Property("amulet of false life",[1,"neck"],[feat([Power("Amulet of False Life",[],"daily","minor",[Requirement("You must be bloodied"),Effect("Gain temporary hit points equal to your healing surge value.")],"","item")])]),
       Property("amulet of health",[1,"neck"],[feat([ft("amulet of health #",("item",0))],"magic"),feat([],"Amulet of Health",["Gain resist ",lambda x:((x.statret("amulet of health #")+1)/2*5)," poison."])]),
       Property("cloak of feywild escape",[4,"neck"],[feat([Power("Cloak of Feywild Escape",[],"daily","move",[Target("one ally you can see"),Effect("You disappear from the world until the start of your next turn, at which point you appear in any unoccupied space within 5 squares of the chosen ally.")],"","item")])]),
       Property("cloak of invisibility",[5,"neck"],[feat([Power("Cloak of Invisibility",["illusion"],"daily","standard",[Effect("You become invisible until the end of the encounter or until you are hit by a melee attack or a ranged attack.")],"","item")])]),
       Property("cloak of resistance",[1,"neck"],[feat([ft("cloak of resistance #",("item",0))],"magic"),feat([Power("Cloak of Resistance",[],"daily","minor",[Effect(["Gain resist ",lambda x:((x.statret("cloak of resistance #")+1)/2*5)," to all damage until the start of your next turn."])],"","item")])]),
       Property("cloak of survival",[2,"neck"],[feat([ft(["cloak of survival #","endurance"],("item",0))],"magic"),feat([],"Cloak of Survival",["Gain a +",lambda x:x.statret("cloak of survival #")," item bonus to endurance checks.  Resist ",lambda x:((x.statret("cloak of survival #")+1)/2*5)," cold and resist ",lambda x:((x.statret("cloak of survival #")+1)/2*5)," fire."])]),
       Property("elven cloak",[2,"neck"],[feat([ft(["elven cloak #","stealth"],("item",0))],"magic"),feat([],"Elven Cloak",["Gain a +",lambda x:x.statret("elven cloak #")," item bonus to stealth checks."])]),
       Property("guardian's cape",[4,"neck"],[feat([Power("Guardian's Cape",["teleportation"],"daily","move",[Effect("Teleport to the space of an ally within 10 squares of you; that ally simultaneously teleports to your original space.  You need not have line of sight or line of effect to the ally's space.")],"","item")])]),
       Property("periapt of wisdom",[3,"neck"],[feat([ft(["periapt of wisdom #"],("item",0))],"magic"),feat([ft(["dungeoneering","heal","insight","nature","perception"],("item",lambda x:((x.statret("periapt of wisdom #")-1)/2))),Power("Periapt of Wisdom",[],"daily","immediate interrupt",[Trigger("You are hit by an attack that targets your Will defense."),Effect("Gain a +5 power bonus to Will against the attack.")],"","item")],"Periapt of Wisdom",["Gain a +",lambda x:((x.statret("periapt of wisdom #")-1)/2)," item bonus to wisdom checks and wisdom-based skill checks."])]),
       Property("safewing amulet",[1,"neck"],[feat([ft(["safewing amulet #"],("item",0))],"magic"),feat([],"Safewing Amulet",["When falling, reduce distance of fall by ",lambda x:x.statret("safewing amulet #"),"0 feet for purpose of calculating damage.  Always land on your feet."])]),
       Property("scarab of invulnerability",[6,"neck"],[feat([Power("Scarab of Invulnerability",[],"daily","minor",[Effect("You have immunity to damage until the end of your next turn.")],"","item")])]),
       Property("stormwalker's cloak",[3,"neck"],[feat([ft(["stormwalker's cloak #"],("item",0))],"magic"),feat([Power("Stormwalker's Cloak",["lightning","thunder"],"daily","minor",[Effect(["Until the end of your next turn, each time you are hit by a melee attack the attacker takes ",dmg(0,lambda x:x.statret("stormwalker's cloak #"),6,["lightning"])," or ",dmg(0,lambda x:x.statret("stormwalker's cloak #"),6,["thunder"])," (your choice)."])],"","item")],"Stormwalker's Cloak",["Gain resist ",lambda x:((x.statret("stormwalker's cloak #")+1)/2*5)," lightning and resist ",lambda x:((x.statret("stormwalker's cloak #")+1)/2*5)," thunder."])]),
#Ring slot properties
       Property("iron ring of the dwarf lords",["ring"],[feat([ft("surges",("",1)),Power("Iron Ring of the Dwarf Lords",[],"daily","immediate interrupt",[Trigger("You are hit by a power that has a pull, push, or slide effect."),Effect("You negate the forced movement."),Line("If you've reached at least one milestone today, you also gain immunity to pull, push, and slide effects (unless you are willing to be moved) until the end of your next turn.")],"","item")],"Iron Ring of the Dwarf Lords","Gain one healing surge")]),
       Property("ring of flight",["ring"],[feat([Power("Ring of Flight",[],"daily","minor",[Effect("Gain a fly speed equal to your speed until the end of your next turn."),Line("If you've reached at least one milestone today, this lasts until the end of your next turn instead")],"","item")],"Ring of Flight","You take no damage from a fall and always land on your feet")]),
       Property("ring of freedom of movement",["ring"],[feat([ft("acrobatics",("item",2)),Power("Ring of Freedom of Movement",[],"daily","minor",[Effect("Until the end of the encounter, gain a +5 power bonus to checks made to escape a grab and a +5 power bonus to saving throws to end the immobilized, restrained, or slowed conditions."),Line("If you've reached at least one milestone today, you can also move across difficult terrain as if it were normal until the end of the encounter.")],"","item")],"Ring of Freedom of Movement","Gain a +2 item bonus to Acrobatics checks")]),
       Property("ring of invisibility",["ring"],[feat([ft("stealth",("item",2)),Power("Ring of Invisibility",["illusion"],"daily","standard",[Effect("Become invisibile until the end of your next turn."),Line("If you've reached at least one milestone today, using this power only requires a minor action.")],"","item")],"Ring of Invisibility","Gain a +2 item bonus to Stealth checks")]),
       Property("ring of protection",["ring"],[feat([Power("Ring of Protection",[],"daily","immediate interrupt",[Trigger("You are hit by an attack."),Effect("Gain a +2 power bonus to a single defense score against that attack."),Line("If you've reached at least one milestone today, this bonus lasts until the start of your next turn instead.")],"","item")],"Ring of Protection","Gain a +1 item bonus to saving throws")]),
       Property("ring of regeneration",["ring"],[feat([ft("surge",("item",3)),Power("Ring of Regeneration",["healing"],"daily","standard",[Effect("Regain one healing surge you've already used today."),Line("If you've reached at least one milestone today, you also gain regeneration 10 until the end of the encounter or until you spend a healing surge.")],"","item")],"Ring of Regeneration","Gain a +3 item bonus to your healing surge value")]),
       Property("ring of true seeing",["ring"],[feat([ft("perception",("item",2)),Power("Ring of True Seeing",[],"daily","minor",[Effect("Until the end of your turn, you can see invisible creatures as if they were visible.  You also ignore the attack penalty for concealment or total concealment."),Line("If you've reached at least one milestone today, this lats until the end of your next turn instead.")],"","item")],"Ring of True Seeing","Gain a +2 item bonus to Perception checks")]),
       Property("ring of wizardry",["ring"],[feat([ft("arcana",("item",3)),Power("Ring of Wizardry",[],"daily","minor",[Effect("Regain the use of an arcane encounter utility power that you've already used (as if you hadn't used it this encounter)."),Line("If you've reached at least one milestone today, you can instead regain the use of an arcane encounter attack power.")],"","item")],"Ring of Wizardry","Gain a +3 item bonus to Arcana checks")]),
       Property("star opal ring",["ring"],[feat([ft("speed",("item",1)),Power("Star Opal Ring",["radiant","teleportation"],"daily","move",[Effect("Teleport up to 10 squares."),Line("If you've reached at least one milestone today, a brillian explosion bursts from your starting square after you complete the teleport."),Target("all creatures in burst",("close burst",3)),Atk([CHAMOD,5],"reflex",damage([4,8],[CHAMOD])),Miss()],"","item")],"Star Opal Ring","Gain a +1 item bonus to speed")]),
#Waist slot properties
       Property("belt of giant strength",["waist"],[feat([ft("athletics",("item",2)),Power("belt of giant strength",[],"daily","free",[Trigger("You hit with a melee attack."),Effect("Add a +10 power bonus to the damage roll.")],"","item")],"Belt of Giant Strength","Gain a +2 item bonus to Athletics checks and Strength ability checks")]),
       Property("belt of sacrifice (heroic)",["waist"],[feat([Power("Belt of Sacrifice",["healing"],"daily","minor",[Effect("Lose two healing surges.  An ally within 5 squares of you regains one healing surge.")],"","item")],"Belt of Sacrifice","Each ally within 5 squares of you gains a +1 item bonus to his or her healing surge value.")]),
       Property("belt of sacrifice (paragon)",["waist"],[feat([Power("Belt of Sacrifice",["healing"],"daily","minor",[Effect("Lose two healing surges.  An ally within 5 squares of you regains one healing surge.")],"","item")],"Belt of Sacrifice","Each ally within 5 squares of you gains a +2 item bonus to his or her healing surge value.")]),
       Property("belt of sacrifice (epic)",["waist"],[feat([Power("Belt of Sacrifice",["healing"],"daily","minor",[Effect("Lose two healing surges.  An ally within 5 squares of you regains one healing surge.")],"","item")],"Belt of Sacrifice","Each ally within 5 squares of you gains a +3 item bonus to his or her healing surge value.")]),
       Property("belt of titan strength",["waist"],[feat([ft("athletics",("item",3)),Power("belt of titan strength",[],"daily","free",[Effect("Gain a +10 power bonus to all melee damage rolls until the start of your next turn.")],"","item")],"Belt of Titan Strength","Gain a +3 item bonus to Athletics checks and Strength ability checks")]),
       Property("belt of vigor (heroic)",["waist"],[feat([ft("surge",("item",1))],"Belt of Vigor","Gain a +1 item bonus to your healing surge value")]),
       Property("belt of vigor (paragon)",["waist"],[feat([ft("surge",("item",2))],"Belt of Vigor","Gain a +2 item bonus to your healing surge value")]),
       Property("belt of vigor (epic)",["waist"],[feat([ft("surge",("item",3))],"Belt of Vigor","Gain a +3 item bonus to your healing surge value")]),
       Property("dynamic belt (heroic)",["waist"],[feat([ft(["acrobatics","athletics"],("item",2)),Power("Dynamic Belt",[],"daily","free",[Effect("Reroll an Acrobatics check or an Athletics check you just rolled.  Use the new result.")],"","item")],"Dynamic Belt","Gain a +2 item bonus to Acrobatics checks and Athletics checks")]),
       Property("dynamic belt (paragon)",["waist"],[feat([ft(["acrobatics","athletics"],("item",4)),Power("Dynamic Belt",[],"daily","free",[Effect("Reroll an Acrobatics check or an Athletics check you just rolled.  Use the new result.")],"","item")],"Dynamic Belt","Gain a +4 item bonus to Acrobatics checks and Athletics checks")]),
       Property("dynamic belt (epic)",["waist"],[feat([ft(["acrobatics","athletics"],("item",6)),Power("Dynamic Belt",[],"daily","free",[Effect("Reroll an Acrobatics check or an Athletics check you just rolled.  Use the new result.")],"","item")],"Dynamic Belt","Gain a +6 item bonus to Acrobatics checks and Athletics checks")]),
       Property("ironskin belt (heroic)",["waist"],[feat([Power("Ironskin Belt",[],"daily","minor",[Effect("Gain resist 5 to all weapon damage until the end of your next turn.")],"","item")])]),
       Property("ironskin belt (paragon)",["waist"],[feat([Power("Ironskin Belt",[],"daily","minor",[Effect("Gain resist 10 to all weapon damage until the end of your next turn.")],"","item")])]),
       Property("ironskin belt (epic)",["waist"],[feat([Power("Ironskin Belt",[],"daily","minor",[Effect("Gain resist 15 to all weapon damage until the end of your next turn.")],"","item")])]),
]

def AdvVaultproperties():
    return [
#Armor properties
       Property("chaos weave #",[3,"armor"],[feat([ft("chaos weave #",("item",0))],"magic"),feat([Power("Chaos Weave Armor",[],"daily","immediate interrupt",[Trigger("You are hit by an attack that deals acid, cold, fire, lightning, or thunder damage."),Effect(["Gain resist ",lambda x:((x.statret("chaos weave #")-1)/2)*10," against that damage type until the end of the encounter."])],"","item")])]),
       Property("# of cleansing",[1,"armor"],[feat([],"Armor of Cleansing","Add a +2 item bonus to your saving throws against ongoing damage.")]),
       Property("pelaurum #",[1,"chainmail","scale","plate"],[feat([ft("pelaurum #",("item",0))],"magic"),feat([],"Pelaurum Armor",["Resist ",lambda x:((x.statret("pelaurum #")+1)/2)*5," fire and resist ",lambda x:((x.statret("pelaurum #")+1)/2)*5," radiant"])]),
       Property("versatile #",[1,"chainmail","plate"],[feat([Power("Versatile Armor",[],"at-will","minor",[Effect("You take a -1 penalty to AC but ignore penalties to speed and checks caused by this armor.  This persists until you use a minor action to return the armor to normal.")],"","item")])]),
       Property("shared suffering #",[1,"armor"],[feat([Power("Shared Suffering Armor",[],"encounter","immediate reaction",[Trigger("An attack gives you ongoing damage"),Effect("The attacker gains an equal amount of untyped ongoing damage.")],"","item")])]),
       Property("shimmering #",[1,"cloth"],[feat([],"shimmering armor","You do not provoke opportunity attacks when you make ranged or area attacks")]),
       Property("stormlord #",[3,"chainmail","scale","plate"],[feat([ft("stormlord #",("item",0))],"magic"),feat([Power("Shared Suffering Armor",[],"daily","immediate interrupt",[Trigger("An ally within 10 squares of you takes lightning and/or thunder damage from an attack"),Effect("The attack hits you instead, and you gain a +2 power bonus to attack rolls until the end of your next turn.")],"","item")],"Stormlord Armor",["Resist ",lambda x:((x.statret("stormlord #")+1)/2)*5," lightning and resist ",lambda x:((x.statret("stormlord #")+1)/2)*5," thunder."])]),
#Weapon Properties
       Property("battlecrazed #",[1,"axe","heavy blade"],[feat([ft("battlecrazed #",["item",0])],"magic"),feat([Power("Battlecrazed Weapon",[],"daily","minor",[Effect(["Deal",lambda x:x.statret("level")/2," damage to yourself, ignoring all resistances.  You are considered bloodied for all purposes (including beneficial effects, such as Dragonborn Fury) until the end of your next turn."])],"","item")],"Battlecrazed Weapon",["While you are bloodied, you dead +",lambda x:(x.statret("battlecrazed #")+1)/2,"d6 damage when you hit with this weapon."])]),
#Implement properties
       Property("symbol of divine reach",[1,"holy symbol"],[feat([ft(["symbol of divine reach #","divineranged","divinearea","divinearea burst"],["",0])],"magic"),feat([],"Symbol of Divine Reach",["Add ",lambda x:x.statret("symbol of divine reach #")," to the range of all ranged or area prayers using this implement."])]),
       Property("orb of debilitating languor",[1,"orb"],[feat([Power("Orb of Debilitating Languor",[],"daily","free",[Trigger("An attack with this orb hits the target's Fortitude defense."),Effect("The target is slowed (save ends).")],"","item")])]),
       Property("orb of insurmountable force",[1,"orb"],[feat([ft("orb of insurmountable force #",["",0])],"magic"),feat([Power("Orb of Insurmountable Force",[],"encounter","free",[Trigger("You use an arcane attack power with this orb."),Effect(["If the attack is successful, you can pus the target ",lambda x:x.statret("orb of insurmountable force #")," squares."])],"","item")])]),
       Property("rod of the infernal",[2,"rod"],[feat([ft(["rod of the infernal #","infernalpact"],["",0])],"magic"),feat([Power("Rod of the Infernal",[],"encounter","minor",[Effect(["Gain ",lambda x:x.statret("level")+x.statret("intmod")," temporary hit points."])],"","item")],"Rod of the Infernal",["When you trigger your infernal pact boon, you gain ",lambda x:x.statret("rod of the infernal #")," additional temporary hit points."])]),
       Property("vicious rod",[1,"rod"],[feat([],"Vicious Rod","When you deal your Warlock's Curse damage with this rod, you roll d8's instead of d6's")]),
       Property("staff of ruin",[1,"staff"],[feat([ft(["staff of ruin #","implementdamage"],["",0])],"magic"),feat([],"Staff of Ruin",["When you make an attack with this staff, add a +", lambda x:x.statret("staff of ruin #")," item bonus to damage rolls."])]),
#Arm slot properties
       Property("feyleaf vambraces",["arm"],[feat([Power("Feyleaf Vambraces",["teleportation"],"daily","free",[Trigger("You are about to make an attack roll an adjacent target."),Effect("Teleport to the nearest square from which you and an ally flank the target.")],"","item")])]),
       Property("razor bracers (heroic)",["arm"],[feat([],"Razor Bracers",["+2 item bonus to escape a grab.  When a creature grabs you, it takes 1d10 damage."])]),
       Property("razor bracers (paragon)",["arm"],[feat([],"Razor Bracers",["+2 item bonus to escape a grab.  When a creature grabs you, it takes 2d10 damage."])]),
       Property("razor bracers (epic)",["arm"],[feat([],"Razor Bracers",["+2 item bonus to escape a grab.  When a creature grabs you, it takes 3d10 damage."])]),
#Feet slot properties
       Property("acrobat boots",["feet"],[feat([ft("acrobatics",["item",1]),Power("Acrobat Boots",[],"at-will","minor",[Effect("Stand up from prone")],"","item")],"Acrobat Boots","+1 item bonus to Acrobatics checks")]),
       Property("goblin stompers",["feet"],[feat([Power("Goblin Stompers",[],"encounter","immediate reaction",[Trigger("A melee attack misses you."),Effect("Shift 1 square")],"","item")])]),
        Property("zephyr boots",["feet"],[feat([],"Zephyr Boots","Gain a fly speed equal to your speed while wearing light armor or no armor")]),
#Hands slot properties
       Property("antipathy gloves",["hands"],[feat([Power("Antipathy Gloves",[],"daily","standard",[Target("one creature",("ranged",10)),Atk([13,lambda x:x.statret("level")/-2],"reflex", None),Hit("The target is restrained (save ends).")],"","item")],"Antipathy Gloves","An enemy must spend 1 extra square of movement to move into a square adjacent to you.")]),
#Head slot properties
       Property("circlet of second chances",["head"],[feat([Power("Circlet of Second Chances",[],"daily","no",[Trigger("You fail a saving throw"),Effect("Reroll the saving throw, using the second result even if it's lower.")],"","item")])]),
       Property("eagle eye goggles",["head"],[feat([ft("basicrangedattack",("item",1)),ft(["and","basic attackattack","rangedattack"],("item",1))],"Eagle Eye Goggles","+1 attack on a ranged basic attack")]),
#Neck slot properties
       Property("brooch of shielding",[1,"neck"],[feat([ft("brooch of shielding #",["item",0])],"magic"),feat([Power("Brooch of Shielding",[],"daily","immediate interrupt",[Trigger("You are hit by an area, close, or ranged attack"),Effect(["Gain resist ",lambda x:((x.statret("brooch of shielding")+3)/2)*5," to all damage against that attack."])],"","item")],"Brooch of Shielding",["Resist ",lambda x:((x.statret("brooch of shielding #")+3)/2)*5," force"])]),
       Property("cloak of displacement",[3,"neck"],[feat([Power("Cloak of Displacement",["teleportation"],"daily","immediate reaction",[Effect(["Use this power when you would be hit by a melee or ranged attack.  The attacker must reroll the attack, using the second result even if it's lower.  If the attacker misses you, you can teleport 1 square."])],"","item")],"Cloak of Displacement","Each encounter, you gain a +2 item bonus to AC and Reflex defenses until an attack hits you.")]),
       Property("healer's brooch",[1,"neck"],[feat([ft(["healer's brooch #","healing"],["",0])],"magic"),feat([],"Healer's Brooch",["When you heal yourself or an ally, add ",lambda x:x.statret("healer's brooch #")," to the hit points gained."])]),
       Property("torc of power preservation",[3,"neck"],[feat([ft(["torc of power preservation #"],["",0])],"magic"),feat([Power("Torc of Power Preservation",[],"daily","free",[Trigger(["You use a level ",lambda x:x.statret("torc of power preservation #")*5," or lower encounter power."]),Effect(["Roll 1d20+",lambda x:x.statret("torc of power preservation #"),".  If the result is 10 or higher, that power renews as if you had taken a short rest.  If the result is lower than 10, you don't expend the use of this power and no daily use of a magic item power occurs."])],"","item")])]),
#Ring slot properties
       Property("ring of feather fall",["ring"],[feat([Power("Ring of Feather Fall",[],"daily","minor",[Effect("Allies within 5 squares of you also benefit from this ring's property until the end of the encounter."),Line("If you've reached at least one milestone today, allies within 10 squares of you also benefit.")],"","item")],"Ring of Feather Fall","You take no damage from a fall and always land on your feet")]),
       Property("war ring",["ring"],[feat([Power("War Ring",[],"daily","free",[Trigger("You score a critical hit with a weapon or implement"),Effect("Add 2 extra dice of critical hit damage based on the weapon or implement.  If your weapon or implement deals no extra damage when you score a critical hit, deal an extra 2d6 damage when you score a critical hit."),Line("If you've reached at least one milestone today, instead of rolling the extra dice of critical hit damage, deal extra damage equal to the maximum value of those dice.")],"","item")],"War Ring","Deal 1 extra die of critical hit damage, either 1d6 or based on the weapon or implement you wield")]),
       ]
def AdvVault2properties():
    return [
#Armor slot properties
        Property("marauder's #",[2, "leather","hide"],[feat([ft("marauder's armor #",["",0])],"magic"),feat([Power("Marauder's Armor",["healing"],"daily","free",[Trigger("You hit with a charge attack."),Effect(["You make a saving throw with a +",lambda x:x.statret("marauder's armor #")," bonus, or you spend a healing surge and regain ",lambda x:x.statret("marauder's armor #")," additional hit points."])],"","item")],"Marauder's Armor",["When you charge, you gain a +",lambda x:(x.statret("marauder's armor #")+1)/2," bonus to AC until the end of your next turn."])]),
        Property("shadow warlock #",[2, "leather"],[feat([],"Shadow Warlock Armor","While you have concealment from Shadow Walk, any creature effected by your curse grants combat advantage to you")]),
#Weapon slot properties
       Property("battle spirit #",[3,"axe","flail","hammer","heavy blade","mace","spear"],[feat([],"Battle Spirit Weapon","While charging, you are insubstantial and can move through enemy's squares.  You still provoke opportunity attacks as normal.")]),
#Arm slot properties
        Property("ankhmon's bracers",["arm"],[feat([],"Ankhmon's Bracers","When you hit an enemy with and arcane power and combat advantage, deal 1d10 extra damage and regain that many hit points")]),
#Neck slot properties
        Property("timeless locket",[3, "neck"],[feat([ft(["timeless locket #", "initiative"],["item",0])],"magic"),feat([],"Timeless Locket",["Gain a +",lambda x:x.statret("timeless locket #")," bonus to initiative checks"])])

        ]
    addProperties(properties)
addProperties(PHBproperties())
addProperties(AdvVaultproperties())
addProperties(AdvVault2properties())
#

def finditem(string, GearCheck=EquipmentLists):
    for gear in GearCheck.values():
        if isinstance(gear, dict):
            z=finditem(string, gear)
            if z!=None: return z
        if isinstance(gear, Item):
            if gear.name()==string: return gear
        if isinstance(gear, Weapon):
            if gear.name==string: return gear

weaponProf={}
for key in weaponList.keys(): weaponProf[key]=feat([ft("proficiency",key)],"Weapon Proficiency: "+key.capitalize(),"Proficient with "+key)
weaponFocus={}
weaponExpertise={}
implementExpertise={}
weaponFocus=weaponFocus.fromkeys(["axe","bow","crossbow","flail","hammer","heavy blade","light blade","mace","pick","polearm","sling","spear","staff","unarmed"])
for key in weaponFocus.keys(): weaponFocus[key]=feat([ft(key+"damage",["feat",raising(1,10)])],key)
for key in weaponFocus.keys(): weaponExpertise[key]=feat([ft(key+"attack",["feat",raiselist(1,[15,25])])],key)
for key in implements: implementExpertise[key]=feat([ft(key+"attack",["feat",raiselist(1,[15,25])])],key)

militaryMelee=feat([ft("proficiency",[])],"Military Melee Proficiency","Proficient with all military melee weapons")
militaryRanged=feat([ft("proficiency",[])],"Military Ranged Proficiency","Proficient with all military ranged weapons")
simpleMelee=feat([ft("proficiency",[])],"Simple Melee Proficiency","Proficient with all simple melee weapons")
simpleRanged=feat([ft("proficiency",[])],"Simple Ranged Proficiency","Proficient with all simple ranged weapons")

for weapon in weaponList.values():
	if "military" in weapon.keys: 
		if "melee" in weapon.keys: militaryMelee.what()[0].resolve.append(weapon.name)
		if "ranged" in weapon.keys: militaryRanged.what()[0].resolve.append(weapon.name)
	if "simple" in weapon.keys: 
		if "melee" in weapon.keys: simpleMelee.what()[0].resolve.append(weapon.name)
		if "ranged" in weapon.keys: simpleRanged.what()[0].resolve.append(weapon.name)
	if "improvised" in weapon.keys:
		weaponProf.pop(weapon.name)

def weaponKeyList(key):
    ret=[]
    for weapon in weaponList.values():
        if isinstance(key, list):
            x=True
            for oneKey in key:
                if not(oneKey in weapon.keys) and not(oneKey in weapon.group): x=False
            if x: ret+=[weapon.name]
        else: 
            if (key in weapon.keys) or (key in weapon.group): ret+=[weapon.name]
    return ret

def humanInit(character): 
	character.addFeat(feat([ft(character.menu("(Human) Pick a stat to increase by 2:",["Str","Con","Dex","Int","Wis","Cha"])[0].lower(),["",2])]))

featPowers={"Angharradh's Favor":Power("Channel Divinity: Angharradh's Favor",["divine"],"encounter","no"
           ,[Trigger("You or an ally within range succeeds on a saving throw")
           ,Target("one ally",("ranged",10))
           ,Effect("The ally gains a +4 power bonus to saving throws until the end of his or her next turn")],"feat","channel divinity")
            ,"Armor of Bahamut":Power("Channel Divinity: Armor of Bahamut",["divine"],"encounter","immediate"
           ,[Trigger("An enemy scores a critical hit on your ally",("Ranged",5))
           ,Effect("Turn a critical hit against you or an ally within range into a normal hit")],"feat","channel divinity")
        ,"Avandra's Rescue":Power("Channel Divinity: Avandra's Rescue",["divine"],"encounter","move"
           ,[Target("one ally")
             ,Effect("Shift into the space of an adjacent ally; that ally simultaneously shifts into your space.  Your space and the ally's space must be the same size.")],"feat","channel divinity")
        ,"Berronar's Salve":Power("Channel Divinity: Berronar's Salve",["divine","healing"],"encounter","immediate reaction"
           ,[Trigger("An ally drops to 0 hit points or fewer")
           ,Trigger("the triggering ally",("ranged",10))
           ,Effect("The target can immediately spend a healing surge")],"feat","channel divinity")
        ,"Blessing of Silvanus":Power("Channel Divinity: Blessing of Silvanus",["divine","healing"],"encounter","immediate reaction"
           ,[Trigger("An ally within 5 squares spends a healing surge")
           ,Trigger("the triggering ally",("close burst",5))
           ,Effect(["The target heals ",choosestat("channel divinity: blessing of silvanus",["int","wis","cha"])," damage"])],"feat","channel divinity")
        ,"Chauntea's Blessing":Power("Channel Divinity: Chauntea's Blessing",["divine"],"encounter","no"
           ,[Trigger("An ally within 10 squares fails a saving throw")
           ,Trigger("the triggering ally",("close burst",10))
           ,Effect("The target rerolls the failed saving throw with a +4 power bonus")],"feat","channel divinity")
        ,"Corellon's Grace":Power("Channel Divinity: Corellon's Grace",["divine"],"encounter","immediate"
           ,[Trigger("Another creature within range spends an action point to take an extra action",("Ranged",10))
           ,Effect("You take a move action")],"feat","channel divinity")
        ,"Eyes of Selune":Power("Channel Divinity: Eyes of Selune",["divine"],"encounter","no"
           ,[Trigger("You fail a saving throw")
           ,Effect("You can immediately reroll the saving throw you just failed")],"feat","channel divinity")
        ,"Fleetness of Mielikki":Power("Channel Divinity: Fleetness of Mielikki",["divine"],"encounter","minor"
           ,[Effect("You gain a +2 power bonus to speed and ignore difficult terrain until the end of your next turn")],"feat","channel divinity")
        ,"Glittergold's Gambit":Power("Channel Divinity: Glittergold's Gambit",["divine"],"encounter","immediate interrupt"
           ,[Trigger("An ally in burst makes an attack roll or skill check",("close burst",10))
           ,Effect("The target immediately rerolls the attack roll or skill check he or she just made, but must keep the second result, even if it is worse.")],"feat","channel divinity")
        ,"Gond's Craft":Power("Channel Divinity: Gond's Craft",["divine"],"encounter","minor"
           ,[Effect("You gain a +2 power bonus to any one attack roll made with a magic item power until the end of your next turn")],"feat","channel divinity")
        ,"Harmony of Erathis":Power("Channel Divinity: Harmony of Erathis",["divine"],"encounter","minor"
           ,[Target("one ally",("ranged",10))
             ,Effect("If you have at least three allies within range, grant one of those allies a +2 power bonus to the first attack roll he or she makes before the start of your next turn")],"feat","channel divinity")
        ,"Ilmater's Martyrdom":Power("Channel Divinity: Ilmater's Martyrdom",["divine","healing"],"encounter","immediate reaction"
           ,[Trigger("An ally in burst is damage by a critical hit"),
             Target("the ally in burst damage by a critical hit",("close burst",10)),
             Effect("The target can immediately gain one healing surge and immediately spend it.  You lose one healing surge.")],"feat","channel divinity")
        ,"Ioun's Poise":Power("Channel Divinity: Ioun's Poise",["divine"],"encounter","minor"
           ,[Target("You or one ally",("ranged",5))
             ,Effect("The target gains a +5 bonus to Will defense until the start of your next turn")],"feat","channel divinity")
        ,"Kord's Favor":Power("Channel Divinity: Kord's Favor",["divine"],"encounter","free"
           ,[Trigger("You or an ally within range scores a critical hit with a melee attack",("Ranged",5)),
             Effect("You or the ally can spend a healing surge")],"feat","channel divinity")
        ,"Kelemvor's Judgement":Power("Channel Divinity: Kelemvor's Judgement",["divine","radiant"],"encounter","standard"
           ,[Target("Each creature in burst",("close blast",raiselist(1,[1,1,1,1,11,11,11,21,21]))),Atk([choosestat("channel divinity: kelemvor's judgement",["int","wis","cha"])],"will", damage([raiselist(1,[5,11,15,21,25]),12],[choosestat("channel divinity: kelemvor's judgement",["int","wis","cha"],False)]))
             ,Miss("Half Damage")],"feat","channel divinity")
        ,"Melora's Tide":Power("Channel Divinity: Melora's Tide",["divine","healing"],"encounter","minor"
           ,[Target("You or one ally; bloodied target only",("ranged",5))
             ,Effect(["Effect: The target gains regeneration ",raising(2,10)," until the end of the encounter or until he/she is no longer bloodied"])],"feat","channel divinity")
        ,"Moradin's Resolve":Power("Channel Divinity: Moradin's Resolve",["divine"],"encounter","minor"
           ,[Effect("Effect: Until the end of your next turn, you gain a +2 bonus to attack rolls against large or larger creatures")],"feat","channel divinity")
        ,"Oghma's Recall":Power("Channel Divinity: Oghma's Recall",["divine"],"encounter","minor"
           ,[Effect("Until the end of your next turn, you gain a +10 power bonus to all knowledge checks (made with the knowledge skills: Arcana, Dungeoneering, History, Nature, or Religion).")],"feat","channel divinity")
        ,"Pelor's Radiance":Power("Channel Divinity: Pelor's Radiance",["divine","implement","radiant"],"encounter","standard"
           ,[Target("Each undead creature in burst",("close burst",1)),Atk([WISMOD],"will",damage([raiselist(1,[5,11,15,21,25]),12],[WISMOD]))
             ,Hit("The target is stunned until the end of your next turn")],"feat","channel divinity")
        ,"Power of Amaunator":Power("Channel Divinity: Power of Amaunator",["divine","radiant"],"encounter","free"
           ,[Trigger("You hit an enemy with a power with the radiant keyword"),
             Effect("Your power deals an extra 1d10 radiant damage to all targets hit by the power used")],"feat","channel divinity")
        ,"Raven Queen's Blessing":Power("Channel Divinity: Raven Queen's Blessing",["divine","healing"],"encounter","free"
           ,[Trigger("Your attack drops an enemy within range to 0 hit points or fewer",("Ranged",10))
            ,Effect("You or an ally within 5 squares of the enemy can spend a healing surge")],"feat","channel divinity")
        ,"Sehanine's Reversal":Power("Channel Divinity: Sehanine's Reversal",["divine"],"encounter","no"
           ,[Trigger("You roll a natural 20 on a saving throw",("Ranged",5))
            ,Effect("Choose an enemy within range.  That creature gains the condition you just saved against")],"feat","channel divinity")
        ,"Righteous Rage of Tempus":Power("Channel Divinity: Righteous Rage of Tempus",["divine"],"encounter","minor"
           ,[Effect("If you hit with the next weapon attack that you make before the end of your next turn and it isn't a critical hit, you roll the extra damage dice that you would roll if you scored a critical hit and deal the result as extra damage.  If the attack is a critical hit, its extra damage is maximized.")],"feat","channel divinity")
        ,"Sheela Peryroyl's Gift":Power("Channel Divinity: Sheela Peryroyl's Gift",["divine"],"encounter","minor"
           ,[Target("you or one ally in burst",("close burst",10)),Effect("The target immediately rolls a saving throw")],"feat","channel divinity")
        ,"Sune's Touch":Power("Channel Divinity: Sune's Touch",["divine"],"encounter","minor"
           ,[Target("one ally in burst",("close burst",1)),Effect("The target gains a +2 power bonus to his or her next attack roll or skill check made before the end of your next turn")],"feat","channel divinity")
        ,"Torm's Justice":Power("Channel Divinity: Torm's Justice",["divine"],"encounter","minor"
           ,[Effect("You gain a +2 power bonus to attack rolls against bloodied enemies until the end of your next turn")],"feat","channel divinity")
        ,"Tymora's Coin":Power("Channel Divinity: Tymora's Coin",["divine"],"encounter","no"
           ,[Trigger("You roll a natural 1 or natural 20 on a saving throw")
            ,Effect("Once before the end of your next turn, you can roll d20 twice for an attack roll or saving throw and use whichever d20 result you prefer")],"feat","channel divinity")
        ,"Waukeen's Silver Tongue":Power("Channel Divinity: Waukeen's Silver Tongue",["divine"],"encounter","immediate interrupt"
           ,[Target("one ally in burst",("close burst",10)),Effect("The target rerolls a Bluff, Diplomacy, or Intimidate check he just rolled, with a +5 power bonus.  He uses the new result, even if it is lower than the original result.")],"feat","channel divinity")

}	

def groupProf(keys, notlegal=["improvised"]):
    ret=[]
    for wpn in weaponList.values():
        test1=True
        test2=True
        for key in keys:
            if (key not in wpn.group) and (key not in wpn.keys): test1=False
        for x in notlegal:
            if x in wpn.keys: test2=False
        if test1 and test2: ret+=[wpn.name]
    return [feat([ft("proficiency",ret)])]

def groupList(keys, notlegal=["improvised"]):
    ret=[]
    for wpn in weaponList.values():
        test1=True
        test2=True
        for key in keys:
            if (key not in wpn.group) and (key not in wpn.keys): test1=False
        for x in notlegal:
            if x in wpn.keys: test2=False
        if test1 and test2: ret+=[wpn.name]
    return ret

specMenus={}

specMenus["implementMastery"]=specialMenu([["Orb: 1/encounter use missed attack against enemy you didn't target, with a +",CHAMOD," bonus to the roll"],["Orb: Either -",lambda x:x.mod("wis")," to targets next save vs. your spell, or increase duration of an at-will power"],["Staff: +1 to AC when wielding a staff, 1/encounter ",plus(lambda x:x.mod("con"),1)," to defense against one attack"],["Tome: 1/encounter all creatures summoned by one power gain a +",CONMOD," bonus to damage rolls."],"Tome: 1/encounter use stored encounter power by expending encounter power of its level or higher",["Wand: 1/encounter ",plus(lambda x:x.mod("dex"),1)," bonus to one attack roll"]],[feat([feat([ft("addfeature","orb of deception")]),ft("addfeature","orb of imposition")]),feat([ft("addfeature","tome of binding")]),feat([ft("addfeature","Tome of Readiness")]),feat([ft("addfeature","staff of defense"),ft("ac",("",lambda x:x.check("weapongroups","staff")))]),feat([ft("addfeature","wand of accuracy")])],"","")
specMenus["genasiManifestation"]=specialMenu(["Earthsoul: +1 fortitude defense, +1 to saving throws, Earthshock power",["Firesoul: +1 reflex defense, resist ",lambda x:raising(5,10)(x)+x.statret("genasiresist")," fire, Firepulse power"],["Stormsoul: +1 fortitude defense, resist ",lambda x:raising(5,10)(x)+x.statret("genasiresist")," lighting, Promise of Storm power"],"Watersoul: You can breathe under water.  +2 racial bonus to saves vs. ongoing damage, and Swiftcurrent power",["Windsoul: Resist ",lambda x:raising(5,10)(x)+x.statret("genasiresist")," cold and Windwalker power"]],[feat([ft("featureadd","earthsoul"),ft("fort",["racial",1]),basePowers["Earthshock"]]),feat([ft("featureadd","firesoul"),ft("ref",["racial",1]),basePowers["Firepulse"]]),feat([ft("featureadd","stormsoul"),ft("fort",["racial",1]),basePowers["Promise of Storm"]]),feat([ft("featureadd","watersoul"),basePowers["Swiftcurrent"]]),feat([ft("featureadd","windsoul"),basePowers["Windwalker"]])],"","")
specMenus["studentOfThePlague"]=specialMenu(["Sight of the Unseen: 1 square of darkvision you can turn on and off at will","Flamespeed: 1/encounter as minor act +1 speed (+2 for charge/run) until end of your next turn","Larger than Life: 1/day as free act, add 1 to the reach of an attack you make"],[feat([ft("featureadd","sight of the unseen")]),feat([ft("featureadd","flamespeed")]),feat([ft("featureadd","larger than life")])],"","")
def addFeats(addList):
    ret={}
    for feature in addList:
        ret[feature.name()]=feature.copy()
    return ret

allFeatDict={}

allFeatDict["Player's Handbook"]=addFeats([
   feat([],"Action Surge","+3 to attacks when you spend an action point",CHECK("checkrace","human"))
  ,feat([],"Agile Hunter","Shift as a free action after scoring a critical hit",lambda x: x.check("checkclass","ranger") and x.check("dex",15) and x.check("feature","hunters quarry"))
  ,feat([ft("perception",["feat",2])],"Alertness","+2 feat bonus to perception, don't grant combat advantage when surprised")
  ,feat([featPowers["Armor of Bahamut"]],"Armor of Bahamut","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","bahamut") or x.check("feature","manifest the divine")))
  ,feat([ft("proficiency","chainmail")],"Armor Proficiency (Chainmail)","Proficient with chainmail armor",lambda x: x.check("str",13) and x.check("con",13) and (x.check("proficiency","leather") or x.check("proficiency","hide")) and not(x.check("proficiency","chainmail")))
  ,feat([ft("proficiency","leather")],"Armor Proficiency (Leather)","Proficient with leather armor", lambda x: not(x.check("proficiency","leather")))
  ,feat([ft("proficiency","hide")],"Armor Proficiency (Hide)","Proficient with hide armor",lambda x: x.check("str",13) and x.check("con",13) and x.check("proficiency","leather") and not(x.check("proficiency","hide")))
  ,feat([ft("proficiency","plate")],"Armor Proficiency (Plate)","Proficient with plate armor",lambda x: x.check("str",15) and x.check("con",15) and x.check("proficiency","scale") and not(x.check("proficiency","plate")))
  ,feat([ft("proficiency","scale")],"Armor Proficiency (Scale)","Proficient with scale armor",lambda x: x.check("str",13) and x.check("con",13) and x.check("proficiency","chainmail") and not(x.check("proficiency","scale")))
  ,feat([ft("firedamage",["feat",raising(1,10)]),ft("radiantdamage",["feat",raising(1,10)])],"Astral Fire",["+",raising(1,10)," damage with fire or radiant power"],lambda x: x.check("dex",13) and x.check("cha",13))
  ,feat([featPowers["Avandra's Rescue"]],"Avandra's Rescue","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","avandra") or x.check("feature","manifest the divine")))
  ,feat([ft("sneakdice",["feat",2])],"Backstabber","The extra damage from your sneak attack class feature increased from D6s to D8s",CHECK("feature","sneak attack"))
  ,feat([],"Blade Opportunist","'+2 bonus to opportunity attack rolls with a heavy or light blade",lambda x: x.check("str",13) and x.check("dex",13))
  ,feat([ft("aciddamage",["feat",raising(1,10)]),ft("colddamage",["feat",raising(1,10)])],"Burning Blizzard",["+",raising(1,10)," damage with acid or cold power"],lambda x: x.check("int",13) and x.check("wis",13))
  ,feat([],"Combat Reflexes","+1 bonus to opportunity attack rolls",CHECK("dex",13))
  ,feat([featPowers["Corellon's Grace"]],"Corellon's Grace","Extra power option for channel divinity",lambda x: x.check("feature","channel divinitiy") and (x.check("deity","corellon") or x.check("feature","manifest the divine")))
  ,feat([ft("necroticdamage",["feat",raising(1,10)]),ft("psychicdamage",["feat",raising(1,10)])],"Dark Fury",["+",raising(1,10)," damage with necrotic or psychic power"],lambda x: x.check("con",13) and x.check("wis",13))
  ,feat([ft("oppAc",("feat",2))],"Defensive Mobility","+2 to AC against opportunity attacks")
  ,feat([],"Distracting Shield","If you hit a foe because of combat challenge, that foe takes -2 to attacks until your next turn",lambda x: x.check("wis",15) and x.check("checkclass","ranger") and x.check("feature","combat challenge"))
  ,feat([],"Dodge Giants","+1 to AC and reflex against large or larger foes",CHECK("checkrace","dwarf"))
  ,feat([],"Dragonborn Frenzy","+2 bonus to damage rolls when bloodied",CHECK("checkrace","dragonborn"))
  ,feat([ft("vision","low-light"),ft("perception",["feat",1])],"Dragonborn Senses","Gain low-light vision",CHECK("checkrace","dragonborn"))
  ,feat([ft("surges",["feat",2])],"Durable","Increase number of healing surges by two")
  ,feat([ft("proficiency",groupList(["axe"])+groupList(["hammer"])),ft(["axedamage","hammerdamage"],("feat",2))],"Dwarven Weapon Training","Gain proficiency and a +2 feat bonus to damage rolls with axes and hammers",CHECK("checkrace","dwarf"))
  ,feat([ft("proficiency",groupList(["spear"])),ft(["speardamage","longswordnamedamage"],("feat",2))],"Eladrin Soldier","Gain proficiency with all spears and a +2 feat bonus to damage rolls with longswords and all spears",CHECK("checkrace","eladrin"))
  ,feat([],"Elven Precision","When you use the elven accuracy power, you gain a +2 bonus to the new attack roll",lambda x: x.check("checkrace","elf") and x.check("power","elven accuracy"))
  ,feat([ft("dragon breathclose blast",["feat",2])],"Enlarged Dragon Breath","When you use your dragon breath power, you may choose to make it blast 5 instead of blast 3",lambda x: "dragonborn" in x.statret("checkrace") and "dragon breath" in x.statret("power"))
  ,feat([ft("acrobatics",("feat",2))],"Escape Artist","You can attempt to escape a grab as a minor action, instead of as a move action",CHECK("training","acrobatics"))
  ,feat([ft("powerpick",PowerPick(powerList["wizarddaily1"].values(),1, 15, "Expanded Spellbook 1")),ft("powerpick",PowerPick(powerList["wizarddaily5"].values(),5, 19, "Expanded Spellbook 5")),ft("powerpick",PowerPick(powerList["wizarddaily9"].values(),9, 25, "Expanded Spellbook 9")),ft("powerpick",PowerPick(powerList["wizarddaily15"].values(),15, 29, "Expanded Spellbook 15")),ft("powerpick",PowerPick(powerList["wizarddaily19"].values(),19, 31, "Expanded Spellbook 19")),ft("powerpick",PowerPick(powerList["wizarddaily25"].values(),25, 31, "Expanded Spellbook 25")),ft("powerpick",PowerPick(powerList["wizarddaily29"].values(),29, 31, "Expanded Spellbook 31"))],"Expanded Spellbook","Choose one additional daily wizard attack spell of each level you can cast for your spellbook",lambda x: x.statret("wis")>=13 and "wizard" in x.statret("checkclass"))
  ,feat([ft("rangeddistance",["feat",5])],"Far Shot","When using a projectile weapon, increase both the normal range and the long range by 5 squares",CHECK("dex",13))
  ,feat([ft("throwndistance",["feat",2])],"Far Throw","When you use a thrown weapon, increase both the normal range and the long range by 2 squares",CHECK("str",13))
  ,feat([],"Fast Runner","You gain a +2 speed bonus when you charge or run",CHECK("con",13))
  ,feat([],"Ferocious Rebuke","When you use infernal wrath and hit, push the target back 1 square in addition to any damage dealt",lambda x:x.check("checkrace","tiefling") and x.check("power","infernal wrath"))
  ,feat([],"Group Insight","Grant allies within 10 squares a +1 racial bonus to insight and initiative checks",CHECK("checkrace","half-elf"))
  ,feat([],"Halfling Agility","Attacker takes -2 penalty on reroll forced by second chance power",lambda x:x.check("checkrace","halfling") and x.check("power","second chance"))
  ,feat([],"Harmony of Erathis","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","erathis") or x.check("feature","manifest the divine")))
  ,feat([ft("layonhands",("feat",lambda x:x.mod("cha")))],"Healing Hands","Ally targeted by lay on hands heals additional hit points equal to your cha mod",lambda x:x.check("checkclass","paladin") and x.check("power","lay on hands"))
  ,feat([ft("fireattack",("",1)),ft("firedamage",("",1)),ft("fearattack",("",1)),ft("feardamage",("",1))],"Hellfire Blood","+1 feat bonus to attack rolls and damage rolls with fire or fear powers",CHECK("checkrace","tiefling"))
  ,feat([ft("saves",("feat",1))],"Human Perseverance","+1 to saving throws",CHECK("checkrace","human"))
  ,feat([ft("infernalpact",("feat",3))],"Improved Dark One's Blessing","Pact boon grants 3 additional hit points",lambda x:x.check("con",15) and x.check("checkclass","warlock") and x.check("feature","infernal pact"))
  ,feat([ft("starpact",("feat",1))],"Improved Fate of the Void","Pact boon grants an additional +1 bonus to die roll",lambda x:(x.check("con",13) or x.check("cha",13)) and x.check("checkclass","warlock") and x.check("feature","star pact"))
  ,feat([ft("initiative",("feat",4))],"Improved Initiative","+4 to initiative checks")
  ,feat([ft("mistystep",("feat",2))],"Improved Misty Step","Pact boon grants additional 2 squares of teleport",lambda x:x.check("int",13) and x.check("checkclass","warlock") and x.check("feature","fey pact"))
  ,feat([ft("inspiredrecovery",("feat",1))],"Inspired Recovery",["Grant ally saving throw with +",lambda x:x.mod("cha")," bonus"],lambda x:x.check("checkclass","warlord") and x.check("feature","inspiring presence"))
  ,feat([featPowers["Ioun's Poise"]],"Ioun's Poise","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","ioun") or x.check("feature","manifest the divine")))
  ,feat([ft(skill,["feat",jackoftrades(skill)]) for skill in allskills.keys()],"Jack of All Trades","+2 to untrained skill checks",CHECK("int",13))
  ,feat([featPowers["Kord's Favor"]],"Kord's Favor","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","kord") or x.check("feature","manifest the divine")))
  ,feat([ft("huntersdice",("feat",2))],"Lethal Hunter","Hunter's Quarry damage dice increase to d8's",lambda x:x.check("checkclass","ranger") and x.check("feature","hunter's quarry"))
  ,feat([ft(["acrobatics","stealth"],("feat",1))],"Light Step","+1 to speed of group for long distance travel, +1 to acrobatics and stealth",CHECK("checkrace","elf"))
  #Linguist
  ,feat([]
               ,"Linguist"
               ,"Learn 3 new languages"
               ,lambda x:x.check("int",13))
  ,feat([ft("athletics",("feat",1))],"Long Jumper","Make standing jumps as if from a running start, +1 athletics",CHECK("training","athletics"))
  ,feat([],"Lost in the Crowd","+2 AC when adjacent to at least two larger enemies",CHECK("checkrace","halfling"))
  ,feat([featPowers["Melora's Tide"]],"Melora's Tide","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","melora") or x.check("feature","manifest the divine")))
  ,feat([featPowers["Moradin's Resolve"]],"Moradin's Resolve","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","moradin") or x.check("feature","manifest the divine")))
  ,feat([],"Mounted Combat","Gain access to the special abilities of your mount")
  ,feat([],"Nimble Blade","+1 to attacks with light blade and combat advantage",CHECK("dex",15))
  ,feat([featPowers["Pelor's Radiance"]],"Pelor's Radiance","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","pelor") or x.check("feature","manifest the divine")))
  ,feat([],"Potent Challenge",["Add ",lambda x:x.mod("con")," damage to target hit with combat challenge opportunity attack"],lambda x: x.check("checkclass","fighter") and x.check("feature","combat challenge"))
  ,feat([],"Power Attack",["Trade +",raising(2,10)," damage (+",raising(3,10)," for 2-handed weapons) for -2 attack"],CHECK("str",15))
  ,feat([],"Powerful Charge","+2 damage, +2 to bull rush on a charge",CHECK("str",13))
  ,feat([],"Precise Hunter","Allies gain +1 attack against target hit by critical hit",lambda x:x.check("wis",15) and x.check("checkclass","ranger") and x.check("feature","hunter's quarry"))
  ,feat([],"Press the Advantage","Retain combat advantage with a critical hit",lambda x:x.check("cha",15) and x.check("checkclass","rogue"))
  ,feat([ft("initiative",("feat",2))],"Quick Draw","Draw a weapon with attack action, +2 initiative",CHECK("dex",13))
  ,feat([ft("lightningdamage",["feat",raising(1,10)]),ft("thunderdamage",["feat",raising(1,10)])],"Raging Storm",["+",raising(1,10)," damage with lightning or thunder power"],lambda x:x.check("con",13) and x.check("dex",13))
  ,feat([featPowers["Raven Queen's Blessing"]],"Raven Queen's Blessing","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","raven queen") or x.check("feature","manifest the divine")))
  ,feat([],"Ritual Caster","Master and perform rituals",lambda x:x.check("training","arcana") or x.check("training","religion"))
  ,feat([featPowers["Sehanine's Reversal"]],"Sehanine's Reversal","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","sehanine") or x.check("feature","manifest the divine")))
  ,feat([ft("proficiency","heavy shield")],"Shield Proficiency (Heavy)","Proficienct with heavy shields",lambda x:x.check("proficiency","light shield") and x.check("str",15))
  ,feat([ft("proficiency","light shield")],"Shield Proficiency (Light)","Proficiency with light shields",CHECK("str",13))
  ,feat([],"Shield Push","Push target hit by combat challenge 1 square",lambda x: x.check("checkclass","fighter") and x.check("feature","combat challenge"))
#Fix me!  Only allowed to get skill focus once per skill, and only when trained in it
  ,feat([specialMenu(allskills.keys(), [feat([ft(x, ("feat",3))]) for x in allskills.keys()], "+3 on "," checks")],"Skill Focus","",lambda x:x.statret("focusnum")>=1)
  ,feat([ft("skillpick",SkillPick(allskills.keys(),1, "ea"))],"Skill Training","Any one bonus trained skill",lambda x: sum([q in x.statret("training") for q in allskills.keys()])<len(allskills))
  ,feat([ft("athletics",("feat",1))],"Sure Climber","Climb at normal speed on any surface; +1 to Athletics",CHECK("training","athletics"))
  ,feat([],"Surprise Knockdown","Knock target prone with critical hit",lambda x:x.check("str",15) and x.check("checkclass","rogue"))
  ,feat([],"Tactical Assault","Ally gains bonus to damage equal to your Int modifier",lambda x:x.check("checkclass","warlord") and x.check("feature","tactical presence"))
  ,feat([ft("hp",("feat",raising(5,10)))],"Toughness",["Gain ",raising(5,10)," hit points"])
  ,feat([ft("ac",("shield", lambda x:x.inventory.dualwield())),ft("ref",("shield", lambda x:x.inventory.dualwield()))],"Two-Weapon Defense","+1 to AC and Reflex while holding a weapon in each hand",lambda x:x.check("dex",13) and x.check("feature","two-weapon fighting"))
  ,feat([ft("primarydamage",("",1))],"Two-Weapon Fighting","+1 damage while holding a melee weapon in each hand",CHECK("dex",13))
  ,feat([specialMenu(sorted(weaponFocus.keys()), [weaponFocus[x] for x in sorted(weaponFocus.keys())],["+", raising(1,10), " damage with "]," weapon group")],"Weapon Focus","")
  ,feat([specialMenu(sorted(weaponList.keys()), [feat([ft("proficiency",x)]) for x in sorted(weaponList.keys())],"Proficient with ")],"Weapon Proficiency","",lambda x: sum([q in x.statret("proficiency") for q in weaponProf.keys()])<len(weaponProf))
  ,feat([],"Wintertouched","Gain combat advantage against foe vulnerable to cold")
###Paragon Feats###
  ,feat([],"Action Recovery","Gain extra saving throws by spending action point",lambda x:x.check("checkrace","human") and x.check("level", 11))
  ,feat([],"Agile Athlete","Roll twice with Acrobatics and Athletics checks",CHECK("level",11))
  ,feat([],"Arcane Reach","Choose square within 2 as origin with close attack power",lambda x:x.check("dex", 15) and x.check("level", 11))
  ,feat([ft("ac",("feat",lambda x:x.check("armortype","chainmail"))),ft("acheck",("",lambda x:x.check("armortype","chainmail")))],"Armor Specialization (Chainmail)","+1 AC with chainmail, reduce check penalty by 1",lambda x:x.check("level", 11) and x.check("proficiency","chainmail") and x.check("dex", 15))
  ,feat([ft("ac",("feat",lambda x:x.check("armortype","hide"))),ft("acheck",("",lambda x:x.check("armortype","hide")))],"Armor Specialization (Hide)","+1 AC with hide armor, reduce check penalty by 1",lambda x:x.check("level", 11) and x.check("proficiency","hide") and x.check("con", 15))
  ,feat([ft("ac",("feat",lambda x:x.check("armortype","plate")))],"Armor Specialization (Plate)","+1 AC with plate armor",lambda x:x.statret("level")>=11 and "plate" in x.statret("proficiency") and x.statret("con")>=15)
  ,feat([ft("speed",("feat",lambda x:x.check("armortype","scale")))],"Armor Specialization (Scale)","Ignore speed penalty of scale armor",lambda x:x.check("level", 11) and x.check("proficiency","scale") and x.check("dex", 15))
  ,feat([],"Back to the Wall","+1 to melee attack, damage, AC when adjacent to a wall",CHECK("level",11))
  ,feat([],"Blood Thirst","+2 damage against bloodied foes",CHECK("level",11))
  ,feat([],"Combat Anticipation","+1 defenses against ranged, area, close attacks",CHECK("level",11))
  ,feat([ft("combatleader",("combatleader",lambda x:max([x.mod("int"),x.mod("cha")])))],"Combat Commander","Improve Combat Leader bonus to Cha or Int modifier",lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("feature","combat leader"))
  ,feat([],"Danger Sense","Roll twice for initiative, use higher result",CHECK("level",11))
  ,feat([],"Deadly Axe","Treat all axes as high crit weapons",lambda x:x.check("level", 11) and x.check("str",17) and x.check("con",13))
  ,feat([],"Defensive Advantage","+2 AC when you have combat advantage against an enemy",lambda x:x.check("level", 11) and x.check("dex",17))
  ,feat([],"Devastating Critical","Deal additional 1d10 damage on a critical hit",CHECK("level",11))
  ,feat([],"Distant Shot","Ignore -2 penalty for long range",CHECK("level",11))
  ,feat([ft("surge",("",lambda x:x.mod("con"))),ft("surges",("",2))],"Dwarven Durability",["Increase number of healing surges by 2 and healing surge value by ", lambda x:x.mod("con")],lambda x:x.check("level", 11) and x.check("checkrace","dwarf"))
  ,feat([ft("dragon breathdice",("feat",4))],"Empowered Dragon Breath","Dragon Breath uses d10's",lambda x:x.check("level", 11) and x.check("checkrace","dragonborn") and x.check("power","dragon breath"))
  ,feat([],"Evasion","No damage from a missed area or close attack that target AC or Reflex",lambda x:x.check("level", 11) and x.check("dex",15))
  ,feat([],"Feywild Protection","+2 defenses when you use Fey Step",lambda x:x.check("level", 11) and x.check("checkrace","eladrin") and x.check("feature","fey step"))
  ,feat([],"Fiery Rebuke",["Target of Infernal Wrath takes additional ",lambda x:5+x.statret("level")/2," fire damage"],lambda x:x.check("level", 11) and x.check("checkrace","tiefling") and x.check("feature","infernal rebuke"))
  ,feat([ft("speed",("feat",1))],"Fleet-Footed","+1 to speed",CHECK("level",11))
  ,feat([ft("fort",("feat",2))],"Great Fortitude","+2 to Fortitude defense",CHECK("level",11))
  ,feat([],"Hammer Rhythm",["Deal ",lambda x:x.mod("con")," damage to target on a miss with a hammer or mace that normally deals no damage"] ,lambda x:x.check("level", 11) and x.check("con",17) and x.check("str",15))
  ,feat([],"Heavy Blade Opportunity","Use at-will power on opportunity attack with heavy blade",lambda x:x.check("level", 11) and x.check("str", 15) and x.check("dex", 15))
  ,feat([],"Improved Second Wind","Heal an additional 5 damage with second wind",CHECK("level",11))
  ,feat([],"Inescapable Force","Force powers ignores insubstantial and deals 1d10 extra damage vs. insubstantial creatures",CHECK("level",11))
  ,feat([ft("will",("feat",2))],"Iron Will","+2 to Will defenses",CHECK("level",11))
  ,feat([],"Lasting Frost","First target hit per turn with cold power gains vulnerable cold 5 after the attack.",CHECK("level",11))
  ,feat([],"Light Blade Precision","+2 damage against large or larger targets",lambda x:x.check("level", 11) and (x.check("size","small") or x.check("size","medium")))
  ,feat([],"Lightning Arc","Affect second target with lightning power on critical hit",CHECK("level",11))
  ,feat([ft("ref",("feat",2))],"Lightning Reflexes","+2 to Reflex defense",CHECK("level",11))
  ,feat([],"Mettle","No damage from missed area or close attacks that target Fortitude or Will",CHECK("level",11))
  ,feat([],"Point-Blank Shot","Ignore cover and concealment within 5 squares",CHECK("level",11))
  ,feat([],"Polearm Gamble","Make opportunity attack against enemy moving to adjacent square",lambda x:x.check("level", 11) and x.check("str",15) and x.check("wis",15))
  ,feat([],"Psychic Lock","Target hit with psychic power takes -2 on next attack roll",CHECK("level",11))
  ,feat([ft("thunderclose blast",("feat",1)),ft("thunderclose burst",("feat",1)), ft("thunderarea burst",("feat",1))],"Resounding Thunder","Add 1 to size of blast or burst with thunder keyword",CHECK("level",11))
  ,feat([],"Running Shot","No attack penalty to ranged attacks after you run",lambda x:x.check("level", 11) and x.check("checkrace","elf"))
  ,feat([],"Scimitar Dance",["Deal ",lambda x:x.mod("dex")," damage to target on a miss with a scimitar that normally deals no damage"],lambda x:x.check("level", 11) and x.check("str",15) and x.check("dex",17))
  ,feat([specMenus["implementMastery"]],"Second Implement","",lambda x:x.check("level", 11) and x.check("checkclass","wizard") and (x.check("feature","implement mastery")))
  ,feat([],"Secret Stride","No penalty to stealth with move while hiding or sneaking",lambda x:x.check("level", 11) and x.check("training","stealth"))
  ,feat([],"Seize the Moment","Gain combat advantage against foe with lower initiative",lambda x:x.check("level", 11) and x.check("dex",17))
  ,feat([ft("ac",("feat",lambda x:x.check("armortype","shield"))),ft("ref",("feat",lambda x:x.check("armortype","shield")))],"Shield Specialization","+1 to AC and Reflex when using a shield",lambda x:x.check("level", 11) and x.check("dex",15) and (x.check("light shield", "proficiency") or x.check("heavy shield", "proficiency")))
  ,feat([],"Sly Hunter","+3 damage with bow against isolated target",lambda x:x.check("level", 11) and x.check("wis",15))
  ,feat([],"Solid Sound","+2 to defense after you use thunder or force power",lambda x:x.check("level", 11) and x.check("con",13))
  ,feat([],"Spear Push","Add 1 square to distance pushed with spear or polearm",lambda x:x.check("level", 11) and x.check("str",15) and x.check("dex",13))
  ,feat([],"Spell Focus","-2 to saves against your wizard spells",lambda x:x.check("level", 11) and x.check("cha",15) and x.check("checkclass","wizard"))
  ,feat([],"Steady Shooter","+3 damage with crossbow if you don't move",lambda x:x.check("level", 11) and x.check("con",15))
  ,feat([],"Sweeping Flail","+2 to attacks with flail against foe with shield",lambda x:x.check("level", 11) and x.check("str",15) and x.check("dex",15))
  ,feat([],"Twofold Curse","Curse the two nearest enemies",lambda x:x.check("level", 11) and x.check("checkclass","warlock") and x.check("feature","warlock's curse"))
  ,feat([],"Uncanny Dodge","Enemies denied bonus to attack from combat advantage",lambda x:x.check("level", 11) and x.check("wis",15))
  ,feat([],"Underfoot","Move through spaces of larger creatures",lambda x:x.check("level", 11) and x.check("checkrace","halfling"))
###Epic Feats###
  ,feat([],"Arcane Mastery","Regain daily spell by spending action point",lambda x:x.check("level",21) and x.check("checkclass","wizard"))
  ,feat([],"Axe Mastery","Critical hit with axe melee attack roll of 19 or 20",lambda x:x.check("str",21) and x.check("con",17) and x.check("level",21))
  ,feat([],"Blind-Fight","Adjacent creatures aren't concealed or invisible to you",lambda x:x.check("level",21) and (x.check("wis",13) or x.check("training","perception")))
  ,feat([],"Bludgeon Mastery","Critical hit with hammer, mace, or staff melee attack roll of 19 or 20",lambda x:x.check("str",19) and x.check("con",19) and x.check("level",21))
  ,feat([],"Epic Resurgence","Regain encounter attack power on critical hit",CHECK("level",21))
  ,feat([],"Flail Mastery","Critical hit with flail melee attack roll of 19 or 20",lambda x:x.check("str",19) and x.check("dex",19) and x.check("level",21))
  ,feat([],"Flanking Maneuver","Move diagonally and through enemies' spaces",lambda x:x.check("dex",17) and x.check("level",21) and x.check("training","acrobatics"))
  ,feat([],"Font of Radiance","Target illuminated with critical hit, takes radiant damage",CHECK("level",21))
  ,feat([],"Heavy Blade Mastery","Critical hit with heavy blade melee attack roll of 19 or 20",lambda x:x.check("str",21) and x.check("dex",17) and x.check("level",21))
  ,feat([],"Irresistible Flame","Treat target's fire resist as 20 lower when determining damage for your attacks",CHECK("level",21))
  ,feat([],"Light Blade Mastery","Critical hit with light blade melee attack roll of 19 or 20",lambda x:x.check("str",17) and x.check("dex",21) and x.check("level",21))
  ,feat([],"Pick Mastery","Critical hit with pick melee attack roll of 19 or 20",lambda x:x.check("str",21) and x.check("con",17) and x.check("level",21))
  ,feat([],"Spear Mastery","Critical hit with spear melee attack roll of 19 or 20",lambda x:x.check("str",19) and x.check("dex",19) and x.check("level",21))
  ,feat([],"Spell Accuracy",["Omit up to ",WISMOD,"squares from any area or close wizard power"],lambda x:x.check("level",21) and x.check("checkclass","wizard"))
  ,feat([],"Triumphant Attack","Target at -2 to attacks and defenses after a critical hit",CHECK("level",21))
  ,feat([],"Two-Weapon Flurry","On successful opportunity attack, make a secondary attack at -5 with offhand weapon",lambda x:x.check("level",21) and x.check("dex",19) and x.check("feature","two-weapon fighting"))
  ,feat([],"Unfettered Stride","Ignore the effects of difficult terrain on your movement",lambda x:x.check("level",21) and x.check("training","acrobatics"))
])
allFeatDict["Arcane Power"]=addFeats([
  feat([],"Arcane Fire","Target hit with fire power gains vulnerable 5 cold vs. first arcane power you use against it before end of next turn",lambda x: x.check("int",13) and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Arcane Fury","Deal extra damage from Furious Assault to all targets in blast or burst",lambda x: x.check("checkrace","half-orc") and x.check("checkclass",arcaneclasses,True))
#Arcane Implement Proficiency
  ,feat([]
        ,"Arcane Implement Proficiency"
        ,"Use arcane implement from another class for your arcane powers"
        ,lambda x: x.check("checkclass",arcaneclasses,True))
  ,feat([],"Arcane Reserves","+2 to damage rolls with arcane at-will powers when all arcane encounter powers are expended",lambda x: x.check("checkrace","human") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Darkfire Implement","Deal twice implement enhancement bonus as damage when hitting with Darkfire",lambda x: x.check("checkrace","drow") and x.check("checkclass",arcaneclasses,True))
#Draconic Spellcaster
  ,feat([]
        ,"Draconic Spellcaster"
        ,["+",raiselist(1,[15,25])," feat bonus to attack rolls with ",lambda x:x.statret("dragonbreathelement")," powers"]
        ,lambda x: x.check("checkrace","dragonborn") and x.check("checkclass",arcaneclasses,True))
#Dual Implement Spellcaster
  ,feat([]
        ,"Dual Implement Spellcaster"
        ,"Add off-hand implement to damage with arcane attack power"
        ,lambda x: x.check("dex",13) and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Elemental Echo",["+1 to attack rolls and +",raising(2,10)," to damage rolls with arcane powers after using genasi racial power"],lambda x: x.check("checkrace","genasi") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Elven Arcane Precision","Use Elven Accuracy to reroll any number of attacks in a single arcane attack power",lambda x: x.check("checkrace","elf") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Fanged Magic",["When you hit with an arcane power while using Longtooth Shifting, one enemy adjacent to target takes ",raising(2,10)," damage"],lambda x: x.check("checkrace","shifter, longtooth") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Magic of the Ages","+1 to attack roll of triggering arcane attack power with Memory of a Thousand Lifetimes",lambda x: x.check("checkrace","deva") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Magic of the Mists","When using Fade Away, attacking with arcane attack power does not end the effect",lambda x: x.check("checkrace","gnome") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Mountain Hammer Spellcasting","When you use Stone's Endurace, your arcane powers ignore enemies' resistances until the end of your next turn",lambda x: x.check("checkrace","goliath") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Nimble Spellcaster","When using an area arcane power, you do not provoke opportunity attacks from the creatures you target with that power",lambda x: x.check("dex",13) and x.check("checkrace","halfling") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Predatory Magic","When using a close arcane attack power with Razorclaw Shifting, shift 1 square as a free action before or after using the power",lambda x: x.check("checkrace","shifter, razorclaw") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Rune-Scribed Scroll",["When you use second wind, gain +1 to attack and +",CONMOD," to damage with arcane powers you use before the end of your turn"],lambda x: x.check("checkrace","dwarf") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Twist the Arcane Fabric","Expend Fey Step as a free action to teleport ally in your close or area attack 3 squares before attacking",lambda x: x.check("checkrace","eladrin") and x.check("checkclass",arcaneclasses,True))
  ,feat([],"Wrathful Magic","Use Infernal Wrath against target you miss with an arcane attack power",lambda x: x.check("checkrace","tiefling") and x.check("checkclass",arcaneclasses,True))
###Arcane Power: Bard Heroic Feats###
#Combat Virtuoso
  ,feat([]
        ,"Combat Virtuoso"
        ,"Use Charisma for attack rolls with multiclass or dilettante powers"
        ,CHECK("checkclass","bard"))
  ,feat([],"Extended Prescience","Virtue of Prescience lasts until end of ally's next turn",lambda x: x.check("feature","virtue of prescience") and x.check("checkclass","bard"))
  ,feat([ft(["and","arcaneattack","charmattack"],["feat",raiselist(1,[15,25])]),ft(["bluff","diplomacy"],["feat",1])],"Feyborn Charm",["+",raiselist(1,[15,25])," feat bonus to attack rolls with arcane charm powers; +1 feat bonus to Bluff and Diplomacy"],lambda x: x.check("checkrace",["eladrin","gnome"],True) and x.check("checkclass","bard"))
  ,feat([],"Friendly Deception","Can apply Words of Friendship bonus to Bluff check",lambda x: x.check("power","words of friendship") and x.check("checkclass","bard"))
  ,feat([],"Infernal Clamor","With Infernal Wrath, allies who can see and hear you gain +1 power bonus to next attack roll against the enemy that hit you",lambda x: x.check("checkrace","tiefling") and x.check("checkclass","bard"))
  ,feat([],"Infuriating Escape","If enemy misses when you use Second Chance, next ally to attack them before the end of your next turn gains combat advantage ",lambda x: x.check("checkrace","halfling") and x.check("checkclass","bard"))
#Prescienct Fortification
  ,feat([],"Prescient Fortification","Increase the bonus from Virtue of Prescience by 2",lambda x: x.check("feature","virtue of prescience") and x.check("checkclass","bard"))
  ,feat([],"Rousing Voice",["When an ally within 10 squares of you uses second wind, they gain ",CHAMOD," temporary hit points"],lambda x: x.check("checkrace","human") and x.check("checkclass","bard"))
###Arcane Power: Sorcerer Heroic Feats###
  ,feat([],"Focusing Spellfury","If you hit 2+ enemies with sorcerer at-will attack power, gain +2 to damage rolls with ranged/melee attack powers until end of your next turn",CHECK("checkclass","sorcerer"))
  ,feat([],"Rising Spellfury","If you hit only 1 enemy with sorcerer at-will attack power, gain +1 to attack rolls with area/close attack powers until end of your next turn",CHECK("checkclass","sorcerer"))  
  ,feat([],"Sorcerous Assassin",["Gain a +",raising(2,10)," feat bonus to damage with poison or psychic powers and combat advantage"],lambda x: x.check("checkrace","drow") and x.check("checkclass","sorcerer"))
  ,feat([],"Student of the Cosmos","+2 feat bonus based on phase - Sun: Initiative and Heal, Moon: Bluff and Stealth, Stars: Insight and Perception",lambda x: x.check("feature","cosmic magic") and x.check("checkclass","sorcerer"))
  ,feat([ft(["and","arcanedamage","lightningdamage"],["feat",raising(1,10)]),ft(["and", "arcanedamage","thunderdamage"],["feat",raising(1,10)])],"Tempest Magic",["+",raising(1,10)," feat bonus to damage rolls with arcane lightning or thunder; +",raising(2,10)," instead when bloodied"],lambda x: x.check("dex",13) and x.check("con",13) and x.check("feature", "storm magic") and x.check("checkclass","sorcerer"))
  ,feat([],"Triggered Chaos","After attack, if enemies reroll from Second Chance is even, slide it 1 square; if odd, you can shift 1 square",lambda x: x.check("checkrace","halfling") and x.check("feature", "wild magic") and x.check("checkclass","sorcerer"))
  ,feat([],"True Dragon's Soul","Gain +1 to Fort, Ref, and Will when first bloodied in an encounter; breath weapon can ignore resistance through Dragon Soul",lambda x: x.check("checkrace","dragonborn") and x.check("feature"," dragon magic") and x.check("checkclass","sorcerer"))
  ,feat([],"Warding soul","Each ally adjacent to you gains any resistance granted by your Spell Source",lambda x: x.check("checkrace","half-elf") and x.check("feature","spell source") and x.check("checkclass","sorcerer"))
###Arcane Power: Swordmage Heroic Feats###
  ,feat([],"Closing Advantage","+1 to melee attacks and damage after hitting with a ranged or area power",CHECK("checkclass","swordmage"))
  ,feat([],"Combat Casting","Ranged and area attacks don't provoke after hitting with a melee power",CHECK("checkclass","swordmage"))
  ,feat([],"Eladrin Swordmage Advance","Make melee basic attack on adjacent enemy after teleporting with Fey Step",lambda x: x.check("checkrace","eladrin") and x.check("checkclass","swordmage"))
  ,feat([ft(["and","swordmagedamage","aciddamage"],["feat",raising(1,10)]),ft(["and","swordmagedamage","colddamage"],["feat",raising(1,10)]),ft(["and","swordmagedamage","firedamage"],["feat",raising(1,10)]),ft(["and","swordmagedamage","lightningdamage"],["feat",raising(1,10)]),ft(["and","swordmagedamage","thunderdamage"],["feat",raising(1,10)])],"Elemental Blade Attunement",["+",raising(1,10)," damage with swordmage acid, cold, fire, lightning, or thunder powers"],lambda x: x.check("checkrace","genasi") and x.check("checkclass","swordmage"))
  ,feat([],"Grasping Ensnarement","When you teleport an enemy with Aegis of Ensarement, that enemy is slowed until the end of your next turn",lambda x: x.check("feature","aegis of ensnarement") and x.check("checkclass","swordmage"))
  ,feat([],"Immortal Warding","Swordmage Warding still active while unconcious; add AC bonus from Swordmage Warding to racial necrotic and radiant resistance",lambda x: x.check("checkrace","deva") and x.check("feature","swordmage warding") and x.check("checkclass","swordmage"))
  ,feat([],"Improved Swordmage Warding","While wearing cloth, leather, or no armor, raise AC from Swordmage Warding by 1",lambda x: x.check("dex",13) and x.check("feature", "swordmage warding") and x.check("checkclass","swordmage"))
  ,feat([],"Risky Aegis","After using Aegis, target gains combat advantage vs. you, and you gain +2 to attack and damage against target",lambda x: x.check("checkrace","human") and x.check("feature","swordmage aegis") and x.check("checkclass","swordmage"))
###Arcane Power: Warlock Heroic Feats###
  ,feat([],"Accursed Coordination","You may place your curse on an enemy that is already cursed; gain combat advantage against targets with two curses",lambda x: x.check("feature","warlock's curse") and x.check("checkclass","warlock"))
  ,feat([],"Curse of Io's Blood",["While you are bloodied, add ",lambda x:x.statret("str")+1," to your warlock's curse damage"],lambda x: x.check("feature","warlock's curse") and x.check("checkrace","dragonborn") and x.check("checkclass","warlock"))
  ,feat([],"Cursed Advantage","You gain combat advantage against bloodied enemies cursed by you",lambda x: x.check("checkrace","drow") and x.check("feature","warlock's curse") and x.check("checkclass","warlock"))
  ,feat([],"Dooming Action","When you spend an action point for an extra action, regain use of your Warlock's Curse damage",lambda x: x.check("feature","warlock's curse") and x.check("checkclass","warlock"))
  ,feat([],"Empowering Shadows","When you have concealment from Shadow Walk, you gain a +1 bonus to damage rolls",lambda x: x.check("feature","shadow walk") and x.check("checkclass","warlock"))
  ,feat([],"Reckless Curse","You gain +1 on attack rolls against targets of your curse, and targets of your curse gain +1 on attack rolls against you",lambda x: x.check("checkrace","human") and x.check("feature","warlock's curse") and x.check("checkclass","warlock"))
  ,feat([],"Vengeful Curse","When an enemy hits you, you can use your Warlock's Curse against that enemy as an immediate reaction",lambda x: x.check("checkrace","tiefling") and x.check("feature","warlock's curse") and x.check("checkclass","warlock"))
  ,feat([],"Vestige Adept","When your pact boon is triggered, as a free action change your vestige to another you have had since last rest",lambda x: x.check("feature","vestige pact") and x.check("checkclass","warlock"))
###Arcane Power: Wizard Heroic Feats###
  ,feat([],"Careful Summoner","Creatures summoned by your arcane summoning powers have +1 to all defenses",lambda x: x.check("con",13) and x.check("checkclass","wizard"))
  ,feat([],"Destructive Wizardry",["When you hit 2+ creatures with an arcane attack power, gain +",lambda x:raising(1,10)(x)+1," damage to that power"],lambda x: x.check("dex",13) and x.check("checkclass","wizard"))
#Eladrin Sword Wizardry
  ,feat([],"Eladrin Sword Wizardry"
        ,"Use longsword as wand for wizard attack powers",lambda x: x.check("dex",13) and x.check("checkrace","eladrin") and x.check("checkclass","wizard"))
  ,feat([]
        ,"Elemental Empowerment"
        ,["When you use a wizard power that has the acid, cold, fire, or thunder keyword, add ",STRMOD," to the damage rolls"]
        ,lambda x: x.check("checkrace","genasi") and x.check("checkclass","wizard"))
  ,feat([]
        ,"Enlarge Spell"
        ,""
        ,lambda x: x.check("wis",15) and x.check("checkclass","wizard"))
  ,feat([]
        ,"Gnome Phantasmist"
        ,""
        ,lambda x: x.check("checkrace","gnome") and x.check("checkclass","wizard"))
  ,feat([]
        ,"Phantom Echoes"
        ,""
        ,lambda x: x.check("cha",13) and x.check("checkclass","wizard"))
  ,feat([]
        ,"Remembered Wizardry"
        ,""
        ,lambda x: x.check("wis",13) and x.check("checkrace","deva") and x.check("checkclass","wizard"))
###Arcane Power: Paragon Feats###
  ,feat([MultiMenu([{"acid":feat([ft("arcaneadmixture","acid")],"acid"),"cold":feat([ft("arcaneadmixture","cold")],"cold"),"fire":feat([ft("arcaneadmixture","fire")],"fire"),"lightning":feat([ft("arcaneadmixture","lightning")],"lightning"),"thunder":feat([ft("arcaneadmixture","thunder")],"thunder")},["power",["arcane"], lambda x:[ft(x.lower()+"addkey", lambda y: y.featureis("arcaneadmixture"))]]],["Add "," keyword to ", " power"])],"Arcane Admixture","Add additional damage type to one arcane power",lambda x:x.check("level", 11) and x.check("checkclass",arcaneclasses,True))
#Needs ritual book
  ,feat([],"Arcane Ritualist"
        ,"Change the key skill of a ritual to Arcana"
        ,lambda x:x.check("level", 11) and x.check("checkclass",arcaneclasses,True))
###Arcane Power: Bard Paragon Feats###
,feat([],"Disheartening Presence","While concious and not bloodied, adjacent bloodied enemies take -1 to attacks",lambda x:x.check("level", 11) and x.check("checkclass","bard"))
,feat([],"Majestic Rescue","Grant target of Majestic Word a saving throw",lambda x:x.check("level", 11) and x.check("checkclass","bard") and x.check("power","majestic word"))
,feat([],"Prescient Aid",["Use Virtue of Presience to grant ally in 10 squares +",WISMOD," bonus to missed attack roll"],lambda x:x.check("level", 11) and x.check("checkclass","bard") and x.check("feature","virtue of prescience"))
,feat([],"Song of Inspiration",["When using Song of Rest, allies can spend healing surge to instead gain ",lambda x:x.mod("cha")+5," temporary HP"],lambda x:x.check("level", 11) and x.check("checkclass","bard") and x.check("feature","song of rest"))
###Arcane Power: Sorcerer Paragon Feats###
,feat([],"Cosmic Spellfury","After hitting with at-will power - Sun: Roll a save; Moon: Gain concealment; Stars: Gain insubstantial until hit",lambda x:x.check("level", 11) and x.check("checkclass","sorcerer") and x.check("feature","cosmic magic"))
,feat([],"Sorcerous Reserves","+1 to attacks when all daily powers are expended",lambda x:x.check("level", 11) and x.check("checkclass","sorcerer"))
  ,feat([],"Sorcerous Vision","Substitute Arcana check for Perception or Insight",lambda x:x.check("level", 11) and x.check("checkclass","sorcerer"))
  ,feat([],"Storm Spellfury","Fly 2 squares after hitting with at-will power",lambda x:x.check("level", 11) and x.check("checkclass","sorcerer") and x.check("feature","storm magic"))
###Arcane Power: Swordmage Paragon Feats
#Probably needs to be modified after Swordmage is added
,feat([],"Greater Swordmage Warding"
      ,"+1 feat bonus to defenses with Swordmage Warding"
      ,lambda x:x.check("level", 11) and x.check("checkclass","swordmage") and x.check("str",13) and x.check("con",13) and x.check("feature","swordmage warding"))
,feat([],"Ensnaring Flourish","+5 damage on melee damage rolls against target teleported with Aegis of Ensnarement until end of your next turn",lambda x:x.check("level", 11) and x.check("checkclass","swordmage") and x.check("power","aegis of ensnarement"))
,feat([],"Greater Aegis of Shielding","Aegis reduces enemy's damage by additional 5 points",lambda x:x.check("level", 11) and x.check("checkclass","swordmage") and x.check("power","aegis of shielding"))
,feat([],"Vigorous Assault",["Gain ",lambda x:x.mod("str")+3," temporary HP when you use Aegis of Assault to teleport"],lambda x:x.check("level", 11) and x.check("checkclass","swordmage") and x.check("power","aegis of assault"))
###Arcane Power: Warlock Paragon Feats###
  ,feat([],"Relentless Curse","Use curse as a free action when enemy cursed by you drops",lambda x:x.check("level",11) and x.check("checkclass","warlock") and x.check("feature","warlock's curse"))
  ,feat([],"Shared Pact","Can give ally in 3 squares benefit of pact boon",lambda x:x.check("level", 11) and x.check("checkclass","warlock") and x.check("feature","warlock's curse") and x.check("feature", "warlock pact"))
  ,feat([],"Vestige Versatility","Access two vestiges at a time.  Choose which to trigger each time your pact boon is triggered or with Eyes of the Vestige.",lambda x:x.check("level",11) and x.check("checkclass","warlock") and x.check("feature","vestige pact"))
###Arcane Power: Wizard Paragon Feats###
  ,feat([],"Improved Orb of Deception","Creature hit with arcane illusion power with orb grants combat advantage to next ally who attacks it before start of your next turn",lambda x:x.check("level",11) and x.check("checkclass","wizard") and x.check("feature","orb of deception") and x.check("cha",15))
  ,feat([],"Improved Orb of Imposition",["Each time creature fails the save chosen by Orb of Imposition, it takes ",lambda x:x.mod("wis")+5," damage"],lambda x:x.check("level",11) and x.check("checkclass","wizard") and x.check("feature","orb of imposition") and x.check("wis",15))
  ,feat([ft("ac",("",lambda x:x.check("weapongroups","staff")))],"Improved Staff of Defense","While you wield a staff, gain a +1 bonus to Fortitude, Reflex, and Will",lambda x:x.check("level",11) and x.check("checkclass","wizard") and x.check("feature","staff of defense") and x.check("con",13) and x.check("dex",13))
  ,feat([],"Improved Tome of Binding","While you wield a tome, creature creted by your arcane summoning powers appear with 10 temporary hit points",lambda x:x.check("level",11) and x.check("checkclass","wizard") and x.check("feature","tome of binding") and x.check("con",15))
  ,feat([],"Improved Tome of Readiness","1/encounter, use stored daily or utility power by using up power of its type (daily or utility) of its level or higher",lambda x:x.check("level",11) and x.check("checkclass","wizard") and x.check("feature","tome of readiness") and x.check("con",13) and x.check("wis",13))
  ,feat([],"Improved Wand of Accuracy","While you wield a wand, your arcane powers ignore enemies' cover (but not superior cover)",lambda x:x.check("level",11) and x.check("checkclass","wizard") and x.check("feature","wand of accuracy") and x.check("dex",15))
###Arcane Power: Epic Feats###
  ,feat([],"Explosive Spellcasting","Deal implement critical damage to any one target in blast or burst",lambda x:x.check("level",21) and x.check("checkclass",arcaneclasses, True))
#Quickened Spellcasting & Trusted Spellcasting need to have power choices
  ,feat([],"Quickened Spellcasting"
        ,"Use at-will power as minor action 1/encounter"
        ,lambda x:x.check("level",21) and x.check("checkclass",arcaneclasses, True))
  ,feat([],"Trusted Spellcasting"
        ,"One arcane encounter power that does not deal damage on a miss now deals half damage on a miss"
        ,lambda x:x.check("level",21) and x.check("checkclass",arcaneclasses, True))
###Arcane Power: Bard Epic Feats###
  ,feat([],"Bard Implement Expertise","Critical hit on a 19-20 with arcane power using a bard implement",lambda x:x.check("level",21) and x.check("checkclass","bard") and x.check("con",15) and x.check("int",15) and x.check("cha",21))
#Fix me!  This feat should do... something
  ,feat([],"Multiclass Mastery"
        ,"Gain two multiclass feats"
        ,lambda x:x.check("level",21) and x.check("checkclass","bard"))
  ,feat([],"Prescient Resurgence","Regain use of Virtue of Prescience when you spend an action point",lambda x:x.check("level",21) and x.check("checkclass","bard") and x.check("feature","virtue of prescience"))
  ,feat([],"Supreme Majesty","Target two creatures with every use of Majestic Word",lambda x:x.check("level",21) and x.check("checkclass","bard") and x.check("power","majestic word") and x.check("cha",19))
###Arcane Power: Sorcerer Epic Feats###
  ,feat([],"Fury of the Storm","Critical hit extra damage dice automatically deal max damage with sorcerer attack powers",lambda x:x.check("level",21) and x.check("checkclass","sorcerer") and x.check("feature","storm magic"))
  ,feat([],"Master of the Cosmic Cycle","Choose which phase to change to each time you change phase in the cosmic cycle",lambda x:x.check("level",21) and x.check("checkclass","sorcerer") and x.check("feature","cosmic magic"))
  ,feat([],"Ruthless Spellfury","1/turn, Use at-will power as free action after a critical hit",lambda x:x.check("level",21) and x.check("checkclass","sorcerer"))
  ,feat([],"Sorcerer Implement Expertise","Critical hit on a 19-20 with arcane power using a sorcerer implement",lambda x:x.check("level",21) and x.check("checkclass","sorcerer") and x.check("str",15) and x.check("dex",15) and x.check("cha",21))
###Arcane Power: Swordmage Epic Feats###
  ,feat([],"Binding Ensnarement","Target of Aegis of Ensnarement is immobilized until the end of your next turn",lambda x:x.check("level",21) and x.check("checkclass","swordmage") and x.check("power","aegis of ensarement"))
  ,feat([],"Charging Aegis","Mark a target as free action after hitting with a charge.  Mark penalty is -3 for that target.",lambda x:x.check("level",21) and x.check("checkclass","swordmage") and x.check("feature","swordmage aegis"))
  ,feat([],"Extended Aegis","You can use your Swordmage Aegis when the target is up to 20 squares away",lambda x:x.check("level",21) and x.check("checkclass","swordmage") and x.check("feature","swordmage aegis"))
  ,feat([],"Shared Warding","While your swordmage warding is active, adjacent allies gain a +1 bonus to AC",lambda x:x.check("level",21) and x.check("checkclass","swordmage") and x.check("feature","swordmage warding"))
###Arcane Power: Warlock Epic Feats###
  ,feat([],"Curse of Doom Ensured","When you attack a cursed enemy, that enemy grants combat advantage to your next ally who attacks it before your next turn",lambda x:x.check("level",21) and x.check("checkclass","warlock") and x.check("feature","warlock's curse"))
  ,feat([],"Ephemeral Stride","With Shadow Walk concealment, move through enemy spaces and gain insubstantial against their opportunity attacks",lambda x:x.check("level",21) and x.check("checkclass","warlock") and x.check("feature","shadow walk"))
#Fix me!  Needs to have a power choice
  ,feat([],"Vestige Mastery"
        ,"Daily vestige may be chosen as a primary vestige"
        ,lambda x:x.check("level",21) and x.check("checkclass","warlock") and x.check("feature","vestige pact"))
  ,feat([],"Warding Curse","+2 to defenses against enemies effected by your curse",lambda x:x.check("level",21) and x.check("checkclass","warlock") and x.check("feature","warlock's curse"))
  ,feat([],"Warlock Implement Expertise","With a warlock implement using an arcane power, score a critical hit on 19-20",lambda x:x.check("level",21) and x.check("con",17) and x.check("cha",17) and x.check("checkclass","warlock"))
###Arcane Power: Wizard Epic Feats###
  ,feat([],"Focused Wizardry","+2 to attack if only one target is in area of blast or burst",lambda x:x.check("level",21) and x.check("checkclass","wizard"))
  ,feat([],"Nightmare Wizardry","Target dazed until end of your next turn on critical hit with arcane illusion power",lambda x:x.check("level",21) and x.check("cha",17) and x.check("checkclass","wizard"))
  ,feat([],"Vengeful Summoner",["Enemies adjacent to your summoned creatures take 2d10+",CONMOD," damage when the summoned creatures die"],lambda x:x.check("level",21) and x.check("con",17) and x.check("checkclass","wizard"))
  ,feat([],"Wizard Implement Expertise","With a wizard implement using an arcane power, score a critical hit on 19-20",lambda x:x.check("level",21) and x.check("dex",15) and x.check("int",21) and x.check("wis",15) and x.check("checkclass","wizard"))
])
allFeatDict["Martial Power"]=addFeats([
  feat([ft("init",("feat",2))],"Martial Alacrity","+2 to initiative rolls, during first turn can shift as a minor action",lambda x: x.check("dex",15) and x.check("checkclass",martialclasses,True))
  ,feat([],"Martial Freedom","+5 to saving throws against the slowed and immobilized conditions",lambda x: x.check("wis",13) and x.check("training","endurance") and x.check("checkclass",martialclasses,True))
###Martial Power: Fighter###
  ,feat([],"Bloodied Invigoration","Invigorating powers grand +2 temporary hp when bloodied",lambda x: x.check("con",13) and x.check("checkrace","dragonborn") and x.check("checkclass","fighter"))
  ,feat([],"Bracing Breath","+1 to attack with invigorating powers after using dragon breath until end of next turn",lambda x: x.check("con",13) and x.check("checkrace","dragonborn") and x.check("checkclass","fighter"))
  ,feat([],"Deep Gash","Enemy takes -2 to saving throws against ongoing damage",lambda x: x.check("con",15) and x.check("checkclass","fighter"))
  ,feat([],"Defensive Resilience","+1 to all defenses with second wind when bloodied",lambda x: x.check("con",13) and x.check("wis",13) and x.check("checkclass","fighter"))
  ,feat([],"Devoted Challenge",["+", WISMOD, " bonus to attacks rolls and damage to attacks granted by combat challenge"],lambda x: x.check("checkrace","dwarf") and x.check("feature","combat challenge") and x.check("checkclass","fighter"))
  ,feat([],"Dirty Fighting","+4 melee damage against surprised enemies",CHECK("checkclass",["fighter","rogue"]))
  ,feat([],"Dragging Flail","When using a flail, slide enemy 1 square when knocking it prone",lambda x: x.check("dex",15) and x.check("checkclass","fighter"))
  ,feat([ft("invigoratingHP",("feat",raising(2,10)))],"Dwarf Stoneblood",["+", raising(2,10)," feat bonus to temporary HP granted from using an invigorating power."],lambda x: x.check("checkrace","dwarf") and x.check("feature","battlerager vigor") and x.check("checkclass","fighter"))
  ,feat([ft(["light bladedamage","heavy bladedamage"],["",lambda x:x.inventory.dualwield() and ("light blade" in x.inventory.equipgroups(0) or "heavy blade" in x.inventory.equipgroups(0)) and ("light blade" in x.inventory.equipgroups(1) or "heavy blade" in x.inventory.equipgroups(1))])],"Fey Blades","+1 damage with blade in each hand",lambda x: x.check("checkrace","eladrin") and x.check("feature","tempest technique") and x.check("checkclass","fighter"))
  ,feat([],"Group Assault","Allies gain +1 damage against your marked targets",lambda x: x.check("checkrace","half-elf") and x.check("checkclass","fighter"))
  ,feat([],"Halfling Stalwart","+1 to attack rolls against Large or larger marked targets",lambda x: x.check("checkrace","halfling") and x.check("checkclass","fighter"))
  ,feat([ft("invigoratingHP",("feat",raising(1,10)))],"Improved Vigor",["+", raising(1,10)," feat bonus to temporary HP granted from using an invigorating power."],lambda x: x.check("training","endurance") and x.check("checkclass","fighter"))
  ,feat([],"Keeper of Storm","Deal thunder or lightning damage when using stormsoul",lambda x: x.check("checkrace","genasi") and x.check("feature","combat challenge") and x.check("checkclass","fighter"))
  ,feat([],"Lingering Wrath","Bonuses from Infernal Wrath last as long as your mark",lambda x: x.check("checkrace","tiefling") and x.check("feature","combat challenge") and x.check("checkclass","fighter"))
  ,feat([ft("earthshockattack",("feat",1))],"Master of Rumbling Earth",["+1 to attack rolls with earthshock, and deal ",STRMOD," damage to targets knocked prone by Earthshock"],lambda x: x.check("checkrace","genasi") and x.check("checkclass","fighter"))
  ,feat([],"Offensive Resilience","+1 to attack roll after using second wind when bloodied",lambda x: x.check("dex",13) and x.check("wis",13) and x.check("checkclass","fighter"))
  ,feat([],"Opportunistic Accuracy","Retain Elven Accuracy when you miss",lambda x: x.check("wis",13) and x.check("checkrace","elf") and x.check("checkclass","fighter"))
  ,feat([],"Polearm Momentum","Knock enemy pushed or slid at least 2 squares prone with a polearm",lambda x: x.check("dex",15) and x.check("wis",15) and x.check("checkclass","fighter"))
  ,feat([],"Reaping Blade","Shift as a minor action when you drop an enemy",lambda x: x.check("dex",15) and x.check("checkclass","fighter"))
  ,feat([],"Shield Defense","+1 AC and Reflex when power requiring shield hits",lambda x: x.check("wis",13) and x.check("checkclass","fighter"))
  ,feat([],"Sideways Defense","Adjacent allies gain +1 defense against marked enemy",lambda x: x.check("checkrace","human") and x.check("feature","combat challenge") and x.check("checkclass","fighter"))
  ,feat([],"Surprising Charge","+1[W] damage on charge with light blade or spear and combat advantage",lambda x: x.check("dex",17) and x.check("checkclass",["fighter","rogue"]))
  ,feat([],"Take Measure","+2 to all defenses against target hit with melee critical hit",lambda x: x.check("wis",15) and x.check("checkclass","fighter"))
  ,feat([],"Thunder Hammer","Enemy takes -2 to saving throws against conditions delivered with hammer or mace",lambda x: x.check("con",15) and x.check("checkclass","fighter"))
  ,feat([],"Victor's Confidence","+2 to saving throws after reducing an enemy to 0 hp",lambda x: x.check("con",15) and x.check("checkclass","fighter"))
###Martial Power: Ranger###
  ,feat([ft("beast"+skill,["feat",jackoftrades(skill,False)]) for skill in allskills.keys()],"Beast Guidance","Your beast gains a +2 feat bonus to any skill in which you are trained",lambda x:x.check("checkclass","ranger") and x.check("feature","beast mastery"))
  ,feat([],"Beast Protector","If an enemy makes a melee attack against your beast companion, it provokes an attack of opportunity from you.",lambda x:x.check("checkclass","ranger") and x.check("feature","beast mastery"))
  #beast training
  ,feat([]
        ,"Beast Training"
        ,"Your beast companion gains training in a skill."
        ,lambda x:x.check("checkclass","ranger") and x.check("feature","beast mastery"))
  ,feat([],"Breath-Resistant Beast",["Your companion gains resist ",lambda x: x.statret("dragonbreathelement")," ",lambda x: 5+x.statret("level")/2],lambda x:x.check("checkclass","ranger") and x.check("checkrace","dragonborn") and x.check("feature","beast mastery"))
  ,feat([],"Brutal Accuracy",["Deal an extra 1d6+",WISMOD," damage with successful Elven Accuracy reroll against your quarry"],lambda x:x.check("checkclass","ranger") and x.check("checkrace","elf") and x.check("feature","hunter's quarry"))
  ,feat([],"Camouflage","When you have any cover or concealment outdoors, gain a +5 feat bonus to stealth checks",lambda x:x.check("checkclass","ranger") and x.check("training","stealth"))
  ,feat([],"Coordinated Opportunity","Gain a +2 bonus to damage if your beast is adjacent to the target of your opporunity attack",lambda x:x.check("checkclass","ranger") and x.check("feature","beast mastery"))
  ,feat([],"Darkfire Targeting",["Deal an extra ",WISMOD," damage with sneak attack or hunter's quarry against target of your Darkfire power"] ,lambda x:x.check("checkclass",["ranger","rogue"],True) and x.check("checkrace","drow"))
  ,feat([],"Drow Beast Mastery","Beast can see through your Cloud of Darkness",lambda x:x.check("checkclass","ranger") and x.check("checkrace","drow") and x.check("feature","beast mastery"))
  ,feat([],"Elven Beast Mastery","Beast companion ignores difficult terrain when shifting and Elven Accuracy can be used for beast's attack",lambda x:x.check("checkclass","ranger") and x.check("checkrace","elf") and x.check("feature","beast mastery"))
  ,feat([],"Expert Tracker","+5 to perception checks to find tracks and for others to find your tracks",lambda x: x.check("wis",13) and x.check("training","perception") and x.check("checkclass","ranger"))
  ,feat([ft("beastorigin","fey")],"Feyborn Companion","Your beast companion gains the Fey origin, +5 bonus to saves vs. charm effects, and can fey step when you do",lambda x:x.check("checkclass","ranger") and x.check("checkrace","eladrin") and x.check("feature","beast mastery"))
  ,feat([],"Fiendish Companion",["Your beast compainion gainst resistance to fire ",lambda x: 5+x.statret("level")/2],lambda x:x.check("checkclass","ranger") and x.check("checkrace","tiefling") and x.check("feature","beast mastery"))
  ,feat([],"Group Quarry","Allies gain a +1 bonus to damage rolls against your quarry",lambda x:x.check("checkclass","ranger") and x.check("checkrace","half-elf") and x.check("feature","hunter's quarry"))
  ,feat([ft("beastac",["feat",1]),ft("beastfort",["feat",1]),ft("beastref",["feat",1]),ft("beastwill",["feat",1])],"Human Beast Mastery","Your beast companion gains a +1 bonus to all defenses",lambda x:x.check("checkclass","ranger") and x.check("checkrace","human") and x.check("feature","beast mastery"))
  ,feat([ft("swiftcurrentmove",["",2]),ft("windwalkermove",["",2])],"Hunter of Wind and Wave","+2 movement with Swiftcurrent or Windwalker powers",lambda x:x.check("checkclass","ranger") and x.check("checkrace","genasi"))
  ,feat([],"Hunter's Aim","Ignore quarry's cover or concealment",lambda x:x.check("checkclass","ranger") and x.check("feature","hunter's quarry"))
  ,feat([],"Lucky Skirmisher","Enemies must roll twice and take lower result on opportunity attacks against you when you run",lambda x:x.check("checkclass",["ranger","rogue"],True) and x.check("checkrace","halfling"))
  ,feat([],"Nimble Companion","Your beast companion gains +2 AC vs. opportunity attacks and can benefit from Second Chance",lambda x:x.check("checkclass","ranger") and x.check("checkrace","halfling") and x.check("feature","beast mastery"))
  ,feat([],"Predatory Action","Deal Hunter's Quarry damage again during extra action from action point",lambda x:x.check("checkclass","ranger") and x.check("feature","hunter's quarry"))
  ,feat([],"Prime Strike","+1 to melee attack rolls if no other creatures are within 3 squares of target",CHECK("checkclass","ranger"))
  ,feat([],"Secure Encampment",["Allies gain +",WISMOD," bonus to Perception and Stealth during an extended rest"],lambda x:x.check("checkclass","ranger") and x.check("wis",13) and x.check("training",["nature","perception","stealth"],False))
  ,feat([ft("beasthp",["feat",lambda x:x.statret("level")*(x.inventory.beast()=="boar")])],"Thundertusk Companion","Your boar's HP increase by your level",lambda x:x.check("checkclass","ranger") and x.check("checkrace","dwarf") and x.check("feature","beast mastery"))
  ,feat([],"Vengeful Beast","Beast gainst +1 to attack and damage rolls against quarry when quarry damages you",lambda x:x.check("checkclass","ranger") and x.check("feature","hunter's quarry") and x.check("feature","beast mastery"))
###Martial Power: Rogue###
  ,feat([],"Aggresive Assault","Slide targets you hit that have not yet acted 1 square",lambda x: x.check("feature",["first strike","brutal scoundrel"],False) and x.check("checkclass","rogue"))
  ,feat([],"Ankle Cutter","Cause Large or larger Sneak Attack targets to be slowed",lambda x: x.check("checkrace","halfling") and x.check("feature","sneak attack") and x.check("checkclass","rogue"))
  ,feat([],"Brutal Teamwork","+2 damage when adjacent to an ally",lambda x: x.check("str",15) and x.check("checkrace","dragonborn") and x.check("checkclass","rogue"))
  ,feat([],"Brutal Wound","Deal additional ongoing damage with sneak attack",lambda x: x.check("feature",["brutal scoundrel", "sneak attack"], False) and x.check("checkclass","rogue"))
  ,feat([],"Cunning Ambusher",["Combine Infernal Wrath with combat advantage for a +",INTMOD," bonus to attack and damage"],lambda x: x.check("checkrace","tiefling") and x.check("checkclass","rogue"))
  ,feat([],"Dwarf Trapsmith","+4 feat bonus to perception checks to find traps and thievery checks to open locks or disable traps",lambda x: x.check("checkrace","dwarf") and x.check("checkclass","rogue"))
  ,feat([],"Group Rattling","Allies gain a +1 bonus to attacks against enemies penalized by your rattling power",lambda x: x.check("checkrace","half-elf") and x.check("training","intimidate") and x.check("checkclass","rogue"))
  ,feat([],"Into the Fray","+1 to speed and melee attack rolls in surprise round",lambda x: x.check("feature","first strike") and x.check("checkclass","rogue"))
  ,feat([ft("light bladelegal","longswordname")],"Longsword Finesse","Use a longsword for sneak attack and rogue powers.  Reduce sneak damage by 1 die size with a longsword.",lambda x: x.check("checkrace","eladrin") and x.check("checkclass","rogue"))
  ,feat([],"Rash Sneak Attack","Can choose to take a +2 bonus on sneak damage, but grant combat advantage to all enemies",lambda x: x.check("checkrace","human") and x.check("feature","sneak attack") and x.check("checkclass","rogue"))
  ,feat([],"Rattling Wrath","Using Infernal Wrath with rattling power inceases penalty to -4.  Infernal Wrath not expended on critical.",lambda x: x.check("cha",15) and x.check("checkrace","tiefling") and x.check("checkclass","rogue"))
  ,feat([],"Reckless Scramble","When a power lets you shift, you can instead move the distance + 2 squares",lambda x: x.check("feature","artful dodger") and x.check("checkclass","rogue"))
  ,feat([],"Ruthless Injury","Enemies at -2 saves against blind, immobilized, slowed, or weakened when delivered with club or mace and sneak attack",lambda x: x.check("feature",["ruthless ruffian","sneak attack"],False) and x.check("checkclass","rogue"))
  ,feat([],"Slaying Action","Deal sneak attack again in a round when spending an action point for an extra action",lambda x: x.check("feature","sneak attack") and x.check("checkclass","rogue"))
  ,feat([],"Sneaky Accuracy","Retain Elven Accuracy if you miss on the reroll on a sneak attack",lambda x: x.check("checkrace","elf") and x.check("feature","sneak attack") and x.check("checkclass","rogue"))
  ,feat([],"Speedy Response","Gain a +1 bonus to speed for that move each time you are hit while moving",lambda x: x.check("dex",15) and x.check("checkclass","rogue"))
  ,feat([ft("light bladelegal","mace")],"Street Thug","Use a mace for sneak attack and rogue powers.  Reduce sneak damage by 1 die size with a mace.",lambda x: x.check("str",13) and x.check("con",13) and x.check("checkclass","rogue"))
  ,feat([],"Trap Sense","+2 feat bonus to all defenses against attacks by traps and to perception checks to find traps",lambda x: x.check("wis",13) and x.check("checkclass","rogue"))
  ,feat([ft("light bladelegal",[x+"name" for x in groupList(["axe","one-handed"])+groupList(["pick","one-handed"])+groupList(["hammer","one-handed"])])],"Tunnel Stalker","Use a one-handed axe, hammer, or pick for sneak attack and rogue powers.  Reduce sneak damage by 1 die size with those weapons.",lambda x: x.check("str",13) and x.check("con",13) and x.check("checkrace","dwarf") and x.check("checkclass","rogue"))
  ,feat([ft("hand crossbownewkey","off-hand")],"Two-Fisted Shooter","Treat the hand crossbow as an off-hand weapon, reload one-handed as free action, extra attack with hand crossbow on crit",lambda x: x.check("checkclass","rogue"))
  ,feat([],"Wielder of Piercing Flame","Firepulse ignores resistance or immunity when you have combat advantage",lambda x: x.check("checkrace","genasi") and x.check("checkclass","rogue"))
###Martial Power: Warlord Feats###
  ,feat([],"Bold Command","Allies gain +1 to attack rolls against enemy that misses you",lambda x: x.check("checkclass","warlord") and x.check("feature","bravura presence") and x.check("checkrace","halfling"))
  ,feat([],"Bolstering Inspiration",["Adjacent Inspiring Word target gains either saving throw or ",WISMOD," additional HP"],lambda x: x.check("checkclass","warlord") and x.check("checkrace","dwarf"))
  ,feat([],"Bravura Spirit","Bloodied ally gains either additional +2 to attack roll or +2 to speed from Bravura Presence",lambda x: x.check("checkclass","warlord") and x.check("feature","bravura presence") and x.check("checkrace","dragonborn"))
  ,feat([],"Command the Darkness","Change how much Cloud of Darkness obscures its area",lambda x: x.check("checkclass","warlord") and x.check("checkrace","drow"))
  ,feat([],"Fey Command","Ally can teleport 1 square before or after attacking with action point",lambda x: x.check("checkclass","warlord") and x.check("checkrace","eladrin") and x.check("feature","tactical presence"))
  ,feat([ft(["bravuraspeed","bravuraatk"],["",1])],"Improved Bravura","Ally gains +1 to attack rolls or speed with Bravura Presence",lambda x: x.check("checkclass","warlord") and x.check("feature","bravura presence"))
  ,feat([ft("inspiringpresencehp",["",2])],"Improved Inspiration","Ally gains +2 hp with Inspiring Presence",lambda x: x.check("checkclass","warlord") and x.check("feature","inspiring presence"))
  ,feat([ft("inspiringwordheal",["",CHAMOD])],"Improved Inspiring Word","Add cha modifier to Inspiring Word hp restored",lambda x: x.check("checkclass","warlord"))
  ,feat([ft(["resourcefulhp","resourcefuldmg"],["",2])],"Improved Resources","Ally gains +2 damage and +2 temporary HP from Resourceful Presence",lambda x: x.check("checkclass","warlord") and x.check("feaure","resourceful presence"))
  ,feat([ft("tacticalpresenceatk",["",1])],"Improved Tactics","Ally gains +1 to attack rolls with Tactical Presence",lambda x: x.check("checkclass","warlord") and x.check("feature","tactical presence"))
  ,feat([],"Inspired Defense","Ally gains +1 to all defenses with Inspiring Word",lambda x: x.check("checkclass","warlord") and x.check("checkrace","human"))
  ,feat([],"Inspired Tactics","Ally gains +1 to attack rolls when spending action point",lambda x: x.check("checkclass","warlord") and x.check("checkrace","half-elf") and x.check("feature","inspiring presence"))
  ,feat([],"Leading Fire","Allies gain +1 to ranged attack rolls against bow target",lambda x: x.check("checkclass","warlord") and x.check("checkrace","elf") and x.check("feature","combat leader"))
  ,feat([],"Lend Might","+1 to attack rolls of attacks you grant",lambda x: x.check("checkclass","warlord"))
  ,feat([],"Saving Inspiration","Ally gains saving throw with Inspiring Word, at cost of extra dice of healing",lambda x: x.check("checkclass","warlord"))
  ,feat([ft("inspiringwordheal",["",INTMOD])],"Tactical Inspiration","Add int modifier to Inspiring Word hp restored",lambda x: x.check("checkclass","warlord") and x.check("feature","eladrin"))
  ,feat([],"Unbalancing Wrath","Infernal Wrath target grants combat advantage",lambda x: x.check("checkclass","warlord") and x.check("checkrace","tiefling"))
###Martial Power: Paragon Feats###
  ,feat([],"Bloody Tenacity","+2 to all defenses when first bloodied",lambda x:x.check("level", 11) and x.check("checkclass",martialclasses, True) and x.check("checkrace","human"))
  ,feat([],"Dragonbreath Warrior",["1[W] extra ",lambda x: x.statret("dragonbreathelement")," damage on successful melee attack after Dragon Breath"],lambda x:x.check("level", 11) and x.check("checkclass",martialclasses, True) and x.check("checkrace","dragonborn"))
###Martial Power: Fighter Paragon Feats
  ,feat([ft("tempesttech",["",raising(1,20)])],"Agile Tempest","+1 damage with Tempest Technique",lambda x:x.check("level", 11) and x.check("dex",15) and x.check("feature","tempest technique") and x.check("checkclass","fighter"))
  ,feat([],"Avenging Spirit","Gain action point when ally is reduced to 0 or fewer HP.  You must use this before the end of your next turn.",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("",""))
  ,feat([ft("speed",["",lambda x:x.check("armortype","chainmail")])],"Chainmail Agility","Ignore speed penalty for chainmail",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("dex",15))
  ,feat([],"Combat Opening","Enable ally to attack your enemy instead of taking combat challenge attack",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("checkrace","half-elf") and x.check("feature","combat challenge"))
  ,feat([],"Daunting Challenge","Enemies you mark take -3 (instead of -2) to attacks that do not include you as a target",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("feature","daunting challenge"))
  ,feat([],"Draconic Arrogance",["Deal ",STRMOD," damage to enemies you push or knock prone."],lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("checkrace","dragonborn"))
  ,feat([],"Elemental Guardian","Racial trait improves when adjacent to an ally",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("con",15) and x.check("checkrace","genasi"))
  ,feat([],"Enduring Wallop",["Deal ongoing ",CONMOD," damage (or improve ongoing damage) with axe, hammer, or pick and fighter daily power."],lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("checkrace","dwarf"))
  ,feat([],"Fey Charge","Use Fey Step as part of charge.  If attack hits, Fey Step is not expended.",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("checkrace","eladrin"))
  ,feat([],"Fiendish Defender","Apply Infernal Wrath to marked enemy that hits your ally",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("checkrace","tiefling") and x.check("feature","combat challenge"))
  ,feat([],"Grit",["Gain ",CONMOD," temporary HP when you spend a healing surge to regain hit points"],lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("con",17))
  ,feat([],"Marked Scourge",["Once per round, add ",WISMOD," to damage against marked enemy."] ,lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("feature","combat challenge"))
  ,feat([ft("battleragedmg",["",raising(1,20)])],"Mighty Battlerage",["Increase damage bonus granted by Battlerage Vigor by ",raising(1,20)],lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("",""))
  ,feat([],"Opportunistic Archer","Use bow for attacks granted by Combat Challenge",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("checkrace","elf") and x.check("feature","combat challenge"))
  ,feat([],"Phalanx Warrior","Adjacent allies gain +1 AC when you wield shield",lambda x:x.check("level", 11) and x.check("checkclass",["fighter","warlord"],True) and x.check("proficiency",["heavy","light"]))
  ,feat([],"Reckless Attacker","Make basic attack as free action after first critical per turn; take -2 AC until end of your next turn",lambda x:x.check("level", 11) and x.check("checkclass","fighter"))
  ,feat([],"Stonefoot Reprisal","Enemy that pushes or slides you provokes opportunity attack",lambda x:x.check("level", 11) and x.check("checkclass","fighter") and x.check("checkrace","dwarf"))
###Martial Power: Ranger Paragon Feats###
  ,feat([],"Bleeding Precision","Deal ongoing 5 damage (or improve ongoing damage) with daily ranger power against quarry",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("feature","hunter's quarry"))
  ,feat([],"Darkhunter","Each enemy in Cloud of Darkness is designated as your quarry while they remain in your cloud",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("checkrace","drow") and x.check("feature","hunter's quarry"))
  ,feat([],"Distracting Companion","If quarry is adjacent to your beast when you hit, they suffer -2 to attack and damage against you and your beast",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("feature",["beast mastery","hunter's quarry"],False))
  ,feat([],"Halfling Beast Mastery","Beast companion gains Second Chance once per encounter",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("checkrace","halfling") and x.check("feature","beast mastery"))
  ,feat([],"Hunter's Advantage","Deal +2 damage against quarry with combat advantage",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("feature","hunter's quarry") and x.check("checkrace","elf"))
  ,feat([],"Hunter's Resurgence","Use second wind as free action when you drop your quarry, but do not gain the normal bonus to defenses",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("feature","hunter's quarry"))
  ,feat([],"Peternatural Senses","When you make a perception check, roll twice and use the higher result",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("training","perception"))
  ,feat([],"Prime Quarry","The bonus to attack rolls granted by Prime Shot inceases to +2 if the target is also your quarry",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("wis",15) and x.check("feature",["hunter's quarry","prime shot"],False))
  ,feat([],"Protective Beast","Whenever your beast companion is adjacent to you, you gain a +1 bonus to AC",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("feature","beast mastery"))
  ,feat([ft("beasthp",["",lambda x:x.mod("wis",5)]),ft("beastsurges",["",1])],"Sturdy Beast",["Your beast companion gains one additional healing surge and ",lambda x:x.mod("wis")+5," additional hit points"],lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("",""))
  ,feat([],"Wrathful Hunter","Gain a +3 instead of +1 when using Infernal Wrath against your quarry",lambda x:x.check("level", 11) and x.check("checkclass","ranger") and x.check("checkrace","tiefling") and x.check("feature","hunter's quarry"))
###Martial Power: Rogue Paragon Feats
  ,feat([],"Avandra's Gift","If enemy misses when you use Second Chance you gain combat advantage for the next attack against them",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("checkrace","halfling"))
  ,feat([],"Bleeding Backstab","Deal ongoing 5 damage (or improve ongoing damage) with daily rogue power when using Sneak Attack",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("feature","sneak attack"))
  ,feat([],"Cull the Weak","+2 bonus to melee damage rolls with combat advantage against bloodied target",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("cha",15))
  ,feat([],"Darkjumper","Teleport within Cloud of Darkness as free action when you create the cloud",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("checkrace","drow"))
  ,feat([],"Evasive Footwork","+1 to AC and Reflex when you shift 2 or more squares",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("dex",17) and x.check("cha",15))
  ,feat([],"Fey Gambit","Gain combat advantage against enemy you fey step to",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("checkrace","eladrin"))
  ,feat([],"Group Flanking","Allies gain combat advantage against enemy you flank",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("checkrace","half-elf"))
  ,feat([],"Infernal Sneak Attack","Combine Sneak Attack with Infernal Wrath for extra die of sneak damage",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("checkrace","tiefling") and x.check("feature","sneak attack"))
  ,feat([],"Opportunistic Sneak Attack","Sneak Attack with opportunity attack slows target",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("feature","sneak attack"))
  ,feat([],"Prime Slayer","+2 ranged damage if you are closest to target",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("checkrace","elf"))
  ,feat([],"Rogue Weapon Mastery","Treat daggers and shuriken as high crit weapons",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("feature","rogue weapon talent"))
  ,feat([],"Roundabout Charge","Each square of movement need not bring you closer to target of your charge, but must charge from at least 3 squares away",lambda x:x.check("level", 11) and x.check("checkclass","rogue") and x.check("training","acrobatics"))
###Martial Power: Warlord Paragon Feats###
  ,feat([],"Bloody Inspiration","Second ally benefits from Inspiring Word if you are bloodied and do not target self",lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("checkrace","dragonborn"))
  ,feat([],"Defensive Surge","Adjacent ally also gains +2 defense bonus when you use second wind",lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("con",15))
  ,feat([],"Elemental Companions","Adjacent allies share energy resistance from your elemental manifestation",lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("checkrace","genasi"))
  ,feat([],"Fey Tactics","Ally within 5 squares can use Fey Step when you do",lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("checkrace","eladrin"))
  ,feat([],"Impetuous Charger","Allies gain combat advantage against enemy you charge",lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("cha",15))
  ,feat([],"Reliable Resources",["Ally gains ",CHAMOD," temporary HP if they spend an action point and do not attack."],lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("feature","resourceful presence"))
  ,feat([],"Steadfast Tactics","Target of Inspiring Word reduces effects of pull, push, or slide by 1 until end of encounter",lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("checkrace","dwarf"))
  ,feat([],"Vital Inspiration",["Allies regain ",CHAMOD," more Hp with second wind"],lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("checkrace","half-elf"))
  ,feat([],"Warlord's Formation","Use aid another action to grant same bonus to two allies simultaneously",lambda x:x.check("level", 11) and x.check("checkclass","warlord") and x.check("int",17))
###Martial Power: Epic Feats###
  ,feat([],"Darkfire Warrior","Regain use of Darkfire after reducing target to 0 hp",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("checkrace","drow"))
  ,feat([],"Dragon Warrior","Regain Dragon Breath when first bloodied",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("con",17) and x.check("checkrace","dragonborn"))
  ,feat([],"Elemental Warrior","Regain use of racial power after scoring critical hit",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("checkrace","genasi"))
  ,feat([],"Epic Recovery","Use second wind twice per encounter",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("con","19"))
  ,feat([],"Feywild Warrior","Teleport yourself and your target after using daily power",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("dex",17) and x.check("checkrace","eladrin"))
  ,feat([],"Fortune's Warrior","Gain combat advantage after using second chance",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("dex",17) and x.check("checkrace","halfling"))
  ,feat([],"Hawkeye Warrior","+1 to attack rolls after using elven accuracy",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("wis",17) and x.check("checkrace","elf"))
  ,feat([],"Infernal Warrior","Retaliate against a critical hit with infernal wrath as free action",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("cha",17) and x.check("checkrace","tiefling"))
  ,feat([PowerMod(["martial","encounter"],["addkey","invigorating"],"Add invigorating keyword to ","")],"Invigorating Exploit","",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True))
  ,feat([],"Martial Mastery","Regain encounter power when spending action point for extra action",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True))
  ,feat([],"Martial Resolve","Make saving throws against dazed, slowed, stunned, weakened, and immobilized at both start and end of turn",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("wis",15) and x.check("training","endurance"))
  ,feat([PowerMod(["martial","encounter"],["addkey","rattling"],"Add rattling keyword to ","")],"Rattling Exploit","",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True))
  ,feat([],"Stoneheart Warrior","Use second wind as free action",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("checkrace","dwarf") and x.check("con",17))
  ,feat([],"Timely Revival","Make death saving throws at start of your turn",lambda x:x.check("level", 21) and x.check("checkclass",martialclasses,True) and x.check("checkrace","human"))
  ,feat([],"Channeled Battlerage","Lose all current temporary HP to reroll damage",lambda x:x.check("level", 21) and x.check("checkclass","fighter") and x.check("con",17) and x.check("feature","battlerager vigor"))
  ,feat([],"Knock-Back Swing","Opportunity attacks with axe, hammer, mace, or pick push target 1 square",lambda x:x.check("level", 21) and x.check("checkclass","fighter") and x.check("con",17))
  ,feat([],"Mobile Warrior","Shift 1 square after attacking with certain flail, heavy blade, light blade, or spear",lambda x:x.check("level", 21) and x.check("checkclass","fighter") and x.check("dex",17))
  ,feat([PowerMod(["fighter","encounter"],["addkey","reliable"],"Add reliable keyword to ","")],"Practiced Reliability","",lambda x:x.check("level", 21) and x.check("checkclass","fighter"))
  ,feat([],"Reaching Whirlwind","Expand fighter power bursts to burst 2 with reach weapon",lambda x:x.check("level", 21) and x.check("checkclass","fighter") and x.check("dex",15) and x.check("wis",15))
  ,feat([],"Rending Tempest","Enemy takes 1[w] (off-hand) extra damage from attacks following a hit with two-weapon attack",lambda x:x.check("level", 21) and x.check("checkclass","fighter") and x.check("dex",17))
  ,feat([],"Tactical Insight","Allies gain +2 damage against marked enemy",lambda x:x.check("level", 21) and x.check("checkclass","fighter") and x.check("checkrace","half-elf"))
  ,feat([],"Unstoppable Charge","Your turn does not automatically end after a charge",lambda x:x.check("level", 21) and x.check("checkclass","fighter") and x.check("str",21) and x.check("con",17))
  ,feat([],"Correcting Aim","+2 to attack rolls against your quarry when you miss",lambda x:x.check("level", 21) and x.check("checkclass","ranger") and x.check("feature","hunter's quarry"))
  ,feat([],"Improved Prime Shot","Prime Shot attack roll bonus increase to +2",lambda x:x.check("level", 21) and x.check("checkclass","ranger") and x.check("feature","prime shot") and x.check("wis",17))
  ,feat([],"Peerless Hunter","Designate two targets as your quarry",lambda x:x.check("level", 21) and x.check("checkclass","ranger") and x.check("feature","hunter's quarry") and x.check("wis",17))
  ,feat([],"Prime Hunter","+1 to melee attack rolls against isolated enemies",lambda x:x.check("level", 21) and x.check("checkclass","ranger"))
  ,feat([],"Quick Beast Command","Command beast to attack as minor action",lambda x:x.check("level", 21) and x.check("checkclass","ranger") and x.check("feature","beast mastery") and x.check("wis",17))
  ,feat([],"Staggering Shot","Slow quarry instead of dealing Hunter's Quarry damage",lambda x:x.check("level", 21) and x.check("checkclass","ranger") and x.check("feature","hunter's quarry"))
  ,feat([],"Surprise Action","Full round of actions during surprise round",lambda x:x.check("level", 21) and x.check("checkclass","ranger") and x.check("wis",17))
  ,feat([],"Artful Provocation","Missed opportunity attack gives you combat advantage against attacker",lambda x:x.check("level", 21) and x.check("checkclass","rogue") and x.check("cha",17) and x.check("feature","artful dodger"))
  ,feat([],"Brutal Advantage",["+",STRMOD," to damage when you have combat advantage and do not sneak attack"],lambda x:x.check("level", 21) and x.check("checkclass","rogue") and x.check("feature","brutal scoundrel") and x.check("str",17))
  ,feat([],"Lasting Advantage","Target grants combat advantage to you after a critical hit",lambda x:x.check("level", 21) and x.check("checkclass","rogue") )
  ,feat([],"One with Shadow","Move through enemies' spaces while hidden",lambda x:x.check("level", 21) and x.check("checkclass","rogue"))
  ,feat([],"Ruthless Terror","Rattling attacks apply -1 penalty on a miss",lambda x:x.check("level", 21) and x.check("checkclass","rogue") and x.check("str",17) and x.check("training","intimidate"))
  ,feat([PowerMod(["rogue","encounter"],["special",""],"Can deal Sneak Attack damage to all targets of ","")],"Whirlwind Sneak Attack","",lambda x:x.check("level", 21) and x.check("checkclass","rogue") and x.check("feature","sneak attack"))
  ,feat([],"Action Grant","Ally gains one of your action points when initiative is rolled",lambda x:x.check("level", 21) and x.check("checkclass","warlord") and x.check("int",15) and x.check("cha",15) and x.check("feature","resourceful presence"))
  ,feat([],"Aggressive Leadership","Bloodied allies gain +2 damage",lambda x:x.check("level", 21) and x.check("checkclass","warlord") and x.check("cha",19))
  ,feat([],"Bold Spirit",["Gain ",CHAMOD," temporary hp after being hit when bloodied or granting combat advantage"],lambda x:x.check("level", 21) and x.check("checkclass","warlord") and x.check("feature","bravura presence"))
  ,feat([],"Call to Glory",["Ally gains ",lambda x:x.statret("level")/2," temporary hp when they hit with an attack you grant"],lambda x:x.check("level", 21) and x.check("checkclass","warlord") and x.check("cha",17))
  ,feat([],"Protective Leadership","Bloodied allies gain +1 to all defenses",lambda x:x.check("level", 21) and x.check("checkclass","warlord") and x.check("int",19))
  ,feat([],"Supreme Inspiration","Heal two targets with Inspiring Word",lambda x:x.check("level", 21) and x.check("checkclass","warlord") and x.check("cha",19))
  ,feat([],"Tactical Cunning","Allies you slide gain +2 to AC",lambda x:x.check("level", 21) and x.check("checkclass","warlord") and x.check("int",17))

])
allFeatDict["Primal Power"]=addFeats([
  feat([ft("thievery",["feat",2])],"Audacious Crow","+2 to Thievery, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([],"Bloodied Spear","+1 to attack, damage with opportunity attacks, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([],"Courageous Heart","+2 to saving throws vs. charm or fear, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([ft("surge",["feat",2])],"Enduring Mountain","+2 extra HP with healing surge, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([ft("intimidate",["feat",2])],"Fearsome Host","+2 to Intimidate, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([ft("athletics",["feat",2])],"Four Winds","+2 to Athletics, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([],"Herbalist","+5 to Heal checks for disease, gain Brew Potion ritual at level 5",lambda x: x.check("training",["dungeoneering","nature"],True) and x.check("training","heal"))
  ,feat([],"Inner Compass","Roll twice for Dungeoneering and Nature checks in natural environment",lambda x: x.check("training",["dungeoneering","nature"],True))
  ,feat([ft("stealth",["feat",2])],"Midnight Stalker","+2 to Stealth, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([ft("initiative",["feat",2])],"Swift Jaguar","+2 to Initiative, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([ft("perception",["feat",2])],"Watchful Owl","+2 to Perception, +1 for each ally in 10 squares with this feat, max +5")
  ,feat([],"Wild Sage","+5 to Nature knowledge checks and natural monster knowledge checks, gain a ritual",lambda x: x.check("training","nature"))
###Primal Power: Any Primal###
  ,feat([ft("nature",["feat",2])],"Animal Empathy","+2 to Nature checks; substitute Nature for Insight when dealing with beasts",lambda x: x.check("checkclass",primalclasses,True) and x.check("training","nature"))
  ,feat([],"Deep Sage","+5 to Dungeoneering knowledge and aberrant creature monster knowledge checks, gain fluency in Dark Speech",lambda x: x.check("checkclass",primalclasses,True) and x.check("training","dungeoneering"))
  ,feat([],"Eyes of the Spirits","Allies affected by Group Awareness ignore -2 concealment penalty",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","elf"))
  ,feat([],"Feral Fey Step","Use Fey Step again the first time you are bloodied",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","eladrin"))
  ,feat([],"Focus the Spirits' Lives","Roll d10 for Memory of a Thousand Lifetimes for Nature checks, beast form attack rolls, and spirit power attack rolls",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","deva"))
  ,feat([],"Half-Elf Spirit Seeker","+1 to all defenses for you and allies when you are first bloodied; +1 to Insight and Nature for allies",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","half-elf"))
  ,feat([ft("light armor",["light armor",lambda x:2*x.check("armortype","hide")])],"Hide Armor Expertise","Can use +2 instead of Dex or Int for determining AC in hide armor",lambda x: x.check("checkclass",primalclasses,True) and x.check("con",15) and x.check("proficiency","hide"))
  ,feat([],"Human Nature Lore","Roll twice for Endurance or Nature checks",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","human"))
  ,feat([],"Longtooth Spirit Shifter","Longtooth Shifting regeneration increases by 2",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","shifter, longtooth"))
  ,feat([],"Manifest Healing","Gain 5 temporary HP when you use a racial power",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","genasi"))
  ,feat([],"Markings of the Elements","Give up resistance to all damage from stone's endurance to gain 5 higher resistance to chosen damage type",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","goliath"))
  ,feat([],"Markings of the Predator","+1 to all defenses when you bloody a creature",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","goliath"))
  ,feat([],"Primal Halfling Counterattack",["+",lambda x:raising(2,10)(x)+2," damage against second chance target until end of next turn."],lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","halfling"))
  ,feat([],"Primal Resilience",["+",CONMOD," extra temporary HP from Half-Orc Resilience"],lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","half-orc"))
  ,feat([],"Razorclaw Spirit Shifter","Shift 1 when damaged by an attack vs. AC or Reflex while using razorclaw shifting",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","shifter, razorclaw"))
  ,feat([],"Reckless Charge","-2 AC for +1 to attack while charging",lambda x: x.check("checkclass",primalclasses,True))
  ,feat([],"Rite of Spirit's Blood","Attack roll bonus from Bloodhunt and Infernal Wrath increased to +2",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","tiefling"))
  ,feat([ft("intimidate",["feat",lambda x:x.statret("armorenchant")*x.check("armortype","hide")])],"Skins of the Slain","Bonus to intimidate checks equal to hide armor enhancement bonus",lambda x: x.check("checkclass",primalclasses,True) and x.check("proficiency","hide"))
  ,feat([ft("speed",["feat",1])],"Spider's Swiftness","+1 to speed, or +2 when affected by polymorph or rage power",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","drow"))
  ,feat([],"Spirits of Stealth","+3 damage against bloodied creature when you are hidden",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","gnome"))
  ,feat([],"Spirits of Stone","+2 to next attack roll when you use second wind",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","dwarf"))
  ,feat([],"Spirits of the Primal Dragons",["When first bloodied, your attacks deal 1d8 extra ",lambda x:x.statret("dragonbreathelement")," damage until end of your next turn."] ,lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","dragonborn"))
  ,feat([],"Staggering Smash","Push target 1 square when you daze or stun it with primal power",lambda x: x.check("checkclass",primalclasses,True))
  ,feat([],"Stone Step Spirits","Ignore 1 square of difficult terrain when you move, or all difficult terrain when you charge",lambda x: x.check("checkclass",primalclasses,True) and x.check("checkrace","dwarf"))
###Primal Power: Barbarian###
  ,feat([],"Bloody Triumph",["+",CHAMOD," damage to your or ally's next damage roll against enemy you bloody."],lambda x: x.check("checkclass","barbarian") and x.check("feature","thaneborn triumph"))
  ,feat([],"Elemental Barbarian","When you use firepulse or promise of storm racial power while raging, gain +2 to attack rolls until end of your next turn",lambda x: x.check("checkclass","barbarian") and x.check("checkrace","genasi"))
  ,feat([],"Fearsome Charge","When you hit with swift charge, you can push the target 1 square",lambda x: x.check("checkclass","barbarian") and x.check("feature","rageblood vigor"))
##Hurl Weapon##
  ,feat([],"Hurl Weapon","Can use any one-handed off-hand weapon as heavy thrown weapon, with range 5/10.",lambda x: x.check("checkclass","barbarian"))
  ,feat([],"Improvised Missile"
                 ,"Can use improvised melee weapons as heavy thrown weapons, with range 5/10.  +2 attacks and damage for this."
                 ,lambda x: x.check("checkclass","barbarian"))
  ,feat([],"Raging Bloodcut",["Reduce the damage of a rage power by ",raising(1,10),"[W] to add ",raising(5,10)," ongoing damage (save ends)."],lambda x: x.check("checkclass","barbarian"))
  ,feat([],"Swift Slayer",["When using Whirling Slayer to shift, shift ",DEXMOD, " squares, instead of just 2."],lambda x: x.check("checkclass","barbarian") and x.check("feature","whirling slayer"))
  ,feat([],"Targeted Assault","You gain a +2 bonus to attack rolls against any creature marked by you.",lambda x: x.check("checkclass","barbarian"))
  ,feat([ft("thunderbornWrathDamage",["",5])],"Thunderborn Rage","The damage of Thunderborn Wrath increases by 5.",lambda x: x.check("checkclass","barbarian") and x.check("feature","thunderborn wrath"))
###Primal Power: Druid###
  ,feat([],"Agile Form","Shift 1 when you use wild shape",lambda x: x.check("checkclass","druid") and x.check("power","wild shape"))
  ,feat([],"Druid of Darkness","+2 damage when you have combat advantage in beast form",lambda x: x.check("checkclass","druid") and x.check("power","wild shape") and x.check("checkrace","drow"))
  ,feat([],"Predator's Burst","While in beast form, +2 to speed, +1 to attack while charging",lambda x: x.check("checkclass","druid") and x.check("feature","primal predator") and x.check("power","wild shape"))
  ,feat([],"Quick Stow","Items change with you in beast form",lambda x: x.check("checkclass","druid") and x.check("power","wild shape"))
  ,feat([],"Stinging Swarm","While you're in beast form, enemies that damage you grant combat advantage to you",lambda x: x.check("checkclass","druid") and x.check("feature","primal swarm") and x.check("power","wild shape"))
  ,feat([],"Strong-Willed Summoning","Creatures you summon gain +1 to attack with instinctive actions",lambda x: x.check("checkclass","druid"))
  ,feat([],"Watchful Guardian","While you're in beast form, you and adjacent allies gain +2 to opportunity attack rolls",lambda x: x.check("checkclass","druid") and x.check("feature","primal guardian") and x.check("power","wild shape"))
  ,feat([],"Wild Bull Rush","While in beast form, +2 to bull rush attacks and use bull rush against any size target",lambda x: x.check("checkclass","druid") and x.check("power","wild shape"))
###Primal Power: Shaman###            
  ,feat([],"Fading Spirit","Spirit companion is hidden when you are hidden",lambda x: x.check("checkclass","shaman") and x.check("checkrace","gnome"))
  ,feat([],"Invigorating Spirit","Ally adjacent to spirit companion shifts 1 after you use healing spirit",lambda x: x.check("checkclass","shaman") and x.check("power","healing spirit"))
  ,feat([ft("spirit's fangsattack",["",2])],"Precise Fangs","+2 to attack roll when you use spirit's fangs",lambda x: x.check("checkclass","shaman") and x.check("feature","stalker spirit"))
  ,feat([],"Protector's Shield","When you hit with your Protector's Shield power, it deals 1d8 extra damage.",lambda x: x.check("checkclass","shaman") and x.check("feature","protector spirit"))
  ,feat([],"Rejuvenating Spirit","When you use Healing Spirit, the target can make a saving throw.",lambda x: x.check("checkclass","shaman") and x.check("power","healing spirit"))
  ,feat([],"Resilient Spirit","Your spirit companion gains a +2 bonus to all defenses.",lambda x: x.check("checkclass","shaman"))
  ,feat([],"Spirit Tribe","Allies in 5 squares gain +2 to skill with Speak with Spirits",lambda x: x.check("checkclass","shaman") and x.check("power","speak with spirits"))
  ,feat([],"Spirit's Fey Step","When you use Fey Step, teleport your spirit companion the same number of squares",lambda x: x.check("checkclass","shaman") and x.check("checkrace","eladrin"))
  ,feat([],"Strengthening Spirit",["When using Healing Spirit, all allies adjacent to your spirit companion gain ",WISMOD," temporary HP"],lambda x: x.check("checkclass","shaman") and x.check("power","healing spirit"))
  ,feat([ft("call spirit companionaction","free")],"Sudden Call","Call Spirit Companion is a free action on your turn.",lambda x: x.check("checkclass","shaman"))
  ,feat([],"Vigorous Spirit",["Target heals ",WISMOD," extra HP with Healing Spirit"],lambda x: x.check("checkclass","shaman") and x.check("power","healing spirit"))
  ,feat([],"Watcher Spirit Adept","Allies gain +2 to Insight and Perception when next to your spirit companion",lambda x: x.check("checkclass","shaman") and x.check("feature","watcher spirit"))
  ,feat([],"World Speaker Spirit Adept","You and your allies ignore difficult terrain while adjacent to your spirit companion",lambda x: x.check("checkclass","shaman") and x.check("feature","world speaker spirit"))
###Primal Power: Warden###            
  ,feat([],"Crippling Crush",["When you immobilize or slow an enemy with a hammer or mace, that enemy takes ",CONMOD," extra damage"],lambda x: x.check("checkclass","warden"))
  ,feat([],"Earthstrength Resilience",["When you use your second wind, gain resist ",lambda x: raising(3,10)(x)-1," until the end of your next turn"],lambda x: x.check("checkclass","warden") and x.check("feature","earthstrength"))
  ,feat([],"Impaling Thrust","Treat critical with heavy blade or spear as a normal hit to immobilize opponent",lambda x: x.check("checkclass","warden"))
  ,feat([],"Lifespirit Vigor","You can grant a saving throw to a second ally in 5 squares with second wind",lambda x: x.check("checkclass","warden") and x.check("feature","lifespirit"))
  ,feat([],"Primal Breath","When you use Dragon Breath, you can choose to mark each target",lambda x: x.check("checkclass","warden") and x.check("checkrace","dragonborn"))
  ,feat([],"Stormheart Push","You may choose to push 2 with Stormheart instead of sliding enemy",lambda x: x.check("checkclass","warden") and x.check("feature","stormheart"))
  ,feat([],"Wildblood Fury",["With second wind, gain a +",WISMOD," bonus to damage vs. each marked enemy until end of your next turn"],lambda x: x.check("checkclass","warden") and x.check("feature","wildblood"))
###Primal Power: Paragon Feats###
  ,feat([],"Thundering Bull Rush","Target 2 creatures with bull rush and choose space you shift into",lambda x:x.check("level", 11) and x.check("checkclass",primalclasses, True))
  ,feat([],"Two-Handed Grasp","Wield a versatile spear in two hands to gain high crit",lambda x:x.check("level", 11) and x.check("checkclass",primalclasses, True))
###Primal Power: Barbarian Paragon Feats###
  ,feat([],"Double Lunge",["Deal ",STRMOD," extra damage to target of Whirling Lunge"],lambda x:x.check("level", 11) and x.check("checkclass","barbarian") and x.check("power","whirling lunge"))
  ,feat([],"Explosive Rage Strike","Reduce rage strike damage by 2[W] to treat range as close burst 1",lambda x:x.check("level", 11) and x.check("checkclass","barbarian") and x.check("power","rage strike"))
  ,feat([],"Reckless Rage","-2 to attack roll to deal 1[W] extra damage with a rage power",lambda x:x.check("level", 11) and x.check("checkclass","barbarian"))
  ,feat([],"Thirsty Blade",["Deal ",STRMOD," damage to adjacent enemies when you drop a target with a charge"],lambda x:x.check("level", 11) and x.check("checkclass","barbarian"))
  ,feat([],"Thunderous War Cry","Targets of your War Cry grant combat advantage to you",lambda x:x.check("level", 11) and x.check("checkclass","barbarian") and x.check("power","war cry"))
  ,feat([],"Violent Reminder","+5 to next damage roll when you drop enemy",lambda x:x.check("level", 11) and x.check("checkclass","barbarian") and x.check("feature","rageblood vigor"))
  ,feat([],"Withering Roar","Target grants combat advantage or takes -2 to all defenses when you hit with roar of triumph",lambda x:x.check("level", 11) and x.check("checkclass","barbarian") and x.check("feature","thaneborn triumph"))
###Primal Power: Druid Paragon Feats###
  ,feat([],"Bolstered Swarm",["Gain ",lambda x:raising(5,10)(x)-5+x.mod("con")," temporary HP when you use wild shape"],lambda x:x.check("level", 11) and x.check("checkclass", "druid") and x.check("feature","primal swarm") and x.check("power","wild shape"))
  ,feat([],"Bolstering Guardian",["Adjacent ally gains ",CONMOD," temporary HP when you drop an enemy"],lambda x:x.check("level", 11) and x.check("checkclass", "druid") and x.check("feature","primal guardian"))
  ,feat([],"Commanding Form","1/round in beast form, give minor action command to summon as free action",lambda x:x.check("level", 11) and x.check("checkclass", "druid") and x.check("power","wild shape"))
  ,feat([],"Pouncing Form",["Shift ",DEXMOD," when you use wild shape"],lambda x:x.check("level", 11) and x.check("checkclass", "druid") and x.check("feature","primal predator") and x.check("power","wild shape"))
  ,feat([],"Scattering Swarm","Shift 2 if an area or close attack damages you in beast form",lambda x:x.check("level", 11) and x.check("checkclass", "druid") and x.check("power","wild shape") and x.check("feature","primal swarm"))
  ,feat([],"Vital Form","Regain second wind when you use Wild Shape",lambda x:x.check("level", 11) and x.check("checkclass", "druid") and x.check("power","wild shape"))
  ,feat([],"Warning Guardian","Adjacent allies don't grant combat advantage when flanked",lambda x:x.check("level", 11) and x.check("checkclass", "druid") and x.check("feature","warning guardian"))
###Primal Power: Shaman Paragon Feats###
  ,feat([],"Cyclone Spirit","Forced movement of enemies adjacent to your spirit companion increased by 1",lambda x:x.check("level", 11) and x.check("checkclass","shaman") and x.check("feature","world speaker spirit"))
  ,feat([],"Ephemeral Spirit","Spirit companion takes half damage from ranged attacks",lambda x:x.check("level", 11) and x.check("checkclass","shaman"))
  ,feat([],"Retributive Spirit","-2 to defenses of creatures that destroys spirit companion",lambda x:x.check("level", 11) and x.check("checkclass","shaman") and x.check("power","call spirit companion"))
  ,feat([],"Sentinel Spirit","+2 to opportunity attack rolls for allies adjacent to spirit companion",lambda x:x.check("level", 11) and x.check("checkclass","shaman") and x.check("feature","watcher spirit"))
  ,feat([],"Shielding Spirit","+2 to all defenses for allies adjacent to spirit companion when you use healing spirit",lambda x:x.check("level", 11) and x.check("checkclass","shaman") and x.check("feature","protector spirit") and x.check("power","healing spirit"))
  ,feat([],"Spirit's Eyes","Roll twice for Perception checks if spirit companion present",lambda x:x.check("level", 11) and x.check("checkclass","shaman"))
  ,feat([],"Vicious Spirit","+2 to damage against bloodied enemies for allies adjacent to your spirit companion when you use healing spirit",lambda x:x.check("level", 11) and x.check("checkclass","shaman") and x.check("feature","stalker spirit") and x.check("power","healing spirit"))
###Primal Power: Warden Paragon Feats###
  ,feat([],"Arcing Throw","Target of a thrown spear doesn't gain cover from allies",lambda x:x.check("level", 11) and x.check("checkclass","warden"))
  ,feat([],"Earthstrength Defenses",["Gain a +",CONMOD," bonus to Fortitude, Reflex, and Will when you use second wind"],lambda x:x.check("level", 11) and x.check("checkclass","warden") and x.check("feature","earthstrength"))
  ,feat([],"Forceful Smash","Critical hit using a hammer or mace also knocks target prone",lambda x:x.check("level", 11) and x.check("checkclass","warden") and x.check("con",15))
  ,feat([],"Lifespirit Healing","Second ally in 5 squares can spend healing surge and make saving thrown when you use second wind",lambda x:x.check("level", 11) and x.check("checkclass","warden"))
  ,feat([],"Maneuvering Attack","Enemies you forcibly move using a polearm or spear grant combat advantage to you until end of your next turn",lambda x:x.check("level", 11) and x.check("checkclass","warden"))
  ,feat([],"Stormheart Thunder","Target gains vulnerable 5 thunder until end of your next turn when slowed by your Stormheart",lambda x:x.check("level", 11) and x.check("checkclass","warden"))
  ,feat([],"Wellspring of Life","Adjacent allies gain +1 to saving throws until end of your next turn when you succeed on Font of Life save",lambda x:x.check("level", 11) and x.check("checkclass","warden") and x.check("feature","font of life"))
  ,feat([],"Wildblood Retribution","Make basic melee attack as free action against marked target when you use second wind",lambda x:x.check("level", 11) and x.check("checkclass","warden") and x.check("feature","wildblood"))
###Primal Power: Epic Feats###
  ,feat([ft("ac",["feat",lambda x:2*x.check("armortype","hide")]),ft(["acheck"],["",lambda x:1*x.check("armortype","hide")]),ft(["and","fearattack","primalattack"],["",lambda x:1*x.check("armortype","hide")])],"Second Skin","+2 AC with hide, reduce check penalty by 1, and +1 to attack with primal fear powers",lambda x:x.check("level", 21) and x.check("checkclass",primalclasses, True) and x.check("proficiency","hide") and x.check("con",17))
  ,feat([],"Overpowering Charge","Knock target prone when you hit with a charge attack",lambda x:x.check("level", 21) and x.check("checkclass","barbarian"))
  ,feat([],"Slayer's Shift","Shift 1 as a free action when you bloody or drop a creature",lambda x:x.check("level", 21) and x.check("checkclass","barbarian"))
  ,feat([],"Sweeping Blade",["Deal ",lambda x:x.mod("str")+4," damage to adjacent enemies when you hit with an opp attack with an axe or heavy blade"],lambda x:x.check("level", 21) and x.check("checkclass","barbarian"))
  ,feat([],"Guardian Resurgence",["Adjacent ally gains ",CONMOD," extra HP when they use their second wind"],lambda x:x.check("level", 21) and x.check("checkclass","druid") and x.check("feature","primal guardian"))
  ,feat([],"Primal Summoning Expertise","Use a minor action to give a standard action command to a primal summoned creature",lambda x:x.check("level", 21) and x.check("checkclass","druid"))
  ,feat([],"Swift Predator","+1 to speed, shifting, in beast form",lambda x:x.check("level", 21) and x.check("checkclass","druid") and x.check("feature","primal predator") and x.check("power","wild shape"))
  ,feat([],"Wild Surge","Use second wind as free action when you use Wild Shape",lambda x:x.check("level", 21) and x.check("checkclass","druid") and x.check("power","wild shape"))
  ,feat([],"Grave Spirit","Allies adjacent to your spirit regain 10 hp when enemy adjacent to your spirit drops",lambda x:x.check("level", 21) and x.check("checkclass","shaman") and x.check("feature","stalker spirit"))
  ,feat([],"Ironheart Spirit","Ally adjacent to your spirit companion shifts 1 when hit",lambda x:x.check("level", 21) and x.check("checkclass","shaman") and x.check("feature","protector spirit"))
  ,feat([],"Purging Spirit","Allies adjacent to spirit make saving throw when you use healing spirit adjacent to spirit",lambda x:x.check("level", 21) and x.check("checkclass","shaman") and x.check("power","healing spirit"))
  ,feat([],"Spirit of Health","Allies adjacent to spirit companion spend a healing surge when you use second wind",lambda x:x.check("level", 21) and x.check("checkclass","shaman") and x.check("feature","protector spirit"))
  ,feat([],"Stone Heart Spirit","Spirit companion provides cover",lambda x:x.check("level", 21) and x.check("checkclass","shaman") and x.check("feature","world speaker spirit"))
  ,feat([],"Triumphant Spirit","Ally makes melee basic attack as free action after dropping enemy adjacent to spirit companion",lambda x:x.check("level", 21) and x.check("checkclass","shaman") and x.check("feature","stalker spirit"))
  ,feat([],"Vexing Spirit","Allies don't grant combat advantage to enemies adjacent to spirit companion",lambda x:x.check("level", 21) and x.check("checkclass","shaman") and x.check("feature","watcher spirit"))
  ,feat([],"Earthstrength Might","Make a melee basic attack as a free action when you use second wind",lambda x:x.check("level", 21) and x.check("checkclass","warden") and x.check("feature","earthstrength"))
  ,feat([],"Far-Reaching Grasp","Warden's Grasp range increases to close burst 10, and triggers on an enemy within 10 squares",lambda x:x.check("level", 21) and x.check("checkclass","warden") and x.check("power","warden's grasp"))
  ,feat([],"Tangling Grasp","Targets of Warden's Grasp are immobilized instead of slowed",lambda x:x.check("level", 21) and x.check("checkclass","warden") and x.check("power","warden's grasp"))
])
allFeatDict["Forgotten Realms"]=addFeats([
  feat([featPowers["Angharradh's Favor"]],"Angharradh's Favor","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","angharradh") or x.check("feature","manifest the divine")))
  ,feat([],"Avowed Dragonfoe","+1 bonus to attack rolls against dragons, +2 while bloodied",CHECK("checkrace","dragonborn"))
  ,feat([featPowers["Berronar's Salve"]],"Berronar's Salve","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","berronar truesilver") or x.check("feature","manifest the divine")))
  ,feat([featPowers["Blessing of Silvanus"]],"Blessing of Silvanus","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","silvanus") or x.check("feature","manifest the divine")))
  ,feat([ft("will",["feat",1])],"Broken Shackles","+1 to Will defense, +2 to saving throws against charm",CHECK("checkrace","dragonborn"))
  ,feat([featPowers["Chauntea's Blessing"]],"Chauntea's Blessing","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","chauntea") or x.check("feature","manifest the divine")))
  ,feat([ft("cloud of darknessclose burst",["feat",1]),ft("darkfireranged",["feat",5])],"Clutch of Darkness","Cloud of Darkness becomes burst 2, Darkfire becomes ranged 15",CHECK("checkrace","drow"))
  ,feat([],"Elemental Assault","+3 elemental damage with Aegis of Assault based on elemental manifestation",lambda x: x.check("checkclass","swordmage") and x.check("power","aegis of assault") and x.check("checkrace","genasi"))
  ,feat([],"Escalating Assault","Cumulative +1 to attack with Aegis of Assault",lambda x: x.check("checkclass","swordmage") and x.check("power","aegis of assault"))
  #Extra Manifestation
  ,feat([]
        ,"Extra Manifestation"
        ,"Allows choice of second manifestation"
        ,CHECK("checkrace","genasi"))
  ,feat([featPowers["Eyes of Selune"]],"Eyes of Selune","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","selune") or x.check("feature","manifest the divine")))
  ,feat([featPowers["Fleetness of Mielikki"]],"Fleetness of Mielikki","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","mielikki") or x.check("feature","manifest the divine")))
  ,feat([],"Ghostwise Heritage","You and ally both use higher result of your Perception checks",CHECK("checkrace","halfling"))
  ,feat([featPowers["Glittergold's Gambit"]],"Glittergold's Gambit","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","garl glittergold") or x.check("feature","manifest the divine")))
  ,feat([],"Gold Dwarf Pride","+1 to AC and attack rolls if you regain conciousness",CHECK("checkrace","dwarf"))
  ,feat([featPowers["Gond's Craft"]],"Gond's Craft","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and x.check("deity","gond"))
  ,feat([featPowers["Ilmater's Martyrdom"]],"Ilmater's Martyrdom","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","ilmater") or x.check("feature","manifest the divine")))
  ,feat([],"Improved Swordbond","Call bonded weapon with minor action from 20 squares away",CHECK("checkclass","swordmage"))
  ,feat([ft(["and","basic attackattack","meleeattack"],("stat change",lambda x:max(x.mod("str"), x.mod("int"))-x.mod("str"))),ft(["and","basic attackdamage", "meleedamage"],("stat change",lambda x:max(x.mod("str"), x.mod("int"))-x.mod("str")))],"Intelligent Blademaster","Use intelligence modifier instead of strength when making a basic attack with a melee weapon",CHECK("checkclass","swordmage"))
  ,feat([featPowers["Kelemvor's Judgement"]],"Kelemvor's Judgement","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","kelemvor") or x.check("feature","manifest the divine")))
  ,feat([ft("genasiresist",["feat",5])],"Manifest Resistance","Increase elemental resistance from manifestation by 5",CHECK("checkrace","genasi"))
  ,feat([],"Moon Elf Resilience","Spend healing surge as free action when using Fey Step when bloodied and more than 5 squares from allies",lambda x: x.check("checkrace","eladrin") and not(x.check("feature","sun elf grace")))
  ,feat([featPowers["Oghma's Recall"]],"Oghma's Recall","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","oghma") or x.check("feature","manifest the divine")))
  ,feat([featPowers["Power of Amaunator"]],"Power of Amaunator","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","amaunator") or x.check("feature","manifest the divine")))
  ,feat([],"Retributive Shield","+2 to attack rolls against foe that triggered Aeigis of Shielding",lambda x: x.check("checkclass","swordmage") and x.check("power","aegis of shielding"))
  ,feat([featPowers["Righteous Rage of Tempus"]],"Righteous Rage of Tempus","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","tempus") or x.check("feature","manifest the divine")))
  ,feat([ft("handcrossbownameweaponsize",["",1])],"Ruthless Hunter","Your hand crossbow deals 1d8 damage, gains high crit property",CHECK("checkrace","drow"))
  ,feat([ft("fort",["feat",1]),ft("will",["feat",1])],"Scion of the Gods","+1 to Fortitude and Will defenses",CHECK("checkrace","tiefling"))
  ,feat([featPowers["Sheela Peryroyl's Gift"]],"Sheela Peryroyl's Gift","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","sheela peryroyl") or x.check("feature","manifest the divine")))
  ,feat([],"Shield of Shadows","+2 to Reflex defense while within your Cloud of Darkness",CHECK("checkrace","drow"))
  ,feat([],"Shield the Fallen","Adjacent bloodied, unconcious, and helpless allies gain +2 to saving throws and all defenses",CHECK("checkrace","dwarf"))
  ,feat([],"Stubborn Survivor","You gain a +2 bonus to saving throws when you have no action points remaining",CHECK("checkrace","human"))
  ,feat([ft("powerpick",PowerPick(powerList["swordmagedaily1"].values(),1, 15, "Swordmage Spellbook 1")),ft("powerpick",PowerPick(powerList["swordmagedaily5"].values(),5, 19, "Swordmage Spellbook 5")),ft("powerpick",PowerPick(powerList["swordmagedaily9"].values(),9, 25, "Swordmage Spellbook 9")),ft("powerpick",PowerPick(powerList["swordmagedaily15"].values(),15, 29, "Swordmage Spellbook 15")),ft("powerpick",PowerPick(powerList["swordmagedaily19"].values(),19, 31, "Swordmage Spellbook 19")),ft("powerpick",PowerPick(powerList["swordmagedaily25"].values(),25, 31, "Swordmage Spellbook 25")),ft("powerpick",PowerPick(powerList["swordmagedaily29"].values(),29, 31, "Swordmage Spellbook 31"))],"Student of Sword Magic","Choose one additional daily Swordmage attack spell of each level you can cast for your spellbook",lambda x: x.check("checkclass","swordmage"))
  ,feat([],"Sun Elf Grace","+1 to all defenses until the end of your next turn if you use Fey Step before becoming bloodied",lambda x: x.check("checkrace","eladrin") and not(x.check("feature","moon elf resilience")))
  ,feat([featPowers["Sune's Touch"]],"Sune's Touch","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","sune") or x.check("feature","manifest the divine")))
  ,feat([featPowers["Torm's Justice"]],"Torm's Justice","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","torm") or x.check("feature","manifest the divine")))
  ,feat([featPowers["Tymora's Coin"]],"Tymora's Coin","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","tymora") or x.check("feature","manifest the divine")))
  ,feat([],"Versatile Resistance","You gain resist 5 cold, resist 5 fire, and resist 5 thunder regardless of your elemental manifestation",CHECK("checkrace","genasi"))
  ,feat([featPowers["Waukeen's Silver Tongue"]],"Waukeen's Silver Tongue","Extra power option for channel divinity",lambda x: x.check("feature","channel divinity") and (x.check("deity","waukeen") or x.check("feature","manifest the divine")))
  ,feat([],"Wild Elf Luck","+1d4 bonus on reroll when using Elven Accuracy",lambda x: x.check("checkrace","elf") and not(x.check("feature","wood elf agility")))
  ,feat([],"Wood Elf Agility","On Acrobatics or Athletics checks, d20 roll of 2-7 counts as 8",lambda x: x.check("checkrace","elf") and not(x.check("feature","wild elf luck")))
###Forgotten Realms Feats###
  ,feat([],"Demonweb Spiral","Enemies damaged by your Darkspiral Aura are immobilized",lambda x:x.check("level", 11) and x.check("checkclass","warlock") and x.check("feature","dark pact"))
  ,feat([],"Distant Swordbond","Call bonded weapon from up to 1 mile away as minor action",lambda x:x.check("level", 11) and x.check("checkclass","swordmage"))
  ,feat([],"Double Aegis","Mark two targets with a Swordmage Aegis power",lambda x:x.check("level", 11) and x.check("checkclass","swordmage"))
  ,feat([ft("darkspiraldie",["",2])],"Improved Darkspiral aura",["Your Darkspiral Aura deals 1d",lambda x:raising(2,10)(x)+6," damage per point in the Darkspiral Aura."],lambda x:x.check("level", 11) and x.check("checkclass","warlock") and x.check("feature","dark pact"))
  ,feat([],"Master of Fire and Darkness","Use both Cloud of Darkness and Darkfire once per encounter",lambda x:x.check("level", 11) and x.check("checkrace","drow"))
  ,feat([],"Merciless Killer","+5 damage if you have combat advantage against bloodied foe",lambda x:x.check("level", 11) and x.check("checkrace","drow"))
  ,feat([],"Moongleam Oath","+1 to attacks and damage against shadow creatures",CHECK("level",11))
  ,feat([],"Shocking Flame","+2 fire or lightning damage on melee attacks when manifesting firesoul or stormsoul",lambda x:x.check("level", 11) and x.check("checkrace","genasi"))
  ,feat([],"Stoneguard","+2 AC against ranged attacks while manifesting earthsoul",lambda x:x.check("level", 11) and x.check("checkrace","genasi"))
  ,feat([ft("speed",["feat",lambda x:min(1,x.check("feature","watersoul")+x.check("feature","windsoul"))])],"Stormrider","+1 speed when manifesting windsoul or watersoul.  Hover while flying.",lambda x:x.check("level", 11) and x.check("checkrace","genasi"))
  ,feat([],"Venemous Heritage","Gain resist 5 poison and +2 to saving throws against poison",lambda x:x.check("level", 11) and x.check("checkrace","drow"))
  ,feat([],"War Wizardry","Your arcane spells gain -5 to attacks, half damage when used against allies",CHECK("level",11))
###Forgotten Realms Feats###
  ,feat([specMenus["genasiManifestation"]],"Double Manifestation","",lambda x:x.check("level",21) and x.check("checkrace","genasi") and x.check("feature","extra manifestation"))
  ,feat([],"Total Aegis","Mark any number of targets in burst with a Swordmage Aegis power",lambda x:x.check("level",21) and x.check("checkclass","swordmage"))
])
allFeatDict["Player's Handbook 2"]=addFeats([
  feat([],"Anger Unleashed","+2 attack for 1 round after becoming bloodied",CHECK("checkrace","half-orc"))
  ,feat([ft("memorydie",["feat",2])],"Auspicious Lineage","Roll d8 instead of d6 for memory of a thousand lifetimes",CHECK("checkrace","deva"))
  ,feat([],"Blurring Claws","+2 damage with combat advantage during razorclaw shifting",CHECK("checkrace","shifter, razorclaw"))
  ,feat([ft("heal",["feat",2])],"Combat Medic","Stabilize the dying as a minor action, +2 on heal checks",CHECK("training","heal"))
  ,feat([],"Coordinated Explosion","+1 to attack rolls with blast or burst if ally is in area")
  ,feat([],"Distant Advantage","Gain combat advantage with ranged attacks against flanked enemies")
  ,feat([],"Echoes of Thunder","+1 damage after you hit with thunder power")
  ,feat([],"Expert Ritualist","+2 bonus to ritual skill checks",CHECK("feature","ritual caster"))
  ,feat([],"Fey Trickster","Gain mage hand and prestidigitation as encounter powers",CHECK("checkrace","gnome"))
  ,feat([ft([x+"namedamage" for x in groupList(["two-handed","melee"],["superior","improvised"])],["feat",lambda x:1+raising(1,10)(x)]),ft("proficiency",groupList(["two-handed","melee"],["superior","improvised"]))],"Goliath Greatweapon Prowess","Gain proficiency, +2 damage with two-handed melee weapons",CHECK("checkrace","goliath"))
  ,feat([],"Gorebrute Charge","+3 damage on charge attacks during longtooth shifting",CHECK("checkrace","shifter, longtooth"))
  ,feat([],"Group Stealth","Nearby allies gain +2 to stealth checks",CHECK("checkrace","gnome"))
  ,feat([specialMenu(sorted(implementExpertise.keys()), [implementExpertise[x] for x in sorted(implementExpertise.keys())],["+",raiselist(1,[15,25])," on attack rolls with "],"")],"Implement Expertise","")
  ,feat([],"Improved Bull Rush","+4 to bull rush attacks",lambda x:x.check("str",13) and x.check("con",13))
  ,feat([],"Improved Grab","+4 to grab attacks",CHECK("str",13))
  ,feat([],"Markings of the Blessed","Roll twice for first saving throw each encounter",CHECK("checkrace","goliath"))
  ,feat([],"Markings of the Victor","Roll twice for first attack roll each encounter",CHECK("checkrace","goliath"))
  ,feat([specialMenu(["con","dex","int","wis","cha"],[feat([ft(["and","basic attackattack","meleeattack"],("stat change",lambda x:max(0,x.mod("con")-x.mod("str")))),ft(["and","basic attackdamage", "meleedamage"],("stat change",lambda x:max(0,x.mod("con")-x.mod("str"))))]),
                                                      feat([ft(["and","basic attackattack","meleeattack"],("stat change",lambda x:max(0,x.mod("dex")-x.mod("str")))),ft(["and","basic attackdamage", "meleedamage"],("stat change",lambda x:max(0,x.mod("dex")-x.mod("str"))))]),
                                                      feat([ft(["and","basic attackattack","meleeattack"],("stat change",lambda x:max(0,x.mod("int")-x.mod("str")))),ft(["and","basic attackdamage", "meleedamage"],("stat change",lambda x:max(0,x.mod("int")-x.mod("str"))))]),
                                                      feat([ft(["and","basic attackattack","meleeattack"],("stat change",lambda x:max(0,x.mod("wis")-x.mod("str")))),ft(["and","basic attackdamage", "meleedamage"],("stat change",lambda x:max(0,x.mod("wis")-x.mod("str"))))]),
                                                      feat([ft(["and","basic attackattack","meleeattack"],("stat change",lambda x:max(0,x.mod("cha")-x.mod("str")))),ft(["and","basic attackdamage", "meleedamage"],("stat change",lambda x:max(0,x.mod("cha")-x.mod("str"))))])],"Use "," instead of str for basic melee attacks")],"Melee Training","")
  ,feat([],"Oncoming Storm","Hit with lightning power to gain +1 on thunder attacks")
  ,feat([],"Potent Rebirth","+2 to attack and damage if reduced to 0 hp",CHECK("checkrace","deva"))
  ,feat([],"Radiant Power","+2 damage with implement power for -2 to attack",CHECK("checkrace","deva"))
  ,feat([],"Restful Healing","Maximize healing between encounters")
  ,feat([],"Savage Assault","Target of Furious Assault takes -1 to defenses",CHECK("checkrace","half-orc"))
  ,feat([],"Shadow Skulk","Stay hidden when you miss with area or ranged attack",CHECK("checkrace","gnome"))
  ,feat([],"Speed Loader","Load crossbow as free action instead of minor")
  ,feat([],"Surging Flame","Fire-resistant target takes extra damage from fire powers")
  ,feat([ft("initiative",["feat",3]),ft("surges",["",1])],"Thirst for Battle","+3 to initiative and one additional healing surge",CHECK("checkrace","half-orc"))
  ,feat([],"Timely Respite","Second wind or total defense grants saving throw")
  ,feat([],"Two-Weapon Threat","+3 damage on opportunity attacks with two melee weapons",lambda x:x.check("dex",13) and x.check("feature","two-weapon fighting"))
  ,feat([specialMenu(sorted(weaponExpertise.keys()), [weaponExpertise[x] for x in sorted(weaponExpertise.keys())],["+",raiselist(1,[15,25])," on attack rolls with "]," weapon group")],"Weapon Expertise","")
  ,feat([ft("initiative",["feat",3])],"Wild Senses","Roll twice when following tracks, +3 to initiative",lambda x:x.check("checkrace","shifter"))
  ,feat([],"Guarunteed Retribution","+1 to next attack roll against oath of enmity target when another enemy hits you",lambda x:x.check("checkclass","avenger") and x.check("feature","censure of retribution") and x.check("power","oath of enmity"))
  ,feat([ft("ac",["",lambda x: not(x.check("armortype",["heavy","shield","leather","hide"],True))])],"Improved Armor of Faith","Gain +1 AC when wearing cloth armor or no armor and not using a shield",lambda x:x.check("checkclass","avenger") and x.check("feature","armor of faith"))
  ,feat([],"Invigorating Pursuit","Gain +2 AC and damage when you charge Oath of Enmity target",lambda x:x.check("checkclass","avenger") and x.check("feature","censure of pursuit") and x.check("power","oath of enmity"))
  ,feat([],"Deadly Rage","+1 damage while raging",CHECK("checkclass","barbarian"))
  ,feat([],"Improved Rageblood Vigor","Gain 5 extra temporary hp from Rageblood Vigor",lambda x:x.check("checkclass","barbarian") and x.check("feature","rageblood vigor"))
  ,feat([],"Improved Roar of Triumph","Roar of Triumph burst is larger, grants you +2 damage",lambda x: x.check("checkclass","barbarian") and x.check("feature","thaneborn triumph"))
  ,feat([],"Rising Fury",["+",lambda x:1+raising(1,10)(x)," feat bonus to damage until the end of your next turn when you reduce enemy to 0 hp"],CHECK("checkclass","barbarian"))
  ,feat([],"Advantage of Cunning","Slide enemy into ally's vacated space when using Virtue of Cunning",lambda x:x.check("checkclass","bard") and x.check("feature","virtue of cunning"))
  ,feat([ft(z,["feat",2]) for z in ["arcana","dungeoneering","history","nature","religion","streetwise"]],"Bardic Knowledge","+2 feat bonus to Arcana, Dungeoneering, History, Nature, Religion, and Streetwise skill checks",CHECK("checkclass","bard"))
  ,feat([],"Improved Majestic Word",["Target of Majestic Word gains ",CHAMOD," temporary HP"],lambda x:x.check("checkclass","bard") and x.check("power","majestic word"))
  ,feat([],"Strength of Valor","Virtue of Valor grants target +2 to next damage roll before end of his or her next turn.",lambda x:x.check("checkclass","bard") and x.check("feature","virtue of valor"))
  ,feat([],"Enraged Boar Form","+1 attack, +2 damage when in charging beast form",lambda x:x.check("checkclass","druid") and x.check("power","wild shape"))
  ,feat([],"Ferocious Tiger Form","+2 damage with combat advantage in beast form",lambda x:x.check("checkclass","druid") and x.check("power","wild shape"))
  ,feat([],"Primal Fury","+1 attacks with primal powers against bloodied enemies",lambda x:x.check("checkclass","druid") and x.check("feature","primal predator"))
  ,feat([],"Primal Instinct","One ally within 5 squares can reroll initiative",lambda x:x.check("checkclass","druid") and x.check("feature","primal guardian"))
  ,feat([],"Insightful Preservation","Preserver's Rebuke grants temporary HP",lambda x:x.check("checkclass","invoker") and x.check("feature","covenant of preservation"))
  ,feat([],"Invoker Defense","+2 feat bonus AC when you hit enemy within 3 squares of you with an invoker power",CHECK("checkclass","invoker"))
  ,feat([],"Resonating Covenant","+1 attack with at-will after using encounter or daily power",lambda x:x.check("checkclass","invoker") and x.check("feature",["covenant of wrath","covenant of preservation"],True))
  ,feat([],"Scouring Wrath","Armor of Wrath gives target vulnerable 2 to all other damage until end of your next turn",lambda x:x.check("checkclass","invoker") and x.check("feature","covenant of wrath"))
  ,feat([],"Protector Spirit Adept","Allies adjacent to spirit companion gain +1 Fort, Ref, Will",lambda x: x.check("checkclass","shaman") and x.check("feature","protector spirit"))
  ,feat([],"Shared Healing Spirit","Change recipient of additional hit points",lambda x: x.check("checkclass","shaman") and x.check("power","healing spirit"))
  ,feat([],"Spirit Speaker","Speak with Spirits grants skill bonus to ally",lambda x: x.check("checkclass","shaman") and x.check("power","speak with spirits"))
  ,feat([],"Stalker Spirit Adept","Allies adjacent to spirit companion can shift as a free action",lambda x: x.check("checkclass","shaman") and x.check("feature","stalker spirit"))
  ,feat([],"Arcane Spellfury","+1 to attack rolls after hitting with sorcerer at-will attack",CHECK("checkclass","sorcerer"))
  ,feat([],"Disciplined Wild Soul","Roll twice to determine Wild Soul damage type",lambda x:x.check("checkclass","sorcerer") and x.check("feature","wild magic"))
  ,feat([],"Improved Dragon Soul","Increase Dragon Soul resistance by 2",lambda x:x.check("checkclass","sorcerer") and x.check("feature","dragon magic"))
  ,feat([],"Sorcerous Blade Channeling","Use dagger to make ranged attacks as melee attacks",CHECK("checkclass","sorcerer"))
  ,feat([],"Crushing Earthstrength",["+",CONMOD," damage after second wind"],lambda x:x.check("checkclass","warden") and x.check("feature","earthstrength"))
  ,feat([],"Revitalizing Font of Life","Successful Font of Life saving throw grants +2 bonus to other saving throws",lambda x:x.check("checkclass","warden") and x.check("feature","font of life"))
  ,feat([],"Sudden Roots","Enemy hit by opportunity attack is slowed",CHECK("checkclass","warden"))
  ,feat([],"Wildblood Cunning","Shift when you use second wind",lambda x:x.check("checkclass","warden") and x.check("feature","wildblood"))
###PHB2 Paragon Feats###
  ,feat([],"Agile Opportunist","Use immediate reaction to attack when subjected to forced movement",CHECK("level", 11))
  ,feat([],"Ascendant Lineage","Memory of a Thousand Lifetimes not expended on failed roll",lambda x:x.check("level", 11) and x.check("checkrace","deva"))
  ,feat([],"Astral Renewal","+2 to next attack when Astral Resistance reduces damage",lambda x:x.check("level", 11) and x.check("checkrace","deva"))
  ,feat([],"Beasthide Shifting","Gain resist 2 to all damage during racial power",lambda x:x.check("level", 11) and x.check("checkrace","shifter"))
  ,feat([],"Cliffwalk Shifting","Gain climb speed during racial power",lambda x:x.check("level", 11) and x.check("checkrace","shifter"))
  ,feat([],"Fade Ally","Fade Away can target nearby ally instead of you",lambda x:x.check("level", 11) and x.check("checkrace","gnome"))
  ,feat([ft(["fort","ref","will"],["feat",1])],"Paragon Defenses","+1 to Fortitude, Reflex, and Will defenses",CHECK("level", 11))
  ,feat([],"Quick Recovery","Regain 5 additional HP when spending a healing surge after a short rest",CHECK("level", 11))
  #Reserve Maneuver
  ,feat([]
               ,"Reserve Maneuver"
               ,"Swap encounter powers during rest"
               ,CHECK("level", 11))
  ,feat([],"Strength from Pain","+5 damage for 1 round after becoming bloodied",lambda x:x.check("level", 11) and x.check("checkrace","half-orc"))
  ,feat([],"Surprising Disappearance","Fade Away gives combat advantage against attacker",lambda x:x.check("level", 11) and x.check("checkrace","gnome"))
  ,feat([],"Two-Weapon Opening","Critical hit with main weapon grants free attack with off-hand weapon",lambda x:x.check("level", 11) and x.check("feature","two-weapon fighting"))
  ,feat([],"Unrelenting Assault","Trigger furious assault on miss",lambda x:x.check("level", 11) and x.check("checkrace","half-orc"))
  ,feat([],"Unyielding Stone",["Stone's Endurance grants ",lambda x:x.mod("con")+x.statret("level")/2,"temporary HP"],lambda x:x.check("level", 11) and x.check("checkrace","goliath"))
  #Versatile Master
  ,feat([]
               ,"Versatile Master"
               ,"Improved Dilettante and paragon multiclassing"
               ,lambda x:x.check("level", 11) and x.check("checkrace","half-elf"))
  ,feat([],"Vexing Flanker","Targets you flank grant combat advantage to your allies",CHECK("level", 11))
  ,feat([],"Inexorable Pursuit","Ignore difficult terrain and move through enemies' spaces when you charge Oath of Enmity target",lambda x:x.check("level", 11) and x.check("checkclass","avenger") and x.check("feature","censure of pursuit") and x.check("power","oath of enmity"))
  ,feat([],"Onslaught of Enmity","Shift 2 squares toward target when you use oath of enmity",lambda x:x.check("level", 11) and x.check("checkclass","avenger") and x.check("power","oath of enmity"))
  ,feat([],"Protected Isolation","Gain +1 AC when adjacent to Oath of Enmity target",lambda x:x.check("level", 11) and x.check("checkclass","avenger") and x.check("feature","censure of retribution") and x.check("power","oath of enmity"))
  ,feat([],"Charging Rampage","Charge as a free action when you score a critical hit",lambda x:x.check("level", 11) and x.check("checkclass","barbarian") and x.check("feature","rampage"))
  ,feat([],"Rageblood Recovery","Spend healing surge when you hit with Swift Charge",lambda x:x.check("level", 11) and x.check("checkclass","barbarian") and x.check("feature","rageblood vigor"))
  ,feat([],"Thaneborn Advance",["Shift up to ",CHAMOD," squares before using Roar of Triumph while raging"],lambda x:x.check("level", 11) and x.check("checkclass","barbarian") and x.check("feature","thaneborn triumph"))
#Improved Cunning
  ,feat([ft("cunningslide",["feat",1])],"Improved Cunning","Slide ally 2 squares instead of 1 with Virtue of Cunning",lambda x:x.check("level", 11) and x.check("checkclass","bard") and x.check("feature","virtue of cunning"))
#Improved Valor
  ,feat([ft("valorhp",["feat",3])],"Improved Valor","Virtue of Valor grants 3 additional temporary hit points",lambda x:x.check("level", 11) and x.check("checkclass","bard") and x.check("feature","virtue of valor"))
  ,feat([ft("songofresthp",("",2))],"Lyric of Rejuvination","Song of Rest grants 2 extra hit points to each healing surge spent",lambda x:x.check("level", 11) and x.check("checkclass","bard") and x.check("feature","song of rest"))
  ,feat([],"Hunting Wolf Form","5 to Perception, +1 to speed in beast form",lambda x:x.check("level", 11) and x.check("checkclass","druid") and x.check("power","wild shape"))
  ,feat([ft("wild shapeaction","free")],"Quick Wild Shape","Use wild shape as a free action",lambda x:x.check("level", 11) and x.check("checkclass","druid") and x.check("power","wild shape"))
  ,feat([],"Stalking Panther Form","+5 to Stealth, +4 initative in beast form",lambda x:x.check("level", 11) and x.check("checkclass","druid") and x.check("power","wild shape"))
  ,feat([],"Overbearing Retribution","Armor of Wrath target knocked prone",lambda x:x.check("level", 11) and x.check("checkclass","invoker") and x.check("feature","covenant of wrath"))
  ,feat([],"Perserver's Vengance","+2 damage when bloodied ally is within 5 squares of you",lambda x:x.check("level", 11) and x.check("checkclass","invoker") and x.check("feature","covenant of preservation"))
  ,feat([],"Speaker of the Gods","Score critical hit on 18-20 after Channel Divinity power",lambda x:x.check("level", 11) and x.check("checkclass","invoker"))
  ,feat([],"Guardian Spirit","Spirit companion grants resist 20 to all damage and +2 on death saving throws to adjacent dying allies",lambda x:x.check("level", 11) and x.check("checkclass","shaman") and x.check("feature","protector spirit"))
  ,feat([ft("call spirit companionaction","free")],"Nimble Spirit","Conjure spirit companion as a free action",lambda x:x.check("level", 11) and x.check("checkclass","shaman") and x.check("feature",["protector spirit","stalker spirit"],True))
  ,feat([],"Arcane Flexibility","Change damage type of criticals to element you have resistance to",lambda x:x.check("level", 11) and x.check("checkclass","sorcerer") and x.check("feature","spell source"))
  ,feat([],"Draconic Spellfury",["Gain ",STRMOD," temporary HP when you hit with an at-will sorcerer attack"],lambda x:x.check("level", 11) and x.check("checkclass","sorcerer") and x.check("feature","dragon magic"))
  ,feat([],"Wild Spellfury",["Adjacent enemies take ",DEXMOD," damage when you hit with an at-will sorcerer attack"],lambda x:x.check("level", 11) and x.check("checkclass","sorcerer") and x.check("feature","wild magic"))
  ,feat([],"Earthstrength Resolve",["Gain ",CONMOD," tempoarary HP when marked enemy attacks ally"],lambda x:x.check("level", 11) and x.check("checkclass","warden") and x.check("feature","earthstrength"))
  ,feat([],"Enhanced Font of Life","+1 to saving throws from Font of Life",lambda x:x.check("level", 11) and x.check("checkclass","warden") and x.check("feature","font of life"))
  ,feat([],"Wildblood Speed",["Shift ",WISMOD," squares as free action when marked enemy attacks an ally"],lambda x:x.check("level", 11) and x.check("checkclass","warden") and x.check("feature","wildblood"))
###PHB 2 Epic feats###
  ,feat([],"Ancient Stone","Gain resist 10 to all damage when Stone's Endurance ends",lambda x:x.check("level", 21) and x.check("checkrace","goliath"))
  ,feat([],"Bow Mastery","Score critical hit on a 19-20 with a bow or a crossbow",CHECK("level", 21))
  ,feat([],"Burst of Savagery","End racial power for 2d6 extra damage and 10 temporary HP",lambda x:x.check("level", 21) and x.check("checkrace","shifter"))
  ,feat([ft("fort",["",4])],"Epic Fortitude","+4 bonus to Fortitude defense",CHECK("level", 21))
  ,feat([ft("ref",["",4])],"Epic Reflexes","+4 bonus to Reflex defense",CHECK("level", 21))
  ,feat([ft("will",["",4])],"Epic Will","+4 bonus to Will defense",CHECK("level", 21))
  ,feat([],"Ferocious Critical","+4 to attack and damage after critical hit",lambda x:x.check("level", 21) and x.check("checkrace","half-orc"))
  ,feat([ft("will",["feat",2])],"Indomitable Will","+2 to Will, +2 to saving throws against dazed, dominated, or stunned",CHECK("level", 21))
  ,feat([ft("ref",["feat",2])],"Opportune Reflexes","+2 to Reflex, +2 to saving throws against ongoing damage",CHECK("level", 21))
  ,feat([],"Primal Resurgence","Regain primal daily power when bloodied 1/day",CHECK("level", 21))
  ,feat([ft(["fort","ref","will"],["feat",2])],"Robust Defences","+2 to Fortitude, Reflex, and Will defenses",CHECK("level", 21))
  ,feat([],"Transcendent Lineage","Roll twice for Memory of a Thousand Lifetimes",lambda x:x.check("level", 21) and x.check("checkrace","deva"))
  ,feat([ft("fort",["feat",2])],"Unyielding Fortitude","+2 to Fortitude, +2 to death saving throws",CHECK("level", 21))
  ,feat([],"Vanishing Act","Teleport up to your speed when you use fade away",lambda x:x.check("level", 21) and x.check("checkrace","gnome"))
  ,feat([],"Mighty Enmity","Pick two Oath of Enmity targets the first time you use the oath in an encounter",lambda x:x.check("level", 21) and x.check("checkclass","avenger") and x.check("power","oath of enmity"))
  ,feat([],"Enduring Rage","Remain conscious at 0 hp or lower while raging",lambda x:x.check("level", 21) and x.check("checkclass","barbarian") and x.check("feature","rageblood vigor"))
  ,feat([],"Thaneborn Conquerer","Roar of Triumph gives enemies a -5 penalty to damage rolls until the end of your next turn",lambda x:x.check("level", 21) and x.check("checkclass","barbarian") and x.check("feature","thaneborn conquerer"))
  ,feat([ft("bardic virtuerange",["feat",5])],"Long Arm of Virtue","Increase range of Bardic Virtue by 5 squares",lambda x:x.check("level", 21) and x.check("checkclass","bard") and x.check("feature","bardic virtue"))
  ,feat([],"Primal Aspect Form","Gain regeneration 2 while in beast form",lambda x:x.check("level", 21) and x.check("checkclass","druid"))
  ,feat([],"Invoked Devastation","You can increase the size of any blast or burst invoker power by 1",lambda x:x.check("level", 21) and x.check("checkclass","invoker"))
  ,feat([],"Mighty Spirit","Spirit companion effects extend to 2 squares",lambda x:x.check("level", 21) and x.check("checkclass","shaman") and x.check("feature",["stalker spirit","protector spirit"],True))
  ,feat([],"Sorcerous Flux","Swap attack rolls of multitarget sorcerer power",lambda x:x.check("level", 21) and x.check("checkclass","sorcerer"))
  ,feat([],"Enduring Font","Font of Life grants two saving throws per turn",lambda x:x.check("level", 21) and x.check("checkclass","warden") and x.check("feature","font of life"))
])
allFeatDict["Player's Handbook 3"]=addFeats([
  feat([],"Alhahn's Mindful Relocation","Shift your speed, instead of 3 squares, with Shifting Fortunes",lambda x:x.check("checkrace","githzerai"))
  ,feat([ft("initiative",["feat",2])],"Battle Hardened","+5 feat bonus to saving throws against fear, +2 feat bonus to initiative checks",lambda x: True)
  ,feat([],"Battle Caster Defense","+4 AC against opportunity attacks after you use ranged or area power",lambda x:True)
  ,feat([],"Battering Shield","Push or slide target 1 additional square with melee attack when using shield",CHECK("proficiency","heavy"))
  ,feat([],"Beguiling Enchantment","Enemy at -2 to attacks against you after you hit it with a charm power until end of its next turn",lambda x:True)
  ,feat([],"Bloodied Ferocity","Make free melee basic attack when first bloodied, but grant combat advantage until end of next turn",CHECK("checkrace","minotaur"))
  ,feat([],"Brutal Ferocity","+2 bonus to the attack and damage rolls of attack granted by Ferocity",lambda x: x.check("checkrace","minotaur") and x.check("feature","ferocity"))
  ,feat([],"Burden of Rejuvination",["When you use Wilden power with ally in 2 squares, gain ",lambda x:max(x.statret("con"),x.statret("wis"))+3," temporary HP."],lambda x:x.check("checkrace","wilden") and x.check("feature","nature's aspect"))
  ,feat([],"Burden of Rejuvination",["When you use Wilden power, may spend healing surge to heal unconcious ally as if they spent a healing surge"],lambda x:x.check("checkrace","wilden") and x.check("feature","nature's aspect"))  
  ,feat([],"Cascading Rush","When you push a target with a bull rush, push enemy adjacent to target 1 square",lambda x:True)
  ,feat([],"Cleanse the Madness",["Gain a ",raising(2,10)," bonus to damage rolls against aberrant creatures"],lambda x:x.check("checkrace",["shardmind","wilden"],lambda x:True))
  ,feat([],"Combat Intuition","When you miss enemy with melee attack, gain +2 to opp. attack rolls vs. them until start of your next turn",lambda x:True)
  ,feat([],"Dakshai's Body-Mind Union","May expend racial power as immediate interrupt to roll save with +5 bonus",lambda x:x.check("checkrace","githzerai") and x.check("power","iron mind"))
  ,feat([],"Deadly Draw","When you pull or slide an enemy to a square adjacent to you, gain combat advantage against them until end of your next turn.",lambda x:True)
  ,feat([],"Directed Bull Rush","When you hit a target with a bull rush, you may slide that target rather than push it",lambda x:True)
  ,feat([],"Focused Mind","+4 feat bonus to saving throws against dazing effects and stunning effects",lambda x:True)
  ,feat([],"Goring Shove","Whenever you hit a target with your Goring Charge, you can push that target 1 square",lambda x:x.check("checkrace","minotaur") and x.check("power","goring charge"))
  ,feat([],"Grounding Shot","Ranged attacks ignore penalty for prone targets, and gain +2 damage against them",lambda x:True)
#Hafted Defense
  ,feat([ft("ac",["shield",0])],"Hafted Defense"
        ,"While wielding a polearm or staff in two hands, gain a +1 shield bonus to AC and Reflex"
        ,lambda x:True)
  ,feat([],"Hammering Iron","When you hit a target with an opportunity attack with a hammer, push that target 1 square",lambda x:True)
  ,feat([],"Headsman's Chop","When you hit a prone target with an axe or heavy blade, the target takes 5 extra damage",lambda x:True)
#  ,feat([],"Hybrid Talent"
 #       ,""
  #      ,lambda x:True)
  ,feat([],"Impending Victory","+1 bonus to attack rolls with at-will powers against bloodied enemies",lambda x:True)
  ,feat([ft(["voyageoftheancientsteleport","wrath of the destroyerattack","pursuitofthehuntershift"],["",2])],"Improved Aspect of Nature","Teleport +2 with Voyage power; +2 to attack roll with Wrath power; +2 shift with Pursuit power",lambda x:x.check("checkrace","wilden") and x.check("feature","nature's aspect"))
  ,feat([],"Iron Resolve of Zerthadlun","While you have at least 1 power point, you gain a +2 feat bonus to saving throws",CHECK("checkrace","githzerai"))
  ,feat([],"Liberating Shard Swarm","When you use your Shard Swarm power, you can also make a saving throw",lambda x:x.check("checkrace","shardmind") and x.check("power","shard swarm"))
  ,feat([],"Low Crawl","You can shift while prone",lambda x:True)
  ,feat([],"Lucky Start","If your initiative is highest in the combat, roll first attack roll twice",lambda x:True)
  ,feat([],"Miryath's First Strike",["First time you hit a creature that has not acted yet, it takes ",lambda x:max(x.mod("dex"),x.mod("wis"))+raising(1,10)(x)," extra psychic damage"],lambda x:x.check("wis",13) and x.check("checkrace","githzerai"))
  ,feat([],"Nimble Runner","+2 reflex until start of next turn when running, do not grant combat advantage from running",lambda x:True)
  ,feat([],"Opportunistic Shove","May bull rush as opportunity attack; on succes, target grants combat advantage until start of your next turn",lambda x:True)
  ,feat([],"Polearm Flanker","With melee attack roll with polearm, if not ajacent to target, choose different square for purposes of flanking",lambda x:True)
  ,feat([],"Power Throw",["May take -2 penalty to attack with heavy thrown weapon for +",raising(2,10)," damage"],lambda x:x.check("str",15))
  ,feat([],"Prime Burst","The benefit of Prime Shot also applies to your area burst attacks",lambda x:True)
  ,feat([ft("psychicdamage",["feat",raising(2,10)])],"Psychic Focus",["Gain a +",raising(2,10)," feat bonus with psychic powers"],CHECK("checkrace","shardmind"))
  ,feat([],"Rapid Assault",["On your first turn during an encounter, gain +",raising(2,10)," damage with melee attacks."],lambda x:True)
  ,feat([],"Secret of Reawakening","1/day after dropping to 0 hp or fewer, change current aspect when no longer dying and recover wilden racial power",lambda x:x.check("checkrace","wilden") and x.check("feature","nature's aspect"))
  ,feat([],"Shifting Defense","When you use the total defense action, you can also shift 1 square",lambda x:True)
#  ,feat([],"Skill Power"
 #       ,""
  #      ,lambda x:True)
  ,feat([],"Spring Step","You can shift 1 square as a free action when you stand up",lambda x:True)
  ,feat([],"Springing Charge","When you score a critical hit with a charge attack, you can charge a different creature as a free action 1/round",lambda x:x.check("checkrace","minotaur"))
  ,feat([],"Steady Feet","When you use the walk action, you can ignore 1 square of difficult terrain",lambda x:True)
  ,feat([],"Strike and Shove","When you score a critical hit with a melee attack, you can push the target 1 square",lambda x:True)
#  ,feat([],"Superior Implement Training"
 #       ,""
  #      ,lambda x:True)
  ,feat([],"Teamwork Defense","While adjacent to 1 or more allies with this feat, gain +1 to AC",lambda x:True)
  ,feat([ft("ac",["feat",lambda x: 2*(not(x.check("armortype",["heavy","shield","leather","hide"],True)))])],"Unarmored Agility","+2 feat bonus to AC while wearing cloth armor or no armor",lambda x:True)
  ,feat([],"Unfailing Vigor","When you roll an 18 or higher on a death saving throw, you can spend a healing surge as if you had rolled a 20",lambda x:True)
  ,feat([MultiMenu([weaponExpertise,implementExpertise],[["+",raiselist(1,[15,25])," on attack rolls with "]," weapon group and "," implements"])],"Versatile Expertise","",lambda x:True)
  ,feat([],"Vicious Advantage","Gain combat advantage against immobilized and slowed targets",lambda x:True)
  ,feat([],"Warding Defense","When you use total defense with a shield, adjacent allies gain +2 AC and Reflex until start of your next turn",lambda x:True)
  ,feat([],"Warding Shard Swarm","When you use Shard Swarm power, gain +2 to all defenses until end of your next turn",lambda x:x.check("checkrace","shardmind") and x.check("power","shard swarm"))
  ,feat([],"Watchful Redoubt","When you use total defense, gain +1 to attack rolls until end of your next turn",lambda x:True)
  ,feat([],"Zuwoth's Enlightened Step","During first round of encounter, don't provoke opportunity attacks from enemies that haven't acted yet",lambda x:x.check("checkrace","githzerai"))
###PHB3: Ardent###
  ,feat([],"Bolstering Mantle","When you spend healing surge, one ally in range of Mantle gains 5 temp HP or make a save",lambda x:x.check("checkclass","ardent") and x.check("feature","ardent mantle"))
  ,feat([ft(["insight","perception"],["mantle of clarity",WISMOD])],"Clarified Instincts",["Insight and Perception bonus of Mantle of Clarity is now equal to ",MOD("wis")],lambda x:x.check("checkclass","ardent") and x.check("feature","mantle of clarity"))
  ,feat([ft(["insight","perception"],["mantle of elation",CONMOD])],"Elated Emotions",["Diplomacy and Intimidate bonus of Mantle of Elation is now equal to ",MOD("con")],lambda x:x.check("checkclass","ardent"))
  ,feat([],"Heartening Surge","The bonus Ardent Surge grants to either defense or attack rolls increases by 1",lambda x:x.check("checkclass","ardent") and x.check("power","ardent surge"))
  ,feat([],"Mandle of Readiness","During surprise round and first round of encounter, you and allies in mantle aura gain +2 speed",lambda x:x.check("checkclass","ardent") and x.check("feature","ardent mantle"))
###PHB3: Battlemind###
  ,feat([],"Deceptive Mind","+2 bonus to all defenses while Battle Resilience is in effect",lambda x:x.check("checkclass","battlemind") and x.check("power","battle resilience"))
  ,feat([],"Improved Speed of Thought","Move 2 additional squares with Speed of Thought",lambda x:x.check("checkclass","battlemind") and x.check("power","speed of thought"))
  ,feat([],"Lure of Iron","Slide the target of your Mind Spike 1 square",lambda x:x.check("checkclass","battlemind") and x.check("power","mind spike"))
  ,feat([],"Punishing Spike","Target damaged by Mind Spike takes -2 to next save it makes before start of your next turn",lambda x:x.check("checkclass","battlemind") and x.check("power","mind spike"))
  ,feat([],"Pursuing Step","Triggering enemy grants combat advantage if you end your shift adjacent to it with Blurred Step",lambda x:x.check("checkclass","battlemind") and x.check("power","blurred step"))
###PHB3: Monk###
  ,feat([],"Crushing Tempest Style","+2 to Flurry of Blows damage when wielding a club",lambda x:x.check("checkclass","monk") and x.check("feature","flurry of blows"))
  ,feat([ft("unarmed attacknamedice",["feat",2])],"Improved Monk Unarmed Strike","Damage die of unarmed strike increased to 1d10",lambda x:x.check("checkclass","monk") and x.check("feature","unarmed combatant"))
  ,feat([],"Pointed Step Style","One target of Flurry of Blows can be 2 squares away from you when you are wielding a spear",lambda x:x.check("checkclass","monk") and x.check("feature","flurry of blows"))
###PHB3: Psion###
  ,feat([],"Controlling Advantage","Increased damage of a forced move against a target granting combat advantage",lambda x:x.check("checkclass","psion"))
  ,feat([],"Discipline Adept","Use each power granted by Discipline Focus twice per encounter",lambda x:x.check("checkclass","psion") and x.check("feature","discipline focus"))
  ,feat([],"Exchange Power","When you use Send Thoughts, you can transfer 1 power point to the target",lambda x:x.check("checkclass","psion") and x.check("power","send thoughts"))
  ,feat([],"Orbiting Orbject","While target of Far Hand is in your square or adjacent, you can sustain it as a free action",lambda x:x.check("checkclass","psion") and x.check("power","far hand"))
  ,feat([],"Precise Mind","+1 to attack rolls with at-will powers until end of turn after augmenting power by at least 2",lambda x:x.check("checkclass","psion"))
###PHB3: Runepriest###
  ,feat([ft("runefeats",["rune of eloquence",1]),ft(["bluff","diplomacy"],["feat",lambda x:x.statret("runefeats")])],"Rune of Eloquence",["Gain +",lambda x:x.statret("runefeats")," bonus to Bluff and Diplomacy checks; Rune feat"],lambda x:x.check("checkclass","runepriest"))
  ,feat([ft("runefeats",["rune of hope",1])],"Rune of Hope",["Target of Rune of Mending gains ",lambda x:x.statret("runefeats")," temporary HPl Rune feat"],lambda x:x.check("checkclass","runepriest"))
  ,feat([ft("runefeats",["rune of vengeance",1])],"Rune of Vengeance",["First time bloodied in an encounter, gain a +",lambda x:x.statret("runefeats")," bonus to damage until end of next turn; Rune feat"],lambda x:x.check("checkclass","runepriest"))
  ,feat([ft("runefeats",["rune of zeal",1]),ft(["athletics","endurance"],["feat",lambda x:x.statret("runefeats")])],"Rune of Zeal",["Gain +",lambda x:x.statret("runefeats")," bonus to Athletics and Endurance checks; Rune feat"],lambda x:x.check("checkclass","runepriest"))
###PHB3: Seeker
  ,feat([],"Bloodied Elusion","When you are bloodied by any attack, you can shift 1 square as a free action",lambda x:x.check("checkclass","seeker"))
  ,feat([],"Improved Inevitable Shot","Inevitable Shot power ignores cover and concealment, but not superior cover or total concealment",lambda x:x.check("checkclass","seeker") and x.check("power","inevitable shot"))
  ,feat([],"Inescapable Shot","Raise range of Inevitable Shot power to 10 squares from original target",lambda x:x.check("checkclass","seeker") and x.check("power","inevitable shot"))
  ,feat([],"Spiritbond Defense","When you use second wind, adjacent ally gains a +2 bonus to all defenses until start of your next turn",lambda x:x.check("checkclass","seeker") and x.check("feature","spiritbond"))
  ,feat([],"Strengthened Bond","First time bloodied in an encounter, regain use of Seeker's Bond power if it is expended",lambda x:x.check("checkclass","seeker") and x.check("feature","seeker's bond"))
###PHB3 Paragon Feats####
#Aspect of the Cultivator
  ,feat([],"Aspect of the Cultivator"
        ,"Replace one Nature's Aspect option with Aspect of the Cultivator"
        ,lambda x:x.check("level", 11) and x.check("checkrace","wilden") and x.check("feature","nature's aspect"))
  ,feat([],"Awaken Aspect","Change Aspect of Nature after a short rest",lambda x:x.check("level", 11) and x.check("checkrace","wilden") and x.check("feature","nature's aspect"))
  ,feat([],"Beast Within","+1 to attack rolls and damage rolls when bloodied",lambda x:x.check("level", 11) and x.check("checkrace","minotaur"))
  ,feat([],"Bloodborn Recovery","When you critical hit with the melee attack granted by Ferocity, you can spend a healing surge",lambda x:x.check("level", 11) and x.check("checkrace","minotaur") and x.check("feature","ferocity"))
  ,feat([],"Bloody Gore","Regain Goring Charge the first time you are bloodied in an encounter",lambda x:x.check("level", 11) and x.check("checkrace","minotaur") and x.check("power","goring charge"))
  ,feat([],"Burden of Liberty","When you use a wilden racial power, one ally in 5 squares can teleport to a square adjacent to you",lambda x:x.check("level", 11) and x.check("checkrace","wilden") and x.check("feature","nature's aspect"))
  ,feat([],"Critical Reserve","1/encounter when you score a critical hit with an unaugmented at-will psionic power, regain 1 power point",lambda x:x.check("level", 11) and x.check("feature","psionic augmentation"))
  ,feat([],"Expanded Fragments","While you are not bloodied, the range of your telepathy increases to 15",lambda x:x.check("level", 11) and x.check("checkrace","shardmind") and x.check("feature","telepathy"))
  ,feat([],"Expansive Burst","Your close burst and area burst attacks ignore cover, but not superior cover",lambda x:x.check("level", 11))
  ,feat([],"Eyes in the Back of your Head","You don't grant combat advantage from being flanked",lambda x:x.check("level", 11))
  ,feat([],"Githzerai Planewalker","Can learn Linked Portal, Planar Portal, or True portal without Ritual Caster feat, +5 on checks to perform those rituals",lambda x:x.check("level", 11) and x.check("checkrace","githzerai"))
  ,feat([],"Grazing Shot",["Target takes ",DEXMOD," damage if you miss on a ranged basic attack"],lambda x:x.check("level", 11))
  ,feat([],"Gritty Determination",["Gain ",lambda x:x.statret("level")/2+x.mod("con")," temp HP when you use a daily attack power"],lambda x:x.check("level", 11))
  ,feat([ft("crystalline mind resist",["",lambda x:max(x.mod("int"),x.mod("wis"))])],"Guarded Mind",["Increase the resistance granted by Crystalline Mind by ",lambda x:max(x.mod("int"),x.mod("wis"))],lambda x:x.check("level", 11) and x.check("checkrace","shardmind") and x.check("feature","crystalline mind"))
  ,feat([],"Healing Fragments",["When you spend a healing surge, each ally in your telepathy range regains ",WISMOD," HP"],lambda x:x.check("level", 11) and x.check("checkrace","shardmind") and x.check("feature","telepathy"))
  ,feat([],"Iron Hands",["Gain a +",WISMOD," bonus to damage rolls while Iron Mind is in effect"],lambda x:x.check("level", 11) and x.check("checkrace","githzerai") and x.check("wis",13))
  ,feat([],"Liberating Teleport","If you teleport on your turn, gain a +2 feat bonus to saving throws at the end of that turn",lambda x:x.check("level", 11))
  ,feat([],"Opportunistic Withdrawal","Your movement does not provoke opportunity attacks from adjacent enemies that are granting you combat advantage",lambda x:x.check("level", 11))
  ,feat([],"Opportunity Sidestep","When you hit with an opportunity attack, you can shift 1 square as a free action",lambda x:x.check("level", 11))
  ,feat([],"Overwhelming Critical","Whenever you score a critical hit, you also knock the target prone",lambda x:x.check("level", 11))
  ,feat([],"Psionic Rejuvenation","When you use your second wind, you also regain 1 power point",lambda x:x.check("level", 11) and x.check("checkrace","shardmind") and x.check("feature","psionic augmentation"))
  ,feat([],"Repel Charge","You can make a melee basic attack against an enemy charging you as an opportunity action",lambda x:x.check("level", 11))
  ,feat([],"Roll with it","You can shift 1 square as a free action after an enemy pulls, pushes, or slides you",lambda x:x.check("level", 11))
  ,feat([],"Secret of Escape","1/day when you drop below 0 hp and don't die, teleport 10 squares to a square adjacent to an ally",lambda x:x.check("level", 11) and x.check("checkrace","wilden"))
  ,feat([],"Shared Danger Sense","Allies in 5 squares of you gain a +2 racial bonus to initiative checks",lambda x:x.check("level", 11) and x.check("checkrace","githzerai"))
#Shield Mastery
  ,feat([],"Shield Mastery"
        ,"When you are wielding a sheild with which you have proficiency, your shield bonus also applies to your fortitude"
        ,lambda x:x.check("level", 11) and x.check("proficiency",["light","heavy"],False))
  ,feat([],"Vicious Ferocity","You can use an at-will attack instead of a melee basic attack for the attack granted by Ferocity",lambda x:x.check("level", 11) and x.check("checkrace","minotaur") and x.check("feature","ferocity"))
  ,feat([],"Wind's Fortunes","When you use Shifting Fortunes, you can teleport instead of shifting",lambda x:x.check("level", 11) and x.check("checkrace","githzerai") and x.check("feature","shifting fortunes"))
###PHB3 Ardent Feats###
  ,feat([],"Alacrity of Fortune","When ally in radius of Mantle of Clarity makes a save, they can shift 1 square as a free action",lambda x:x.check("level", 11) and x.check("checkclass","ardent") and x.check("feature","mantle of clarity"))
  ,feat([],"Elation of Fortune","When ally in radius of Mantle of Elation makes a save, they gain +1 to attack rolls until end of their next turn",lambda x:x.check("level", 11) and x.check("checkclass","ardent") and x.check("feature","mantle of elation"))
  ,feat([],"Improved Ardent Surge",["The target of Ardent Surge regains ",CHAMOD," additional HP"],lambda x:x.check("level", 11) and x.check("checkclass","ardent") and x.check("power","ardent surge"))
  ,feat([ft("mantle radius",["",5])],"Widened Mantle","Radius of Ardent Mantle increases to 10",lambda x:x.check("level", 11) and x.check("checkclass","ardent") and x.check("feature","ardent mantle"))
###PHB3 Battlemind Feats###
  ,feat([],"Defiant Fire","First time you are bloodied in an encounter, gain a use of Battle Resilience that is only usable against next attack against you",lambda x:x.check("level", 11) and x.check("checkclass","battlemind") and x.check("power","battle resilience"))
  ,feat([ft("battlemind's demandclose burst",["",2])],"Demand's Reach","Burst of Battlemind's Demand increases to 5",lambda x:x.check("level", 11) and x.check("checkclass","battlemind") and x.check("power","battlemind's demand"))
  ,feat([],"Linebreaker","Can end movement in enemy's space then slide them 1 square with Speed of Thought",lambda x:x.check("level", 11) and x.check("checkclass","battlemind") and x.check("power","speed of thought"))
  ,feat([],"Steel Rebuke",["When you damage a target with Mind Spike, adjacent enemies take ",lambda x:max(x.mod("wis"),x.mod("cha"))," psychic damage"],lambda x:x.check("level", 11) and x.check("checkclass","battlemind") and x.check("power","mind spike"))
###PHB3 Monk Feats###
  ,feat([],"Brutal Flurry",["When you target only one creature with Flurry of Blows, the target takes ",raising(2,20)," extra damage"],lambda x:x.check("level", 11) and x.check("checkclass","monk") and x.check("feature","flurry of blows"))
  ,feat([],"Effortless Motion","When you use a monk movement technique, gain a +1 bonus to AC until the end of your next turn",lambda x:x.check("level", 11) and x.check("checkclass","monk"))
  ,feat([],"Simple Precision","Gain a +1 bonus to the attack rolls for monk at-will powers until end of next turn after hitting with a monk at-will power or basic attack",lambda x:x.check("level", 11) and x.check("checkclass","monk"))
  ,feat([],"Starblade Flurry","Can add a single target within 5 squares to Flurry of Blows by throwing a dagger or shuriken",lambda x:x.check("level", 11) and x.check("checkclass","monk") and x.check("feature","flurry of blows"))
###PHB3 Psion Feats###
  ,feat([],"Desperate Renewal","Can spend healing surge regain 2 power points for second wind, instead of recovering hit points",lambda x:x.check("level", 11) and x.check("checkclass","psion"))
  ,feat([],"Dominating Mind","When you daze, dominate, or stun a target with a psionic effect, they get -2 to the first save against that effect",lambda x:x.check("level", 11) and x.check("checkclass","psion"))
  ,feat([],"Predictive Defense","Gain +2 to all defenses against melee attacks after hitting an enemy with an unaugmented at-will power",lambda x:x.check("level", 11) and x.check("checkclass","psion"))
  ,feat([],"Targeting Force","When you immobilize or restrain a target with a psionic power, gain +2 to next attack roll with force power against that target",lambda x:x.check("level", 11) and x.check("checkclass","psion"))
###PHB3 Runepriest Feats###
  ,feat([],"Defiant Light","Gain resist 5 necrotic, resist 5 radiant, and +1 to attack rolls with runepriest powers against targets vulnerable to radiant damage",lambda x:x.check("level", 11) and x.check("checkclass","runepriest") and x.check("feature","defiant word"))
  ,feat([ft("runefeats",["rune of escape",1])],"Rune of Escape",["Whenever ally in 5 squares uses 2nd wind, they can shift ",lambda x:x.statret("runefeats")," squares"],lambda x:x.check("level", 11) and x.check("checkclass","runepriest"))
  ,feat([ft("runefeats",["rune of torment",1])],"Rune of Torment",["When enemy in 5 squares fails a save against an effect caused by one of your runepriest powers, they take ",lambda x:x.statret("runefeats")," damage"],lambda x:x.check("level", 11) and x.check("checkclass","runepriest"))
  ,feat([],"Wrath of Defeat","When you drop to 0 hp or fewer, use immediate interrupt to make a melee basic attack with a +2 bonus to the attack roll",lambda x:x.check("level", 11) and x.check("checkclass","runepriest") and x.check("feature","wrathful hammer"))
###PHB3 Seeker Feats###
  ,feat([],"Bloodbond Wrath","Target of Encaging Spirits grants combat advantage to you until end of your next turn",lambda x:x.check("level", 11) and x.check("checkclass","seeker") and x.check("power","encaging spirits"))
  ,feat([],"Inevitable Volley","When you use Inevitable Shot, make two ranged basic attacks against two different targets",lambda x:x.check("level", 11) and x.check("checkclass","seeker") and x.check("power","inevitable shot"))
  ,feat([ft("basicrangeddamage",["",lambda x:max(x.mod("dex"),x.mod("int"))])],"Primal Eye",["Add ",lambda x:max(x.mod("dex"),x.mod("int"))," to damage rolls with ranged basic attacks"],lambda x:x.check("level", 11) and x.check("checkclass","seeker"))
  ,feat([],"Punishing Rebuke","Sprit's Rebuke deals 1[W] extra damage",lambda x:x.check("level", 11) and x.check("checkclass","seeker") and x.check("power","spirit's rebuke"))
###PHB3 Epic Feats###
  ,feat([],"Adamantine Mind","+4 to all defenses, instead of +2, with Iron Mind",lambda x:x.check("level", 21) and x.check("checkrace","githzerai") and x.check("power","iron mind"))
  ,feat([],"Burden of Vision","Gain blindsight 10 until end of your next turn when you use a Wilden racial power",lambda x:x.check("level", 21) and x.check("checkrace","wilden") and x.check("feature","nature's aspect"))
  ,feat([],"Champion of Nature","When you reach a milestone, choose a second aspect of nature to manifest",lambda x:x.check("level", 21) and x.check("checkrace","wilden") and x.check("feature","nature's aspect"))
  ,feat([],"Clarifying Presence","When any ally in telepathy range makes a saving throw vs. daze or stun, they can roll twice and use either result",lambda x:x.check("level", 21) and x.check("checkrace","shardmind") and x.check("feature","telepathy"))
  ,feat([],"Cleaving Axe","1/round when you reduce an enemy to 0 HP, make a melee basic attack as a free action",lambda x:x.check("level", 21))
  ,feat([],"Deft Aim","When you use a bow or a crossbow to make a ranged basic attack against AC, you can attack Reflex instead",lambda x:x.check("level", 21))
  ,feat([],"Iron Body",["While Iron Mind is in effect, gain resist ",WISMOD," to all damage"],lambda x:x.check("level", 21) and x.check("checkrace","githzerai") and x.check("power","iron mind"))
  ,feat([],"Long Step","Whenever you shift, you can shift 1 additional square",lambda x:x.check("level", 21))
  ,feat([],"Mythic Senses","When you roll for initiative, you can substitute a Perception check for your Initiative check",lambda x:x.check("level", 21) and x.check("checkrace","minotaur"))
  ,feat([],"Peerless Reaction","When you are hit by an attack, you can expend Iron Mind as immediate interrupt to use your second wind",lambda x:x.check("level", 21) and x.check("checkrace","githzerai") and x.check("power","iron mind"))
  ,feat([],"Rapid Regeneration",["While you have regeneration, the value of the regeneration increases by ",CONMOD],lambda x:x.check("level", 21))
  ,feat([],"Rejuvenating Shardswarm","When you use your Shard Swarm, you can also spend a healing surge",lambda x:x.check("level", 21) and x.check("checkrace","shardmind") and x.check("power","shard swarm"))
  ,feat([],"Secret of Enduring Vigor","1/day when you drop to 0 hp or fewer, you can spend a healing surge as an immediate interrupt",lambda x:x.check("level", 21) and x.check("checkrace","wilden"))
  ,feat([ft("initiative",["feat",8])],"Superior Initiative","You gain a +8 feat bonus to initiative checks",lambda x:x.check("level", 21))
  ,feat([],"Telepathic Sustenance","Allies within your telepathy range don't need to breathe",lambda x:x.check("level", 21) and x.check("checkrace","shardmind") and x.check("feature","telepathy"))
  ,feat([],"Uncanny Scent","Ignore concealment and total concealment when attacking creatures within 2 squares; determine location of invisible creatures within 2 squares",lambda x:x.check("level", 21) and x.check("checkrace","minotaur") and x.check("training","perception"))
  ,feat([],"Vicious Stomp","When you knock a target prone with Goring Charge, make a melee basic attack against target as a free action",lambda x:x.check("level", 21) and x.check("checkrace","minotaur") and x.check("power","goring charge"))
###PHB3 Ardent Feats###
  ,feat([],"Endangering Outrage",["Each enemy affected by Ardent Outrage has vulerability ",CONMOD," to all damage until end of your next turn"],lambda x:x.check("level", 21) and x.check("checkclass","ardent") and x.check("power","ardent outrage"))
  ,feat([],"Epic Alacrity","Each ally affected by Ardent Alacrity can shift half their speed",lambda x:x.check("level", 21) and x.check("checkclass","ardent") and x.check("power","ardent alacrity"))
###PHB3 Epic Ardent Feats###
  ,feat([],"Devouring Demand","When you augment Battlemind's Demand, you can target up to three creatures in the burst",lambda x:x.check("level", 21) and x.check("checkclass","battlemind") and x.check("power","battlemind's demand"))
  ,feat([],"Vengeance Spike","When you damage a target with Mind Spike, gain +2 to attack rolls against that target until end of your next turn",lambda x:x.check("level", 21) and x.check("checkclass","battlemind") and x.check("power","mind spike"))
###PHB3 Epic Monk Feats###
  ,feat([],"Centered Master","Centered Flurry of Blows can slide each target 2 squares",lambda x:x.check("level", 21) and x.check("checkclass","monk") and x.check("power","centered flurry of blows"))
  ,feat([],"Stone Fist Master","Each target of your Stone Fist Flurry grants combat advatage for the next attack agaisnt it before end of your next turn",lambda x:x.check("level", 21) and x.check("checkclass","monk") and x.check("power","stone fist flurry of blows"))
  ,feat([],"Unarmed Mastery","Crit on 19-20 when making melee attack with unarmed strike",lambda x:x.check("level", 21) and x.check("checkclass","monk") and x.check("feature","unarmed combatant"))
###PHB3 Epic Psion Feats###
  ,feat([],"Psychic Bastion","+4 to all defenses until end of your next turn after critical hit with psionic psychic power",lambda x:x.check("level", 21) and x.check("checkclass","psion"))
  ,feat([],"Resilient Shield","Resist 10 to all damage until end of your next turn after critical hit with psionic force power",lambda x:x.check("level", 21) and x.check("checkclass","psion"))
###PHB3 Epic Runepriest Feats###
  ,feat([ft("runefeats",["rune of battle",1])],"Rune of Battle",["When you crit with runepriest power, ally adjacent to target makes melee basic attack with +",lambda x:x.statret("runefeats")," bonus to attack and damage"],lambda x:x.check("level", 21) and x.check("checkclass","runepriest"))
  ,feat([ft("runefeats",["rune of health",1])],"Rune of Health",["Each ally other than target in range of Rune of Mending regains ",lambda x:x.statret("rune of health")+3," HP"],lambda x:x.check("level", 21) and x.check("checkclass","runepriest") and x.check("power","rune of mending"))
###PHB3 Epic Seeker Feats###
  ,feat([],"Inevitable Accuracy","When you do not hit with Inevitable Accuracy, regain the use of the power",lambda x:x.check("level", 21) and x.check("checkclass","seeker") and x.check("power","inevitable shot"))
  ,feat([],"Ruthless Price","When you use Encaging Spirits, you can immobilize the any of the targets, instead of slowing them",lambda x:x.check("level", 21) and x.check("checkclass","seeker") and x.check("power","encaging spirits"))
  ,feat([],"Spiritbond Outrage","Targets damaged with Spirit's Rebuke also fall prone",lambda x:x.check("level", 21) and x.check("checkclass","seeker") and x.check("power","spirit's rebuke"))
])
allFeatDict["Multiclass"]=addFeats([
###Multiclass###
  feat([ft("religion",("training",5)),ft("clericimplement","Holy Symbol"),ft("checkclass","cleric"),Power("Healing Word",basePowers["Healing Word"].keys,"daily",basePowers["Healing Word"].action,basePowers["Healing Word"].effects[1:])],"Initiate of the Faith","Healing Word 1/day, can use holy symbols for clerical powers, Religion skill training",lambda x: x.check("wis",13) and not(x.check("class","cleric")) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")))
  ,feat([ft("skillpick",SkillPick("fighter",1, "Fighter Skill")),ft("checkclass","fighter")],"Student of the Sword","1/encounter gain +1 on one attack roll with chosen weapon style.  Mark target of attack.",lambda x: x.check("str",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","fighter")))
  ,feat([ft("skillpick",SkillPick("paladin",1, "Paladin Skill")),ft("checkclass","paladin"),Power("Divine Challenge",basePowers["Divine Challenge"].keys,"encounter",basePowers["Divine Challenge"].action,basePowers["Divine Challenge"].effects)],"Soldier of the Faith","1/encounter use Divine Challenge, can use holy symbols or a Holy Avenger for paladin powers.",lambda x: x.check("str",13) and x.check("cha",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","paladin")))
  ,feat([ft("skillpick",SkillPick("ranger",1, "Ranger Skill")),ft("checkclass","ranger"),ft("feat",[feat([],"Hunter's Quarry")])],"Warrior of the Wild",["Deal an extra ",raising(1,10),"d",lambda x:6+x.featuretotal("huntersdice"),plus(lambda x: x.featuretotal("huntersbonus"))," damage on one attack each encounter against your quarry"],lambda x: (x.check("str",13) or x.check("dex",13)) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","ranger")))
  ,feat([ft("thievery",("training",5)),ft("checkclass","rogue"), ft("feat",[feat([],"Sneak Attack")])],"Sneak of Shadows",["Deal an extra ",raiselist(1,[1,11,21,21]),"d",lambda x:6+x.featuretotal("sneakdice"),plus(lambda x:x.featuretotal("sneakbonus"))," damage on one attack each encounter when you have combat advantage"],lambda x: x.check("dex",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","rogue")))
  ,feat([ft("skillpick",SkillPick("warlock", 1, "Warlock Skill")),ft("checkclass","warlock"),atWillAsEncounter("WarlockSpecial","Pact Initiate Power")],"Pact Initiate","",lambda x: x.check("cha",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","warlock")))
  ,feat([ft("skillpick",SkillPick("warlord",1, "Warlord Skill")),ft("checkclass","warlord"),Power("Inspiring Word",basePowers["Inspiring Word"].keys,"daily",basePowers["Inspiring Word"].action,basePowers["Inspiring Word"].effects[1:])],"Student of Battle","Training in one warlord skill, 1/day use Inspiring Word power.",lambda x: x.check("str",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","warlord")))
  ,feat([ft("arcana",("training",5)),ft("checkclass","wizard"),atWillAsEncounter(powerList["wizardat-will1"].values(),"Arcane Initiate Power")],"Arcane Initiate","Training in Arcana, one wizard at-will power as an encounter power, can use wizard implements",lambda x: x.check("int",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","wizard")))
###PHB2 Multiclass Feats###
  ,feat([ft("religion",("training",5)),ft("checkclass","invoker"),atWillAsEncounter(powerList["invokerat-will1"].values(),"Acolyte of Divine Secrets power")],"Acolyte of Divine Secrets","Training in religion, one invoker at-will power as an encounter power, can use Invoker implements",lambda x: x.check("wis",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","invoker")))
  ,feat([ft("arcana",("training",5)),ft("checkclass","sorcerer")],"Arcane Prodigy",["Training in Arcana, +",lambda x:1+raising(1,10)(x)," bonus damage 1/encounter, can use Sorcerer implements."],lambda x: x.check("cha",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","sorcerer")))
  ,feat([ft("skillpick",SkillPick("bard",1, "Bard Skill")),ft("checkclass","bard"),Power("Majestic Word",basePowers["Majestic Word"].keys,"daily",basePowers["Majestic Word"].action,basePowers["Majestic Word"].effects[:-1])],"Bardic Delittante","Training in one bard skill, 1/day use Majestic Word power, can use bard implements",lambda x: x.check("cha",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","bard")))
  ,feat([ft("skillpick",SkillPick("barbarian",1, "Barbarian Skill")),ft("checkclass","barbarian")],"Berserker's Fury","Training in one barbarian skill, 1/day gain +2 bonus to damage rolls until end of the encounter",lambda x: x.check("str",13) and x.check("con",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","barbarian")))
  ,feat([ft("skillpick",SkillPick("warden",1, "Warden Skill")),ft("checkclass","warden")],"Defender of the Wild","Training in one warden skill, mark all adjacent enemies 1/encounter",lambda x: x.check("str",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","warden")))
  ,feat([ft("religion",("training",5)),ft("checkclass","avenger"),Power("Oath of Enmity",basePowers["Oath of Enmity"].keys,"daily",basePowers["Oath of Enmity"].action,basePowers["Oath of Enmity"].effects)],"Divine Bloodline","Training in religion, 1/encounter use Oath of Enmity power, can wield avenger implements",lambda x: x.check("wis",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","avenger")))
  ,feat([ft("nature",("training",5)),ft("checkclass","druid"),basePowers["Wild Shape"].copy(),atWillAsEncounter(powerList["druidat-will1"].values(),"Initiate of the Old Faith power","encounter","beast form")],"Initiate of the Old Faith","Training in nature, gain Wild Shape power, gain 1 druid at-will power as encounter, can wield druid implements",lambda x: x.check("wis",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","druid")))
  ,feat([ft("nature",("training",5)),ft("checkclass","shaman"),Power("Call Spirit Companion",basePowers["Call Spirit Companion"].keys,basePowers["Call Spirit Companion"].often, "standard",basePowers["Call Spirit Companion"].effects),atWillAsEncounter([basePowers["Spirit's Fangs"],basePowers["Spirit's Shield"]],"Spirit Talker Power")],"Spirit Talker","Training in nature, gain Call Spirit Companion, can wield shaman implements",lambda x: x.check("wis",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","shaman")))
###PHB3 Multiclass Feats###
  ,feat([ft("skillpick",SkillPick("battlemind",1,"Battlemind Skill")),ft("checkclass","battlemind"),Power("Battlemind's Demand",basePowers["Battlemind's Demand"].keys,"encounter", basePowers["Battlemind's Demand"].action,basePowers["Battlemind's Demand"].effects+[Special("The mark lasts until the end of your next turn.")],"battlemind","multiclass")],"Demanding Talent","Gain training in one battlemind class skill, gain Battlemind's Demand 1/encounter",lambda x: x.check("con",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","battlemind")))
  ,feat([ft("skillpick",SkillPick("psion",1,"Psion Skill")),ft("checkclass","psion"),atWillAsEncounter(powerList["psionat-will1"].values(),"Disciplined Talent Power")],"Disciplined Talent","Training in one psion class skill, use one 1st level unaugmented psion at-will power 1/encounter, use psion implements",lambda x: x.check("int",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","psion")))
  ,feat([ft("skillpick",SkillPick("ardent",1,"Ardent Skill")),ft("checkclass","ardent"),Power("Ardent Surge",basePowers["Ardent Surge"].keys,"daily", basePowers["Ardent Surge"].action,basePowers["Ardent Surge"].effects[1:],"ardent","multiclass")],"Fervent Talent","Training in one ardent class skill, use Ardent Surge 1/day",lambda x: x.check("cha",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","ardent")))
  ,feat([ft("skillpick",SkillPick("monk",1,"Monk Skill")),ft("checkclass","monk"),atWillAsEncounter([basePowers["Centered Flurry of Blows"],basePowers["Stone Fist Flurry of Blows"]],"Monastic Disciple Power")],"Monastic Disciple","Training in one monk class skill, use flurry of blows 1/encounter, use monk implements",lambda x: x.check("dex",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","monk")))
  ,feat([ft("nature",["training",5]),ft("checkclass","seeker"),Power("Inevitable Shot",basePowers["Inevitable Shot"].keys,"daily", basePowers["Inevitable Shot"].action,basePowers["Inevitable Shot"].effects[:-1],"seeker","multiclass"),atWillAsEncounter(powerList["seekerat-will1"].values(),"Primal Sharpshooter Power")],"Primal Sharpshooter","Training in Nature, use one 1st level seeker at-will power 1/encounter, use Inevitable Shot 1/day",lambda x: x.check("wis",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","seeker")))
  ,feat([ft("religion",["training",5]),ft("checkclass","runepriest"),Power("Rune of Mending",basePowers["Rune of Mending"].keys,"daily", basePowers["Rune of Mending"].action,basePowers["Rune of Mending"].effects[1:-2],"runepriest","multiclass")],"Student of Divine Runes","Training in Religion, use Rune of Mending 1/day",lambda x: x.check("str",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","runepriest")))
###Martial Power: Multiclass feats###
  ,feat([ft("feat",[feat([],"combat superiority")])],"Battle Acumen",[plus(lambda x:x.mod("wis"),1)," bonus to opportunity attacks.  Attack stops opponents movement if it hits."],lambda x:x.check("checkclass","fighter") and not x.check("class","fighter") and x.check("paragonname","paragon multiclass"))
  ,feat([ft("skillpick",SkillPick("fighter",1, "Fighter Skill")),ft("checkclass","fighter")],"Battle Awareness","1/encounter: basic melee attack against shifting enemy or enemy that makes an attack that doesn't target you.",lambda x: x.check("str",13) and x.check("wis",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","fighter")))
  ,feat([ft("featureadd","combat leader"),ft("initiative ",["combat leader",2])],"Battle Instructor",["Each ally in 10 squares that can see and hear you gains a +",lambda x:x.statret("combatleader")," power bonus to initiative"],lambda x:x.check("checkclass","warlord") and not(x.check("class","warlord")) and x.check("paragonname","paragon multiclass"))
  ,feat([ft("featureadd","prime shot")],"Courageous Shooter","+1 on ranged attack rolls if no allies are closer to your target than you are.",lambda x:x.check("checkclass","ranger") and not x.check("class","ranger") and x.check("paragonname","paragon multiclass"))
  ,feat([ft("featureadd","first strike")],"First In","Combat advantage against any creatures that have not yet acted this encounter",lambda x:x.check("checkclass","rogue") and not x.check("class","rogue") and x.check("paragonname","paragon multiclass"))
  ,feat([ft("skillpick",SkillPick("warlord",1, "Warlord Skill")),ft("checkclass","warlord")],"Inspiring Leader",["Training in Warlord skill,1/encounter: Ally who can see you and spends an action point gains ",lambda x:x.statret("level")/2+1," temporary HP"],lambda x: x.check("str",13) and x.check("cha",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","warlord")))
  ,feat([ft("stealth",("training",5)),ft("checkclass","rogue"), ft("light bladelegal",["macename","clubname"]),ft(["rattlingdamage","macenamedamage"],["",2]),ft(["rattlingdamage","clubnamedamage"],["",2]),ft("proficiency",["club","mace"]), ft("feat",[feat([],"Ruthless Ruffian")])],"Ruthless Efficiency",["Training in stealth, Club / Mace proficiency, club and mace work with light blade rogue powers, add str mod to Rattling keyword powers with club or mace",plus(lambda x:x.featuretotal("sneakbonus"))," damage on one attack each encounter when you have combat advantage"],lambda x: x.check("dex",13) and x.check("str",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","rogue")))
  ,feat([ft("skillpick",SkillPick(["bluff","intimidate"],1,"Sly Dodge Skill")),ft("checkclass","rogue")],"Sly Dodge",["Training in bluff or intimidate, 1/encounter, when an enemy makes an opportunity attack against you, add ",CHAMOD," to you AC against that attack"] ,lambda x: x.check("dex",13) and x.check("cha",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","rogue")))
  ,feat([ft("skillpick",SkillPick("warlord",1, "Warlord Skill")),ft("checkclass","warlord")],"Inspiring Leader",["Training in Warlord skill, 1/encounter: Ally who can see you and spends an AP to attack gains a +1 bonus to that attack roll"],lambda x: x.check("str",13) and x.check("int",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","warlord")))
  ,feat([ft("skillpick",SkillPick("ranger",1, "Ranger Skill")),ft("onehanddual",["onehanddual",1]),ft("checkclass","ranger")],"Two-Blade Warrior","Training in Ranger skill, wield one-handed weapon in off hand as though it were an off-hand weapon",lambda x: x.check("str",13) and x.check("int",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not(x.check("class","warlord")))
###Primal Power: Multiclass feats###
  ,feat([],"Hunting Predator","While you are in beast form, you gain +1 to speed",CHECK("feature","initiate of the old faith"))
  ,feat([Power("Healing Spirit",basePowers["Healing Spirit"].keys,"encounter",basePowers["Inspiring Word"].action,basePowers["Inspiring Word"].effects[1:])],"Mending Spirit","You gain the shaman power Healing Spirit 1/encounter",CHECK("feature","spirit talker"))
  ,feat([ft("featureadd","rampage")],"Rampant Fury","1/round, when you critical with a barbarian power, make a melee basic attack as a free action",CHECK("feature","berserker's fury"))
  ,feat([],"Warden's Endurance","1/encounter, make saving throw at start of your turn",CHECK("feature","defender of the wild"))
#Forgotten Realms: Multiclass Feats
  ,feat([ft("arcana",("training",5)),ft("checkclass","swordmage")],"Blade Initiate","1/day when wielding a blade gain +1 to AC for rest of encounter, or +3 if you have one hand free",lambda x: x.check("int",13) and (len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility")) and not x.check("swordmage","class"))
  ,feat([ft("checkclass","spellscarred"),specMenus["studentOfThePlague"]],"Student of the Plague","",lambda x: len(x.statret("checkclass"))<2 or x.check("feature","multiclass versatility"))
#Novice Power, etc.
  ,feat([specialMenu(["1","3","7","13","17","23","27"],[feat([ft("replacepower","encounter"+str(x))]) for x in [1,3,7,13,17,23,27]],"Replace one level "," encounter power with one from your secondary class")],"Novice Power","",lambda x:len(x.statret("checkclass"))>1 and x.check("level",4) and not(x.check("checkclass",psionicAugmentation,True)))
  ,feat([specialMenu(["1","3","7","13","17","23","27"],[feat([ft("replacepower","at-will"+str(x))]) for x in [" 1 #2",3,7,13,17,23,27]],"Replace one level "," at-will attack power with one from your secondary class")],"Psionic Complement","",lambda x:len(x.statret("checkclass"))>1 and x.check("level",4) and x.check("class",psionicAugmentation,True) and x.statret("checkclass")[1] in psionicAugmentation)
  ,feat([specialMenu(["1","3","7","13","17","23","27"],[feat([ft("replacepower","at-will"+str(x)),ft("psps",("",-2))])]+[feat([ft("replacepower","at-will"+str(x)),ft("psps",("",(x+9)/10*-2))]) for x in [3,7,13,17,23,27]],"Replace one level "," at-will attack power with an encounter attack power from your secondary class.  Lose some power points")],"Psionic Conventionalist","",lambda x:len(x.statret("checkclass"))>1 and x.check("level",4) and x.check("class",psionicAugmentation,True) and x.statret("checkclass")[1] not in psionicAugmentation)
  ,feat([specialMenu(["1","3","7","13","17","23","27"],[feat([ft("replacepower","encounter"+str(x)),ft("psps",("",(x+9)/10*2))]) for x in [1,3,7,13,17,23,27]],"Replace one level ",[" encounter attack power with an at-will attack power from your secondary class.  ",lambda x:x.statret("psps")," PSPs"])],"Psionic Dabbler","",lambda x:len(x.statret("checkclass"))>1 and x.check("level",4) and not(x.check("class",psionicAugmentation,True)) and x.statret("checkclass")[1] in psionicAugmentation)
  ,feat([specialMenu(["2","6","10","16","22"],[feat([ft("replacepower","utility"+str(x))]) for x in [2,6,10,16,22]],"Replace one level "," utility power with one from your secondary class")],"Acolyte Power","",lambda x:len(x.statret("checkclass"))>1 and x.check("level",8))
  ,feat([specialMenu(["1","5","9","15","19","25","29"],[feat([ft("replacepower","daily"+str(x))]) for x in [1,5,9,15,19,25,29]],"Replace one level "," daily power with one from your secondary class")],"Adept Power","",lambda x:len(x.statret("checkclass"))>1 and x.check("level",10))
])
allFeatList={}
for x in allFeatDict.keys():
    for z in allFeatDict[x].keys():
        allFeatList[z]=allFeatDict[x][z]
specMenus["deities"]=specialMenu(deities,[],"Follower of ","")
for deity in specMenus["deities"].optionNames:
	specMenus["deities"].optionFeats+=[feat([ft("deity",deity.lower())])]

def statmenu(statlist, pre="", post="", num=2):
    return specialMenu(statlist, [feat([ft(x,["",num])]) for x in statlist], pre, post)

specMenus["dragonbornBreath"]=specialMenu(["Acid","Cold","Fire","Lightning","Poison"],[])
specMenus["dragonSoul"]=specialMenu(["acid","cold","fire","lightning","thunder"],[feat([])]*5,["Resist ",lambda x:raising(5,10)(x)+x.statret("dragon soul resistance")," "],[".  Your arcane powers ignore up to ",lambda x:raising(5,10)(x)+x.statret("dragon soul resistance")," resistance of this element."])
for element in specMenus["dragonbornBreath"].optionNames:
	specMenus["dragonbornBreath"].optionFeats+=[feat([ft("dragonbreathelement",element.lower()),Power("Dragon Breath"
                  ,[element.lower()],"encounter","minor", [Target("All creatures in area",("close blast",3)),Atk([choosestat("dragon breath",["str","con","dex"]),raising(2,10)],"reflex", damage([raising(1,10),6],[CONMOD]))],"dragonborn","racial power")],"Dragon Breath")]

racePower={"bugbear": Power("Predatory Eye",[],"encounter","minor",[Effect(["If you have combat advantage against a target, you deal +",raising(1,10),"d6 damage on the next attack you make against that target.  You must apply this bonus before the end of your next turn."])],"bugbear","racial power"),
           "changeling1": Power("Changeling Disguise",["polymorph"],"at-will","minor",[Effect("You alter your physical form to take on the appearance of any Medium humanoid.  You retain your statistics in your new for, and your clothing, armor, and possessions do not change.  The new form lasts until you change form again."),Line("Any creature that attempts to see through your ruse makes an insight check opposed by your Bluff check, and you gain a +5 bonus to your check.")],"changeling","racial power"),
           "changeling2": Power("Changeling Trick",[],"encounter","minor",[Target("one creature",("melee",1)),Effect("You make a Bluff check opposed by the target's passive Insight.  If your check succeeds, you gain combat advantage against the target until the end of your next turn.")],"changeling","racial power"),
           "deva": Power("Memory of a Thousand Lifetimes",[],"encounter","no",[Trigger("You make an attack roll, a saving throw, a skill check, or an ability check and dislike the result"),Effect(["You add 1d",lambda x:6+x.featuretotal("memorydie")," to the triggering roll"])],"deva","racial power"),
           "doppelganger": Power("Change Shape",["polymorph"],"at-will","minor",[Effect("You can alter your physical form to take on the appearance of any medium humanoid, including a unique individual.")],"doppleganger","racial power"),
           "drow1": Power("Cloud of Darkness",[],"encounter","minor",[Effect("This power creates a cloud of darkness that remains in place until the end of your next turn.  The cloud blocks line of sight for all creatures except you.  Any creature except you within the cloud is blinded.",("close burst",1))],"drow","racial power"),
           "drow2": Power("Darkfire",[],"encounter","minor", [Target("one creature",("ranged",10)),Atk([choosestat("darkfire",["int","wis","cha"]),raising(2,10)],"reflex", None),Hit("Until the end of your next turn, all attacks against the target have combat advantage, and the target cannot benefit from invisibility or concealment.")],"drow","racial power"),
           "elf": Power("Elven Accuracy",[],"encounter","free",[Effect("Reroll an attack roll.  Use the second roll, even if it's lower.")],"elf","racial power"),
           "eladrin":Power("Fey Step",["teleportation"],"encounter","move",[Effect("Teleport up to 5 squares")],"eladrin","racial power"),
           "githyanki": Power("Telekinetic Leap",[],"encounter","move",[Target("you or one ally",("ranged",10)),Effect("The target can fly up to 5 squares.  If this power is used on an ally, that ally must remain in your line of sight at all times during this effect.")],"githyanki","racial power"),
           "githzerai": Power("Iron Mind",[],"encounter","immediate interrupt",[Trigger("You are hit by an attack"),Effect("You gain a +2 bonus to all defenses until the end of your next turn")],"githzerai","racial power"),
           "gnoll": Power("Ferocious Charge",[],"encounter","standard",[Effect(["You charge and deal an extra ",raising(2,10)," damage on a successful attack"])],"gnoll","racial power"),
           "gnome": Power("Fade Away",["illusion"],"encounter","immediate reaction",[Trigger("You take damage"),Effect("You are invisible until you attack or until the end of your next turn.")],"gnome","racial power"),
           "goblin": Power("Goblin Tactics",[],"at-will","immediate reaction",[Trigger("You are missed by a melee attack"),Effect("You shift one square")],"goblin","racial power"),
           "goliath": Power("Stone's Endurance",[],"encounter","minor",[Effect(["You gain resist ",raising(5,10)," to all damage until the end of your next turn."])],"goliath","racial power"),
           "halfling": Power("Second Chance",[],"encounter","immediate",[Effect("When an attack hits you, force an enemy to roll the attack again.  The enemy must use the second roll, even if it's lower.")],"halfling","racial power"),
           "half-orc": Power("Furious Assault",[],"encounter","free",[Trigger("You hit an enemy"),Effect("The attack deals 1[W] extra damage if it's a weapon attack or 1d8 extra damage if it isn't")],"half-orc","racial power"),
           "hobgoblin": Power("Hobgoblin Resilience",[],"encounter","immediate reaction",[Trigger("You suffer an effect that a save can end"),Effect("You make a saving throw against the effect")],"hobgoblin","racial power"),
           "kalashtar": Power("Bastion of Mental Clarity",[],"encounter","immediate interrupt",[Trigger("An enemy hits or misses you with an attack against your Will"),Target("You and each ally in burst",("close burst",5)),Effect("Each target gains a +4 power bonus to Will until the end of your next turn.")],"kalashtar","racial power"),
           "kobold": Power("Shifty",[],"at-will","minor",[Effect("You shift 1 square")],"kobold","racial power"),
           "minotaur": Power("Goring Charge",[],"encounter","standard",[Effect("You charge and make the following attack in place of a basic melee attack"),Target("one creature",("melee",1)),Atk([choosestat("goring charge",["str","dex","con"]),raising(2,10),2],"AC", damage([raising(1,10),6],[choosestat("goring charge",["str","dex","con"], False)])),Hit("You knock the target prone")],"minotaur","racial power"),
           "orc": Power("Warrior's Surge",["healing","weapon"],"encounter","standard",[Atk([STRMOD],"AC", damage(raising(1,20),[STRMOD]),["melee"]),Hit("You can spend a healing surge")],"orc","racial power"),
           "shadar-kai": Power("shadow jaunt",["teleportation"],"encounter","move",[Effect("You teleport 3 squares and become insubstantial until the start of your next turn")],"shadar-kai","racial power"),
           "shardmind": Power("Shard Swarm",["teleportation"],"encounter","move",[Target("each enemy in burst",("close burst",1)),Effect("Each target grants combat advantage to you until the end of your next turn.  You then teleport half your speed.")],"shardmind","racial power"),
           "shifter, longtooth": Power("Longtooth Shifting",["healing"],"encounter","minor",[Special("You must be bloodied to use this power"),Effect(["Until the end of the encounter or until rendered unconscious, you gain a +2 bonus to damage rolls.  In addition, for as long as you are bloodied, you gain regeneration ",raising(2,10)])],"longtooth shifter","racial power"),
           "shifter, razorclaw": Power("Razorclaw Shifting",[],"encounter","minor",[Special("You must be bloodied to use this power"),Effect("Until the end of the encounter or until rendered unconscious, your speed increases by 2 and you gain a +1 bonus to AC and reflex defense")],"razorclaw shifter","racial power"),
           "tiefling": Power("Infernal Wrath",[],"encounter","minor",[Effect(["You can channel your fury to gain a +1 power bonus on your next attack roll against an enemy that hit you since your last turn.  If your attack hits and deals damage, add ", lambda x:x.mod("cha")," extra damage"])],"tiefling","racial power"),
           "warforged": Power("Warforged Resolve",["healing"],"encounter","minor",[Effect(["You gain ",lambda x:3+x.statret("level")/2," temporary hit points and can make a saving throw against one effect on you that deals ongoing damage.  If you are bloodied, you also regain ",lambda x:3+x.statret("level")/2," hit points."])],"warforged","racial power"),
           "wilden1": Power("Voyage of the Ancients",["teleportation"],"encounter","free",[Trigger("You hit an enemy with an area or close attack"),Effect(["You teleport ",lambda x:x.statret("voyageoftheancientsteleport")+3," squares.  Choose a single enemy that you hit with the attack.  You and one ally you can see gain combat advantage against that enemy until the end of your next turn."])],"wilden","racial power"),
           "wilden2": Power("Wrath of the Destroyer",[],"encounter","immediate reaction",[Trigger("A bloodied enemy attacks you or your ally adjacent to you"),Effect("You either make a basic melee attack against the triggering enemy or charge it.  If your attack hits, the enemy is also dazed until the end of your next turn.")],"wilden","racial power"),
           "wilden3": Power("Pursuit of the Hunter",[],"encounter","immediate reaction",[Trigger("An enemy within 2 squares of you moves on its turn"),Effect(["You shift ",lambda x:x.statret("pursuitofthehuntershift")+3," squares.  Until the end of your next turn, you deal 1d6 extra damage to the triggering enemy when you hit it, and you ignore the -2 penalty to attack rolls for attacking it when it has cover or concealment."])],"wilden","racial power"),
           }



raceList={
          "Bugbear":[feat([ft(["intimidate","stealth","str","dex"],["racial",2])],"Racial Skills","+2 to intimidate and stealth checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([ft("weaponsize",("racial",1))],"Oversized","Use weapons of your size or one size larger than you")
                       ,feat([racePower["bugbear"]],"Predatory Eye")],
          "Changeling":[feat([ft(["bluff","insight","cha"],["racial",2])],"Racial Skills","+2 to Bluff and Insight checks")
                       ,feat([statmenu(["dex","int"],"+2 to")],"Changeling Stat Bonus")
                       ,feat([],"Shapechanger","You are a shapechanger, and are subject to effects or conditions that affect shapechangers.")
                       ,feat([ft("will",["racial",1])],"Mental Defense","You have a +1 racial bonus to Will")
                       ,feat([racePower["changeling1"]],"Changeling Disguise")
                       ,feat([racePower["changeling2"]],"Changeling Trick")],
          "Deva":[feat([ft(["history","religion","int","wis"],["racial",2])],"Racial Skills","+2 to history and religion checks")
                       ,feat([ft("origin","immortal")],"Origin")
                       ,feat([],"Astral Majesty","+1 bonus to all defenses against attacks made by bloodied creatures")
                       ,feat([],"Astral Resistance",["Necrotic and Radiant Resistance ",lambda x:x.statret("level")/2+5])
                       ,feat([racePower["deva"]],"Memory of a Thousand Lifetimes")],
          "Doppelganger":[feat([ft(["bluff","insight","int","cha"],["racial",2])],"Racial Skills","+2 to bluff and insight checks")
                       ,feat([ft("will",["racial",1])],"Mental Defense","+1 racial bonus to will defense")
                       ,feat([racePower["doppelganger"]],"Change Shape")],
          "Dragonborn":[feat([ft(["history","intimidate","str","cha"],["racial",2]),ft("intimidate",["racial",2])],"Racial Skills","+2 to history and intimidate checks")
                       ,feat([],"Dragonborn Fury","+1 racial bonus to attack rolls when bloodied")
                       ,feat([ft("surge",["racial",lambda x: x.mod("con")])], "Draconic Heritage","Add con mod to healing surge value")
                       ,feat([specMenus["dragonbornBreath"]],"Breath Weapon Element")],
          "Drow":[feat([ft(["intimidate","stealth","dex","cha"],["racial",2])],"Racial Skills","+2 to intimidate and stealth checks")
                       ,feat([ft("vision","darkvision")],"Vision")
                       ,feat([ft("origin","fae")],"Origin")
                       ,feat([],"Trance","Trance for 4 hours instead of sleeping for 6")
                       ,feat([racePower["drow1"],racePower["drow2"]],"Lolthtouched","Once per encounter, use either the Cloud of Darkness or Darkfire power")],
          "Dwarf"     :[feat([ft(["dungeoneering","endurance","wis","con"],["racial",2])],"Racial Skills","+2 to dungeoneering and endurance checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([], "Cast Iron Stomach","+5 racial bonus on saves vs. poison")
                       ,feat([], "Dwarven Resiliance","Use second wind as minor action instead of standard action")
                       ,feat([ft("speed",["",-1]),ft("speed", ["armor", 0]),ft("speed", ["encumberance", 0])],"Encumbered Speed","No speed penalty for amor or encumberance")
                       ,feat([ft("proficiency", ["warhammer","throwing hammer"])],"Dwarven Weapon Proficiency","Proficient with warhammer and throwing hammer")
                       ,feat([], "Stand your Ground","May move 1 less square when forced to move and save to avoid being knocked prone")],
          "Eladrin"   :[feat([ft(["arcana","history","dex","int"],["racial",2])],"Racial Skills","+2 to arcana and history checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([ft("skillpick",SkillPick(allskills.keys(),1, "Eladrin Skill"))],"Eladrin Education","Any one bonus skill")
                       ,feat([ft("feat", [weaponProf["longsword"]])],"Eladrin Weapon Proficiency", "Proficient with longsword")
                       ,feat([ft("will",["racial",1])],"Eladrin Will","+1 to will defense and +5 racial bonus on saves vs. charm")
                       ,feat([ft("origin","fae")],"Origin")
                       ,feat([],"Trance","Trance for 4 hours instead of sleeping for 6")
                       ,feat([racePower["eladrin"]],"Eladrin Power")],
          "Elf"       :[feat([ft(["nature","perception","dex","wis"],["racial",2]),ft("speed",["",1])],"Racial Skills","+2 on nature and perception checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([ft("proficiency", ["longbow","shortbow"])],"Elven Weapon Proficiency","Proficient with longbow and shortbow")
                       ,feat([ft("origin","fae")],"Origin")
                       ,feat([],"Group Awareness","+1 racial bonus on perception checks to all non-elven allies in 5 squares")
                       ,feat([],"Wild Step","Ignore difficult terrain when shifting")
                       ,feat([racePower["elf"]],"Elf Power")],
         "Githyanki":[feat([ft(["history","con","int","initiative"],["racial",2])],"Racial Bonuses","+2 to history checks")
                       ,feat([],"Danger Sense","+2 to initiative checks")
                       ,feat([ft("will",["racial",1])],"Githyanki Willpower","+1 to will defense and +2 racial bonus on saves vs. charm")
                       ,feat([racePower["githyanki"]],"Telekinetic Leap","")],
          "Githzerai":[feat([ft(["acrobatics","athletics","wis"],["racial",2])],"Racial Skills","+2 to acrobatics and athletics checks")
                       ,feat([statmenu(["dex","int"])],"Githzerai Stat Bonus")
                       ,feat([ft("initiative",["racial",2])],"Danger Sense","+2 to initiative checks")
                       ,feat([],"Defended Mind","+2 racial bonus to saving throws against effects that daze, dominate, or stun.")
                       ,feat([],"Shifting Fortunes","when you use your second wind, you can shift 3 squares as a free action.")
                       ,feat([racePower["githzerai"]],"Iron Mind","")],
          "Genasi":[feat([ft(["endurance","nature","str","int"],["racial",2])],"Racial Skills","+2 to endurance and nature checks")
                       ,feat([ft("origin","elemental")],"Origin")
                    ,feat([ft("featpick",FeatPick(0, "Elemental Manifestation",0,
                           [feat([ft("fort",["racial",1]),basePowers["Earthshock"]],"Earthsoul","+1 fortitude defense, +1 to saving throws, Earthshock power"),
                           feat([ft("ref",["racial",1]),basePowers["Firepulse"]],"Firesoul",["+1 reflex defense, resist ",lambda x:raising(5,10)(x)+x.statret("genasiresist")," fire, Firepulse power"]),
                           feat([ft("fort",["racial",1]),basePowers["Promise of Storm"]],"Stormsoul",["+1 fortitude defense, resist ",lambda x:raising(5,10)(x)+x.statret("genasiresist")," lighting, Promise of Storm power"]),
                           feat([basePowers["Swiftcurrent"]],"Watersoul","You can breathe under water.  +2 racial bonus to saves vs. ongoing damage, and Swiftcurrent power"),
                           feat([basePowers["Windwalker"]],"Windsoul",["Resist ",lambda x:raising(5,10)(x)+x.statret("genasiresist")," cold and Windwalker power"])
                           ]))],"featpick")],
          "Gnoll":[feat([ft(["intimidate","con","dex"],["racial",2]),ft("speed",["",1])],"Racial Skills","+2 to intimidate checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([],"Blood Fury",["+",raising(2,20)," bonus to damage rolls when bloodied"])
                       ,feat([racePower["gnoll"]],"Ferocious Charge","")],
          "Gnome":[feat([ft(["arcana","stealth","int","cha"],["racial",2]),ft("speed",["",-1])],"Racial Skills","+2 to arcana and stealth checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([ft("origin","fae")],"Origin")
                       ,feat([],"Reactive Stealth","If you have cover / concealment when you roll initative you can make a stealth check to avoid notice")
                       ,feat([],"Small","Cannot wield two-handed weapons, must hold versatile weapons in two hands")
                       ,feat([racePower["gnome"]],"Fade Away","")],
          "Goblin":[feat([ft(["stealth","thievery","dex","cha"],["racial",2])],"Racial Skills","+2 to stealth and thievery checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([ft("ref",["racial",1])],"Goblin Reflexes","+1 to reflex defense")
                       ,feat([racePower["goblin"]],"Goblin Tactics","")],
          "Goliath":[feat([ft(["athletics","nature","str","con"],["racial",2])],"Racial Skills","+2 to athletics and nature checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([ft("ref",["racial",1])],"Mountain's Tenacity","+1 to will defense")
                       ,feat([],"Powerful Athlete","When you make an Athletics check to jump or climb, roll twice and use either result")
                       ,feat([racePower["goliath"]],"Stone's Endurance","")],
          "Half-Elf"  :[feat([ft(["diplomacy","insight","con","cha"],["racial",2])],"Racial Skills","+2 on diplomacy and insight checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([ft("powerpick",PowerPick("dilettante",0, 31, "Half-elf Dilettante"))],"Dilettante","One at will power from different class as encounter power")
                       ,feat([ft("checkrace","elf"),ft("checkrace","human")],"Dual Heritage","Can take feats that have human or elf as prerequisite")
                       ,feat([],"Group Diplomacy","+1 racial bonus on diplomacy checks to all allies in 10 squares")],
          "Half-Orc"  :[feat([ft(["endurance","intimidate","str","dex"],["racial",2])],"Racial Skills","+2 on endurance and intimidate checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([],"Half-Orc Resilience",["The first time you are bloodied in an encounter, you gain ",raising(5,10)," temporary hit points"])
                       ,feat([],"Swift Charge","You gain a +2 bonus to speed when charging")
                       ,feat([racePower["half-orc"]],"Furious Assault")],
          "Halfling"  :[feat([ft(["acrobatics","thievery","dex","cha","oppAC"],["racial",2])],"Racial Skills","+2 on acrobatics and thievery checks")
                       ,feat([],"Bold","+5 racial bonus on saves vs. fear")
                       ,feat([ft("oppAc",["racial",2])],"Nimble Reaction","+2 AC vs. opportunity attacks")
                       ,feat([],"Small","Cannot wield two-handed weapons, must hold versatile weapons in two hands")
                       ,feat([racePower["halfling"]],"Halfling Power")
                       ,feat([ft("size",["",-1])],"Small Size")],
          "Hobgoblin":[feat([ft(["athletics","history","con","cha","initiative"],["racial",2])],"Racial Skills","+2 to athletics and history checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([],"Battle Ready","+2 to initiative checks")
                       ,feat([racePower["hobgoblin"]],"Hobgoblin Resilience","")],
          "Human"     :[feat([statmenu(["str","con","dex","int","wis","cha"],"+2 to ")],"Human Stat Bonus")
                       ,feat([ft("skillpick",SkillPick("classskills",1, "Human Bonus"))],"Bonus Skill", "Training in one additional class skill")
                       ,feat([ft("powerpick",PowerPick("at-will1",0, 31, "Human At-will"))], "Bonus At-Will Power", "Pick one extra at will power from your class")
                       ,feat([], "Bonus Feat", "One extra feat at first level")
                       ,feat([ft("featpick",FeatPick(1, "Human Bonus Feat"))], "featpick")
                       ,feat([ft(["will","fort","ref"],["racial",1])],"Human Defense Bonuses","+1 to fort, ref, and will defenses")],
          "Kalashtar":[feat([ft(["insight","wis","cha"],["racial",2])],"Racial Skills","+2 to insight checks")
                       ,feat([statmenu(allskills.keys(), "+2 to ")],"Kalashtar Skill Bonus")
                       ,feat([],"Telepathy","You can communicate telepathically with any creature within 5 squares of you that has a language.")
                       ,feat([],"Dual Mind","At the start of your turn, instead of the end, make a saving throw against each daze or dominate effect.")
                       ,feat([racePower["kalashtar"]],"Bastion of Mental Clarity","")],
          "Kobold":[feat([ft(["stealth","thievery","con","dex"],["racial",2])],"Racial Skills","+2 to stealth and thievery checks")
                       ,feat([],"Trap Sense","+2 to defenses against traps")
                       ,feat([racePower["kobold"]],"Shifty","")],
          "Minotaur":[feat([ft(["nature","perception","str"],["racial",2])],"Racial Skills","+2 to nature and perception checks")
                       ,feat([statmenu(["con","wis"],"+2 to ")],"Minotaur Stat Bonus")
                       ,feat([ft("surges",["",1])],"Vitality","You have one additional healing surge.")
                       ,feat([],"Ferocity","If you are reduced to 0 hit points you may make a melee attack as an immediate interrupt")
                       ,feat([],"Heedless Charge","+2 racial bonus to AC against opportunity attacks you provoke during a charge")
                       ,feat([racePower["minotaur"]],"Goring Charge","")],
          "Orc":[feat([ft(["str","con"], ["racial",2])],"Stat Bonus")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([],"Running Charge","When you charge, add 2 to your speed")
                       ,feat([racePower["orc"]],"Warrior's Surge","")],
          "Shadar-Kai":[feat([ft(["acrobatics","stealth","dex","int"],["racial",2]),ft("stealth",["racial",2])],"Racial Skills","+2 to acrobatics and stealth checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([ft("origin","shadow")],"Origin")
                       ,feat([ft("fort",["racial",1])],"Winterkin","+1 to fortitude defense")
                       ,feat([racePower["shadar-kai"]],"Shadow Jaunt","")],
          "Shardmind":[feat([ft(["arcana","endurance","int"],["racial",2])],"Racial Skills","+2 to arcana and endurance checks")
                       ,feat([statmenu(["wis","cha"], "+2 to ")],"Shardmind Stat Bonus")
                       ,feat([statmenu(allskills.keys(), "+2 to ")],"Shardmind Skill Bonus")
                       ,feat([],"Telepathy","You can communicate telepathically with any creature within 5 squares of you that has a language.")
                       ,feat([],"Crystalline Mind",["You have resist ",lambda x:raising(5,10)(x)+x.statret("crystalline mind resist")," psychic"])
                       ,feat([],"Living Construct","Do not eat, drink, breathe, sleep.  No Endurance checks to resist starvation, thirst, or suffocation.")
                       ,feat(["origin","immortal"],"Origin")
                       ,feat([racePower["shardmind"]],"Shard Swarm","")],         
          "Shifter, Longtooth":[feat([ft(["athletics","endurance","str","wis"],["racial",2])],"Racial Skills","+2 to athletics and endurance checks")
                       ,feat([ft("checkrace","shifter")])
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([racePower["shifter, longtooth"]],"Longtooth Shifting","")],
          "Shifter, Razorclaw":[feat([ft(["acrobatics","stealth","dex","wis"],["racial",2])],"Racial Skills","+2 to acrobatics and stealth checks")
                       ,feat([ft("checkrace","shifter")])
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([racePower["shifter, razorclaw"]],"Razorclaw Shifting","")],
          "Tiefling"  :[feat([ft(["bluff","stealth","int","cha"],["racial",2])],"Racial Skill","+2 bonus on bluff and stealth checks")
                       ,feat([ft("vision","low-light")],"Vision")
                       ,feat([],"Bloodhunt","+1 racial bonus on attacks vs. bloodied foes")
                       ,feat([],"Fire Resistance",["Fire Resistance ",lambda x:x.statret("level")/2+5])
                       ,feat([racePower["tiefling"]],"Tiefling Power")],        
          "Warforged"  :[feat([ft(["endurance","intimidate","str","con"],["racial",2])],"Racial Skills","+2 to endurance and intimidate checks")
                       ,feat([],"Living Construct","Do not eat, drink, breathe, sleep.  No Endurance checks to resist starvation, thirst, or suffocation.")
                       ,feat([],"Unsleeping Watcher","You enter a state of inactivity for 4 hours for an extended rest.  You are fully aware of surroundings during a rest.")
                       ,feat([],"Warforged Resilience","+2 racial bonus to saving throws against ongoing damage.  May take better of your die roll or 10 for death saving throw.")
                       ,feat([racePower["warforged"]],"Warforged Resolve","")],
          "Wilden"  :[feat([ft(["nature","stealth","wis"],["racial",2])],"Racial Skill","+2 bonus on nature and stealth checks")
                       ,feat([statmenu(["con","dex"],"+2 to ")],"Wilden Stat Bonus")
                       ,feat([ft("origin","fae")],"Origin")
                       ,feat([statmenu(["fort","ref","will"],"+1 to ","",1)],"Hardy Form")
                       ,feat([],"Nature's Aspect","Choose an aspect of nature after each rest.  Gain access to that racial encounter power for the day.")
                       ,feat([racePower["wilden1"]],"Voyage of the Ancients")
                       ,feat([racePower["wilden2"]],"Wrath of the Destroyer")
                       ,feat([racePower["wilden3"]],"Pursuit of the Hunter")],
}