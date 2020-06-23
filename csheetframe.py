from __future__ import with_statement
from types import *
from scrolled import *
from class4th import *
from dircache import *
from tkFileDialog import *

class EntryBox(Toplevel):
	def __init__(self, parent, title, width, default=""):
		Toplevel.__init__(self, parent)
		self.transient(parent)
		self.title(title)
		self.parent=parent
		self.grab_set()
		self.entryVar=Entry(self, width=width)
		self.entryVar.insert(0, default)
		self.entryVar.focus_set()
		self.entryVar.grid(row=0, column=0)
		self.entryVar.focus_set()
		Button(self, text="OK", command=self.clickOK).grid(row=0, column=1)
		Button(self, text="Cancel", command=self.destroy).grid(row=0, column=2)
		self.retvar=None
		def hitEnter(*args):
			self.clickOK()
		def hitEscape(*args):
			self.destroy()
		self.bind("<Return>",hitEnter)
		self.bind("<Escape>",hitEscape)
	
	def clickOK(self):
		self.retvar=self.entryVar.get()
		self.destroy()
	
	def runit(self):
		self.wait_window(self)
		return self.retvar

class ConfigMenu(Toplevel):
	def __init__(self, parent):
		Toplevel.__init__(self, parent)
		self.transient(parent)
		self.title("Configure Options")
		self.grab_set()
		frame=Frame(self)
		frame.grid()

		Label(frame, text="Button Relief:").grid(row=0, column=0)
		relief=Menubutton(frame, text=RELIEF).grid(row=0, column=1)
		relief.menu=Menu(relief, tearoff=0)
		relief["menu"]=relief.menu
		for x in [FLAT, GROOVE, RIDGE, SUNKEN, RAISED]:
			relief.menu.add_command(text=x, command=self.setRelief(x))
		
		addBar.menu=self.createAddMenu(addBar)
		addBar["menu"]=addBar.menu

		Label(frame, text="Option changes will take effect next time the program is run.").grid()
	
	def setRelief(self, val):
		RELIEF=val

def makeCascade(theDict, themenu, theclicky):
			for entry in sorted(theDict.keys()):
				if isinstance(theDict[entry], dict):
					themenu.add_cascade(label=entry, menu=makeCascade(theDict[entry], Menu(themenu, tearoff=0),theclicky))
				else: themenu.add_command(label=entry, command=theclicky(theDict[entry]))
			return themenu

class CsheetFrame:
	def __init__(self, master, character=None):
		self.root=master
		self.master=Scrolledframe(master, width=640, height=480)

		self.filename=None

		self.yscroll=Scrollbar(master, orient="vertical", command=self.master.yview)
		self.yscroll.grid(row=0, column=1, rowspan=120, sticky="nwse")
		self.xscroll=Scrollbar(master, orient="horizontal", command=self.master.xview)
		self.xscroll.grid(row=1, column=0, sticky="nwse")

		self.master["yscrollcommand"]=self.yscroll.set
		self.master["xscrollcommand"]=self.xscroll.set
		def scroll_up(event):
			self.master.update_scrollregion()
			if event.delta<0 or event.delta==40:
				self.master.yview("scroll", 5, "units")
			else:
				self.master.yview("scroll", -5, "units")
		def home(event):
			self.master.update_scrollregion()
			self.master.yview("moveto", 0.0)
		def end(event):
			self.master.update_scrollregion()
			self.master.yview("moveto", 1.0)
		master.bind("<Control-s>",self.save)
		master.bind("<MouseWheel>",scroll_up)
#		master.bind("<Home>",home)
#		master.bind("<End>",end)
#		master.bind("<Prior>",home)
#		master.bind("<Next>",end)
#		master.bind("<Up>", scroll_up)
#		master.bind("<Down>", scroll_up)
	
		master.columnconfigure(0,weight=1)
		master.rowconfigure(0,weight=1)

		self.master.grid(row=0, column=0, sticky="nwse")
		self.char=character
                self.sub=None
                self.createSub()

		self.char=character
		menubar = Menu(master)
		filemenu=Menu(menubar, tearoff=0)
		editmenu=Menu(menubar, tearoff=0)
		optionsmenu=Menu(menubar, tearoff=0)
		#loadlist=Menu(filemenu, tearoff=0)
		filelist=listdir("save"+os.sep)
		#def load(file):
		#	def clickit():
		#		self.load(file[:-4])
		#	return clickit

		#for x in filelist:
		#	if x[-4:]==".csh":
		#		loadlist.add_command(label=x, command=load(x))
		#filemenu.add_cascade(menu=loadlist, label="Load")
		filemenu.add_command(label="Load", command=self.load)
		filemenu.add_command(label="Save", command=self.save)
		filemenu.add_command(label="Save as...", command=self.saveAs)
		filemenu.add_separator()
		filemenu.add_command(label="Quit",command=self.root.destroy)
		editmenu.add_command(label="Rename", command=self.rename)
		setLevelLambda=lambda x: lambda: self.setLevel(x)		
		setRaceLambda=lambda x: lambda: self.setRace(races[x])
		setClassLambda=lambda x: lambda: self.setClass(x)

		menubar.add_cascade(label="File", menu=filemenu)


		self.statboosts=[None,None,None,None,None,None,None,None,None,None,None,None]

		master.config(menu=menubar)

		self.nameLabel=self.makeAmenu(self.master(), "", 1, 1)
		self.nameLabel.menu.add_command(label="Rename", command=self.rename)
		
		self.levelLabel=self.makeAmenu(self.master(), "", 1, 2)
		for i in range(1,31):
			self.levelLabel.menu.add_command(label=i,command=setLevelLambda(i))
		
		editmenu.add_cascade(label="Set Level", menu=self.levelLabel.menu)

		self.raceLabel=self.makeAmenu(self.master(),"Choose Race", 1, 3)
		self.raceLabel.config(fg="darkred")
		for i in range(0, len(races)):
			self.raceLabel.menu.add_command(label=races[i], command=setRaceLambda(i))		
		
		editmenu.add_cascade(label="Choose Race", menu=self.raceLabel.menu)
		
		self.classLabel=self.makeAmenu(self.master(),"Choose Class", 1, 4)
		self.classLabel.config(fg="darkred")
		for oneClass in sorted(classes):
			self.classLabel.menu.add_command(label=oneClass, command=setClassLambda(oneClass))
		
		editmenu.add_cascade(label="Choose Class", menu=self.classLabel.menu)
		
		self.sizeOriginTypeLabel=Label(self.master())
		self.sizeOriginTypeLabel.grid(sticky="w",pady=0,  row=1,column=7)

		self.paragonLabel=Menu(self.master())
		self.epicLabel=Menu(self.master())
		rownum=2
		self.initLabel=Label(self.master())
		self.initLabel.grid(sticky="w",pady=0,  row=rownum, column=1, columnspan=10)
		rownum+=1
		self.hpLabel=Label(self.master())
		self.hpLabel.grid(sticky="w",pady=0,  row=rownum, column=1, columnspan=10)
		rownum+=1
		self.defensesLabel=Label(self.master())
		self.defensesLabel.grid(sticky="w",pady=0,  row=rownum, column=1, columnspan=10)
		rownum+=1
		self.speedLabel=Label(self.master())
		self.speedLabel.grid(sticky="w",pady=0,  row=rownum, column=1, columnspan=10)
		rownum+=1
		self.statFrame=Frame(self.master())
		self.statframerownum=rownum
		rownum+=1
 		
