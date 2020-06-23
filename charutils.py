import os
from types import *
from Tkinter import *

MAXLEVEL=30
BASESTAT=10
MAXPOINTS=20
SAVEDIR="save"+os.sep
SELECTCURSOR="hand2"
WEALTHTYPES=["Astral Diamond","Platinum","Gold","Silver","Copper"]
WEALTHINFO={"Astral Diamond":["ad",0.002,2],
		    "Platinum":["pp",0.02,1],
		    "Gold":["gp",0.02,None],
		    "Silver":["sp",0.02,-1],
		    "Copper":["cp",0.02,-2]}
#rDict={"flat":FLAT,"sunken":SUNKEN,"raised":RAISED,"goove":GROOVE,"ridge":RIDGE}
#RELIEF=rDict[RELIEF]
NAME="Bob"
RELIEF=FLAT

STRMOD=lambda x:x.mod("str")
DEXMOD=lambda x:x.mod("dex")
CONMOD=lambda x:x.mod("con")
CHAMOD=lambda x:x.mod("cha")
INTMOD=lambda x:x.mod("int")
WISMOD=lambda x:x.mod("wis")
LEVEL=lambda x:x.statret("level")

CHECK=lambda stat, val:lambda x:x.check(stat, val)
NOTCHECK=lambda stat, val: lambda x:not(x.check(stat, val))
repeatableFeats=["skill focus","skill training","weapon focus","weapon proficiency","linguist","versatile expertise","weapon expertise","implement expertise","superior implement training","hybrid talent"]
allskills={"acrobatics":"dex","arcana":"int","athletics":"str","bluff":"cha","diplomacy":"cha","dungeoneering":"wis","endurance":"con","heal":"wis","history":"int","insight":"wis","intimidate":"cha","nature":"wis","perception":"wis","religion":"int","stealth":"dex","streetwise":"cha","thievery":"dex"}
classes=[]

BOOKS=["Player's Handbook","Player's Handbook 2","Player's Handbook 3","Adventurer's Vault","Adventurer's Vault II","Arcane Power","Divine Power","Eberron Player's Guide","Forgotten Realms Player's Guide","Martial Power","Martial Power II"]

if "Player's Handbook" in BOOKS:
	classes+=["cleric","fighter","rogue","ranger","paladin","warlock","warlord","wizard"]
if "Player's Handbook 2" in BOOKS:
	classes+=["avenger","barbarian","bard","druid","invoker","shaman","sorcerer","warden"]
if "Player's Handbook 3" in BOOKS:
	classes+=["ardent","battlemind","monk","psion","runepriest","seeker"]
if "Forgotten Realms Player's Guide" in BOOKS:
	classes+=["swordmage"]
if "Eberron Player's Guide" in BOOKS:
	classes+=["artificer"]
races=["bugbear","changeling","deva","doppelganger","drow","dragonborn","drow","dwarf","eladrin","elf","genasi","githyanki","githzerai","gnoll","gnome","goblin","goliath","half-elf","half-orc","halfling","hobgoblin","human","kalashtar","kobold","minotaur","orc","shardmind","shadar-kai","shifter, longtooth","shifter, razorclaw","tiefling","warforged","wilden"]
elements=["acid","cold","fire","force","lightning","necrotic","poison","psychic","radiant","thunder"]
deities=[]
if "Player's Handbook" in BOOKS: 
	deities+=["Asmodeus","Avandra","Bahamut","Bane","Corellon","Erathis","Gruumsh","Ioun","Kord","Lolth","Melora","Moradin","Pelor","Raven Queen","Sehanine","Tiamat","Torog","Vecna","Zehir"]
if "Forgotten Realms Player's Guide" in BOOKS:
	for x in ["Akadi","Abbathor","Amaunator","Angharradh","Arvoreen","Asmodeus","Auril","Baalzebul","Baervan Wildwanderer","Bahaumut","Bahgtru","Bane","Baravar Cloakshadow","Bazim-Gorag","Bel","Belial","Berronar Truesilver","Beshaba","Brandobaris","Callarduran Smoothhands","Chauntea","Clangeddin Silverbeard","Corellon","Cyric","Cyrrollalee","Deep Sashelas","Dispater","Dugmaren Brightmantle","Erevan Ilesere","Fenmarel Mestarine","Fzoul Chembryl","Garagos","Garl Glittergold","Ghaunadaur","Glassya","Gond","Grumbar","Gruumsh","Hoar","Hruggek","Ilmater","Istishia","Jergal","Kelemvor","Kossuth","Labelas Enoreth","Levistus","Llira","Lolth","Lovitar","Luthic","Maglubiyet","Malar","Mammon","Marthammor Duin","Mephistopheles","Mielikki","Milil","Moradin","Obould","Oghma","Red Knight","Selune","Shar","Sharess","Shargaas","Sheela Peryroyl","Shevarash","Shialla","Siamorphe","Silvanus","Solonor Thelandira","Sseth","Sune","Talona","Tempus","Thard Harr","Tiamat","Tymora","Torm","Umberlee","Uthgar","Valkur","Vaprak","Vergadain","Waukeen","Zehir"]:
		if x not in deities: deities.append(x)
