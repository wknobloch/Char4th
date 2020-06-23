from types import *
from charutils import *

class SkillPick:
	def __init__(self, skillChoices, numChoices, basename="Choose Skill"):
		self.classskills=""
		if isinstance(skillChoices, str):
			self.skillChoices=[]
			self.classskills=skillChoices
		else:
			self.skillChoices=[x.lower() for x in skillChoices]
		self.chosen=[-1]*numChoices
		self.needmenu=True
		if numChoices>=len(self.skillChoices) and not(self.classskills):
			for x in xrange(numChoices):
				self.chosen[x]=x
			self.needmenu=False
		self.basename=basename

	def chosenFeature(self):
		ret=[]
		for x in self.chosen:
			if x<>-1:
				ret.append(ft(self.skillChoices[x].lower(),["training",5]))
		return feat(ret)

	def copy(self):
		if self.classskills=="":
			ret=SkillPick(self.skillChoices, len(self.chosen), self.basename)
		else:
			ret=SkillPick(self.classskills, len(self.chosen), self.basename)
		ret.chosen=[x for x in self.chosen]
		return ret

class PowerPick:
	def __init__(self, powerChoices, levelReq=0, maxLevel=31, basename="Choose Power"):
		self.powerChoices=[]
		self.classPower=False
		self.specialPower=""
		if isinstance(powerChoices, str):
			self.classPower=True
			self.specialPower=powerChoices
		else:
			self.powerChoices=[x for x in powerChoices]
		self.chosen=-1
		self.levelReq=levelReq
		self.maxLevel=maxLevel
		self.basename=basename

	def chosenFeature(self):
		if self.chosen==-1:
			return feat([])
		ret = self.powerChoices[self.chosen]
		if self.specialPower=="dilettante":
			ret.often="encounter"
		return feat([ft("power",[ret])])
	
	def copy(self):
		ret=PowerPick(self.powerChoices, self.levelReq)
		ret.chosen=self.chosen
		return ret

class Inventory:
	def __init__(self):
		self.equipped=[None]*len(itemslots)
		self.inventory=[]

	def buy(self, item, enchant=0):
		if isinstance(item, Weapon):
			self.inventory.append(Item(item.copy()))
		else:
			self.inventory.append(item.copy())
		self.inventory[-1].enchantPlus(enchant)
	
	def drop(self, item):
		g=[x.name() for x in self.inventory].index(item)
		self.inventory.remove(self.inventory[g])

	def remove(self,slot):
		removea=self.equipped[itemslots[slot]]
		if removea!=None:
			for st in removea.eqslots():
				if st!="1hand" and st!="ring":	self.equipped[itemslots[st]]=None
			if "1hand" in removea.eqslots():
				if "off hand" in removea.eqslots(): removea.eqslots().remove("off hand")
				if "primary hand" in removea.eqslots(): removea.eqslots().remove("primary hand")
			if "left ring" in removea.eqslots(): removea.eqslots().remove("left ring")
			if "right ring" in removea.eqslots(): removea.eqslots().remove("right ring")
			self.inventory.append(removea)

	def dualwield(self):
		if self.equipped[0]!=None and self.equipped[1]!=None:
			return isinstance(self.equipped[0].desc, Weapon) and isinstance(self.equipped[1].desc, Weapon) and (self.equipped[0]!=self.equipped[1] or "double weapon" in self.equipped[0].desc.keys)
		return False

	def feats(self):
		featslist=[]
		for x in xrange(0,len(self.equipped)):
			if self.equipped[x]!=None:
				z=0
				if self.equipped[x].slots[0]=="1hand" or self.equipped[x].slots[0]=="ring": z=1
				if x == itemslots[self.equipped[x].slots[z]]:
					if self.equipped[x].features()!=None: featslist+=self.equipped[x].features()
		return featslist
	
	def implements(self):
		implementslist=[]
		if self.equipped[0]!=None:
			if self.equipped[0].desc in implements:
				implementslist.append(self.equipped[0].desc)
		if self.equipped[1]!=None:
			if self.equipped[1].desc in implements and self.equipped[1].desc not in implementslist:
				implementslist.append(self.equipped[1].desc)
		if self.equipped[10]!=None:
			if self.equipped[10].desc in implements and self.equipped[10].desc not in implementslist:
				implementslist.append(self.equipped[10].desc)
		return implementslist
	
	def beast(self):
		if self.equipped[11]!=None:
			return self.equipped[11].desc
		return ""
	
	def equipgroups(self, num):
		if self.equipped[num]!=None:
			return self.equipped[num].desc.group
		return []
	
	def weapons(self, onlyequipped=False, more=[]):
		def addExtra(weapon):
			ret=[]
			if "double weapon" in weapon.desc.keys:
				weapon.desc.remkey("two-handed")
				ret.append(weapon.copy())
				weapon.desc.addkey(["one-handed", "primary"])
				ret[0].desc.addkey(["one-handed", "offhand"])
				ret[0].desc.dmg=ret[0].desc.doublewpndmg
			return ret
		weaponslist=[]+list(more)
		if self.equipped[0]!=None:
			if isinstance(self.equipped[0].desc,Weapon):
				if self.equipped[1]==None: weaponslist.append(self.equipped[0].copy())
				elif (not isinstance(self.equipped[1].desc, Weapon)) or self.equipped[1]==self.equipped[0]:
					weaponslist.append(self.equipped[0].copy())
					weaponslist+=addExtra(weaponslist[-1])
				else: 
					if isinstance(self.equipped[1].desc,Weapon):
						ggg=[self.equipped[0].copy(), self.equipped[1].copy()]
						ggg[0].desc.addkey("primary")
						ggg[1].desc.addkey("offhand")