#		self.statbuyButton=Button(self.master(), text="Statpoints", command=self.pickStats,relief=GROOVE, fg="blue")
# 		self.statbuyButton.grid(sticky="w", row=rownum, column=2)
# 		self.statlevelButton=Button(self.master(), text="Level Stats", command=self.setStatboosts,relief=GROOVE, fg="blue")
# 		self.statlevelButton.grid(sticky="w", row=rownum, column=3, columnspan=10)

 		editmenu.add_command(label="Spend Statpoints", command=self.pickStats)
 		editmenu.add_command(label="Level Stats", command=self.setStatboosts)
 		rownum+=1
		
		self.feats=Frame(self.master())
		self.featrownum=rownum
		rownum+=1
		Label(self.master(), text="Wealth").grid(row=rownum, column=1)
		Label(self.master(), text="Inventory").grid(row=rownum, column=3)
		addBar=Menubutton(self.master(), text="Add Items", fg="blue", relief=RELIEF, cursor=SELECTCURSOR)
		addBar.grid(row=rownum, column=4, sticky="w", columnspan=10)
		addBar.menu=self.createAddMenu(addBar)
		addBar["menu"]=addBar.menu
		self.createAddMenu(editmenu)
		
		rownum+=1
		self.inven=Frame(self.master())
		self.invenrownum=rownum
		self.cash=[StringVar() for x in list(WEALTHTYPES)]			
		rownum+=1
		
		self.beastlabel=Label(self.master())
		self.beastlabel.grid(sticky="nw",row=rownum, column=1, columnspan=10)
		self.beastlabel.config(justify="left")
		rownum+=1

		self.powers=Frame(self.master())
		self.powerrownum=rownum
		rownum+=1
		Label(self.master(), text="Notes:", anchor="w").grid(row=rownum, column=1)
		
		rownum+=1
		self.textbox=Text(self.master(),height=2, width=50, wrap=WORD)
		self.textbox.grid(sticky="nw", row=rownum, column=1, columnspan=10)
		self.textbox.bind("<Key>",self.addTextLines)
		
		self.showpowers=[1, 1, 1, 1, 1]
		self.hiddenPowers=[]
		legalFeats=[]

		self.char.showmods=IntVar()
		self.char.showmods.set(1)
		optionsmenu.add_checkbutton(label="Show stat mods", variable=self.char.showmods, command=self.update)
		menubar.add_cascade(label="Edit", menu=editmenu)
		menubar.add_cascade(label="Options", menu=optionsmenu)
		if character!=None:
			self.update()

##############Core Stuff####################		
	def addTextLines(self, event=""):
		bottom=False
		if self.master.client_y <= self.master.H-self.master.client_h:
			bottom=True
		self.textbox.config(height=float(self.textbox.index(END)))
		if bottom:
			self.master.update_scrollregion()
			self.master.yview("moveto", 1.0)

	def rename(self, event=None):
		ret=EntryBox(self.root, "Rename",20).runit()
		if ret!=None: self.char.name=ret
		self.update()
	
	def destroySub(self):
		if self.sub.children=={}:
			self.sub.destroy()
			self.createSub()
	def createSub(self):
		self.sub=Frame(self.master())
		self.sub.grid(row=0, column=0, rowspan=50, sticky="n")

	def makeAmenu(self, root, thetext, rownum, columnnum, colspan=1):
		ret=Menubutton(root, text=thetext, fg="blue", relief=RELIEF, cursor=SELECTCURSOR)
		ret.grid(row=rownum, column=columnnum, sticky="w", columnspan=colspan)
		ret.menu=Menu(ret, tearoff=0)
		ret["menu"]=ret.menu
		return ret

	def update(self):
		self.char.fastlookup={}
		self.char.setQuicklook()
		self.legalFeats=[]
		self.nameLabel.config(text=self.char.name)
		if self.char.race!="": self.raceLabel.config(fg="blue")
		if self.char.charclass!="": self.classLabel.config(fg="blue")
		self.levelLabel.config(text="Level "+str(self.char.statret("level")))
		if self.char.statret("race")<>"":
			self.raceLabel.config(text=self.char.statret("race").capitalize())
		if self.char.statret("class")<>"":
			self.classLabel.config(text=self.char.statret("class").capitalize())
		self.sizeOriginTypeLabel.config(text=self.char.statret("size").capitalize()+" "+self.char.statret("origin").capitalize()+" "+self.char.statret("type").capitalize())
		self.setPrestigeLabel("paragon")
		self.setPrestigeLabel("epic")
		initval="Initiative:"+" "+str(self.char.statret("initiative"))
		initval+=" \tSenses: Perception +"+str(self.char.statret("perception"))
		for x in self.char.statret("vision"):
			initval+="; "+x.capitalize()+" vision"

		self.initLabel.config(text=initval)
		hpval=""
		if self.char.statret("class")!="":
			hpval="HP: "+str(self.char.statret("hp"))+"; Bloodied: "+str(self.char.statret("hp")/2)+"; Surge:"+str(self.char.statret("surge"))+"; Per day: "+str(self.char.statret("surges"))
		self.hpLabel.config(text=hpval)
		defensesval="AC: "+str(self.char.statret("ac"))+"; Fortitude: "+str(self.char.statret("fort"))+"; Reflex: "+str(self.char.statret("ref"))+"; Will: "+str(self.char.statret("will"))

		self.defensesLabel.config(text=defensesval)
		self.speedLabel.config(text="Speed: "+str(self.char.statret("speed")))

		self.statFrame.destroy()
		self.statFrame=Frame(self.master())
		self.statFrame.grid(sticky="w",pady=0,  row=self.statframerownum, column=1, columnspan=10)
		self.skillLabel=Label(self.statFrame, justify="left", text="Skills:")
                self.skillLabel.grid(sticky="w",pady=0, row=0, column=0)
		self.statLabel=Label(self.statFrame, justify="left")
		self.statLabel.grid(sticky="w",pady=0,  row=3, column=0, columnspan=10)
		def clicky(newchoice, theskillpick, theindex):
			def clickit():
				theskillpick.chosen[theindex]=theskillpick.skillChoices.index(newchoice)
				self.update()
			return clickit
		spMenus=[]
		pickedSkills=[]
		pickedSkillpicks=[]
		theColumn=1
		trainedskills=self.char.statret("training")
		for skillpick in self.char.statret("skillpick"):
				chosenIndex=0
				g=skillpick.classskills
				if g=="classskills": g=self.char.statret("class")
				if g!="":
					if [x.lower() for x in classList[g.title()].skillList]<>skillpick.skillChoices:
						skillpick.skillChoices=[x.lower() for x in classList[g.title()].skillList]
						skillpick.chosen=[-1 for x in skillpick.chosen]
				for chosen in skillpick.chosen:
					if chosen==-1:
						spMenus.append(Menubutton(self.statFrame, text=skillpick.basename.title(), fg="darkred", relief=RELIEF, cursor=SELECTCURSOR))
						spMenus[-1].grid(row=0, column=theColumn, sticky="w")
						spMenus[-1].menu=Menu(spMenus[-1], tearoff=0)
						spMenus[-1]["menu"]=spMenus[-1].menu
						for newChosen in skillpick.skillChoices:
							if newChosen.lower() not in trainedskills:
	                                			spMenus[-1].menu.add_command(label=newChosen.title(), command=clicky(newChosen, skillpick, chosenIndex))
						theColumn+=1
					if chosen<>-1 and skillpick.needmenu:
						pickedSkills.append(skillpick.skillChoices[chosen].lower())
						pickedSkillpicks.append(skillpick)
					chosenIndex+=1
		skillLabels=[]
		numskills=0
		skillrow=0
		for x in sorted(allskills.keys()):
			if self.char.featuretotal(x)>0:
				numskills+=1
				if numskills==9:
					skillrow+=1
					theColumn=1
				if x not in pickedSkills:
					skillLabels.append(Label(self.statFrame, text=x.title()+" +"+str(self.char.statret(x))))
					skillLabels[-1].grid(row=skillrow, column=theColumn, sticky="w")
					theColumn+=1
				else:
					skillLabels.append(Menubutton(self.statFrame, text=x.title()+" +"+str(self.char.statret(x)), fg="blue", relief=RELIEF, cursor=SELECTCURSOR))
					skillLabels[-1].grid(row=skillrow, column=theColumn, sticky="w")
					skillLabels[-1].menu=Menu(skillLabels[-1], tearoff=0)
					skillLabels[-1]["menu"]=skillLabels[-1].menu
					skillpick=pickedSkillpicks[pickedSkills.index(x)]
					chosenIndex=skillpick.chosen.index(skillpick.skillChoices.index(x.lower()))
					for newChosen in skillpick.skillChoices:
						if newChosen.lower() not in trainedskills:
							skillLabels[-1].menu.add_command(label=newChosen, command=clicky(newChosen, skillpick, chosenIndex))
					theColumn+=1

		self.updateStats()
		self.updateLegalFeats()
		self.getPowerLabels()
		self.getFeatLabels()
		self.setInventory()
		self.beastlabel.config(text=self.char.beasttext())

	def wrapup(self):
		self.master.wait_window(self.master)