deities=sorted(deities)
deities+=["Pantheon","Other"]
implements=["orb","wand","dagger","staff","rod","holy symbol","totem","holy avenger","pact blade","ki focus","heavy blade","light blade"]
martialclasses=["fighter","ranger","rogue","warlord"]
arcaneclasses=["artificer","bard","sorcerer","swordmage","warlock","wizard"]
divineclasses=["avenger","cleric","invoker","paladin","runepriest"]
primalclasses=["barbarian","druid","seeker","shaman"]
psionicclasses=["ardent","battlemind","monk","psion"]
psionicAugmentation=["ardent","battlemind","psion"]
powersources={"martial":martialclasses,
		    "arcane":arcaneclasses,
		    "divine":divineclasses,
		    "primal":primalclasses}
languages=["common","deep speech","draconic","dwarven","elven","giant","goblin","primordial","supernal","abyssal"]
classimplements={}
for x in classes: classimplements[x]=[]
classimplements["artificer"]=["rod","staff","wand"]
classimplements["avenger"]=["holy symbol"]
classimplements["bard"]=["wand"]
classimplements["cleric"]=["holy symbol"]
classimplements["druid"]=["staff","totem"]
classimplements["invoker"]=["rod","staff"]
classimplements["monk"]=["ki focus","weaponimplement"]
classimplements["paladin"]=["holy symbol","holy avenger"]
classimplements["psion"]=["orb","staff"]
classimplements["swordmage"]=["heavy blade","light blade"]
classimplements["wizard"]=["orb","staff","tome","wand"]
classimplements["warlock"]=["wand","rod","pact blade"]
classimplements["shaman"]=["totem"]
classimplements["sorcerer"]=["dagger","staff"]
warlockPacts={"dark pact":"Spiteful Glamor","fey pact":"Eyebite","infernal pact":"Hellish Rebuke","star pact":"Dire Radiance","vestige pact":"Eyes of the Vestige"}
itemslots={"primary hand":0,"off hand":1,"armor":2,"arm":3,"feet":4,"hands":5,"head":6,"neck":7,"left ring":8,"right ring":9,"waist":10,"holy symbol":11,"ki focus":12,"beast":13}

def MOD(stat, z=None):
	translate={"str":"Str mod","con":"Con mod","dex":"Dex mod","int":"Int mod","wis":"Wis mod","cha":"Cha mod","level":"Level","half level":"1/2 level","speed":"Speed","surge":"Healing Surge"}
	orft=[" ("]
	mux=1
	if stat.startswith("2"):
		orft[0]+="2x "
		stat=stat[1:]
		mux=2
	orft[0]+=translate[stat]
	if z=="min1":
		mod=lambda x:max(1, x.mod(stat)*mux)
	elif z==None:
		if stat in ["level","speed","surge"]:mod=lambda x:x.statret(stat)
		elif stat=="half level":mod=lambda x:x.statret("level")/2
		else: mod=lambda x:max(0,x.mod(stat)*mux)
	elif isinstance(z,int):
		if stat in ["level","speed","surge"]:mod=lambda x:x.statret(stat)+z
		elif stat=="half level":mod=lambda x:x.statret("level")/2+z
		else: mod=lambda x:x.mod(stat)*mux+z
		orft.append(" + "+str(z))
	elif isinstance(z,str):
		if stat in ["level","speed","surge"]:mod=lambda x:x.statret(stat)+x.mod(z)
		elif stat=="half level":mod=lambda x:x.statret("level")/2+x.mod(z)
		elif z in ["level","speed","surge"]: mod=lambda x:x.mod(stat)+x.statret(z)
		elif z=="half level": mod=lambda x:x.mod(stat)+x.statret("level")/2
		else: mod=lambda x:max(0,x.mod(stat)*mux+x.mod(z))
		orft.append(" + "+translate[z])
	elif callable(z):
		if stat in ["level","speed","surge"]:mod=lambda x:x.statret(stat)+z(x)
		elif stat=="half level":mod=lambda x:x.statret("level")/2+z(x)
		else: mod=lambda x:max(0,x.mod(stat)*mux+z(x))
		orft+=[" + ",z]
	orft.append(")")
	return lambda x:[mod, orfeat("",orft,["showmods",1])]		

