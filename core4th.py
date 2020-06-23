from __future__ import with_statement
from custom import *
from csheetframe import *


class Core:
	def __init__(self, name=NAME,load=None, framestyle="tkframe"):
		
		self.name=name
		self.stats=[BASESTAT]*6
		self.points=MAXPOINTS
		self.level=1

		self.race=""
		self.charclass=""
		self.ftrs=[LIGHTARMOR]

		self.inventory=Inventory()
		self.showmods=None
		self.fastlookup={}
		self.quicklook={}
		self.basefeats()
		self.wealth=[0]*len(WEALTHTYPES)
		guyframe=None
		if framestyle=="tkframe":
			guyframe=CsheetFrame(Tk(), self)
		self.frame=guyframe
		if load!=None:
			self.frame.load(load)
		

	def basefeats(self):
		for x in [1,2,4,6,8,10,11,12,14,16,18,20,21,22,24,26,28,30]:
			self.addFeat(feat([ft("featpick",FeatPick(x, "Level "+str(x)+" feat"))],"featpick"))
		for x in BONUSFEAT:
			self.addFeat(x)
		attackFt = lambda z: ft(["and","implementattack", z+"attack"],["magic", lambda x:x.check("checkclass",z)*max([x.statret(q+"implement") for q in classimplements[z]]+[0])])
		damageFt = lambda z: ft(["and","implementdamage", z+"damage"],["magic", lambda x:x.check("checkclass",z)*max([x.statret(q+"implement") for q in classimplements[z]]+[0])])

		self.addFeat(feat([attackFt(z) for z in classimplements.keys()]+[damageFt(z) for z in classimplements.keys()],"implements"))

	def reset(self):
		self.name=NAME
		self.stats=[BASESTAT]*6
		self.points=MAXPOINTS
		self.level=1
		self.remRace()
		self.remClass()
		self.ftrs=[LIGHTARMOR]
		self.inventory=Inventory()
		self.basefeats()
		self.fastlookup={}
		self.quicklook={}

	def features(self):
		featlist=[]
		for a in self.ftrs:
			if a.levelReq()<=self.level:
				featlist.append(a)
		for feature in featlist:
			for what in feature.what():
				if what.when=="feat":
					if feature.name() in ["paragon","epic","delayfeat"]:
						for g in what.resolve:
							if g.preReqs(self):
								featlist+=[g]
					else:
						featlist+=[g for g in what.resolve]
				if what.when =="skillpick":
					if what.resolve.chosenFeature().what()!=[]:
						featlist.append(what.resolve.chosenFeature())
				if what.when=="languagepick":
					if what.resolve.chosenFeature().what()!=[]:
						featlist.append(what.resolve.chosenfeature())
				if what.when=="powerpick":
					if what.resolve.chosenFeature().what()!=[] and self.check("level",what.resolve.levelReq) and self.statret("level")<what.resolve.maxLevel:
						featlist.append(what.resolve.chosenFeature())
					
		if self.inventory.feats()!=[]: return featlist+self.inventory.feats()
		else: return featlist

	def powers(self):
		powerlist=[x for x in BASEATTACK]
		if "power" in self.quicklook.keys():
			for x in self.quicklook["power"]:
				powerlist+=x
		return powerlist
	
	def findPowers(self, keys):
		powerlist=self.powers()
		for x in keys:
			removelist=[]
			for power in powerlist:
				if (x not in power.keys) and ((x in classes and power.powerclass != x) or (x in powersources and power.powerclass not in powersources[x]) or (x in ["at-will","encounter","daily"] and power.often!=x)): removelist.append(power)
			for power in removelist:
				powerlist.remove(power)
		return powerlist

###############The Output Stuff##################
	def addFrame(self, cframe):
		self.frame=cframe
		if self.frame.char==None: self.frame.addChar(self)

	def menu(self, title, elements, refresh=True):
                ret=self.frame.menu(title, elements, refresh)
                return ret

        def getinput(self, text, row=19, col=0):
                return self.frame.getinput(text, row, col).returnValue()

	def update(self):
		self.frame.update()

	def wrapup(self):
		self.frame.wrapup()