#						ggg+=addExtra(ggg[0])+addExtra(ggg[1])
						weaponslist+=ggg+addExtra(ggg[0])+addExtra(ggg[1])
		elif self.equipped[1]!=None:
			if isinstance(self.equipped[1].desc, Weapon):
				ggg=self.equipped[1].copy()
				ggg.desc.addkey("offhand")
				weaponslist+=[ggg]+addExtra(ggg)
		if not onlyequipped:
			for item in weaponslist:
				item.desc.addkey("equipped")
			for item in self.inventory:
				if isinstance(item.desc, Weapon): 
					weaponslist.append(item.copy())
					weaponslist+=addExtra(weaponslist[-1])
		thrownStuff=[]
		for weapon in weaponslist:
			if ("thrownmelee" in weapon.desc.keys) and "melee" in weapon.desc.keys:
			 	thrownStuff.append(weapon.copy())
			 	thrownStuff[-1].desc.remkey("melee")
			 	thrownStuff[-1].desc.addkey("ranged")
		weaponslist+=thrownStuff
		return weaponslist

	def output(self):
		z=""
		for key in itemslots.keys():
			if self.equipped[itemslots[key]]!=None:
				test=True
				for slot in self.equipped[itemslots[key]].eqslots():
					if slot!="1hand" and slot!="ring": 
						if itemslots[slot]<itemslots[key]: test=False
				if test: z+=key.capitalize()+": "+self.equipped[itemslots[key]].name()+"\n"
		for item in self.inventory:
			z+=item.name().capitalize()+"\n"
		return z

	def htmlOut(self):
		z=""
		for key in itemslots.keys():
			if self.equipped[itemslots[key]]!=None:
				test=True
				for slot in self.equipped[itemslots[key]].eqslots():
					if slot!="1hand" and slot!="ring": 
						if itemslots[slot]<itemslots[key]: test=False
				if test: z+="<b>"+key.capitalize()+":</b> "+self.equipped[itemslots[key]].name().capitalize()+"</td><td>"+str(self.equipped[itemslots[key]].weight)+"\n"
		havelist={}
		for item in self.inventory:
			if item.name() not in havelist:
				havelist[item.name()]=1
			else: havelist[item.name()]+=1
		for item in self.inventory:
			if havelist[item.name()]>0:
				if havelist[item.name()]>1:
					z+=str(havelist[item.name()])+" "
				z+=item.name().capitalize()+"</td><td>"+str(item.weight*havelist[item.name()])+"\n"
				havelist[item.name()]=0
		return z[:-1]
	
	def load(self):
		z=0
		for key in itemslots.keys():
			if self.equipped[itemslots[key]]!=None:
				test=True
				for slot in self.equipped[itemslots[key]].eqslots():
					if slot!="1hand" and slot!="ring":
						if itemslots[slot]<itemslots[key]: test=False
				if test: z+=self.equipped[itemslots[key]].weight
		for item in self.inventory:
			z+=item.weight
		return z

class Item:
	def __init__(self, itemDesc=None, slots=[], features=[], enchantments=[], weight=0, property=None):
		enchants=list(enchantments)
		self.slots=list(slots)
		feats=list(features)
		if "2hand" in slots:
			self.slots.remove("2hand")
			self.slots+=["primary hand","off hand"]
		self.desc=itemDesc
		self.weight=weight
		if isinstance(itemDesc, Weapon):
			if "one-handed" in itemDesc.keys and "1hand" not in itemDesc.keys: self.slots.append("1hand")
			if "two-handed" in itemDesc.keys and "primary hand" not in itemDesc.keys: self.slots.append("primary hand")
			if "two-handed" in itemDesc.keys and "off hand" not in itemDesc.keys: self.slots.append("off hand")
			if features==[]:
				if "defensive" in itemDesc.keys: feats.append(feat([ft("ac",("defensive",lambda x:x.inventory.dualwield() and x.check("proficiency",self.desc.name)))]))
				if "spiked shield"==itemDesc.name: feats.append(feat([ft(["ac","ref"],("shield",lambda x:x.check("proficiency","light shields"))),ft("armortype","shield"),ft("armortype","light shield")]))
			if enchants==[]:
				if itemDesc.name=="dagger":
					enchants.append(feat([ft("daggerimplement",["enhancement",0])],"magic"))
				if "staff" in itemDesc.group:
					enchants.append(feat([ft("staffimplement",["enhancement",0])],"magic"))
				if "light blade" in itemDesc.group:
					enchants.append(feat([ft("light bladeimplement",["enhancement",0])],"magic"))
				if "heavy blade" in itemDesc.group:
					enchants.append(feat([ft("heavy bladeimplement",["enhancement",0])],"magic"))
				if "dagger" in itemDesc.group:
					enchants.append(feat([ft("daggerimplement",["enhancement",0])],"magic"))
			self.weight=itemDesc.weight
			self.desc=itemDesc.copy()
		self.slots.sort()
		x=0
		while x+1<len(self.slots):
			if self.slots[x]==self.slots[x+1]: self.slots.remove(self.slots[x+1])
			else: x=x+1
		self.ftrs=[x.copy() for x in feats]
		self.enchantments=[x.copy() for x in enchants]
		self.property=None
		if property!=None: self.property=property.copy()

	def eqslots(self):
		if self.property==None: return self.slots
		elif self.property.slots==[]: return self.slots
		return self.property.slots

	def enchantPlus(self, newPlus):
		if isinstance(self.desc, Weapon):
			self.desc.enchantment=newPlus
		else:
			for x in self.enchantments:
				if x.name()=="enchant":
					self.enchantments.remove(x)
					break
			if newPlus>0:
				self.enchantments.append(feat([ft("enchantnum",newPlus)],"enchant"))
		for x in self.enchantments:
			if x.name()=="magic":
				for z in x.what():
					z.resolve[1]=newPlus
		if self.property!=None:
			for x in self.property.enchantment:
				if x.name()=="magic":
					for z in x.what():
						z.resolve[1]=newPlus
	def setProperty(self, newprop):
		if newprop==None: self.property=None
		else: 
			self.property=newprop.copy()
			for x in self.property.enchantment:
				if x.name()=="magic":
					for z in x.what():
						z.resolve[1]=self.enchantment()
		
	def enchantment(self):
		if isinstance(self.desc, Weapon):
			return self.desc.enchantment
		else: 
			for x in self.enchantments:
				if x.name()=="enchant":
					for what in x.what():
						if what.when=="enchantnum":
							return what.resolve
		return 0
	def canPlus(self):
		if isinstance(self.desc, Weapon): return True
		for x in self.features():
			if x.name()=="magic":
				return True
		return False

	def features(self):
		ret=self.enchantments+self.ftrs
		if self.property!=None: ret+=self.property.enchantment
		return ret

	def armorType(self):
		for feat in self.ftrs:
			for what in feat.what():
				if what.when=="armortype" and what.resolve not in ["light","heavy","shield"]: return what.resolve
		return None 
	
	def cleanname(self):
		if isinstance(self.desc,Weapon):return self.desc.name
		else: return self.desc

	def name(self):
		ret=self.cleanname()
		if self.property!=None:
			ret=self.property.name.replace("#", ret)
		if self.enchantment()>0:
			ret+=" +"+str(self.enchantment())
		return ret

	def copy(self):
		return Item(self.desc, self.slots, self.ftrs, self.enchantments, self.weight, self.property)