def sumlist(thelist):
	if isinstance(thelist[0],list):ret=[]
	if isinstance(thelist[0],str):ret=""
	if isinstance(thelist[0],int):ret=0
	for x in thelist:
		ret+=x
	return ret

class inputClass:
	def __init__(self, csheet, txt="", row=19, col=0):
		csheet.update()
		self.value=None
                self.master=csheet
		self.modalPane=Frame(self.master.sub)

		self.modalPane.grid(row=row, column=col)

		if txt<>"": Label(self.modalPane, text=txt).pack()
		self.entry=Entry(self.modalPane)
		self.entry.pack()
		self.entry.bind("<Return>",self._choose)

	def _choose(self, event=None):
		self.value=self.entry.get()
		self.modalPane.destroy()
		self.master.destroySub()

	def returnValue(self):
		self.modalPane.wait_window(self.modalPane)
		return self.value
#Res is the most important function here, and many other things are based on the idea of res.
#Res takes in a value, which can be string, int, list, or function, and a character.
#The end result is what that value would be for a given character.
#For example, if a feat gives "Add your charisma mod to how much you heal",
#I would use lambda x: x.statmod("cha") in the feat list.  Res would take in the lambda, 
#and return the characters stat mod.  I run pretty much everything through res before printing it out.

#All functions that are used in res take in one input (the character), and return one output
#If a function in charutils has a def(modit), it is creating a function that will later be passed through res.

#val=the value / function
#character=the character used in the function if val is a function	

def res(val, character, listAsText=True):
	if callable(val): x=res(val(character), character, listAsText)
	else: x=val
	if (isinstance(x, list)) or (isinstance(x,tuple)):
		retlist=[res(z, character) for z in x]
		ret="" 
		if listAsText:
			for z in retlist: ret+=str(z)
		else: ret=retlist
	else: ret=x
	return ret

#Plus creates a function that sticks a + sign in front of positive numbers.
#Going back to the example at the top, res(plus(lambda x: x.statmod("cha"))) could return
#'+5', '-1', or '', depending on the character's cha.
def plus(func, printzero=0):
	def modit(character):
		z=res(func, character)
		if z<0: return str(z)
		if (z==0) and (printzero==0): return ""
		if z+printzero>0: return "+"+str(z)
	return modit

#Checks for given feature, returns vals[0] if false, vals[1]
#vals=list[value if False, value if True]
#feature=feature to check for
def orfeat(val1, val2, feature):
	def modit(character):
		check=False
		if isinstance(feature, list):
			if len(feature)>2: check=character.check(feature[0], feature[1], feature[2])
			else: check=character.check(feature[0], feature[1]) 
		if feature in races: 
			if character.check("checkrace",feature): check=True
		if feature in allskills.keys():
			if character.check("training",feature): check=True
		elif character.check("feature",feature): check=True
		if check: return val2
		else: return val1
	return modit

#Very useful.  Start at value, raise by 1 for every num levels.
#Used in spell damage, some weapon damage, many feats, etc. etc.
#val: base number/multiplier
#num: how many levels before val goes up
def raising(val, num):
	def ret(character):
		x=0
		for z in range(1,30,num):
			if character.check("level",z): x+=val
		return x
	return ret

#As above, but adds 1 for each number in list that the character level is equal to above.
#For example, a level 15 character would return val+val*5 for nums=[1,1,2,2,15,25,30]
#val: base number/multiplier
#nums: list of levels that the number goes up
def raiselist(val, nums):
	def ret(character):
		x=val
		for z in nums:
			if character.check("level",z): x+=val
		return x
	return ret

#it's the 2[w] thing you see all over the PHB.  If you don't know what that means, you are reading the wrong program's code.
def W(mux, weapon, character):
	sendkeys=[weapon.name+"name"]+list(weapon.keys)+list(weapon.group)
	die1=weapon.dmg[0]
	die2=weapon.dmg[1]
	for x in xrange(character.modmux(sendkeys+[""], "weaponsize")):
		die1,die2 = dieSizeUp(die1, die2, ("two-handed" in weapon.keys)+1)
	return [mux*die1,die2]

def weaponBoost(boosts, weapon, character):
	ret=0
	for boost in boosts:
		isRightWeaponGroup=FALSE
		if isinstance(boost[0], str):
			if boost[0] in weapon.keys: isRightWeaponGroup=True
		else:
			if boost[0][0]=="both":
				if "equipped" not in weapon.keys or not character.inventory.dualwield():
					for akey in boost[0][1:]:
						if akey in weapon.keys: isRightWeaponGroup=True
				else:
					test1=False
					test2=False
					for akey in boost[0][1:]:
						if akey in character.inventory.equipped[0].desc.group: test1=True
						if akey in character.inventory.equipped[1].desc.group: test2=True
					if test1 and test2: isRightWeaponGroup=True
			else:
				for akey in boost[0]:
					if akey in weapon.keys: isRightWeaponGroup=True
		if isRightWeaponGroup:
			ret+=res(boost[1], character)
	return ret

