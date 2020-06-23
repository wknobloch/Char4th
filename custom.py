
from charutils import *
#Custom file:
#You can modify the information in this file to code additional powers, feats, and other modifications to your campaign.
#This file will not be modified when the program is updated.  To reset defaults, delete this file.

#Default Variables
BASESTAT=10
MAXLEVEL=30
MAXPOINTS=20
SELECTCURSOR="hand2"
NAME="Bob"

#RELIEF: Options are FLAT, SUNKEN, RAISED, GROOVE, or RIDGE
RELIEF=FLAT


#WEALTHINFO:  "Money Name":["abbreviation", weight, displaydrop]
#displaydrop: If something has a positive display number, the printout will not display this money source if the character has none
#of this wealth.  If something has a negative display number, it will be removed from the printout if the character has none of this
#wealth and has some wealth of a positive display.  This is to cater the output to higher or lower level characters.  If you want
#a value to always display, choose "none" for displaydrop.

WEALTHTYPES=["Astral Diamond","Platinum","Gold","Silver","Copper"]
WEALTHINFO={"Astral Diamond":  [  "ad",0.002,2],
            "Platinum":["pp",0.02,1],
            "Gold":    ["gp",0.02,None],
            "Silver":  ["sp",0.02,-1],
            "Copper":  ["cp",0.02,-2]}

#DM Options

#Races
#races.remove("bugbear")
#Classes
#classes.remove("cleric")

#languages=["common","deep speech","draconic","dwarven","elven","giant","goblin","primordial","supernal","abyssal"]

#To modify deities:
#PHB Deities
#deities=["Asmodeus","Avandra","Bahamut","Bane","Corellon","Erathis","Gruumsh","Ioun","Kord","Lolth","Melora","Moradin","Pelor","Raven Queen","Sehanine","Tiamat","Torog","Vecna","Zehir","Pantheon","Other"]
#Forgotten Realms Deities
#deities=["Akadi","Abbathor","Amaunator","Angharradh","Arvoreen","Asmodeus","Auril","Baalzebul","Baervan Wildwanderer","Bahaumut","Bahgtru","Bane","Baravar Cloakshadow","Bazim-Gorag","Bel","Belial","Berronar Truesilver","Beshaba","Brandobaris","Callarduran Smoothhands","Chauntea","Clangeddin Silverbeard","Corellon","Cyric","Cyrrollalee","Deep Sashelas","Dispater","Dugmaren Brightmantle","Erevan Ilesere","Fenmarel Mestarine","Fzoul Chembryl","Garagos","Garl Glittergold","Ghaunadaur","Glassya","Gond","Grumbar","Gruumsh","Hoar","Hruggek","Ilmater","Istishia","Jergal","Kelemvor","Kossuth","Labelas Enoreth","Levistus","Llira","Lolth","Lovitar","Luthic","Maglubiyet","Malar","Mammon","Marthammor Duin","Mephistopheles","Mielikki","Milil","Moradin","Obould","Oghma","Red Knight","Selune","Shar","Sharess","Shargaas","Sheela Peryroyl","Shevarash","Shialla","Siamorphe","Silvanus","Solonor Thelandira","Sseth","Sune","Talona","Tempus","Thard Harr","Tiamat","Tymora","Torm","Umberlee","Uthgar","Valkur","Vaprak","Vergadain","Waukeen","Zehir"]
#(Default option is all deities)


#To add implements to a class:
#implements.append("ritual knife")
#classimplements["warlock"].append("ritual knife")
#(You also must add the implement to the equipment lists, below)

from powers4th import *

BONUSFEAT=[
feat([ft("featpick",FeatPick(0,"Background Feat",0,
    [feat([ft(zzz,("background",2))],zzz.capitalize()+" Background","+2 bonus to "+zzz+" checks") for zzz in allskills.keys()]
    +[feat([ft("skillpick",SkillPick(allskills.keys(),1, "Background Skill Training"))],"Background Skill Training","Any one bonus trained skill",lambda x: sum([q in x.statret("training") for q in allskills.keys()])<len(allskills))
    ]))],"featpick")
#feat([ft("arcana",("",4))],"Magic Savvy Campaign","+4 bonus to Arcana checks"),
#feat([ft(["ac","fort","ref","will"],("",-10))],"Deadly Campaign","-10 to all defenses")
]

#powerList["wizardencounter1"]["slaying bolt of slaying"]=Power(
#     "Slaying Bolt of Slaying",["arcane","implement","fire"],"encounter","standard",
#          [Target("one creature",("ranged",10)),Atk([INTMOD],"fortitude", damage([5,6],[INTMOD])),
#          Hit("If the target is of natural origin, it is slain instantly."),
#          Miss("You die."),
#          Effect("Lose 2 healing surges.  If you do not have two healing surges left to lose, instead lose hit points equal to your bloodied value.")
#          ],"wizard","attack",1)

from libraries import *
allFeatDict["Dragon Magazine"]=addFeats([
    feat([],"Bolstering Breath","Dragon breath only targets enemies.  Allies in burst gain +1 on attacks until end of your next turn.",lambda x:x.check("checkrace","dragonborn") and x.check("power","dragon breath"))
    ])
for z in allFeatDict["Dragon Magazine"].keys():
    allFeatList[z]=allFeatDict["Dragon Magazine"][z]
#raceList["Halfling"].append(feat([ft("nature",["racial",2]),ft("acrobatics",["",-2])],"Adjusted Racial Boosts","Halfings are more skilled in nature, but less skilled in acrobatics, in this campaign."))

#EquipmentLists["Weapons"]["Superior Melee"]["gouge"]=Weapon("gouge",["superior","melee","two-handed"],2,(2,6),12,["axe","spear"])
#EquipmentLists["Implements"]["ritual knife"]=Item("ritual knife",["1hand"],[],[feat([ft("ritual knifeimplement",["enhancement",0])],"magic")],2)
#EquipmentLists["Misc"]["crown"]=Item("crown",["head"],[],[],2)

#propertyList["slaying"]=Property("slaying #",[5,"melee"],[feat([],"Slaying Weapon","Slays the target instantly")])

from class4th import *

#classList["Ardent"].hp=14
#classList["Ardent"].skillList.append("Acrobatics")
          