class Property:
	def __init__(self, name, legal, enchantment, slots=[]):
		self.name=name
		self.legal=list(legal)
		self.enchantment=[x.copy() for x in enchantment]
		self.slots=list(slots)
		
	def legalItem(self, item):
		setret=True
		for x in self.legal:
			if x=="weapon":
				return isinstance(item.desc, Weapon)
			elif isinstance(x, int):
				if item.enchantment()<x: return False
			elif x in ["armor","arm","feet","hands","head","neck","ring","waist"]:
				if x not in item.slots: return False
			elif x in ["shield","light shield","heavy shield","plate","scale","chainmail","hide","leather","cloth"]:
				setret=False
				if item.armorType()==None: return False
				elif x in item.armorType(): return True
			elif x in ["axe","bow","crossbow","flail","hammer","heavy blade","light blade","mace","pick","polearm","sling","spear","staff"]:
				setret=False
				if not isinstance(item.desc, Weapon): return False
				elif x in item.desc.group: return True
			elif x in ["ranged", "melee"]:
				if not isinstance(item.desc, Weapon): return False
				elif x in item.desc.keys or (x=="ranged" and ("heavy thrown" in item.desc.keys or "light thrown" in item.desc.keys)): return True
				else: return False
			elif x!=item.cleanname():
				return False
		return setret
					
				
	
	def copy(self):
		return Property(self.name, self.legal, self.enchantment, self.slots)

class Weapon:
	def __init__(self, name, keys, prof, dmg, weight, group, rng=(), enchantment=0):
		self.name=name
		self.keys=keys
		self.prof=prof
		self.dmg=[dmg[0],dmg[1]]
		self.weight=weight
		self.group=group
		if "melee" in keys and ("heavy thrown" in keys or "light thrown" in keys) and "thrownmelee" not in keys: keys.append("thrownmelee")
		self.rng=rng
		self.enchantment=enchantment
		self.doublewpndmg=list([0,0])
		if len(dmg)==4:
			self.dmg=list(dmg[:2])
			self.doublewpndmg=list(dmg[2:])

	def charkey(self, character):
		return self.keys+character.weaponkeys(self.name, self.keys)

	def addkey(self, key):
		if isinstance(key, list): self.keys+=key
		else: self.keys.append(key)

	def remkey(self, key):
		if isinstance(key, list):
			for k in key: self.keys.remove(k)
		else: self.keys.remove(key)

	def __cmp__(self, other):
		if not(isinstance(other, Weapon) or isinstance(other, Item)): return -1
		if isinstance(other, Weapon): return cmp(self.name, other.name)
		return cmp(self.name(), other.name())

	def copy(self):
		ret=Weapon(self.name, list(self.keys), self.prof, self.dmg, self.weight, list(self.group), self.rng, int(self.enchantment))
		if self.doublewpndmg<>(0,0):
			ret.doublewpndmg=(self.doublewpndmg[0],self.doublewpndmg[1])
		return ret