#Returns the value for an attack roll that does use a weapon
#stat=list[stats added to attack roll]
#vs=defense attack goes against
#damage=function that determines damage done
#keywords=keywords of the attack ("radiant", for example)
#bonus=# added to attack bonus
#legalgroups=weapon groups allowed for this attack

def attack(stats, vs, damage, keywords=None, legalgroups=[]):
	def modit(character):
		def checkLegalGroups(ingroups, keys):
			groups=list(ingroups)
			for x in legalgroups: groups+=character.featurestr(x+"legal")
			if groups==[]: return True
			illegal=[]
			for x in groups:
				if x[0]=="!": illegal.append(x[1:])
			for x in illegal: groups.remove("!"+x)
			if sum([x in groups for x in keys])==0: return False
			if illegal<>[]:
				if sum([x in illegal for x in keys])>0: return False
			return True
		if keywords==None:
			bonus=character.statret("level")/2
			for stat in stats: bonus+=res(stat, character)
			if damage!=None: dmg=damage(character)+["noweapon"]
			else: dmg=[None, None, None,"noweapon"]
			return [[bonus,vs]+dmg], 0
		else:
			z=LEVEL(character)/2
			weaponboosts=[]
			for stat in stats:
				if isinstance(stat, list): weaponboosts.append(stat)					
				else: z+=res(stat, character)
			ret=[]
			didit=[]
			for weapon in character.statret("weapons"):
				weaponkeys=[j for j in weapon.desc.charkey(character)]
				if (sum([key in weaponkeys for key in keywords])==len(keywords)) and  checkLegalGroups(legalgroups, weapon.desc.group+weaponkeys+[weapon.desc.name+"name"]) and repr(weaponkeys)+weapon.name() not in didit:
					didit.append(repr(weaponkeys)+weapon.name())
					if damage!=None: 
						q=damage(character, weapon.desc)
					else: 
						q=[None, None, None]
					prof=0
					if weapon.desc.name.lower() in character.statret("proficiency"): prof=weapon.desc.prof
					boost=weaponBoost(weaponboosts, weapon.desc, character)
					ret+=[[z+prof+boost,vs]+q+[weapon]]
			return ret, "melee" not in keywords
	return modit

#Returns damage
#die=weapon damage multiplyer if in, dice damage if list ( [1,6] = 1d6, 1=1[w]
#stats=list[stats added to damage]

def damage(die, stats, bdie=[]):
	def modit(character, weapon=""):
		bonusdie=list(bdie)
		if isinstance(die, list):
			mux=res(die[0],character)
			dice=res(die[1],character)
			if bonusdie!=[]:
				bonusdie=res(bonusdie,character)
				if bonusdie[0]!=0:
					mux=[mux,bonusdie[0]]
					dice=[dice, bonusdie[0]]
			bonus=0
			if mux!=0:
				for stat in stats: bonus+=res(stat, character)
			return [mux,dice,bonus]
		else:
			mux=res(die, character)
			bonus=0
			weaponboosts=[]
			for stat in stats: 
				if isinstance(stat, list): weaponboosts.append(stat)
				else: bonus+=res(stat, character)
			if weapon!="":
				boost=weaponBoost(weaponboosts, weapon, character)
				q=W(mux, weapon, character)+[bonus+boost]
			else: q=[0,0,bonus]
			if bonusdie!=[]:
				bonusdie=res(bonusdie,character)
				if bonusdie[0]!="0":
					q[0]=[q[0],bonusdie[0]]
					q[1]=[q[1],bonusdie[1]]
			return q
	return modit

def dieSizeUp(numdice, die, hands):
	onehanded={"1d4":[1,6],"1d6":[1,8],"1d8":[1,10],"1d10":[1,12],"1d12":[2,6],"2d6":[2,8],"2d8":[2,10]}
	twohanded={"1d8":[2,4],"2d4":[1,10],"1d10":[1,12],"1d12":[2,6],"2d6":[2,8],"2d8":[2,10]}
	ret=[numdice, die]
	stringdie=str(numdice)+"d"+str(die)
	if hands==1 and stringdie in onehanded: ret=list(onehanded[stringdie])
	if hands==2 and stringdie in twohanded: ret=list(twohanded[stringdie])
	return ret

def jackoftrades(skill, notit=True, Num=2):
    if notit: ret=lambda x: Num*(not(x.check("training",skill)))
    else: ret=lambda x: Num*(x.check("training",skill))
    return ret