##############Stats Stuff####################
	def setClass(self, theClass):
		self.char.miniAttach(theClass)
		self.update()

	def setRace(self, theRace):
		self.char.attachRace(theRace)
		self.update()

	def setLevel(self, level):
		if self.char==None: return 0
		self.char.level=level
		self.char.fastlookup["level"]=level
		self.levelupStatboosts()
		self.update()

	def levelupStatboosts(self):
		for x in [4,8,11,14,18,21,24,28]:
			self.char.remFeat("statboost"+str(x))
		if self.char.statret("level")>3: self.char.addFeat(feat([ft(self.statboosts[0], ["",1]),ft(self.statboosts[1], ["",1])],"statboost4"))
		if self.char.statret("level")>7: self.char.addFeat(feat([ft(self.statboosts[2], ["",1]),ft(self.statboosts[3], ["",1])],"statboost8"))
		if self.char.statret("level")>10: self.char.addFeat(feat([ft("str", ["",1]),ft("con", ["",1]),ft("dex", ["",1]),ft("int", ["",1]),ft("wis", ["",1]),ft("cha", ["",1])],"statboost11"))
		if self.char.statret("level")>13: self.char.addFeat(feat([ft(self.statboosts[4], ["",1]),ft(self.statboosts[5], ["",1])],"statboost14"))
		if self.char.statret("level")>17: self.char.addFeat(feat([ft(self.statboosts[6], ["",1]),ft(self.statboosts[7], ["",1])],"statboost18"))
		if self.char.statret("level")>20: self.char.addFeat(feat([ft("str", ["",1]),ft("con", ["",1]),ft("dex", ["",1]),ft("int", ["",1]),ft("wis", ["",1]),ft("cha", ["",1])],"statboost21"))
		if self.char.statret("level")>23: self.char.addFeat(feat([ft(self.statboosts[8], ["",1]),ft(self.statboosts[9], ["",1])],"statboost24"))
		if self.char.statret("level")>27: self.char.addFeat(feat([ft(self.statboosts[10], ["",1]),ft(self.statboosts[11], ["",1])],"statboost28"))

	def updateStats(self):
		statlist=["str","dex","wis","con","int","cha"]
		stattxt=""
		for stat in statlist: 
			stattxt+=stat.capitalize()+": "+str(self.char.statret(stat)).ljust(4)+"("+str(self.char.mod(stat))+")"
			if stat=="wis": stattxt+="\n"
			else: stattxt+="\t"
		
		self.statLabel.config(text=stattxt) 
 
	def pickStats(self):
		if self.char==None: pass
		statlist=["str","con","dex","int","wis","cha"]

		buttons=[]
		
		buttonFrame=Frame(self.sub)
		pointsLabel=Label(buttonFrame)
		pointsLabel.grid(row=0)
		pLabelUpdate=lambda: pointsLabel.config(text="You have "+str(self.char.points)+" points remaining")
		pLabelUpdate()

		okButton=Button(buttonFrame, text="Done", command=buttonFrame.destroy, state=DISABLED)
		okButton.grid(row=1)
		if self.char.points==0: okButton.config(state=NORMAL)

		def plusit(st):
			def plus():
				try: del self.char.fastlookup["core"+st]
				except: pass
				try: del self.char.fastlookup[st]
				except: pass

				cost=1
				if(self.char.statret("core"+st)>12):cost+=1
				if(self.char.statret("core"+st)>15):cost+=1
				if(self.char.statret("core"+st)>16):cost+=1
				if(self.char.statret("core"+st)>17):cost+=2000
				if cost<=self.char.points:
					self.char.points=self.char.points-cost
					self.char.statmod(st, 1)
					self.updateStats()
					pLabelUpdate()
				if self.char.points==0: okButton.config(state=NORMAL)
			return plus

		def minusit(st):
			def minus():
				try: del self.char.fastlookup["core"+st]
				except: pass
				try: del self.char.fastlookup[st]
				except: pass
				cost=-1
				if (self.char.statret("core"+st)>13):cost-=1
				if (self.char.statret("core"+st)>16):cost-=1
				if (self.char.statret("core"+st)>17):cost-=1
				if (self.char.statret("core"+st)>18):cost-=2000
				if (self.char.statret("core"+st)>10) or (self.char.statret("core"+st)>8 and self.char.statret("core"+st)==min(self.char.stats)):
					self.char.points=self.char.points-cost
					self.char.statmod(st, -1)
					self.updateStats()
					pLabelUpdate()
					if self.char.points>0: okButton.config(state=DISABLED)
			return minus
		gridrow=1
		for stat in statlist:
			gridrow=gridrow+1
			buttons.append(Frame(buttonFrame))
			Button(buttons[-1],width=5, text=stat+"+", command=plusit(stat)).grid(row=0, column=0)
			Button(buttons[-1],width=5, text=stat+"-", command=minusit(stat)).grid(row=0, column=1)
			buttons[-1].grid(row=gridrow)
		buttonFrame.grid()
		self.sub.wait_window(buttonFrame)
		self.destroySub()
		self.update()
		
	def setStatboosts(self):
		if self.char==None: return 0
		statlist=["str","con","dex","int","wis","cha"]
		
		buttons=[]
		
		buttonFrame=Frame(self.sub)

		okButton=Button(buttonFrame, text="Done", command=buttonFrame.destroy)
		okButton.grid(row=0)


		LvlMenus=[]
		
		def clicky(st, num):
			def clickit():
				if (num%2==1):
					if self.statboosts[num-1]==st: return 0
				if (num%2==0):
					if self.statboosts[num+1]==st: return 0
				self.statboosts[num]=st
				LvlMenus[num].config(text=st)
			return clickit
		
		for i in range(0, 12):
			LvlMenus.append(Menubutton(buttonFrame, text=str(self.statboosts[i]), relief=RAISED, width=4,cursor=SELECTCURSOR))
			LvlMenus[i].menu=Menu(LvlMenus[i], tearoff=0)
			LvlMenus[i]["menu"]=LvlMenus[i].menu
			LvlMenus[i].grid(row=i/2+1, column=i%2+1)
			for stat in statlist:
				LvlMenus[i].menu.add_command(label=stat, command=clicky(stat, i))
			

		Label(buttonFrame, text="Level 4 stat boosts:").grid(row=1, column=0)
		Label(buttonFrame, text="Level 8 stat boosts:").grid(row=2, column=0)
		Label(buttonFrame, text="Level 14 stat boosts:").grid(row=3, column=0)
		Label(buttonFrame, text="Level 18 stat boosts:").grid(row=4, column=0)
		Label(buttonFrame, text="Level 24 stat boosts:").grid(row=5, column=0)
		Label(buttonFrame, text="Level 28 stat boosts:").grid(row=6, column=0)

		buttonFrame.grid()
		self.sub.wait_window(buttonFrame)
		self.levelupStatboosts()
		self.update()
		self.destroySub()

##############Paragon Stuff####################
	def legalPrestige(self, list):
		ret=[]
		for x in list.keys():
			if list[x].preReqs(self.char):
				ret.append(x)
		return sorted(ret)
	
	def setPrestigeLabel(self, prestige):
		def clicky(newChosen):
			def clickit():
				self.char.remFeat(prestige)
				self.char.addFeat(newChosen)
				self.update()
			return clickit

		def makeMenu(e):
			paraLabel=self.char.statret("paragonname")
			if paraLabel=="":
				paraLabel="paragon"
			legal = self.legalPrestige(paragonList)
			self.paragonLabel.destroy()
			self.paragonLabel=self.makeAmenu(self.master(), paraLabel.title(), 1, 5)
			if paraLabel.title()=="Paragon": self.paragonLabel.config(fg="darkred")
			self.paragonLabel["menu"]=self.paragonLabel.menu
			for newChosen in legal:
				self.paragonLabel.menu.add_command(label=newChosen,command=clicky(paragonList[newChosen]))

		def makeEpicMenu(e):
			paraLabel=self.char.statret("epicname")
			if paraLabel=="":
				paraLabel="epic"
			legal = self.legalPrestige(epicList) 
			self.epicLabel.destroy()
			self.epicLabel=self.makeAmenu(self.master(), paraLabel.title(), 1, 6)
			if paraLabel.title()=="Epic": self.epicLabel.config(fg="darkred")
			self.epicLabel["menu"]=self.epicLabel.menu
			for newChosen in legal:
				self.epicLabel.menu.add_command(label=newChosen,command=clicky(epicList[newChosen]))

		paraLabel=self.char.statret(prestige+"name")
		if paraLabel=="":
			paraLabel=prestige

		if prestige=="paragon":
			self.paragonLabel.destroy()
			if self.char.level<11: 
				self.paragonLabel=Menu(self.master())
			else:
				self.paragonLabel=self.makeAmenu(self.master(), paraLabel.title(), 1, 5)
				if paraLabel.title()=="Paragon": self.paragonLabel.config(fg="darkred")
				self.paragonLabel.bind("<Button-1>", makeMenu)
		else:
			self.epicLabel.destroy()
			if self.char.level<21: 
				self.epicLabel=Menu(self.master())
			else:
				self.epicLabel=self.makeAmenu(self.master(), paraLabel.title(), 1, 6)
				if paraLabel.title()=="Epic": self.epicLabel.config(fg="darkred")
				self.epicLabel.bind("<Button-1>", makeEpicMenu)
       		