class specialMenu:
	def __init__(self, optionNames, optionFeats, preName="", postName="", featTitles=None):
		self.optionNames=list(optionNames)
		self.optionFeats=[x.copy() for x in optionFeats]
		self.chosen=0
		self.preName=preName
		self.postName=postName
		self.featTitles=None
		if featTitles<>None:
			self.featTitles=[x for x in featTitles]
	def chosenFeature(self):
		return self.optionFeats[self.chosen]
	
	def clicky(self, newChosen, cFrame):
		def clickit():
			self.chosen=newChosen
			cFrame.update()
		return clickit
	
	def name(self):
		if self.featTitles==None:
			return ""
		else: return self.featTitles[self.chosen]
	
	def desc(self):
		ret1=self.optionNames[self.chosen]
		ret2=self.preName
		ret3=self.postName
		if isinstance(self.optionNames[self.chosen],str):
			ret1=[self.optionNames[self.chosen]]
		if isinstance(self.preName, str):
			ret2=[self.preName]
		if isinstance(self.postName, str):
			ret3=[self.postName]
		return ret2+ret1+ret3

	def nameLabel(self, root, row, column, cFrame):
		if self.featTitles==None:
			if self.name()=="": return None
			return Label(root, text=res(self.name(), cFrame.char))
		else:
			ret=Menubutton(root, text=res(self.name(), cFrame.char), fg="blue", relief=RELIEF, cursor=SELECTCURSOR)
			ret.menu=Menu(ret, tearoff=0)
			ret["menu"]=ret.menu
			for newChosen in range(0,len(self.featTitles)):
				ret.menu.add_command(label=res(self.featTitles[newChosen],cFrame.char), command=self.clicky(newChosen, cFrame))
			return ret

	def descLabel(self, root, row, column, cFrame):
		if self.featTitles<>None:
			Label(root, text=res(self.desc(), cFrame.char)).grid(row=row, column=column, sticky="w")
		else:
			ret=Menubutton(root, text=res(self.desc(), cFrame.char), fg="blue", relief=RELIEF, cursor=SELECTCURSOR)
			ret.grid(row=row, column=column, sticky="w")
			ret.menu=Menu(ret, tearoff=0)
			ret["menu"]=ret.menu
			for newChosen in range(0,len(self.optionNames)):
				ret.menu.add_command(label=res(self.optionNames[newChosen], cFrame.char), command=self.clicky(newChosen, cFrame))

	def copy(self):
		g=specialMenu(self.optionNames, self.optionFeats, self.preName, self.postName, self.featTitles)
		g.chosen=self.chosen
		return g

class PowerMod(specialMenu):
	def __init__(self, powerChoices, modeffect, prename, postname):
		self.powerChoices=list(powerChoices)
		self.chosen="one power"
		self.modeffect=list(modeffect)
		self.prename=prename
		self.postname=postname

	def chosenFeature(self):
		return feat([ft(self.chosen.lower()+self.modeffect[0], self.modeffect[1])])

	def clicky(self, newChosen, cFrame):
		def clickit():
			self.chosen=newChosen
			cFrame.update()
		return clickit

	def name(self):
		return ""
	
	def desc(self):
		return self.prename+self.chosen+self.postname

	def nameLabel(self, root, row, column, cFrame):
		return None

	def descLabel(self, root, row, column, cFrame):
		ret=Menubutton(root, text=res(self.desc(), cFrame.char), fg="blue", relief=RELIEF, cursor=SELECTCURSOR)
		ret.grid(row=row, column=column, sticky="w")
		ret.menu=Menu(ret, tearoff=0)
		ret["menu"]=ret.menu
		for newChosen in [x.name() for x in cFrame.char.findPowers(self.powerChoices)]:
			ret.menu.add_command(label=newChosen, command=self.clicky(newChosen, cFrame))

	def copy(self):
		ret=PowerMod(self.powerChoices, self.modeffect, self.prename, self.postname)
		ret.chosen=self.chosen
		return ret


class FeatPick:
	def __init__(self, levelReq=0, basename="Choose feat", chosen=0,flist=[]):
		self.levelReq=levelReq
		self.basename=basename
		self.chosen=chosen
		self.featlist=[x for x in flist]

	def chosenFeature(self):
		if self.chosen==0:
			return feat([])
		else:
			return self.chosen

	def clicky(self, newChosen, cFrame):
		def clickit():
			self.chosen=newChosen.copy()
			cFrame.update()
		return clickit

	def nameLabel(self, root, row, column, cFrame):
		name=self.chosenFeature().name()
		if name=="": name=self.basename
		ret=Menubutton(root, text=res(name, cFrame.char), fg="blue", relief=RELIEF, cursor=SELECTCURSOR)
		if self.chosen==0: ret.config(fg="darkred")
		ret.grid(row=row, column=column, sticky="w")
		ret.menu=Menu(ret, tearoff=0)
		ret["menu"]=ret.menu
		def makeMenu(e):
			ret.menu.destroy()
			ret.menu=Menu(ret, tearoff=0)
			ret["menu"]=ret.menu
			if self.featlist==[]:
				legal = cFrame.legalFeats
				for z in legal:
					if len(z)>1:
						menu=Menu(ret.menu, tearoff=0)
						for newChosen in z[:-1]:
							menu.add_command(label=newChosen.name()+"   |   "+res(newChosen.desc(), cFrame.char), command=self.clicky(newChosen, cFrame))
						ret.menu.add_cascade(menu=menu, label=z[-1])