################Core Character Stuff#############
	def pointbuy(self, stat):
		cost=1
		if(self.statret(stat)>12):cost+=1
		if(self.statret(stat)>15):cost+=1
		if(self.statret(stat)>16):cost+=1
		if(self.statret(stat)>17):cost+=2000
		if cost<=self.points:
			self.points=self.points-cost
			self.statmod(stat, 1)
	
	def remRace(self):
		if self.race<>"":
			for x in raceList[self.race.title()]:
				self.remFeat(x.named)
			self.race=""

	def attachRace(self, race):
		self.remRace()
		if race<>"":
			self.race=race.title()
			for x in raceList[race.title()]: self.addFeat(x)
	
	def remClass(self):
		if self.charclass!="":
			for x in classList[self.charclass.title()].features:
				self.remFeat(x.named)
			self.remClassProficiencies()
			self.remClassPowers()
		self.fastlookup={}

	def miniAttach(self, Class):
		self.remClass()
		if Class<>"":
			self.charclass=Class.title()
			z=classList[Class.title()]
			for x in z.features: self.addFeat(x)
			self.classProficiencies()
			self.setQuicklook()
			if self.check("feature","psionic augmentation"):
				self.psionicClassPowers()
			else:
				self.classPowers()

#################Class Stuff######################
	def classProficiencies(self):
		Class=classList[self.charclass]
		g={        "military melee":militaryMelee,
                   "military ranged":militaryRanged,
                   "simple melee":simpleMelee,
                   "simple ranged":simpleRanged}

		addit1=[]
		addit2=[]
		armornames=""
		weaponnames=""
		for x in Class.prof:
			x=x.lower()
			if x in ["cloth","leather","hide","chainmail","scale","plate","heavy","light"]: 
				addit1.append(x)
				if len(armornames)>0: armornames+=", "
				armornames+=x.title()
				if x=="light" or x=="heavy": armornames+=" Shields"
			elif x in ["military melee", "military ranged", "simple melee", "simple ranged"]:  
				addit2.append(g[x].copy())
				if len(weaponnames)>0: weaponnames+=", "
				weaponnames+=x.title()
			elif x=="military light blades":
				addit1+=[z for z in weaponKeyList(["military","light blade"])]
				if len(weaponnames)>0: weaponnames+=", "
				weaponnames+=x.title()
			elif x=="military heavy blades":
				addit1+=[z for z in weaponKeyList(["military","heavy blade"])]
				if len(weaponnames)>0: weaponnames+=", "
				weaponnames+=x.title()
			else: 
				addit1.append(x)
				if len(weaponnames)>0: weaponnames+=", "
				weaponnames+=x.title()
		self.addFeat(feat([ft("feat",addit2),ft("proficiency",addit1)],"Class Armor Proficiencies",armornames))
		self.addFeat(feat([],"Class Weapon Proficiencies",weaponnames))

	def remClassProficiencies(self):
		self.remFeat("Class Armor Proficiencies")
		self.remFeat("Class Weapon Proficiencies")

	def remClassPowers(self):
		removeit=[]
		for q in self.ftrs:
			if q.name()=="class power":
				removeit.append(q)
		for q in removeit:
			self.remFeat(q.name())

	def classPowers(self):
		self.addFeat(feat([ft("powerpick",PowerPick("at-will1", 0, MAXLEVEL+1, "At-will #"+str(x+1))) for x in xrange(2+self.featuretotal("at-willpowers"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("encounter1",1, 13, "Encounter 1"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("encounter3",3, 17, "Encounter 3"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("encounter7",7, 23, "Encounter 7"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("encounter13",13, 27, "Encounter 13"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("encounter17",17, MAXLEVEL+1, "Encounter 17"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("encounter23",23, MAXLEVEL+1, "Encounter 23"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("encounter27",27, MAXLEVEL+1, "Encounter 27"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily1",1, 15, "Daily 1"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily5",5, 19, "Daily 5"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily9",9, 25, "Daily 9"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily15",15, 29, "Daily 15"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily19",19, MAXLEVEL+1, "Daily 19"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily25",25, MAXLEVEL+1, "Daily 25"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily29",29, MAXLEVEL+1, "Daily 29"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility2",2, MAXLEVEL+1, "Utility 2"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility6",6, MAXLEVEL+1, "Utility 6"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility10",10, MAXLEVEL+1, "Utility 10"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility16",16, MAXLEVEL+1, "Utility 16"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility22",22, MAXLEVEL+1, "Utility 22"))],"class power"))

	def psionicClassPowers(self):
		self.addFeat(feat([ft("powerpick",PowerPick("at-will1",1, 7, "At-will 1 #1"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("at-will1",1, 13, "At-will 1 #2"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("at-will3",3, 17, "At-will 3"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("at-will7",7, 23, "At-will 7"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("at-will13",13, 27, "At-will 13"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("at-will17",17, MAXLEVEL+1, "At-will 17"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("at-will23",23, MAXLEVEL+1, "At-will 23"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("at-will27",27, MAXLEVEL+1, "At-will 27"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily1",1, 15, "Daily 1"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily5",5, 19, "Daily 5"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily9",9, 25, "Daily 9"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily15",15, 29, "Daily 15"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily19",19, MAXLEVEL+1, "Daily 19"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily25",25, MAXLEVEL+1, "Daily 25"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("daily29",29, MAXLEVEL+1, "Daily 29"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility2",2, MAXLEVEL+1, "Utility 2"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility6",6, MAXLEVEL+1, "Utility 6"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility10",10, MAXLEVEL+1, "Utility 10"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility16",16, MAXLEVEL+1, "Utility 16"))],"class power"))
		self.addFeat(feat([ft("powerpick",PowerPick("utility22",22, MAXLEVEL+1, "Utility 22"))],"class power"))

################Feat Stuff######################
	def addFeat(self, feature):
		self.ftrs.append(feature.copy())

	def remFeat(self, name):
		feature=""
		for q in self.ftrs:
			if q.named==name: feature=q
		if isinstance(feature, feat):
			self.ftrs.remove(feature)

	def myclass(self):
		if self.charclass in classList: return classList[self.charclass]
		else: return charClass(0,0,0)

	def myrace(self):
		if self.race in raceList: return raceList[self.race]
		else: return feat([])

####################Skill Stuff########################
	def oneClassSkill(self, theclass, title):
		sklist=[x for x in classList[theclass].skillList]
		for k in self.statret("training"): 
			if k.capitalize() in sklist: sklist.remove(k.capitalize())
		q=0
		if len(sklist)==1: q=sklist[0]
		elif len(sklist)>1: q=self.menu("Pick a skill to train:",sklist)[0]
		if q!=0: self.addFeat(feat([ft(q.lower(),["training",5])],title))	

	def pickSkills(self, sL, num):
		if num==0: return 0
		alreadyhave=[]
		skillList=[a for a in sL]
		for k in self.statret("training"):
			if k.capitalize() in skillList: skillList.remove(k.capitalize())
		ret=[]
		while num>0:
			if len(skillList)<=num:
				num=0
				for y in skillList:
					ret+=[skillTrain[y.lower()]]
			else:
				choice=self.menu("Choose a skill to train ("+str(num)+" remain):",skillList)[0]
				skillList.remove(choice)
				ret+=[skillTrain[choice.lower()]]
			num+=-1
		self.addFeat(feat([ft("feat",ret)],"Class Skills"))
		
######################Inventory Stuff##################
	def weaponkeys(self, name, keys):
		ret=[]
		for x in keys:
			ret+=self.featurestr(x+"newkey")
		ret+=self.featurestr(name+"newkey")
		return ret
	
	def handsFree(self):
		ret=[True, True]
		for x in range(2):
			if self.inventory.equipped[x]!=None:
				if isinstance (self.inventory.equipped[x].desc, Weapon):
					if self.inventory.equipped[x].name() not in ["unarmed attack","spiked gauntlet","battlefist"]:
						ret[x]=False
				else: ret[x]=False
		return ret

	def equip(self, item, onehandchoice=""):
		if isinstance(item.desc, Weapon):
			if "versatile" in item.desc.keys and self.check("feature","small"):
				if "off-hand" not in item.slots:
					item.slots.append("off hand")
			if "two-handed" in item.desc.keys and self.check("feature","small"):
				return 0
		if "ring" in item.eqslots():
			if onehandchoice=="primary hand": onehandchoice="left ring"
			if onehandchoice=="off hand": onehandchoice="right ring"
		self.inventory.inventory.remove(item)
		if "1hand" in item.eqslots():
			item.eqslots().append(onehandchoice)
		if "ring" in item.eqslots():
			item.eqslots().append(onehandchoice)

		for slot in item.eqslots():
			if slot!="1hand" and slot!="ring":
				self.inventory.remove(slot)
				self.inventory.equipped[itemslots[slot]]=item

        def equippedGroup(self, key):
                ret=[]
                if self.inventory.equipped[0]!=None:
                        if isinstance(self.inventory.equipped[0].desc, Weapon):
                                 ret.append(self.inventory.equipped[0].desc.group)
                if self.inventory.equipped[1]!=None:
                        if isinstance(self.inventory.equipped[1].desc, Weapon) and self.inventory.equipped[0]!=self.inventory.equipped[1]:
                                ret.append(self.inventory.equipped[1].desc.group)
                return key in ret

#####################Statret Stuff############################
	def translate(self, trans):
		transdict={0:"",1:"str"    ,2:"con",    3:"dex",    4:"int",    5:"wis",     6:"cha"
                         ,"healingsurge":"surge","healingsurges":"surges"}
		if transdict.has_key(trans): return transdict[trans]
		return trans
	def statmod(self, stat, num):
		stat=self.translate(stat)
		if stat=="str": self.stats[0]+=num
		if stat=="con": 
			self.stats[1]+=num
			self.statmod("hp", num)
		if stat=="dex": self.stats[2]+=num
		if stat=="int": self.stats[3]+=num
		if stat=="wis": self.stats[4]+=num
		if stat=="cha": self.stats[5]+=num
		if stat=="level": self.level+=num
		if stat=="all":
			for x in range(1,len(self.stats)+1): self.statmod(x,1)


	def check(self, stat, val, orand=False):
		"orand is or when true, and when false"
		z=self.statret(stat)
		if not isinstance(val, list): val=[val]
		for value in val:
			if isinstance(z, list):
				if (value in z) and orand: return True
				elif value not in z and not orand: return False
			if isinstance(z, int):
				if z>=value and orand: return True
				elif z<value and not orand: return False
			if isinstance(z, str):
				if value==z and orand:return True
				elif value!=z and not orand: return False
		if orand: return False
		else: return True
				

	def statret(self, stat):
		stat=self.translate(stat)
		try:
			return self.fastlookup[stat]
		except: 
			pass;
		self.fastlookup[stat]=0
		if stat=="showmods": self.fastlookup[stat]=self.showmods.get()
		if stat in ["corestr", "str"]: self.fastlookup[stat]=self.stats[0]
		if stat in ["corecon", "con"]: self.fastlookup[stat]=self.stats[1]
		if stat in ["coredex", "dex"]: self.fastlookup[stat]=self.stats[2]
		if stat in ["coreint", "int"]: self.fastlookup[stat]=self.stats[3]
		if stat in ["corewis", "wis"]: self.fastlookup[stat]=self.stats[4]
		if stat in ["corecha", "cha"]: self.fastlookup[stat]=self.stats[5]
		if stat in WEALTHTYPES:
			self.fastlookup[stat]=self.wealth[WEALTHTYPES.index(stat)]
		if stat in [x[0] for x in WEALTHINFO.values()]:
			for x in range(len(WEALTHTYPES)):
				if WEALTHINFO[WEALTHTYPES[x]][0]==stat: self.fastlookup[stat]=self.wealth[x]
		if stat=="load": self.fastlookup[stat]=self.inventory.load()+sum([self.statret(x)*WEALTHINFO[x][1] for x in WEALTHTYPES])
		if stat=="normalload": self.fastlookup[stat]=self.statret("str")*10
		if stat=="heavyload": self.fastlookup[stat]=self.statret("str")*20
		if stat=="pushload": self.fastlookup[stat]=self.statret("str")*50
		if stat in itemslots.keys():
			if self.inventory.equipped[itemslots[stat]]==None: self.fastlookup[stat]=""
			else: self.fastlookup[stat]=self.inventory.equipped[itemslots[stat]].name()
			return self.fastlookup[stat]
		if "choosestat" in stat:
			if stat in self.quicklook.keys(): self.fastlookup[stat]=self.quicklook[stat][0]
			return self.fastlookup[stat]
			
		if stat=="weapongroups":
			self.fastlookup[stat]=[]
			for x in self.inventory.equipped[:1]:
				if x!=None:
					if isinstance(x.desc, Weapon):
						self.fastlookup[stat]+=list(x.desc.group)
		if stat=="weaponkeys":
			self.fastlookup[stat]=[]
			for x in self.inventory.equipped[:1]:
				if x!=None:
					if isinstance(x.desc, Weapon):
						self.fastlookup[stat]+=list(x.desc.charkey(self))
		if stat in allskills: 
			self.fastlookup[stat]=self.level/2+self.mod(allskills[stat])
			if allskills[stat] in ["con","dex","str"]: self.fastlookup[stat]+=self.statret("acheck")
		if stat=="ac":            self.fastlookup[stat]=10+self.level/2+self.statret("light armor")
		if stat=="fort":          self.fastlookup[stat]=10+self.level/2+max(self.mod("str"),self.mod("con"))
		if stat=="ref":           self.fastlookup[stat]=10+self.level/2+max(self.mod("dex"),self.mod("int"))
		if stat=="will":          self.fastlookup[stat]=10+self.level/2+max(self.mod("wis"),self.mod("cha"))
		if stat=="hp": self.fastlookup[stat]=self.myclass().levelhp*(self.level-1)+self.myclass().hp+self.statret("con")
		if stat=="surge": self.fastlookup[stat]=self.statret("hp")/4
		if stat=="surges": self.fastlookup[stat]=self.myclass().surgenum+self.mod("con")
		if stat=="level": self.fastlookup[stat]=self.level
		if stat=="speed": self.fastlookup[stat]=6
		if stat=="checkrace": self.fastlookup[stat]=[self.race.lower()]
		if stat=="checkclass": self.fastlookup[stat]=[self.charclass.lower()]
		if stat=="race": self.fastlookup[stat]=self.race.lower()
		if stat=="class": self.fastlookup[stat]=self.charclass.lower()
		if stat=="handsfree": self.fastlookup[stat]=self.handsFree()
		if stat=="classskills":
			if self.charclass=="": self.fastlookup[stat]=[]
			else: self.fastlookup[stat]=classList[self.charclass].skillList
		if stat in powerList.keys():
			self.fastlookup[stat]=powerList[stat].values()
			return self.fastlookup[stat]
		if stat in [x.lower()+"dilettante" for x in classList.keys()]:
			self.fastlookup[stat]=[]
			for x in classList.keys():
				if x<>self.charclass:
					self.fastlookup[stat]+=self.statret(x.lower()+"at-will1")
			return self.fastlookup[stat]
		if stat=="feature": self.fastlookup["feature"]=[a.name().lower() for a in self.features()]+self.statret("featureadd")
		if stat=="initiative": self.fastlookup[stat]=self.level/2+self.mod("dex")
		if stat in ["origin", "type","paragonname", "epicname","dragonbreathelement","beastsize"]:
			if stat in self.quicklook.keys():
				self.fastlookup[stat]=self.quicklook[stat][0]
			elif stat=="origin": self.fastlookup[stat]="natural"
			elif stat=="type": self.fastlookup[stat]="humanoid"
			else: self.fastlookup[stat]=""
		if stat=="weapons": self.fastlookup[stat]=self.inventory.weapons(False, self.statret("addweapon"))
		if stat=="implements": self.fastlookup[stat]=self.inventory.implements()
		if stat=="powermods":
			if stat in self.quicklook.keys():
				return self.quicklook[stat]
		if stat in ["addweapon","featureadd","deity", "training","vision","skillpick","powerpick","languagepick","languages","armortype","replacepower", "subtype", "proficiency","dailypowerchoices","encounterpowerchoices","at-willpowerchoices","utilitypowerchoices"]: self.fastlookup[stat]=[]
		if stat=="power": self.fastlookup[stat]=[a.name().lower() for a in self.powers()]
		if stat=="focusnum":
			z = [a for a in self.statret("training")]
			remList=[]
			for skill in z:
				if "skill focus: "+skill in self.statret("feature"): remList+=[skill]
			self.fastlookup[stat]=len(z)-len(remList)
		if stat=="armorenchant":
			if self.inventory.equipped[itemslots["armor"]]==None: self.fastlookup[stat]=0
			else: self.fastlookup[stat]=self.inventory.equipped[itemslots["armor"]].enchantment()
		if stat in ["showmods","handsfree","weaponkeys","weapongroups","classkills","race","level","class","armorenchant", "focusnum","power","powermods", "implements","weapons","origin","type","paragonname","epicname","dragonbreathelement","beastsize", "feature"]: return self.fastlookup[stat]
		self.fastlookup[stat]+=self.featuretotal(stat)
		if stat=="size": 
			q={-2:"tiny",-1:"small",0:"Medium",1:"Large",2:"Huge",3:"Gargantuan"}
			if self.fastlookup[stat]<-2:self.fastlookup[stat]=-2
			if self.fastlookup[stat]>3:self.fastlookup[stat]=3
			self.fastlookup[stat]=q[self.fastlookup[stat]]
			return self.fastlookup[stat]
		elif stat=="acheck" and self.fastlookup[stat]>0:
			self.fastlookup[stat]=0
		return self.fastlookup[stat] 
        

	def mod(self, stat):
		return self.statret(stat)/2-5

	def featurestr(self, mod):
		z=[]
		if mod in self.quicklook.keys():
			for resolve in self.quicklook[mod]:
				if isinstance(resolve, list):
					if isinstance(resolve[0],Item): z+=[item.copy for item in resolve]
					else: z+=[res(item, self) for item in resolve]
				elif isinstance(resolve, Item): z+=[resolve.copy()]
				else: z+=[res(resolve, self)]
		return z

	def testlist(self, mod, val):
		if isinstance(val, list):
			if mod in val: return True
		elif mod==val: return True
		return False 

	def modtotal(self, mod):
		z=0
		for q in self.features():
			for x in q.what():
				if isinstance(x.resolve, list) and x.when not in ["feat","power"]:
					if x.resolve[0]==mod: z=max(z,res(x.resolve[1],self))
		return z
						
	def setQuicklook(self):
		quicklook={}
		for feat in self.features():
			for what in feat.what():
				whenlist=what.when
				if not(isinstance(what.when, list)): whenlist=[what.when]
				if "and" in whenlist:
					if "and" not in quicklook: quicklook["and"]=[[what.when, what.resolve]]
					else: quicklook["and"]+=[[what.when, what.resolve]]
				else:
					for when in whenlist:
						if when not in quicklook: quicklook[when]=[what.resolve]
						else: quicklook[when]+=[what.resolve]
		self.quicklook=quicklook

	def featuretotal(self, mod):
		if mod in ["addweapon","featureadd","languages","checkrace","subtype","proficiency","checkclass","origin","deity","vision","skillpick", "powerpick","armortype","replacepower","languagepick"]:
			return self.featurestr(mod)
		if mod=="training":
			z=[]
			for x in allskills.keys():
				if x in self.quicklook:
					for resolve in self.quicklook[x]:
						if isinstance(resolve, list):
							if resolve[0]=="training": z+=[x] 
			return z
		if mod in ["at-willpowerchoices","dailypowerchoices","encounterpowerchoices","utilitypowerchoices"]:
			z=[self.charclass.lower()]
			if mod in self.quicklook:
				for resolve in self.quicklook[mod]:
					if resolve.lower() not in z: z.append(resolve.lower())
			return z
					
		z=0
		k={}
		if mod in self.quicklook:
			for resolve in self.quicklook[mod]:
				modtype=resolve[0]
				value=res(resolve[1], self)
				if modtype=="": z+=value
				elif modtype in k: k[modtype]=max(value, k[modtype])
				else: k[modtype]=value
		z+=sum(k.values())
		return z

	def featureis(self, mod):
		z=""
		if mod in self.quicklook:
			return res(self.quicklook[mod][0], self)
		return z

	def modmux(self, keys, style):
		z=0
		k={}
		modstyle=[mod+style for mod in keys]
		for val in modstyle:
			if val in self.quicklook.keys():
				for resolve in self.quicklook[val]:
					modtype=resolve[0]
					value=res(resolve[1], self)
					if modtype=="": z+=value
					elif modtype in k: k[modtype]=max(value, k[modtype])
					else: k[modtype]=value
		if "and" in self.quicklook.keys():
			for test in self.quicklook["and"]:
				if sum([check in modstyle for check in test[0][1:]])==len(test[0][1:]):
					modtype=test[1][0]
					value=res(test[1][1], self)
					if modtype=="": z+=value
					elif modtype in k: k[modtype]=max(value, k[modtype])
					else: k[modtype]=value
		z+=sum(k.values())
		return z
######Output Stuff####
	def printfeats(self, split=False):
		
		ret1=""
		ret2=["",""]
       		for theFeat in self.ftrs+self.inventory.feats():
       			pgon=False
       			if theFeat.name() in ["paragon","epic"]:
       				theFeats=theFeat.what()[0].resolve
       				pgon=True
       			else:
       				theFeats=[theFeat]
       			for feat in theFeats:
       				if ((feat.string(self)!="") or (feat.featPick<>None)) and (feat.levelReq()<=self.statret("level")) and not(pgon and not(feat.preReqs(self))):
       					if not split: ret1+=feat.string(self)+"\n"
       					else:
       						ret2[0]+=feat.name()+"\n"
       						ret2[1]+=res(feat.desc(), self)+"\n"
                                        
		if not split: return ret1
		else: return ret2

	def htmlFeats(self):
		ret=["",""]
		retList=["","","",""]
		sumfeats=[0,0,0,0]
		for theFeat in self.ftrs+self.inventory.feats():
			pgon=False
			featType=0
			if theFeat.name() in ["paragon","epic"]:
				theFeats=theFeat.what()[0].resolve
				pgon=True
				featType=2
			else:
				theFeats=[theFeat]
				if self.race!="":
					if theFeat.named in [x.named for x in raceList[self.race.title()]]: featType=1
				if self.charclass!="":
					if theFeat.named in [x.named for x in classList[self.charclass.title()].features]+["Class Armor Proficiencies","Class Weapon Proficiencies"]: featType=2
				if theFeat.named in [x.named for x in self.inventory.feats()]: featType=3
					
			for feat in theFeats:
				if ((feat.string(self)!="") or (feat.featPick<>None)) and (feat.levelReq()<=self.statret("level")) and not(pgon and not(feat.preReqs(self))) and "Stat for " not in feat.named:
					text="\n\t\t\t<tr><td nowrap>"+feat.name()+"</td><td>"+res(feat.desc(), self)+"</td></tr>"
					retList[featType]+=text
					sumfeats[featType]+=1
		sum=0
		retNum=0
		captions={0: "Feats",1: "Racial Features",2: "Class Features",3: "Item Properties"}
		for x in range(4):
			if retList[x]!="": ret[retNum]+="\n\t\t<table id=\"featstable\">\n\t\t\t<CAPTION>"+captions[x]+"</CAPTION>"+retList[x]+"\n\t\t</table>\n\t\t"
			sum+=sumfeats[x]
			if sum>=len(allskills): retNum=1
		return ret

	def printpowers(self):
		ret=""
		for power in self.powers(): 
			ret+=power.output(self)+"\n"
		return ret

	def beasttext(self):
		quickret=lambda x: x.title()+": "+str(self.statret("beast"+x.lower()))+"\t"
		if self.inventory.equipped[itemslots["beast"]]==None:
			return ""
		else:
			z=self.inventory.equipped[itemslots["beast"]].name().title()+"\n"
			for x in ["str","dex","wis","con","int","cha","size","speed","AC","fort","ref","will","hp"]:
				z+=quickret(x)
				if x=="hp":
					z+="\tSurge: "+str(self.statret("beasthp")/4)
				if x in ["wis","cha","size","speed","will","hp"]:
					z+="\n"
			for x in allskills.keys():
				if self.statret("beast"+x)!=0:
					z+=x.title()+": "+str(self.statret("beast"+x.lower())+self.mod("beast"+allskills[x])+self.statret("level")/2)+"\t"
			return z
			

	def shortpowers(self):
		x=0
		ret=""
		for power in sorted(list(self.powers())):
			often=self.featureis(power.name().lower()+"often")
			if often=="": often=power.often
			if power.name()[:16]=="Channel Divinity":
				if x<1:
					x=1
					ret+="Channel Divinity Powers:\n"
			elif often=="at-will" and x<2:
				if x>0: ret+="\n"
				x=2
				ret+="At-will powers:\n"
			elif often=="encounter" and x<3:
				if x>0: ret+="\n"
				x=3
				ret+="Encounter powers:\n"
			elif often=="daily" and x<4:
				if x>0: ret+="\n"
				x=4
				ret+="Daily powers:\n"

			if sum([isinstance(z,Attack) for z in power.effects])>0:
				ret+=power.output(self)
			else:
				ret+=power.name().ljust(40)+" "
				for key in power.keys:
					ret+=key.capitalize()+" "
				ret+="\n"
		return ret

	def printability(self,stat):
		z=stat.capitalize()+":"+" "+str(self.statret(stat))+"("
		if self.mod(stat)+self.statret("level")/2>-1: z+="+"
		z+=str(self.mod(stat)+self.statret("level")/2)+")"
		return z