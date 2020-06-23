from __future__ import with_statement
from Tkinter import *
import httplib
import os
import sys
import time

update=True

version="08/20/10"
filelist=["char4th.pyw","charutils.py","class4th.py","classes.py","core4th.py","csheetframe.py","libraries.py","powers4th.py","scrolled.py","paragons.py"]

class MyDialog:
    def __init__(self):
        self.core=Tk()
        self.top = Frame(self.core)
        self.top.grid()
        self.core.title("Update available")

        self.theLabel=Label(self.top, text="A new update is available.  Updating will automatically exit the program.\nDo you wish to update now?")
        self.theLabel.grid(row=0,column=0,columnspan=2)
        self.b1=Button(self.top, text="Yes", command=self.ok)
        self.b1.grid(row=1,column=0,sticky="e")
        self.b2=Button(self.top, text="No",command=self.cancel)
        self.b2.grid(row=1,column=1,sticky="w")


    def ok(self):
        self.top.destroy()
        self.top=Frame(self.core)
        self.top.grid()
        self.theLabel=Label(self.top)
        self.theLabel.grid()
        self.core.title("Updating...")
        for x in filelist:
            self.core.title("Downloading: "+x)
            tries=0
            while tries<5:
                try:
                    success=True
                    conn.request("GET", "/"+x)
                    r1=conn.getresponse()
                except:
                    
                    tries+=1
                    success=False
                    self.core.title("Timeout #"+str(tries)+"  Retry: "+x)
                if success: tries=5
            if not(success):
                self.theLabel.config(text="Timeout\nUpdate failed")
                Button(self.top, text="Ok", command=self.top.destroy).grid(row=1,column=0, sticky="we")
                self.top.wait_window(self.top)
                sys.exit()
            with open(x, "w") as f:
                f.write(r1.read())
        print "update complete"
        self.core.title("Update complete")
        self.theLabel.config(text="Update successfully completed\nTo view changes made in this version, please visit char4th.game-host.org.\nPlease submit any bugs, ideas, or feature requests to char4th@gmail.com")
        self.theLabel.grid(row=0, column=0, columnspan=2)
        self.b1=Button(self.top, text="Ok", command=self.core.destroy)
        self.b1.grid(row=1, column=0, columnspan=2)
        self.top.wait_window(self.top)
        sys.exit()
      
    def cancel(self):
        self.core.destroy()

connection=True

try:
    conn = httplib.HTTPConnection("char4th.game-host.org",timeout=2)
    conn.request("GET", "/char4th.pyw")
    r1=conn.getresponse()
except:
    connection=False
    update=False
if connection: 
    update=not("version=\""+version in r1.read())
    for x in filelist:
        if x not in os.listdir('.'): update=True
    if update:
        g=MyDialog()
        g.core.wait_window(g.core)
        update=False

if not(os.path.isdir("save")):
    os.mkdir("save")
if "custom.py" not in os.listdir('.'):
    with open("custom.py", "w") as f:
          f.write("""
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

BONUSFEAT=[
#feat([ft("featpick",FeatPick(0,"DM Option Bonus Feat"))],"featpick"),
#feat([ft("arcana",("",4))],"Magic Savvy Campaign","+4 bonus to Arcana checks"),
#feat([ft(["ac","fort","ref","will"],("",-10))],"Deadly Campaign","-10 to all defenses")
]

from powers4th import *

#powerList["wizardencounter1"]["slaying bolt of slaying"]=Power(
#     "Slaying Bolt of Slaying",["arcane","implement","fire"],"encounter","standard",
#          [Target("one creature",("ranged",10)),Atk([INTMOD],"fortitude", damage([5,6],[INTMOD])),
#          Hit("If the target is of natural origin, it is slain instantly."),
#          Miss("You die."),
#          Effect("Lose 2 healing surges.  If you do not have two healing surges left to lose, instead lose hit points equal to your bloodied value.")
#          ],"wizard","attack",1)

from libraries import *

#raceList["Halfling"].append(feat([ft("nature",["racial",2]),ft("acrobatics",["",-2])],"Adjusted Racial Boosts","Halfings are more skilled in nature, but less skilled in acrobatics, in this campaign."))

#EquipmentLists["Implements"]["ritual knife"]=Item("ritual knife",["1hand"],[],[feat([ft("ritual knifeimplement",["enhancement",0])],"magic")],2)
#EquipmentLists["Misc"]["crown"]=Item("crown",["head"],[],[],2)

#propertyList["slaying"]=Property("slaying #",[5,"melee"],[feat([],"Slaying Weapon","Slays the target instantly")])

from class4th import *

#classList["Ardent"].hp=14
#classList["Ardent"].skillList.append("Acrobatics")
          """)

from core4th import *

if not(update):
    c=Core()
    c.frame.master.master.title("4E Character Creator update "+version)

    c.frame.master.wait_window(c.frame.master)

sys.exit(0)