#				for newChosen in legal[0]:
#					hero.add_command(label=newChosen.name(), command=self.clicky(newChosen, cFrame))
#				for newChosen in legal[1]:
#					paragon.add_command(label=newChosen.name(), command=self.clicky(newChosen, cFrame))
#				for newChosen in legal[2]:
#					epic.add_command(label=newChosen.name(), command=self.clicky(newChosen, cFrame))
#				for newChosen in legal[3]:
#					multiclass.add_command(label=newChosen.name(), command=self.clicky(newChosen, cFrame))
#				if len(legal[0])>0:ret.menu.add_cascade(menu=hero, label="Heroic Feats")
#				if len(legal[1])>0:ret.menu.add_cascade(menu=paragon, label="Paragon Feats")
#				if len(legal[2])>0:ret.menu.add_cascade(menu=epic, label="Epic Feats")
#				if len(legal[3])>0:ret.menu.add_cascade(menu=multiclass, label="Multiclass Feats")
			else:
				for newChosen in self.featlist:
					ret.menu.add_command(label=newChosen.name(), command=self.clicky(newChosen, cFrame))
		ret.bind("<Button-1>", makeMenu)

	def copy(self):
		return FeatPick(self.levelReq, self.basename, self.chosen, self.featlist)

class MultiMenu:
	def __init__(self, featlists=[], text=[], chosen=[]):
		self.featlists=list(featlists)
		self.chosen=list(chosen)
		if chosen==[]:
			self.chosen=["" for x in featlists]
		self.text=list(text)
		self.frame=None

	def name(self):
		return ""

	def desc(self):
		if "" in self.chosen:
			return ""
		else:
			ret=list(self.text[0])
			for x in range(len(self.chosen)):
				ret+=list(self.chosen[x])
				ret+=list(self.text[x+1])
		return ret

	def chosenFeature(self):
		ret=[]
		for x in range(len(self.chosen)):
			if self.chosen[x] !="":
				if isinstance(self.featlists[x], list): ret+=self.featlists[x][2](self.chosen[x])
				else: ret+=self.featlists[x][self.chosen[x]].wht
		return feat(ret)

	def clicky(self, newChosen, num, cFrame):
		def clickit():
			self.chosen[num]=newChosen
			cFrame.update()
		return clickit
	
	def descLabel(self, root, row, column, cFrame):
		ret=Frame(root)
		ret.grid(row=row, column=column, sticky="w", columnspan=10)
		Label(ret, text=res(self.text[0],cFrame.char)).grid(row=0, column=0)
		for x in range(len(self.chosen)):
			newMenu=Menubutton(ret, fg="blue",relief=RELIEF, cursor=SELECTCURSOR)
			newMenu.menu=Menu(newMenu, tearoff=0)
			newMenu["menu"]=newMenu.menu
			if isinstance(self.featlists[x],list):
				if self.chosen[x]=="": newMenu.config(fg="darkred",text="<choose>")
				else: newMenu.config(fg="darkred",text=self.chosen[x])
				if self.featlists[x][0]=="power":
					for power in cFrame.char.findPowers(self.featlists[x][1]):
						newMenu.menu.add_command(label=power.name(), command=self.clicky(power.name(), x, cFrame))
			else:
				try: newMenu.config(fg="blue", text=self.featlists[x][self.chosen[x]].name())
				except: newMenu.config(fg="darkred", text="<choose>")
				for newChosen in self.featlists[x].values():
					newMenu.menu.add_command(label=newChosen.name(), command=self.clicky(newChosen.name(), x, cFrame))
			newMenu.grid(row=0, column=x*2+1)
			Label(ret, text=res(self.text[x+1], cFrame.char)).grid(row=0, column=x*2+2)

	def copy(self):
		return MultiMenu(self.featlists, self.text, self.chosen)

class ft:
	def __init__(self, when, what):
		self.when=when
		if isinstance(what, list) or isinstance(what, tuple):
			self.resolve=list(what)
		elif isinstance(what, specialMenu) or isinstance(what, SkillPick):
			self.resolve=what.copy()
		else: 
			self.resolve=what
	
	def copy(self):
		return ft(self.when, self.resolve)

class feat:
	def __init__(self, features, name="", desc="",prereqs=lambda x:True):
		self.preReqs=prereqs
		self.named=name
		self.description=desc
		self.wht=[]
		powers=[]
		self.specMenu=None
		self.featPick=None
		self.powerMod=None
		for what in features:
			if isinstance(what, ft): 
				if what.when=="featpick": self.featPick=what.resolve
				else: self.wht.append(what.copy())
			if isinstance(what, specialMenu): self.specMenu=what.copy()
			if isinstance(what, MultiMenu): self.specMenu=what.copy()
			if isinstance(what, Power): powers.append(what.copy()) 
		if powers!=[]: self.wht.append(ft("power",powers))

	
	
	def levelReq(self):
		if self.featPick==None: return 0
		else: return self.featPick.levelReq

	def string(self, character):
		if (res(self.name(),character)=="") or (res(self.desc(),character)==""): return ""
		z=res(self.name(),character).ljust(40)
		z+=res(self.desc(),character)
		return z

	def name(self):
		if self.featPick<>None:
			x=self.featPick.chosenFeature().name()
			if x=="": x=self.featPick.basename
			if x=="": x=self.named
			return x
		if self.specMenu<>None:
			if self.specMenu.name()<>"": return self.specMenu.name()
		return self.named
	
	def desc(self):
		if self.featPick!=None: x=self.featPick.chosenFeature().desc()
		elif self.specMenu!=None:
			if self.specMenu.desc()!="": x=self.specMenu.desc()
			else: x=self.description
		else: x=self.description
		return x
	
	def nameLabel(self, root, row, column, cFrame):
		x=None
		if self.specMenu<>None:
			x=self.specMenu.nameLabel(root, row, column, cFrame)
		if (x==None) and (self.featPick==None):
			Label(root, text=res(self.name(), cFrame.char)).grid(row=row, column=column, sticky="w")
		elif self.featPick<>None:
			self.featPick.nameLabel(root, row, column, cFrame)
		else: x.grid(row=row, column=column, sticky="w")
	
	def descLabel(self, root, row, column, cFrame):
		if self.specMenu!=None:
			self.specMenu.descLabel(root, row, column, cFrame)
		elif self.featPick!=None:
			self.featPick.chosenFeature().descLabel(root, row, column, cFrame)
		else:
			Label(root, text=res(self.desc(), cFrame.char)).grid(row=row, column=column, sticky="w")

	def prereqs(self, char):
		return self.preReqs(char)

	def what(self):
		if self.featPick<>None:
			return self.featPick.chosenFeature().what()
		if self.specMenu<>None:
			return self.specMenu.chosenFeature().what()+self.wht
		return self.wht

	def __cmp__(self, other):
		if not(isinstance(other, feat)): return -1
		return cmp(self.name(), other.name())
	
	def copy(self, setfrom=""):
		ret=feat([x.copy() for x in self.wht], self.named, self.description, self.prereqs)
		if self.specMenu!=None: ret.specMenu=self.specMenu.copy()
		if self.featPick!=None: ret.featPick=self.featPick.copy()
		return ret