##############Feat Stuff####################
	def updateLegalFeats(self):
		"helper function for feat.nameLabel()"
		if self.legalFeats==[]:
			ret=[]
			for z in sorted(allFeatDict.keys()):
				q=[]
				for x in allFeatDict[z].values():
					if x.preReqs(self.char) and (not(self.char.check("feature",x.name().lower())) or x.name().lower() in repeatableFeats):
						q.append(x)
				q=sorted(q)
				q.append(z)
				ret.append(q)
			self.legalFeats=ret

	def getFeatLabels(self):
		"part of update(), displays feats"
		self.feats.destroy()
		self.feats=Frame(self.master(), bd=1, relief=RAISED)
		self.feats.grid(sticky="w",pady=0, row=self.featrownum, column=1, columnspan=10)
		def clicky(newChoice, theFeature):
			def clickit():
				theFeature.resolve.chosen=newChoice
				self.update()
			return clickit
		def clicky2(newChoice, theFeatPick):
			def clickit():
				theFeatPick.chosen=newChoice
				self.update()
			return clickit
		rownum=0
		for theFeat in self.char.ftrs+self.char.inventory.feats():
			pgon=False
			if theFeat.name() in ["paragon", "epic"]:
				theFeats=theFeat.what()[0].resolve
				pgon=True
			else:
				theFeats=[theFeat]
			for feat in theFeats:
				if ((feat.string(self.char)!="") or (feat.featPick<>None)) and (feat.levelReq()<=self.char.statret("level")):
					if feat.name()[:8]=="Stat for" and feat.name()[9:] not in self.char.statret("power"):
						self.char.remFeat(feat.name())
					elif not(pgon and not(feat.preReqs(self.char))):
						feat.nameLabel(self.feats, rownum, 0, self)
						feat.descLabel(self.feats, rownum, 1, self)
						rownum+=1
##############Power Stuff####################
	def resetPowerCounter(self):
		"Helper function for getPowerLabels"
		for x in range(0, len(self.showpowers)):
			if self.showpowers[x]<>0: self.showpowers[x]/=self.showpowers[x]
		charpowers=self.char.statret("power")
		rem=[]
		for x in self.hiddenPowers:
			if x.lower() not in charpowers: rem.append(x)
		for x in rem:
			self.hiddenPowers.remove(x)

	def getPowerLabels(self):
		"part of update(), displays the powers"
		self.powers.destroy()
		self.powers=Frame(self.master())
		self.powers.grid(sticky="w", pady=0, row=self.powerrownum, column=1, columnspan=10)
		def clicky(thePower):
			def clickit(args):
				if thePower in self.hiddenPowers: self.hiddenPowers.remove(thePower)
				else: self.hiddenPowers.append(thePower)
				self.update()
			return clickit

		def clicky2(newchoice, thepowerpick):
			def clickit():
				thepowerpick.chosen=thepowerpick.powerChoices.index(newchoice)
				self.update()
			return clickit

		rownum=0
		Menubuttons=[]
		powerBoxes=[]
		powerBoxes.append(Frame(self.powers,bd=1,relief=RAISED)) #Channel Divinity
		powerBoxes.append(Frame(self.powers,bd=1,relief=RAISED)) #At-Will
		powerBoxes.append(Frame(self.powers,bd=1,relief=RAISED)) #Encounter
		powerBoxes.append(Frame(self.powers,bd=1,relief=RAISED)) #Daily
		unpickedBox=Frame(self.powers, bd=1, relief=RAISED)
		self.resetPowerCounter()

		pickedPowers=[]
		pickedPowerpicks=[]
		unpickedRow=0
		pMenus=[]
		for powerpick in self.char.statret("powerpick"):
			if powerpick.classPower:
				if len(self.char.statret("checkclass"))>1 and (powerpick.specialPower in self.char.statret("replacepower")) or (powerpick.basename.lower() in self.char.statret("replacepower")):
					powerPicks=self.char.statret(self.char.statret("checkclass")[1].lower()+powerpick.specialPower)
					if powerPicks==0:
						if "encounter" in powerpick.specialPower:
							powerPicks=self.char.statret(self.char.statret("checkclass")[1].lower()+powerpick.specialPower.replace("encounter","at-will"))
						elif "at-will" in powerpick.specialPower:
							powerPicks=self.char.statret(self.char.statret("checkclass")[1].lower()+powerpick.specialPower.replace("at-will","encounter"))
				elif powerpick.specialPower=="paragonmulticlass":
					multiclass=self.char.statret("checkclass")[1].lower()
					if powerpick.basename=="Multiclass At-Will":
						powerPicks=self.char.statret(multiclass+"at-will")
					elif powerpick.basename=="Multiclass Encounter":
						powerPicks=self.char.statret(multiclass+"encounter1")+self.char.statret(multiclass+"encounter3")+self.char.statret(multiclass+"encounter7")
					elif powerpick.basename=="Multiclass Utility":
						powerPicks=self.char.statret(multiclass+"utility2")+self.char.statret(multiclass+"utility6")+self.char.statret(multiclass+"utility10")
					elif powerpick.basename=="Multiclass Daily":
						powerPicks=self.char.statret(multiclass+"daily1")+self.char.statret(multiclass+"daily5")+self.char.statret(multiclass+"daily9")+self.char.statret(multiclass+"daily15")+self.char.statret(multiclass+"daily19")
				else:
					powerPicks=[]
					if powerpick.specialPower[0]=="a": type="at-will"
					elif powerpick.specialPower[0]=="e": type="encounter"
					elif powerpick.specialPower[0]=="d": type="daily"
					elif powerpick.specialPower[0]=="u": type="utility"
					for x in self.char.statret(type+"powerchoices"):
						if self.char.statret(x.lower()+powerpick.specialPower)!=0:
							powerPicks+=self.char.statret(x.lower()+powerpick.specialPower)
				if powerPicks!=[]:
					if powerPicks<>powerpick.powerChoices:
						powerpick.powerChoices=[x for x in powerPicks]
						powerpick.chosen=-1
			if (powerpick.chosen==-1) and (self.char.statret("level")>=powerpick.levelReq) and (self.char.statret("level")<powerpick.maxLevel):
				unpickedBox.grid(row=0, column=0, columnspan=10, sticky="w")
				pMenus.append(self.makeAmenu(unpickedBox, powerpick.basename, unpickedRow, 0))
				pMenus[-1].config(fg="darkred")
				for newChosen in sorted(powerpick.powerChoices):
					if newChosen.name().lower() not in self.char.statret("power"):
						pMenus[-1].menu.add_command(label=newChosen.name(), command=clicky2(newChosen, powerpick))
			elif (self.char.statret("level")>=powerpick.levelReq) and (self.char.statret("level")<powerpick.maxLevel):
				pickedPowers.append(powerpick.powerChoices[powerpick.chosen].name())
				pickedPowerpicks.append(powerpick)
			unpickedRow+=1

		for power in sorted(list(self.char.powers())):
			pname=power.name().ljust(40)+" "
			pkeys=""
			if power.name() in self.hiddenPowers: 
				prest=""
			else: prest=power.output(self.char, False)
			for key in power.keys+sorted(self.char.featurestr(power.name().lower()+"addkey")): pkeys+=res(key, self.char).capitalize()+"  "
			whichBox=0
			often=self.char.featureis(power.name().lower()+"often")
			if often=="": often=power.often
			if power.name()[:16]=="Channel Divinity": 
				whichBox=0
				color="red"
			elif often=="at-will": 
				whichBox=1
				color="green"
			elif often=="encounter": 
				whichBox=2
				color="red"
			elif often=="daily": 
				whichBox=3
				color="cyan"

			powerBoxes[whichBox].grid(row=whichBox+1, column=0, columnspan=10, sticky="w")
			if power.name() in pickedPowers:
				thisPower=Menubutton(powerBoxes[whichBox], text=pname+pkeys+"\t"+power.pSource(),justify=LEFT, fg="blue",bg=color, relief=RELIEF, cursor=SELECTCURSOR)
				thisPower.menu=Menu(thisPower, tearoff=0)
				thisPower["menu"]=thisPower.menu
				powerpick=pickedPowerpicks[pickedPowers.index(power.name())]
				for newChosen in sorted(powerpick.powerChoices):
					if newChosen.name().lower() not in self.char.statret("power"):
						thisPower.menu.add_command(label=newChosen.name(), command=clicky2(newChosen, powerpick))
			else:
				thisPower=Label(powerBoxes[whichBox], text=pname+pkeys+"\t"+power.pSource(),justify=LEFT,bg=color)
			if prest<>"":
				restPower=Label(powerBoxes[whichBox], text=prest, justify=LEFT)
			expandButton=Label(powerBoxes[whichBox])

			thisPower.grid(row=self.showpowers[whichBox], column=0,sticky="w")	
			expandButton.config(text="+", borderwidth=1, relief=GROOVE)
			expandButton.grid(row=self.showpowers[whichBox], column=1, sticky="nw")
			expandButton.bind("<Button-1>", clicky(power.name()))
			if prest<>"": 
				restPower.grid(row=self.showpowers[whichBox]+1, column=0, sticky="w")
				self.showpowers[whichBox]+=1	
			self.showpowers[whichBox]+=1