class EffectType:
	def __init__(self, effect, aoe=[]):
		self.effect=effect
		if isinstance(effect, list):
			self.effect=[x for x in effect]
		self.aoe=[x for x in aoe]
	
	def setAoe(self, keys, character):
		ret=""
		if self.aoe!=[]:
			ret="\t"+str(res(self.aoe[0], character).capitalize())+" "
			if not isinstance(self.aoe[1], str): ret+=str(res(self.aoe[1], character)+character.modmux(keys, res(self.aoe[0], character).lower()))
			else: ret+=str(res(self.aoe[1], character))
			if len(self.aoe)==3: ret+=" within "+str(res(self.aoe[2], character))+" squares"
		return ret
	
	def finalOut(self, text):
		if text=="": return ""
		ret=""
		while (len(text)>90) and (text[35:].find(" ")!=-1):
			q=text[85:].find(" ")
			ret+="\t"+text[:q+85]+"\n"
			text=text[q+85:]
		return ret+"\t"+text+"\n"

	def htmlOut(self, character, keylist, powerclass, powername):
		keys=[res(x, character) for x in keylist]+[powername]
		while "" in keys:
			keys.remove("")
		ret=""
		if self.aoe!=[]: ret="\n\t\t\t<div id=\"line\"><b>"+self.setAoe(keys+[powerclass], character)+"</b></div>"
		ret+="\n\t\t\t<div id=\"line\">"
		z=""
		for x in self.effect:
			if isinstance(x, TextHelp):
				z+=str(x.result(character, keys, powerclass, powername))
			else:
				q=res(x, character, False)
				if isinstance(q, list):
					for g in q:
						if isinstance(g, TextHelp):
							z+=str(g.result(character, keys, powerclass, powername))
						else: z+=str(g)
				else: z+=str(q)
		if ":" in z: z="<b>"+z[:z.index(":")+1]+"</b>"+z[z.index(":"):]
		return ret+z+"</div>"

	def output(self, character, keylist, powerclass, powername):
		keys=[res(x, character) for x in keylist]+[powername]
		while "" in keys:
			keys.remove("")
		ret=self.setAoe(keys+[powerclass], character)
		if self.aoe!=[]: ret+="\n"
		z=""
		for x in self.effect:
			if isinstance(x, TextHelp):
				z+=str(x.result(character, keys, powerclass, powername))
			else:
				q=res(x, character, False)
				if isinstance(q, list):
					for g in q:
						if isinstance(g, TextHelp):
							z+=str(g.result(character, keys, powerclass, powername))
						else: z+=str(g)
				else: z+=str(q)
		return ret+self.finalOut(z)

	def copy(self):
		return EffectType(self.effect, self.aoe)

class Target(EffectType):
	def __init__(self, target, aoe=[]):
		if isinstance(target, list): self.effect=[x for x in target] 
		else: self.effect=target 
		self.aoe=[x for x in aoe]
	
	def output (self, character, keylist, powerclass, powername):
		keys=[res(x, character) for x in keylist]+[powername]
		ret="\tTarget: "+res(self.effect, character).capitalize()
		ret+=self.setAoe(keys+[powerclass], character)+"\n"
		return ret
	
	def htmlOut (self, character, keylist, powerclass, powername):
		keys=[res(x, character) for x in keylist]+[powername]
		ret="<div class=\"targetbox\">"
		ret+="\n\t\t\t<div id=\"line\" class=\"target\"><b>Target: </b>"+res(self.effect, character).capitalize()+"</div>"
		if self.aoe!=[]:
			ret+="\n\t\t\t<div class=\"aoe\"><b>"+self.setAoe(keys+[powerclass], character)+"</b></div>"
		return ret+"</div>"

	def copy(self):
		return Target(self.effect, self.aoe)

class TextHelp:
	def __init__(self, num, type, dmgdie1=0, dmgdie2=0, dmgtype=[]):
		self.num=num
		self.type=type
		self.dmgdie1=dmgdie1
		self.dmgdie2=dmgdie2
		self.dmgtype=list(dmgtype)
	
	def result(self, char, inkeys, powerclass, powername):
		if self.type=="damage":
			keys=list(inkeys)
			if self.dmgtype!=[]:
				for x in elements:
					if x in keys:
						keys.remove(x)
			dummy=Atk([],"",damage([self.dmgdie1,self.dmgdie2],[self.num]))
			z=dummy.output(char, keys+self.dmgtype, powerclass, powername)
			if z.find(";")==-1: return "0 damage"
			else: return z[z.find(";")+2:-1]
		else:
			retnum=res(self.num, char)
			return retnum+char.modmux(keys+[""],self.type)
	

dmg=lambda y,d1=0,d2=0, dtype=[]: TextHelp(y, "damage",d1,d2, dtype)
heal=lambda y, d1=0, d2=0: TextHelp(y, "healing",d1,d2)

def EffectHelper(text, effect, aoe=[]):
		if isinstance(effect, list):
			ret1=list(effect)
			ret1[0]=text+ret1[0]
		else: 
			ret1=effect
			ret1=text+ret1
		ret2=[x for x in aoe]
		return EffectType(ret1, ret2)

Trigger=lambda y,z=[]: EffectHelper("Trigger: ",y,z)
Hit=lambda y,z=[]: EffectHelper("Hit: ",y,z)
Miss=lambda y="Half damage.",z=[]: EffectHelper("Miss: ",y,z)
Effect=lambda y,z=[]: EffectHelper("Effect: ",y,z)
Special=lambda y,z=[]: EffectHelper("Special: ",y,z)
Line=lambda y,z=[]: EffectHelper("     ",y,z)
Requirement=lambda y,z=[]: EffectHelper("Requirement: ",y,z)
Aftereffect=lambda y,z=[]: EffectHelper("   Aftereffect: ",y,z)
Sustain=lambda x="minor",y="The zone persists.",z=[]: EffectHelper("Sustain "+x+": ",y,z)
Other=lambda x,y=[]: EffectType(x,y)
Augment=lambda x: EffectType("Augment "+str(x))

class Atk(EffectType):
	def __init__(self,stats, vs, damage, keywords=None, legalgroups=[], element="default"):
		self.attackRoll=attack(stats, vs, damage, keywords, legalgroups)
		self.element=element
	
	def output(self, character, keylist, powerclass, powername):
		ret=""
		keys=[res(x, character) for x in keylist]+[powername]
		while "" in keys:
			keys.remove("")
		elementor=False
		if "or" in keys and "weapon" not in keys:
			elementor=True
			keys.remove("or") 
		elementtext=""
		anded=False
		remlist=[]
		if not(elementor):
			for key in keys:
				if key in elements:
					if elementtext=="":
						elementtext=" "+key
					elif not(anded):
						if "or" in keys: elementtext=" "+key+" or"+elementtext
						else: elementtext=" "+key+" and"+elementtext
						anded=True
					else: elementtext=" "+key+","+elementtext
					if "or" in keys: remlist.append(key)
			if "or" in keys:
				for key in remlist: keys.remove(key)
		if self.element!="default": elementtext=" "+self.element
		attacks, ranged=self.attackRoll(character)
		numelements=0
		elemlist=[]
		elemkey=-1
		if elementor:
			tempval=0
			for key in keys:
				if key in elements:
					tempval+=1
					elemlist+=[key]
			if tempval>0 and len(attacks)==1: 
				attacks=attacks*tempval
				for key in elemlist: keys.remove(key)
			else: elemetor=False
		diebonus=[""]*len(attacks)
		for x in xrange(0,len(attacks)):
			if isinstance(attacks[x][2], list):
				diebonus[x]="+"+str(attacks[x][2][1])+"d"+str(attacks[x][3][1])
				attacks[x][2]=attacks[x][2][0]
				attacks[x][3]=attacks[x][3][0]
		diecounter=0
		for value in attacks:
			rangetxt=""
			if powerclass in ["epic","paragon"]: sendkeys=list(keys)+character.statret("checkclass")
			else: sendkeys=list(keys)+[powerclass]
			if elementor: 
				elemkey+=1
				sendkeys+=[elemlist[elemkey]]
			if isinstance(value[5],Item): 
				enchantment=max(value[5].enchantment(), character.statret("weaponenchant"))
				value[0]+=enchantment
				weaponKeys=value[5].desc.charkey(character)
				if value[4]!=None:
					value[4]+=enchantment
					if "equipped" in weaponKeys and "versatile" in weaponKeys and character.inventory.equipped[1]==None: value[4]+=1
				printout="\t"
				if "primary" in weaponKeys: printout+="[Primary] "
				elif "offhand" in weaponKeys: printout+="[Offhand] "
				printout+=value[5].name()+": "
				sendkeys+=weaponKeys
				sendkeys+=value[5].desc.group
				sendkeys.append(value[5].desc.name+"name")
				if ranged and "ranged" in weaponKeys:
					if "heavy thrown" in weaponKeys or "light thrown" in weaponKeys: rangebonus=character.statret("throwndistance")
					else: rangebonus=character.statret("rangeddistance") 
					rangetxt=" (Ranged "+str(value[5].desc.rng[0]+rangebonus)+"/"+str(value[5].desc.rng[1]+rangebonus)+")"
			elif not(elementor): printout="Attack: "
			else: printout="\t"+elemlist[elemkey]+":"
			attbonus=value[0]+character.modmux(sendkeys+[""], "attack")
			if attbonus>-1: printout+="+"
			printout+=str(attbonus)+" vs. "+res(value[1],character)
			if value[2]!=None: mux=value[2]+character.modmux(sendkeys+[""], "mux")
			else: mux=0
			if value[3]!=None: dice=value[3]+character.modmux(sendkeys+[""], "dice")
			else: dice=0
			if value[4]!=None: dmgbonus=value[4]+character.modmux(sendkeys+[""], "damage")
			else: dmgbonus=0
			if (mux!=0) or (dmgbonus!=0): printout+="; "
			if mux!=0:printout+=str(mux)+"d"+str(dice)
			printout+=diebonus[diecounter]
			diecounter+=1
			if (dmgbonus<0) or ((mux==0) and (dmgbonus!=0)): printout+=str(dmgbonus)
			elif dmgbonus>0: printout+="+"+str(dmgbonus)
			if elementor: elementtext=" "+elemlist[elemkey]
			if (mux!=0) or (dmgbonus!=0): printout+=elementtext+" damage"
			printout+=rangetxt+"\n"
			ret+="\t"+printout
		return ret

	def copy(self):
		ret=Atk([],"",None)
		ret.attackRoll=self.attackRoll
		ret.element=self.element
		return ret