##############Inventory Stuff####################
	def createAddMenu(self, theMenu):
		"Creates the menu to add items to inventory"
		def clicky(theItem):
			def clicked():
				num=EntryBox(self.root, "Buy",5,"1").runit()
				try: num=int(num)
				except: num=None
				if num!=None:
					for x in range(num): 
						self.char.inventory.buy(theItem.copy())
					self.update()
			return clicked
		addmenu=Menu(theMenu, tearoff=0)
		
		makeCascade(EquipmentLists, addmenu, clicky)
				
		if not(isinstance(theMenu, Menubutton)):
			theMenu.add_cascade(label="Add Items", menu=addmenu)
		return addmenu

	def setInventory(self):
		"Part of update(), displays the inventory"
		def discard(theitem, num=0):
			def clickit():
				for x in range(num):
					self.char.inventory.drop(theitem)
				self.update()
			return clickit
		def equip(theitem, str=""):
			def clickit():
				self.char.equip(theitem, str)
				self.update()
			return clickit
		def unequip(theitem):
			def clickit():
				self.char.inventory.remove(theitem)
				self.update()
			return clickit
		def setEnchant(theitem, newplus):
			def clickit():
				theitem.enchantPlus(newplus)
				self.update()
			return clickit
		def setProperty(theitem, newproperty):
			def clickit():
				theitem.setProperty(newproperty)
				self.update()
			return clickit
		for x in range(len(self.cash)):
			try: self.char.wealth[x]=int(self.cash[x].get())
			except: self.char.wealth[x]=0
		self.inven.destroy()
		self.inven=Frame(self.master())
		for x in range(len(self.cash)):
			Label(self.inven, text=WEALTHTYPES[x], anchor="w").grid(row=x, column=0)
			Entry(self.inven, width=5, textvariable=self.cash[x]).grid(row=x, column=1)

		self.inven.grid(row=self.invenrownum, column=1, columnspan=10, sticky="w")
		rownum=0
		for key in itemslots:
			if self.char.inventory.equipped[itemslots[key]]!=None:
				test=True
				for slot in self.char.inventory.equipped[itemslots[key]].eqslots():
					if slot!="1hand" and slot!="ring": 
						if itemslots[slot]<itemslots[key]: test=False
				if test: 
					Label(self.inven, text=key.capitalize()+":").grid(row=rownum, column=2, sticky="w")
					x=self.makeAmenu(self.inven, self.char.inventory.equipped[itemslots[key]].name(), rownum, 3)
					x.menu.add_command(label="Unequip", command=unequip(key))
					if self.char.inventory.equipped[itemslots[key]].canPlus():
						enchantmenu=Menu(x.menu, tearoff=0)
						for newPlus in range(0,7):
							enchantmenu.add_command(label="+"+str(newPlus), command=setEnchant(self.char.inventory.equipped[itemslots[key]],newPlus))
						x.menu.add_cascade(label="Enchant", menu=enchantmenu)

					rownum+=1
		havelist={}
		for item in self.char.inventory.inventory:
			if item.name() not in havelist:
				havelist[item.name()]=1
			else: havelist[item.name()]+=1
		for item in self.char.inventory.inventory:
			if havelist[item.name()]>0:
				x=self.makeAmenu(self.inven, item.name().capitalize(), rownum, 3)
				if havelist[item.name()]>1: x.config(text=str(havelist[item.name()])+" "+item.name().capitalize())
				if havelist[item.name()]==1:
					x.menu.add_command(label="Discard", command=discard(item.name(), 1))
				z=0
				while havelist[item.name()]>=5*(2**z):
					if z==0: x.menu.add_command(label="Discard 1",command=discard(item.name(), 1))
					x.menu.add_command(label="Discard "+str(5*(2**z)),command=discard(item.name(), 5*(2**z)))
					z+=1
				if havelist[item.name()]>1:
					x.menu.add_command(label="Discard All", command=discard(item.name(), havelist[item.name()]))
				if "1hand" in item.eqslots():
					z=Menu(x.menu, tearoff=0)
					done=False
					if self.char.statret("onehanddual")==0 and isinstance(item.desc,Weapon):
						if "off-hand" not in item.desc.charkey(self.char):
							x.menu.add_command(label="Equip", command=equip(item, "primary hand"))
							done=True
					if not(done):
						z.add_command(label="Primary Hand", command=equip(item, "primary hand"))
						z.add_command(label="Off Hand", command=equip(item, "off hand"))
						x.menu.add_cascade(label="Equip", menu=z)
				elif "ring" in item.eqslots():
					z=Menu(x.menu, tearoff=0)
					z.add_command(label="left ring", command=equip(item, "left ring"))
					z.add_command(label="right ring", command=equip(item, "right ring"))
					x.menu.add_cascade(label="Equip",menu=z)
				elif item.eqslots()!=[]:
					x.menu.add_command(label="Equip", command=equip(item))
				if item.canPlus():
					enchantmenu=Menu(x.menu, tearoff=0)
					for newPlus in range(0,7):
						enchantmenu.add_command(label="+"+str(newPlus), command=setEnchant(item,newPlus))
					x.menu.add_cascade(label="Enchant", menu=enchantmenu)
				legalproperties=[]
				for property in propertyList.keys():
					if propertyList[property].legalItem(item): legalproperties.append(property)
				if len(legalproperties)>0:
					propertymenu=Menu(x.menu, tearoff=0)
					propertymenu.add_command(label="No property", command=setProperty(item, None))
					for property in sorted(legalproperties):
						propertymenu.add_command(label=property,command=setProperty(item, propertyList[property]))
					x.menu.add_cascade(label="Property", menu=propertymenu)
				rownum+=1
				havelist[item.name()]=0

##############Save / Load####################
	def saveAs(self):
		self.save(None)

	def save(self, filename=True):
		self.update()
		if filename:
			filename=self.filename
		if filename==None:
			filename = asksaveasfilename(parent=self.root, defaultextension=".csh", initialdir=SAVEDIR, filetypes=[("Character Sheet File","*.csh")],title='Save as...')
			self.filename=filename
		if len(filename)==0:
			return 0
		self.textfile(filename)
		I="|"
		with open(filename,"w") as f:
			f.write("File::CSH2")
			f.write("\nName::"+self.char.name+"\nStats::"+repr(self.char.stats)+"\nPoints::"+str(self.char.points)+"\nLevel::"+str(self.char.level)+"\nRace::"+self.char.race+"\nCharclass::"+self.char.charclass+"\nParagon::"+self.char.statret("paragonname")+"\nEpic::"+self.char.statret("epicname")+"\nStatboosts::"+repr(self.statboosts))
			featlist=list(self.char.ftrs)
			for a in featlist:
				for what in a.wht:
					if what.when=="feat":
						featlist+=list(what.resolve)
			for a in featlist:
				if a.featPick!=None:
					f.write("\nFeatpick::"+a.featPick.basename)
					if a.featPick.chosen==0: f.write(I+"0")
					else: 
						f.write(I+a.featPick.chosen.name())
						featlist+=[a.featPick.chosen]		
				for what in a.wht:
					if what.when=="powerpick":
						if what.resolve.chosen!=-1:
							f.write("\nPowerpick::"+what.resolve.basename)
							f.write(I+what.resolve.powerChoices[what.resolve.chosen].name())
				if a.specMenu!=None:
					f.write("\nSpecMenu::"+a.name())
					if isinstance(a.specMenu.chosen, list):
						f.write(I)
						f.write(repr(a.specMenu.chosen))
					else: f.write(I+str(a.specMenu.chosen))
				for what in a.wht:
					if what.when=="skillpick":
						f.write("\nSkillpick::"+what.resolve.basename)
						f.write(I+repr(what.resolve.chosen))
			itemList={}
			for a in self.char.inventory.inventory:
				z="\nItem::"+a.cleanname()
				if a.enchantment()>0: z+=" +"+str(a.enchantment())
				if a.property!=None: z+=I+"Property::"+a.property.name.replace("#","").strip()
				if z not in itemList: itemList[z]=1
				else: itemList[z]+=1
			for a in itemList.keys():
				f.write(a)
				if itemList[a]>1: f.write(I+"Quantity::"+str(itemList[a]))

			for key in itemslots:
				if self.char.inventory.equipped[itemslots[key]]!=None:
					test=True
					for slot in self.char.inventory.equipped[itemslots[key]].eqslots():
						if slot!="1hand" and slot!="ring":
							if itemslots[slot]<itemslots[key]: test=False
					if test:
						g=self.char.inventory.equipped[itemslots[key]]
						f.write("\nItem::*Equipped*"+g.cleanname())
						if g.enchantment()>0: f.write(" +"+str(g.enchantment()))
						if g.property!=None: f.write(I+"Property::"+g.property.name.replace("#","").strip())
						if "1hand" in g.eqslots():
							f.write(I+"Hand::"+str("primary hand" in g.eqslots()))
						if "ring" in g.eqslots():
							f.write(I+"Hand::"+str("left ring" in g.eqslots()))
			f.write("\nShowpowers::"+repr(self.showpowers))
			f.write("\nHiddenpowers::"+repr(self.hiddenPowers))
			f.write("\nShowmods::"+repr(self.char.showmods.get()))
			for x in WEALTHTYPES:
				if self.char.statret(x)>0:
					f.write("\n"+x+"::"+str(self.char.statret(x)))
			f.write("\nNotes::"+self.textbox.get(1.0, END))

	def load(self, ret=""):
		if ret=="":
			file = askopenfile(parent=self.root,mode='rb', initialdir=SAVEDIR, filetypes=[("Character Sheet File","*.csh"),("All Files","*.*")],title='Choose a file')
			if file != None:
				data=file.read()
				self.filename=file.name
			else:
				return 0
		else:
			with open("save"+os.sep+ret+".csh") as f:
				self.filename=f.name
				data=f.read()
		
		self.char.reset()
		
		if not data.startswith("File::CSH2"): 
			self.legacyLoad(data)
			return 0

		self.textbox.delete(1.0, END)
		self.textbox.insert(END,data[data.index("\nNotes::")+8:].rstrip())
		data=data[:data.index("\nNotes::")].rstrip()+"\n"
		self.addTextLines()
		def textListtoList(textlist):
			retlist=[]
			textlist=textlist.replace("]","")
			textlist=textlist.replace("[","")
			if textlist=="": return retlist
			while "," in textlist:
				retlist.append(textlist[:textlist.index(",")].strip(" '"))
				textlist=textlist[textlist.index(",")+1:].strip(" '")
			retlist.append(textlist)
			return retlist

		def textDicttoDict(textdict):
			retdict={}
			for x in textdict:
				if "|" in x: retdict[x[:x.index("|")]]=x[x.index("|")+1:]
			return retdict

		listdata={}
		while "\n" in data:
			info=data[:data.index("\n")].rstrip()
			if "::" in info:
				z=info[:info.index("::")]
				if z in listdata:
					if isinstance(listdata[z],list):
						listdata[z].append(info[info.index("::")+2:])
					else:
						listdata[z]=[listdata[z], info[info.index("::")+2:]]
				else: listdata[z]=info[info.index("::")+2:]
			data=data[data.index("\n")+1:]
		self.char.name=listdata["Name"]
		for x in ["Stats", "Statboosts", "Showpowers","Hiddenpowers"]: 
			if x in listdata.keys(): listdata[x]=textListtoList(listdata[x])
		for x in ["Featpick", "SpecMenu", "Powerpick", "Skillpick"]: 
			if x in listdata.keys():
				if isinstance(listdata[x], str): listdata[x]=[listdata[x]]
				listdata[x]=textDicttoDict(listdata[x])
			else:
				listdata[x]={}
		for x in xrange(len(self.char.stats)):
			self.char.stats[x]=int(listdata["Stats"][x])
		self.char.points=int(listdata["Points"])
		self.char.level=int(listdata["Level"])
		self.char.attachRace(listdata["Race"])
		self.char.miniAttach(listdata["Charclass"])
		for x in WEALTHTYPES:
			z=0
			if x in listdata: z=listdata[x]
			self.char.wealth[WEALTHTYPES.index(x)]=z
			self.cash[WEALTHTYPES.index(x)].set(z)
		featlist=list()
		try:
			self.char.addFeat(paragonList[listdata["Paragon"]])
			featlist+=list(paragonList[listdata["Paragon"]].what()[0].resolve)
		except:
			pass
		try:
			self.char.addFeat(epicList[listdata["Epic"]])
			featlist+=list(epicList[listdata["Epic"]].what()[0].resolve)
		except:
			pass

		for x in xrange(len(self.statboosts)):
			if "None" in listdata["Statboosts"][x]: self.statboosts[x]=None
			else: self.statboosts[x]=listdata["Statboosts"][x].strip("'")
		self.levelupStatboosts()
		self.update()

		featlist+=list(self.char.ftrs)
		for a in featlist:
			if a.featPick!=None:
				if a.featPick.basename in listdata["Featpick"]:
					if listdata["Featpick"][a.featPick.basename]!="0":
						featlistbyname=[featinlist.name() for featinlist in a.featPick.featlist]
						if listdata["Featpick"][a.featPick.basename] in featlistbyname:
							a.featPick.chosen=a.featPick.featlist[featlistbyname.index(listdata["Featpick"][a.featPick.basename])]
							featlist+=[a.featPick.chosen]
						else:
							try:
								a.featPick.chosen=allFeatList[listdata["Featpick"][a.featPick.basename]]
								featlist+=[a.featPick.chosen]
							except:
								print "Error - Feat: ",listdata["Featpick"][a.featPick.basename]," not found."
								listdata["Featpick"][a.featPick.basename]="0"
								a.featPick.chosen=0
					else: a.featPick.chosen=0
					listdata["Featpick"].pop(a.featPick.basename)
				else: a.featPick.chosen=0
		for a in featlist:
			if a.specMenu!=None:
				if isinstance(a.specMenu, PowerMod):
					for x in listdata["SpecMenu"].keys():
						if a.name()==x:
							a.specMenu.chosen=listdata["SpecMenu"][x]
				if isinstance(a.specMenu, MultiMenu):
					for x in listdata["SpecMenu"].keys():
						if a.name()==x:
							listdata["SpecMenu"][x]=textListtoList(listdata["SpecMenu"][x])
							a.specMenu.chosen=list(listdata["SpecMenu"][x])
				else:
					for x in listdata["SpecMenu"].keys():
						if a.specMenu.featTitles!=None:
							if x in a.specMenu.featTitles:
								a.specMenu.chosen=int(listdata["SpecMenu"][x])
						else:
							if a.name()==x:
								a.specMenu.chosen=int(listdata["SpecMenu"][x])
		self.update()
		for a in featlist:
			for what in a.wht:
				if what.when=="powerpick":
					if what.resolve.basename in listdata["Powerpick"]:
						listByName=[x.name() for x in what.resolve.powerChoices]
						if listdata["Powerpick"][what.resolve.basename] in listByName:
							what.resolve.chosen=listByName.index(listdata["Powerpick"][what.resolve.basename])
						else:what.resolve.chosen=-1
						listdata["Powerpick"].pop(what.resolve.basename)
					else: what.resolve.chosen=-1
				if what.when=="skillpick":
					if what.resolve.basename in listdata["Skillpick"]:
						infolist=textListtoList(listdata["Skillpick"][what.resolve.basename])
						for x in xrange(len(what.resolve.chosen)):
							try: 
								what.resolve.chosen[x]=int(infolist[x])
							except:
								what.resolve.chosen[x]=-1
		self.update()
		try:
			if isinstance(listdata["Item"], str):
				listdata["Item"]=[listdata["Item"]]
			for x in listdata["Item"]:
				try:
					theItem=x
					addproperty=None
					equipit=False
					hand=False
					quantity=1
					if "*Equipped*" in theItem:
						equipit=True
						theItem=theItem.replace("*Equipped*","")
					if "|Quantity::" in theItem:
						quantity=int(theItem[theItem.index("|Quantity::")+11:])
						theItem=theItem[:theItem.index("|Quantity::")]
					if "|Hand::" in theItem:
						if "|Hand::True" in theItem:hand=True
						theItem=theItem[:theItem.index("|Hand::")]
					if "|Property::" in theItem:
						addproperty=theItem[theItem.index("|Property::")+11:]
						if addproperty in propertyList.keys(): addproperty=propertyList[addproperty]
						else: addproperty=None
						theItem=theItem[:theItem.index("|Property::")]
					enchant=0
					if theItem[-2]=="+":
						enchant=int(theItem[-1])
						theItem=theItem[:-3]
					finalItem=finditem(theItem)
					for x in range(quantity):
						if finalItem!=None:
							self.char.inventory.buy(finalItem, enchant)
							self.char.inventory.inventory[-1].setProperty(addproperty)
							if equipit:
								if "1hand" not in self.char.inventory.inventory[-1].slots and "ring" not in self.char.inventory.inventory[-1].slots:
									self.char.equip(self.char.inventory.inventory[-1])
								elif hand: self.char.equip(self.char.inventory.inventory[-1],"primary hand")
								else: self.char.equip(self.char.inventory.inventory[-1],"off hand")
				except: print "Item not found: ",x
		except: pass
		self.showpowers=[int(x) for x in listdata["Showpowers"]]
		self.HiddenPowers=list(listdata["Hiddenpowers"])
		self.char.showmods.set(int(listdata["Showmods"]))
		self.update()

	def legacyLoad(self, data):
		"To load old .csh files"
		class iterate:
			def __init__(self, string, symbol, ci=0):
				self.ci=ci
				self.data=string
				self.symbol=symbol
			def next(self):
				if self.symbol not in self.data[self.ci:]:
					return self.data[self.ci:]
				nextci=self.ci+self.data[self.ci:].index(self.symbol)
				ret=self.data[self.ci:nextci]
				self.ci=nextci+1
				return ret
		data=iterate(data, "|")
		self.char.name=data.next()
		infolist=iterate(data.next()[1:-1], ",")
		for x in xrange(len(self.char.stats)):
			self.char.stats[x]=int(infolist.next())
		self.char.points=int(data.next())
		self.char.level=int(data.next())
		self.char.attachRace(data.next())
		self.char.miniAttach(data.next())
		self.char.remFeat("paragon")
		pgon=data.next()
		if "." not in pgon: epic=""
		else: 
			epic=pgon[pgon.index(".")+1:]
			pgon=pgon[:pgon.index(".")]
		featlist=list()
		if pgon!="":
			self.char.addFeat(paragonList[pgon])
			featlist+=list(paragonList[pgon].what()[0].resolve)
		if epic!="":
			self.char.addFeat(epicList[epic])
			featlist+=list(epicList[epic].what()[0].resolve)
		infolist=iterate(data.next()[1:-1], ",")
		for x in xrange(len(self.statboosts)):
			z=infolist.next()
			if "None" in z: self.statboosts[x]=None
			else: self.statboosts[x]=z.strip()[1:-1]
		self.levelupStatboosts()
		featpicks={}
		z=data.next()
		while z!="X":
			featpicks[z]=data.next()
			z=data.next()
		powerpicks={}
		z=data.next()
		while z!="X":
			powerpicks[z]=data.next()
			z=data.next()
		specMenus={}
		z=data.next()
		while z!="X":
			specMenus[z]=data.next()
			z=data.next()
		skillpicks={}
		z=data.next()
		while z!="X":
			skillpicks[z]=data.next()
			z=data.next()
		inventory=[]
		z=data.next()
		while z!="X":
			inventory.append(z)
			z=data.next()
		inventory.append("equiplist")
		z=data.next()
		while z!="X":
			inventory.append(z)
			z=data.next()
		self.update()
		featlist+=list(self.char.ftrs)
		for a in featlist:
			if a.featPick!=None:
				if a.featPick.basename in featpicks:
					if featpicks[a.featPick.basename]!="0":
						featlistbyname=[featinlist.name() for featinlist in a.featPick.featlist]
						if featpicks[a.featPick.basename] in featlistbyname:
							a.featPick.chosen=a.featPick.featlist[featlistbyname.index(featpicks[a.featPick.basename])]
							featlist+=[a.featPick.chosen]
						else:
							try:
								a.featPick.chosen=allFeatList[featpicks[a.featPick.basename]]
								featlist+=[a.featPick.chosen]
							except:
								print "Error - Feat: ",featpicks[a.featPick.basename]," not found."
								featpicks[a.featPick.basename]="0"
							a.featPick.chosen=0
					else: a.featPick.chosen=0
					featpicks.pop(a.featPick.basename)
				else: a.featPick.chosen=0
		for a in featlist:
			if a.specMenu!=None:
				if isinstance(a.specMenu, PowerMod):
					for x in specMenus.keys():
						if a.name()==x:
							a.specMenu.chosen=specMenus[x]
				if isinstance(a.specMenu, MultiMenu):
					for x in specMenus.keys():
						if a.name()==x:
							MultiMenuList=iterate(specMenus[x]+",X", ",")
							z=MultiMenuList.next()
							a.specMenu.chosen=[]
							while z!="X":
								a.specMenu.chosen+=[z]
								z=MultiMenuList.next()
				else:
					for x in specMenus.keys():
						if a.specMenu.featTitles!=None:
							if x in a.specMenu.featTitles:
								a.specMenu.chosen=int(specMenus[x])
						else:
							if a.name()==x:
								a.specMenu.chosen=int(specMenus[x])
		self.update()
		for a in featlist:
			for what in a.wht:
				if what.when=="powerpick":
					if what.resolve.basename in powerpicks:
						what.resolve.chosen=int(powerpicks[what.resolve.basename])
						powerpicks.pop(what.resolve.basename)
					else: what.resolve.chosen=0
				if what.when=="skillpick":
					if what.resolve.basename in skillpicks:
						infolist=iterate(skillpicks[what.resolve.basename][1:-1], ",")
						for x in xrange(len(what.resolve.chosen)):
							z=infolist.next()
							what.resolve.chosen[x]=int(z)
		addproperty=None
		equipit=False
		for a in inventory:
			if a=="equiplist": equipit=True
			if a in propertyList.keys(): addproperty=propertyList[a]
			elif a not in ["True","False"]:
				val=a
				enchant=0
				if val[-2]=="+":
					enchant=val[-1]
					val=val[:-3]
				theItem=finditem(val)
				if theItem!=None:
					self.char.inventory.buy(theItem, int(enchant))
					self.char.inventory.inventory[-1].setProperty(addproperty)
					if equipit:
						if "1hand" not in self.char.inventory.inventory[-1].slots and "ring" not in self.char.inventory.inventory[-1].slots:
							self.char.equip(self.char.inventory.inventory[-1])
				addproperty=None
			elif a=="True":
				self.char.equip(self.char.inventory.inventory[-1],"primary hand")
			elif a=="False":
				self.char.equip(self.char.inventory.inventory[-1],"off hand")
		infolist=iterate(data.next()[1:-1], ",")
		for x in xrange(len(self.showpowers)):
			z=infolist.next()
			self.showpowers[x]=int(z)
		infolist=iterate(data.next()[1:-1], ",")
		z=infolist.next().strip()[1:-1]
		while z<>"X":
			if z=="0": self.char.showmods.set(0)
			elif z=="1": self.char.showmods.set(1)
			else: self.hiddenPowers+=[z]
			z=infolist.next().strip()[1:-1]
		
		self.textbox.delete(1.0, END)
		self.textbox.insert(END,data.data[data.ci:-1])
		self.update()

	def shortpowers(self):
		powers=[]
		ret=""
		for power in sorted(list(self.char.powers())):
			if power.name() not in self.hiddenPowers: powers.append(power.htmlOut(self.char))
			#else: ret+="\n"+power.htmlOut(self.char, True)
		x=0
		if ret!="":
			ret="\n<div id=\"container\" style=\"width:50%\">"+ret+"\n</div>"
		for power in powers:
			if x==0:
				ret+="\n<div class=\"page-break\"></div>"
				ret+="\n<div id=\"powerContainer\">"
			if x%2==0:
				ret+="\n\t<div id=\"powerRow\">"
			ret+=power
			x+=1
			if x%2==0:
				ret+="\n\t</div>"
			if x==6:
				ret+="\n</div>"
				x=0
		if x!=0:
			if x%2!=0:
				ret+="\n\t\t<div></div>"
				ret+="\n\t</div>"
			if x<5:
				ret+="\n\t<div></div>"
			ret+="\n</div>"
		return ret

	def textfile(self, filename):
		if filename.endswith(".csh"): filename=filename.replace(".csh",".html")
		else: filename+=".html"
		
		with open(filename,"w") as f:
			f.write("""<head>
<title></title>
<style type="text/css">
body {background: white;	font-size: 10pt;	font-family: serif;}
h1 {font-size: 12pt;	text-align: center;}
table {font-size: 10pt;	font-family: serif;	border-spacing:0px;	border-collapse:collapse;}
#container {display:table;	width:99%;}
#grid {	width:100%;}
#grid td{ border:1px solid grey;}
.box{display:table-cell;}
.stats {width: 20%;}
.hp {width: 35%;	border: 1px solid grey;}
	#hptable {align:center;	width:95%;}
	#hptable td{ border-bottom: 1px solid grey;	}
.defenses {width:10%;}
.type {width:30%;}
	#typetable {border-spacing: 1px;	width: 100%;	border: 1px solid grey;	border-collapse:separate;}
	#typetable td{text-align:center;}
#skills {display:table-cell;	width: 20%;}
#feats1 {display:table-cell;	width: 80%;}
#feats2 {display:table-cell;	width: 100%;}
#featstable {border: 1px solid grey;width:100%;}
	#featstable td {vertical-align:top;}
	#featstable caption {text-align:center;}
.money {width: 16%;}
.left { display:table-cell;	width:100%;	white-space:nowrap;}
.right {display:table-cell;	text-align:right;	white-space:nowrap;}
.title{	display:block;	width:100%;}
	.at-willBG {background:lawngreen;}
	.encounterBG {background:red;}
	.dailyBG {background:silver;}
.aoe{display:table-cell;	width:100%;	text-align:right;	white-space:nowrap; padding-right:4px;}
.target{display:table-cell;	width:100%;}
.targetbox{	border-collapse:collapse;}
#powerContainer {width:99%;	height:99%;	display:table;	border-collapse:separate;	border-spacing:5px;}
#powerRow {	width:100%;	display:table-row;}
.power {font-family:sans-serif;	font-size:8pt;	width:50%;	height:32%;	display:table-cell;	border: 2px solid}
	.at-will {border-color: lawngreen;}
	.encounter {border-color: red;}
	.daily {border-color: silver;}
#line{text-indent:20px; padding-left:4px; padding-right:4px;}
#line2{text-indent:40px; padding-left:4px; padding-right:4px;}
@media all{.page-break { display:none; }}
@media print{.page-break { display:block; page-break-before:always; }}
</style>
</head>
<body>
<div id="container">
	<div id="header"
		<h1>
			""")
			f.write(self.char.name)
			f.write("""
		</h1>
	</div>
</div>
<div id="container">
	<div class="stats box">
		<table id="grid">""")
			for x in ["str","con","dex","int","wis","cha"]:
				f.write("\n\t\t\t<tr><td>"+x.title()+"</td><td>"+str(self.char.statret(x))+"</td><td>+"+str(self.char.mod(x))+"</td><td>+"+str(self.char.mod(x)+self.char.statret("level")/2)+"</td></tr>")
			f.write("""
		</table>
	</div>
	<div class="hp box">
		<table id="hptable" align="center">""")
			f.write("\n\t\t\t<tr><td>Max HP: "+str(self.char.statret("hp"))+"</td></tr>")
			f.write("\n\t\t\t<tr><td>Current:</td></tr>")
			f.write("\n\t\t\t<tr><td>&nbsp;</td></tr>")
			f.write("\n\t\t\t<tr><td>Bloodied: "+str(self.char.statret("hp")/2)+"</td></tr>")
			f.write("\n\t\t\t<tr><td>Surge: "+str(self.char.statret("surge"))+"</td></tr>")
			f.write("\n\t\t\t<tr><td>Per day: "+str(self.char.statret("surges"))+"</td></tr>")
			f.write("""
		</table>
	</div>
	<div class="defenses box">
		<table id="grid">""")
			f.write("\n\t\t\t<tr><td>AC:</td><td>"+str(self.char.statret("ac"))+"</td></tr>")
			f.write("\n\t\t\t<tr><td>Fort:</td><td>"+str(self.char.statret("fort"))+"</td></tr>")
			f.write("\n\t\t\t<tr><td>Ref:</td><td>"+str(self.char.statret("ref"))+"</td></tr>")
			f.write("\n\t\t\t<tr><td>Will:</td><td>"+str(self.char.statret("will"))+"</td></tr>")
			f.write("\n\t\t\t<tr><td>Speed:</td><td>"+str(self.char.statret("speed"))+"</td></tr>")
			f.write("\n\t\t\t<tr><td>Init:</td><td>"+str(self.char.statret("initiative"))+"</td></tr>")
			f.write("""
		</table>
	</div>
	<div class="type box">
		<table id="typetable">
			<tr><td>Level """+str(self.char.statret("level"))+" "+self.char.statret("race")+" "+self.char.statret("class")+"""</td></tr>
			<tr><td>""")
			if self.char.statret("paragonname")!="": f.write(self.char.statret("paragonname").title())
			else: f.write("&nbsp;")
			f.write("</td></tr>")
			f.write("""
			<tr><td>""")
			if self.char.statret("epicname")!="": f.write(self.char.statret("epicname").title())
			else: f.write("&nbsp;")
			f.write("</td></tr>")
			f.write("""
			<tr><td>"""+self.char.statret("size")+" "+self.char.statret("origin")+" "+self.char.statret("type"))
			f.write("""</td></tr>
			<tr><td>Passive Perception: """+str(self.char.statret("perception")+10)+"""</tr></td>
			<tr><td>""")
			if self.char.statret("vision")!=[]: 
				for x in range(len(self.char.statret("vision"))):
					if x>0: f.write("; ")
					f.write(self.char.statret("vision")[x].capitalize()+" vision")
			else: f.write("&nbsp;")
			f.write("</td></tr>")
			f.write("""
		</table>
	</div>
</div>
<div id="container">
	<div id="feats1">""")
			feattext=self.char.htmlFeats()
			f.write(feattext[0])
			f.write("""
	</div>
	<div id="skills">
		<table id="grid">""")
			f.write("\n\t\t\t<CAPTION>&nbsp;</CAPTION>")
			f.write("\n\t\t\t<tr><td width=\"100%\">Skill</td><td>Tr</td><td>Total</td></tr>")
			for x in allskills.keys():
				f.write("\n\t\t\t<tr><td>"+x.title()+"</td><td>")
				if x in self.char.statret("training"): f.write("X")
				else: f.write("&nbsp;")
				f.write("</td><td>"+str(self.char.statret(x))+"</td></tr>")
			f.write("""
		</table>
	</div>
</div>
<div id="container">
	<div id="feats2">""")
			f.write(feattext[1]+"\n")
			f.write("""
	</div>
</div>
<div id="container">
	<div id="money box">
		<table id="grid">
			<CAPTION>Wealth</CAPTION>""")
			moneysize=3
			wealth=[x for x in WEALTHTYPES]
			x=0
			wealthMod=0
			for coin in wealth:
				if (WEALTHINFO[coin][2]>=wealthMod-2 and WEALTHINFO[coin][2]<=wealthMod) or self.char.statret(coin)>0:
					text=str(self.char.statret(coin))
					if text=="0": text="&nbsp;"
					f.write("\n\t\t\t<tr><td>"+WEALTHINFO[coin][0].capitalize()+"</td><td>"+text+"</td></tr>")
					wealthMod=max(wealthMod, WEALTHINFO[coin][2])
					moneysize+=1
			f.write("""
			<tr><td colspan=2>Load: """+str(self.char.statret("load"))+"""</td></tr>
			<tr><td>Light:</td><td>"""+str(self.char.statret("normalload"))+"""</td></tr>
			<tr><td>Heavy:</td><td>"""+str(self.char.statret("heavyload")*2)+"""</td></tr>
			<tr><td>Drag:</td><td>"""+str(self.char.statret("pushload")*5)+"""</td></tr>
		</table>
	</div>
	<div class="box">
		<table id="grid">
			<CAPTION>Inventory</CAPTION>
			<tr><td width=\"44%\">Item</td><td width=\"5%\">lbs</td><td width=\"44%\">Item</td><td width=\"5%\">lbs</td></tr>""")
			z=0
			inventorylist=[]
			inventorytext=self.char.inventory.htmlOut()
			while "\n" in inventorytext:
				inventorylist.append(inventorytext[:inventorytext.index("\n")])
				inventorytext=inventorytext[inventorytext.index("\n")+1:]
			if inventorytext!="":
				inventorylist.append(inventorytext)
			moneysize=max(moneysize, len(inventorylist)/2+1)
			for x in range(moneysize):
				f.write("\n\t\t\t<tr><td>")
				if len(inventorylist)>x: f.write(inventorylist[x])
				else: f.write("&nbsp;</td><td>")
				f.write("</td><td>")
				if len(inventorylist)>x+moneysize: f.write(inventorylist[x+moneysize])
				else: f.write("&nbsp;</td><td>")
				f.write("</td><tr>")
			f.write("""
		</table>
	</div>
</div>
<div id="container">""")
			beasttext="\n\t<p>"+self.char.beasttext().replace("\n","</p>\n\t<p>")
			f.write(beasttext+"</p>\n\t<p></p>")
			f.write("\n\t<p>Notes:</p>\n\t<p>"+self.textbox.get(1.0, END).replace("\n","</p>\n\t<p>"))
			f.write("""</p>
</div>""")
			powertext=self.shortpowers()
			f.write(powertext)
			f.write("""
</body>
</html>""")