class Power:
	def __init__(self, name, keys, often, action, effects=[], powerclass="", powerSource="", powerlevel=0):
		self.named=name
		self.keys=list(keys)
		self.often=often
		self.action=action
		self.effects=[x.copy() for x in effects]
		self.powerclass=powerclass
		self.powersource=powerSource
		self.powerlevel=powerlevel
		
	def name(self):
		return self.named
	
	def keys(self):
		return self.keys
	
	def often(self):
		return self.often
	
	def action(self):
		return self.action
	
	def effects(self):
		return self.effects
	
	def pSource(self):
		ret=self.powerclass.title()
		if ret !="" and self.powersource!="": ret+=" "+self.powersource
		else: ret=self.powersource.title()
		if ret !="" and self.powerlevel>0: ret+=" "+str(self.powerlevel)
		return ret

	def output(self, character, namerow=True):
		ret=""
		often=character.featureis(self.name().lower()+"often")
		if often=="": often=self.often
		action=character.featureis(self.name().lower()+"action")
		if action=="": action=self.action
		if namerow:
			ret+=self.name().ljust(40)+" "
			for key in self.keys+sorted(character.featurestr(self.name().lower()+"addkey")):
				ret+=res(key, character).capitalize()+" "
			ret+="\n"
		ret+="\t"+often.capitalize()+"\t"+action.capitalize()
		if action not in ["immediate reaction","immediate interrupt"]:
			ret+=" action"
		ret+="\n"
		for effect in self.effects: 
			ret+=effect.output(character, self.keys+character.featurestr(self.name().lower()+"addkey"), self.powerclass, self.name().lower())
		if not namerow and ret[-1]=="\n": ret=ret[:-1] 
		return ret

	def htmlOut(self, character, nameOnly=False):
		often=character.featureis(self.name().lower()+"often")
		if often=="": often=self.often
		action=character.featureis(self.name().lower()+"action")
		if action=="": action=self.action
		ret=""
		if not nameOnly: ret="\n\t\t<div class=\"power "+often+"\">"
		ret+="\n\t\t\t<div class=\""+often+"BG title\">"+"\n\t\t\t\t<div class=\"left\"> "+self.name()+"</div>\n\t\t\t\t<div class=\"right\">"+self.pSource()+"</div>\n\t\t\t</div>"
		if nameOnly: return ret
		ret+="\n\t\t\t<div class=\"left\">"+often.capitalize()+" <b>(+)</b> "
		for x in self.keys+character.featurestr(self.name().lower()+"addkey"):
		  ret+=x.capitalize()+" "
		ret+="</div><div class=\"right\">"+action.capitalize()
		if action not in ["immediate reaction","immediate interrupt"]:
			ret+=" action"
		ret+="</div>"
		for effect in self.effects:
			if isinstance(effect,Atk): ret+="\n\t\t\t<div id=\"line2\" colspan=2>"+effect.output(character, self.keys+character.featurestr(self.name().lower()+"addkey"), self.powerclass, self.name().lower()).replace("\t","").replace("\n","</div>\n\t\t\t<div id=\"line2\" colspan=2>")+"</div>"
			else: ret+=effect.htmlOut(character, self.keys+character.featurestr(self.name().lower()+"addkey"), self.powerclass, self.name().lower())
		return ret+"\n\t\t</div>"

	def copy(self):
		return Power(self.named, self.keys, self.often, self.action, self.effects, self.powerclass, self.powersource, self.powerlevel)
	
	def __cmp__(self, othr):
		if (self.powersource=="item" or othr.powersource=="item") and self.powersource!=othr.powersource: return othr.powersource=="item"
		return cmp(self.name(),othr.name())

class charClass:
	def __init__(self, hp, levelhp, surgenum, features=[0,0,0,0],prof=[], skillList=[]):
		self.hp=hp
		self.levelhp=levelhp
		self.surgenum=surgenum
		self.prof=prof
		self.skillList=skillList
		self.features=features

class choosestat:
	def __init__(self, power, choices, makefeat=True):
		self.power=power
		self.choices=choices
		self.makefeat=makefeat
	def __call__(self, character):
		if not(character.check("feature","stat for "+self.power)):
			if self.makefeat:
				ftlist=[feat([ft("choosestat"+self.power,x)]) for x in self.choices]
				character.addFeat(feat([specialMenu(self.choices,ftlist)],"Stat for "+self.power))
			return character.mod(self.choices[0])
		return character.mod(character.statret("choosestat"+self.power))