from charutils import *
from paragons import *
from powers4th import *

classList={"Ardent" :charClass(12, 5, 7, [feat([ft(["fort","will"],["class",1])],"Save Bonus")
                    ,feat([ft("featpick",FeatPick(0, "Ardent Mantle",0,
                           [feat([ft("featureadd","ardent mantle"),ft("power",[basePowers["Ardent Alacrity"].copy()]),ft(["insight","perception"],["mantle of clarity",2])],"Mantle of Clarity",["You and allies in ",lambda x:x.statret("mantle radius")+5," squares gain +",WISMOD," defenses vs. opp. attacks and +2 to Insight and Perception"])
                           ,feat([ft("featureadd","ardent mantle"),ft("power",[basePowers["Ardent Outrage"].copy()]),ft(["diplomacy","intimidate"],["mantle of elation",2])],"Mantle of Elation",["You and allies in ",lambda x:x.statret("mantle radius")+5," squares gain +",CONMOD," damage on opp. attacks and +2 to Diplomacy and Intimidate"])]))],"ardent mantle featpick")
                    ,feat([ft("power",[basePowers["Ardent Surge"].copy()])],"Ardent Surge")
                    ,feat([ft("psps",["",raiselist(1,[1,3,3,7,7,13,17,17,21,21,23,23,27,27])])],"Psionic Augmentation",["",lambda x:x.statret("psps")," Power Points; use power points each encounter to augment at-will powers."])
                    ,feat([ft("skillpick",SkillPick("ardent",4, "Ardent Skill"))],"Class Skills")]
                    ,["Cloth","Leather","Hide","Chainmail","Simple Melee","Simple Ranged","Military Melee"]
                    ,["Arcana","Athletics","Bluff","Diplomacy","Endurance","Heal","Insight","Intimidate","Streetwise"]),
           "Artificer" :charClass(12, 5, 6, [feat([ft(["fort","will"],["class",1])],"Save Bonus")
                    ,feat([],"Arcane Empowerment","Can empower 1 item, plus 1 additional item per milestone reached.")
                    ,feat([],"Impart Energy","Use 1 arcane empowerment to recharge the daily power of a magic item, max 1/day/item")
                    ,feat([],"Augment Energy","Infuse weapon or implement to give user ability to add 2 to an attack roll, max 1/day/item")
                    ,feat([],"Arcane Rejuvination",["Allies gain ",lambda x:x.statret("level")/2+x.mod("int")," temporary hit points when they use a daily item power"])
                    ,feat([basePowers["Healing Infusion: Curative Admixture"],basePowers["Healing Infusion: Resistive Formula"]],"Healing Infusion",["Create ",lambda x:raising(1,16)(x)+1," infusions per extended rest, expend them to power Healing Infusion powers"])
                    ,feat([ft("feat",[allFeatList["Ritual Caster"]])],"Ritual Caster","Master and perform rituals")
                    ,feat([],"Artificer Weapon Bonus","Even nonmagic thrown weapons return to your hand after using them")
                    ,feat([ft("skillpick",SkillPick("artificer",3, "Artificer Skill")),ft("arcana",["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Simple Melee","Simple Ranged"]
                    ,["Arcana","Diplomacy","Dungeoneering","Heal","History","Perception","Thievery"]),
           "Avenger" :charClass(14, 6, 7, [feat([ft(["fort","ref","will"],["class",1])],"Save Bonus")
                    ,feat([ft("power",[basePowers["Channel Divinity 8"].copy(),basePowers["Channel Divinity 9"].copy(), basePowers["Oath of Enmity"].copy()])],"Channel Divinity","Once per encounter use a Channel Divinity power")
                    ,feat([specMenus["deities"]],"Worship")
                    ,feat([ft("featpick",FeatPick(0, "Avenger's Censure",0,
                            [feat([ft("featureadd","avenger's censure")],"Censure of Pursuit",["+",lambda x:raising(2,10)(x)+x.mod("dex")," damage vs. Oath of Enmity target when they choose to move away."]),
                            feat([ft("featureadd","avenger's censure")],"Censure of Retribution",["When enemy other than Oath target hits you, gain a cumulative +",INTMOD," bonus to damage vs. Oath target."]),
                            feat([ft("featureadd","avenger's censure")],"Censure of Unity",["Gain a +",raising(1,11)," bonus to damage rolls against Oath of Enmity target for each ally adjacent to that target."])]))],"avenger's censure featpick")
                    ,feat([ft("ac",["",lambda x: (3+x.statret("armoroffaith"))*(not(x.check("armortype",["heavy","shield","leather","hide"],True)))])],"Armor of Faith","+3 AC when neither in cloth armor or no armor and not using a shield")
                    ,feat([ft("skillpick",SkillPick("avenger",3, "Avenger Skill")),ft("religion",["training",5])],"Class Skills")]
                    ,["Cloth","Simple Melee","Simple Ranged","Military Melee"]
                    ,["Acrobatics","Athletics","Endurance","Heal","Intimidate","Perception","Religion","Stealth","Streetwise"]),
           "Barbarian" :charClass(15, 6, 8, [feat([ft("fort",["class",2])],"Save Bonus")
                    ,feat([ft(["ac","reflex"],("",lambda x:raising(1,10)(x)*(not(x.check("armortype","heavy")))))],"Barbarian Agility",["While you are not wearing heavy armor, you gain a +",raising(1,10)," bonus to AC and Reflex"])
                    ,feat([ft("featpick",FeatPick(0, "Feral Might",0,
                            [feat([ft("featureadd","feral might"),basePowers["Swift Charge"]],"Rageblood Vigor",["When attack drops enemy, gain ",lambda x: x.mod("con")-5+raising(5,10)(x)," temporary HP"]),
                            feat([ft("featureadd","feral might"),basePowers["Roar of Triumph"]],"Thaneborn Triumph",["Whenever you bloody an enemy, the next attack roll you or ally makes vs. enemy gains +",CHAMOD," bonus"]),
                            feat([ft("featureadd","feral might"),basePowers["War Cry"]],"Thunderborn Wrath",["Once per round when your attack bloodies an enemy, each enemy adjacent to you takes ",CONMOD," thunder damage"])]))],"feral might featpick")
                    ,feat([ft("feat",[feat([ft("power",[basePowers["Rage Strike"]])],"Rage Strike","",CHECK("level",5))])],"delayfeat","")
                    ,feat([],"Rampage","1/round, when you critical with a barbarian power, make a melee basic attack as a free action")
                    ,feat([ft("skillpick",SkillPick("barbarian",3, "Barbarian Skill"))],"Class Skills")]
                    ,["Cloth","Leather","Hide","Simple Melee","Military Melee"]
                    ,["Acrobatics","Athletics","Endurance","Heal","Intimidate","Nature","Perception"]),
           "Bard" :charClass(12, 5, 7, [feat([ft(["reflex","will"],["class",1])],"Save Bonus")
                    ,feat([ft("power",[basePowers["Majestic Word"].copy(),basePowers["Words of Friendship"].copy()])],"","")
                    ,feat([ft("feat",[allFeatList["Ritual Caster"]])],"Bard Training",["Master and perform rituals, ",raising(1,10),"/day cast a ritual of your level or lower without paying component cost"])
                    ,feat([ft("featpick",FeatPick(0, "Bardic Virtue",0,
                            [feat([ft("featureadd","bardic virtue")],"Virtue of Cunning",["Once per round, when enemy misses an ally within ",lambda x:x.mod("int")+5+x.statret("bardic virtuerange")," squares, slide that ally ",lambda x:x.statret("cunningslide")+1," square(s)."]),
                            feat([ft("featureadd","bardic virtue")],"Virtue of Valor",["Once per round, when ally within "" squares bloodies an enemy, grant that ally ",lambda x:x.mod("con")+raising(2,10)(x)-1+x.statret("valorhp")," temporary hit points."]),
                            feat([ft("featureadd","bardic virtue")],"Virtue of Prescience",["1/encounter interrupt- enemy hits ally within ",lambda x: 5+x.statret("bardic virtuerange")," squares, grant ally +",WISMOD," bonus to targeted defense until end of that enemy's turn"])]))],"bardic virtue featpick")
                    ,feat([],"Multiclass Versatility","You can choose class-specific multiclass feats from more than one class.")
                    ,feat([ft(skill,["",jackoftrades(skill,True,1)]) for skill in allskills.keys()],"Skill Versatility","You gain a +1 bonus to untrained skill checks.")
                    ,feat([],"Song of Rest",["If you play an instrument or sing during a short rest, allies regain ",lambda x:x.mod("cha")+x.statret("songofresthp")," extra hit points per healing surge spent after the rest."])
                    ,feat([ft("skillpick",SkillPick("bard",4, "Bard Skill")),ft("arcana",["training",5])],"Class Skills")]
                    ,["cloth","leather","hide","chainmail","Light","Simple Melee","Simple Ranged","Military Ranged","longsword","scimitar","short sword"]
                    ,["Acrobatics","Arcana","Athletics","Bluff","Diplomacy","Dungeoneering","Heal","History","Insight","Intimidate","Nature","Perception","Religion","Streetwise"]),
           "Battlemind" :charClass(15, 6, 9, [feat([ft(["will"],["class",2])],"Save Bonus")
                    ,feat([ft("powerpick",PowerPick([basePowers["Battle Resilience"], basePowers["Speed of Thought"]],0,31,"Psionic Study"))],"Psionic Study")
                    ,feat([ft("power",[basePowers["Battlemind's Demand"], basePowers["Blurred Step"], basePowers["Mind Spike"]])],"Psionic Defense")
                    ,feat([ft("psps",["",raiselist(1,[1,3,3,7,7,13,17,17,21,21,23,23,27,27])])],"Psionic Augmentation",["",lambda x:x.statret("psps")," Power Points; use power points each encounter to augment at-will powers."])
                    ,feat([ft("skillpick",SkillPick("battlemind",3, "Battlemind Skill"))],"Class Skills")]
                    ,["Cloth","leather","hide","chainmail","scale","light","heavy","Simple Melee","Simple Ranged","Military Melee"]
                    ,["Arcana","Athletics","Bluff","Diplomacy","Endurance","Heal","Insight","Intimidate"]),
           "Cleric" :charClass(12, 5, 7, [feat([ft("will",["class",2])],"Save Bonus")
                    ,feat([basePowers["Channel Divinity: Divine Fortune"], basePowers["Healing Word"]],"Channel Divinity","Once per encounter use a Channel Divinity power")
                    ,feat([ft("powerpick",PowerPick([basePowers["Channel Divinity: Turn Undead"], basePowers["Channel Divinity: Healer's Mercy"]],0,31,"Channel Divinity Option"))],"Channel Divinity Option")
                    ,feat([specMenus["deities"]],"Worship")
                    ,feat([ft("clerichealing",["",lambda x:x.mod("wis")])],"Healer's Lore",["Add ",WISMOD," to hit points healed with cleric powers that let a creature spend a healing surge"])
                    ,feat([ft("feat",[allFeatList["Ritual Caster"]])],"Ritual Caster","Master and perform rituals")
                    ,feat([ft("skillpick",SkillPick("cleric",3, "Cleric Skill")),ft("religion",["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Hide","Chainmail","Simple Melee","Simple Ranged"]
                    ,["Arcana","Diplomacy","Heal","History","Insight","Religion"]),
           "Druid" :charClass(12, 5, 7, [feat([ft(["will","reflex"],["class",1])],"Save Bonus")
                    ,feat([ft("featpick",FeatPick(0, "Primal Aspect",0,
                            [feat([ft("featureadd","primal aspect"),ft("light armor",["light armor",CONMOD])],"Primal Guardian","While not in heavy armor, use you Con in place of you Dex or Int to determine AC."),
                            feat([ft("featureadd","primal aspect"),ft("speed",["",lambda x:not(x.check("armortype","heavy"))])],"Primal Predator",["Once per round, when ally within "" squares bloodies an enemy, grant that ally ",lambda x:x.mod("con")+raising(2,10)(x)-1+x.statret("valorhp")," temporary hit points."]),
                            feat([ft("featureadd","primal aspect")],"Primal Swarm",["While in beast form and not in heavy armor, reduce damage you take from melee and ranged attacks by ",CONMOD,"."])]))],"primal aspect featpick")
                    ,feat([basePowers["Wild Shape"]],"Wild Shape","")
                    ,feat([ft("feat",[allFeatList["Ritual Caster"]])],"Ritual Caster","Master and perform rituals.  1/day use Animal Messenger without expending components.")
                    ,feat([ft("at-willpowers",["",1])],"Extra at-will power")
                    ,feat([ft("skillpick",SkillPick("druid",3, "Druid Skill")),ft("nature",["training",5])],"Class Skills")]
                    ,["cloth","Leather","Hide","Simple Melee","Simple Ranged"]
                    ,["Arcana","Athletics","Diplomacy","Endurance","Heal","History","Insight","Nature","Perception"]),
           "Fighter":charClass(15, 6, 9, [feat([ft("fort",["class",2])],"Save Bonus")
                    ,feat([],"Combat Challenge","Mark attacked enemy: -2 on attacks that don't include you, bonus attacks vs. them")
                    ,feat([ft("featpick",FeatPick(0, "Combat Style",0,
                            [feat([],"Combat Superiority",[plus(lambda x:x.mod("wis"),1)," bonus to opportunity attacks.  Attack stops opponents movement if it hits."]),
                             feat([basePowers["Combat Agility"]],"Combat Agility","Gain the Combat Agility power")]))],"combat style featpick")
                    ,feat([ft("featpick",FeatPick(0, "Weapon Talent",0,
                            [feat([ft("featureadd","fighter weapon talent"),ft("one-handedattack",("",1))],"One-handed weapon mastery","+1 on attacks with one-handed weapons"),
                            feat([ft("featureadd","fighter weapon talent"),ft("two-handedattack",("",1))],"Two-handed weapon mastery","+1 on attacks with two-handed weapons"),
                            feat([],"Battlerager Vigor",["Additional benefits with temporary HP, gain ",CONMOD," temp HP when you hit an enemy"]),
                            feat([ft("off-handattack",["class-feature",lambda x:x.inventory.dualwield()]),ft("feat",[allFeatList["Two-Weapon Defense"]]),ft(["and","meleedamage","off-handdamage"],["class-feature",lambda x:x.inventory.dualwield()*(2+x.statret("tempesttech"))*(not(x.check("armortype", "heavy")) or x.check("armortype","chainmail"))]),ft("meleedamage",["class-feature",lambda x:x.inventory.dualwield()*(1+x.statret("tempesttech"))*(not(x.check("armortype","heavy")) or x.check("armortype","chainmail"))])],"Tempest Technique","+1 attack rolls w/off-hand weapons, two weapon defense, bonus damage when 2-weapon fighting"),
                            feat([ft("ac",["",lambda x: int(x.statret("handsfree")[1]*(not(x.statret("handsfree")[0])))]),ft("fort",["",lambda x:2*int((not(x.statret("handsfree")[0]))*x.statret("handsfree")[1])]),ft(["unarmed attacknameattack"],["proficiency",raising(2,10)])],"Brawler Style",["+1 AC and +2 Fortitude when armed and offhand is free; +",raising(2,10)," to unarmed attacks and grabs"])]))],"weapon talent featpick")
                    ,feat([ft("skillpick",SkillPick("fighter",3,"Fighter Skill"))],"Class Skills")]
                    ,["Cloth","Leather","Hide","Chainmail","Scale","Light","Heavy","Simple Melee","Military Melee","Simple Ranged","Military Ranged"]
                    ,["Athletics","Endurance","Heal","Intimidate","Streetwise"]),
           "Invoker" :charClass(10, 4, 6, [feat([ft(["fort","ref","will"],["class",1])],"Save Bonus")
                    ,feat([ft("power",[basePowers["Channel Divinity: Rebuke Undead"].copy()])],"Channel Divinity","Once per encounter use a Channel Divinity power")
                    ,feat([specMenus["deities"]],"Worship")
                    ,feat([ft("featpick",FeatPick(0, "Divine Covenant",0,
                            [feat([ft("featureadd","divine covenant"),basePowers["Channel Divinity: Perserver's Rebuke"]],"Covenant of Preservation","When you use a divine encounter or daily attack power on your turn, slide an ally within 10 squares of you 1 square"),
                             feat([ft("featureadd","divine covenant"),basePowers["Channel Divinity: Armor of Wrath"]],"Covenant of Wrath","When you use a divine encounter or daily attack power on your turn, gain +1 damage / enemy attacked with the power"),
                             feat([ft("featureadd","divine covenant"),basePowers["Channel Divinity: Maledictor's Doom"]],"Covenant of Malediction","When you use a divine encounter/daily attack power on your turn, push one hit target 1 square")]))],"divine covenant featpick")
                    ,feat([ft("feat",[allFeatList["Ritual Caster"]])],"Ritual Caster","Master and perform rituals")
                    ,feat([ft("skillpick",SkillPick("invoker",3, "Invoker Skill")),ft("religion",["training",5])],"Class Skills")]
                    ,["cloth","Leather","Hide","Chainmail","Simple Melee","Simple Ranged"]
                    ,["Arcana","Diplomacy","Endurance","History","Insight","Intimidate","Religion"]),
           "Monk":charClass(12, 5,7, [feat([ft(["fort","ref","will"],["class",1])],"Save Bonus")
                    ,feat([ft("weaponenchant",["ki focus",lambda x:x.statret("ki focusimplement")])],"ki focus weapon")
                    ,feat([ft("weaponimplement",["enhancement",lambda x: max([z.enchantment() for z in x.inventory.weapons(True)]+[0])])],"ki focus weapon")
                    ,feat([ft("featpick",FeatPick(0, "Monastic Tradition",0,
                           [feat([ft("featureadd","monastic tradition"),basePowers["Centered Flurry of Blows"].copy(),ft("fort",["",raising(1,10)])],"Centered Breath",["Centered Flurry of Blows power, +",raising(1,10)," to Fortitude defense"])
                           ,feat([ft("featureadd","monastic tradition"),basePowers["Stone Fist Flurry of Blows"].copy(),ft("will",["",raising(1,10)])],"Stone Fist",["Stone Fist Flurry of Blows power, +",raising(1,10)," to Will defense"])]))],"monastic tradition featpick")
                    ,feat([ft("unarmed attacknameattack",["",3]),ft("unarmed attacknamedice",["",4]),ft("unarmed attacknewkey","off-hand")],"Unarmed Combatant","+3 proficiency, 1d8 damage, and offhand property for unarmed strike")
                    ,feat([ft("ac",["",lambda x: (2+x.statret("unarmoreddefense"))*(not(x.check("armortype",["heavy","shield","leather","hide"],True)))])],"Unarmored Defense","+2 AC with cloth armor or no armor and no shield")
                    ,feat([ft("skillpick",SkillPick("monk",4,"Monk Skill"))],"Class Skills")]
                    ,["Cloth","Club","Dagger","Quarterstaff","Shuriken","Sling","Spear"]
                    ,["Acrobatics","Athletics","Diplomacy","Endurance","Heal","Insight","Perception","Religion","Stealth","Thievery"]),
           "Paladin":charClass(15, 6,10, [feat([ft(["fort","ref","will"],["class",1])],"Save Bonus")
                    ,feat([ft("power",[basePowers["Channel Divinity: Divine Mettle"],basePowers["Channel Divinity: Divine Strength"],basePowers["Divine Challenge"].copy()])],"Channel Divinity","Once per encounter use a Channel Divinity power")
                     ,feat([ft("powerpick",PowerPick([basePowers["Lay on Hands"], basePowers["Ardent Vow"], basePowers["Virtue's Touch"]],0,31,"Lay on Hands Option"))],"Lay on Hands Option")
                    ,feat([specMenus["deities"]],"Worship")
                    ,feat([ft("skillpick",SkillPick("paladin",3,"Paladin Skill")),ft("religion",["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Hide","Chainmail","Scale","Plate","Light","Heavy","Simple Melee","Military Melee","Simple Ranged"]
                    ,["Diplomacy","Endurance","Heal","History","Insight","Intimidate","Religion"]),
           "Psion" :charClass(12, 4, 6, [feat([ft(["will"],["class",2])],"Save Bonus")
                    ,feat([ft("featpick",FeatPick(0, "Discipline Focus",0,
                           [feat([ft("featureadd","discipline focus"),ft("power",[basePowers["Far Hand"].copy(), basePowers["Forceful Push"].copy()])],"Telekinesis Focus","Gain the powers Far Hand and Forceful Push")
                           ,feat([ft("featureadd","discipline focus"),ft("power",[basePowers["Distract"].copy(), basePowers["Send Thoughts"].copy()])],"Telepathy Focus","Gain the powers Distract and Send Thought")]))],"discipline focus featpick")
                    ,feat([ft("feat",[allFeatList["Ritual Caster"]])],"Ritual Caster","Master and perform rituals.  Gain either Sending or Tenser's Floating Disc, and one other 1st level ritual")
                    ,feat([ft("psps",["",raiselist(1,[1,3,3,7,7,13,17,17,21,21,23,23,27,27])])],"Psionic Augmentation",["",lambda x:x.statret("psps")," Power Points; use power points each encounter to augment at-will powers."])
                    ,feat([ft("skillpick",SkillPick("psion",4, "Psion Skill"))],"Class Skills")]
                    ,["Cloth","Simple Melee","Simple Ranged"]
                    ,["Arcana","Bluff","Diplomacy","Dungeoneering","History","Insight","Intimidate","Perception"]),
           "Ranger" :charClass(12, 5, 6, [feat([ft(["fort","ref"],["class",1])],"Save Bonus")
                    ,feat([ft("featpick",FeatPick(0, "Ranger Fighting Style", 0,
                           [feat([ft("feat",[allFeatList["Defensive Mobility"]])],"Archer Fighting Style","+2 to AC against opportunity attacks"),
                            feat([ft("feat",[allFeatList["Toughness"]]), ft("onehanddual",("onehanddual",1))],"Two-Blade Fighting Style","Toughness, and can wield one-handed weapon in your off-hand"),
                            feat([basePowers["BeastAttack"]],"Beast Mastery","Tame a beast as an ally"),
                            feat([ft("feat",[allFeatList["Quick Draw"]])],"Hunter Fighting Style","Quick Draw bonus feat, sheathe as free action, +4 to AC vs. opp attacks from firing a ranged weapon"),
                            feat([ft("feat",[allFeatList["Two-Weapon Defense"]]),ft("speed",["",lambda x:"two-handed" not in x.statret("weaponkeys") and "shield" not in x.statret("armortype")])],"Marauder Fighting Style","Two weapon defense feat; +1 to speed when not using a shield or a two-handed weapon")]))],"ranger fighting style featpick")
                    ,feat([],"Hunter's Quarry",["Deal an extra ",raising(1,10),"d",lambda x:6+x.featuretotal("huntersdice"),plus(lambda x: x.featuretotal("huntersbonus"))," damage on one attack each round against your quarry"])
                    ,feat([ft("featpick",FeatPick(0, "Ranger Positioning",0,
                            [feat([],"Prime Shot","+1 on ranged attack rolls if no allies are closer to your target than you are.")
                            ,feat([],"Running Attack","If you use a standard action that lets you move at least 2 squares, gain +1 to attack rolls for that action")
                           ]))],"ranger positioning option")
                    ,feat([ft("skillpick",SkillPick("ranger",4, "Ranger Skill")),ft("skillpick",SkillPick(["Dungeoneering","Nature"],1, "Ranger Skill 2"))],"Class Skills")]
                    ,["Cloth","Leather","Hide","Simple Melee","Military Melee","Simple Ranged","Military Ranged"]
                    ,["Acrobatics","Athletics","Dungeoneering","Endurance","Heal","Nature","Perception","Stealth"]),
           "Runepriest" :charClass(12, 5, 7, [feat([ft(["will"],["class",2])],"Save Bonus")
                    ,feat([],"Rune Master","When using Runic power, attune yourself to either Rune of Destruction or Rune of Protection, and gain that benefit")
                    ,feat([],"Rune of Destruction","While you are attuned to this rune, allies gain a +1 bonus to attack rolls that are adjacent to you")
                    ,feat([],"Rune of Protection",["While you are attuned to this rune, allies adjacent to you gain resist ",raising(2,11)," to all damage"])
                    ,feat([basePowers["Rune of Mending"]],"Rune of Mending")
                    ,feat([ft("featpick",FeatPick(0, "Runic Artistry",0,
                           [feat([ft("featureadd","runic artistry")],"Defiant Word",["+",WISMOD," bonus to damage rolls against an enemy that has missed you since your last turn"])
                           ,feat([ft("featureadd","runic artistry"),ft("proficiency",weaponKeyList(["military","mace"])+weaponKeyList(["military","hammer"]))],"Wrathful Hammer",["Proficiency with military hammers and maces.  +",CONMOD," bonus to damage rolls against an enemy that has damaged you since your last turn"])]))],"runepriest featpick")
                    ,feat([ft("skillpick",SkillPick("runepriest",3, "Runepriest Skill")),ft("religion",["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Hide","Chainmail","Scale","Light","Simple Melee","Simple Ranged"]
                    ,["Arcana","Athletics","Endurance","Heal","History","Insight","Religion","Thievery"]),
           "Rogue"  :charClass(12, 5, 6, [feat([ft("ref",["class",2])],"Save Bonus")
                    ,feat([],"First Strike","Combat advantage against any creatures that have not yet acted this encounter")
                    ,feat([ft("featpick",FeatPick(0, "Rogue Tactics",0,
                           [feat([ft("featureadd","rogue tactics")],"Artful Dodger",[plus(lambda x: x.mod("cha"),1)," AC vs. Opportunity Attacks"])
                           ,feat([ft("featureadd","rogue tactics")],"Brutal Scoundrel",[plus(lambda x: x.mod("str"),1)," sneak attack damage"])
                           ,feat([ft("featureadd","rogue tactics"),ft("light bladelegal",["macename","clubname"]),ft(["rattlingdamage","macenamedamage"],["",2]),ft(["rattlingdamage","clubnamedamage"],["",2]),ft("proficiency",["club","mace"])],"Ruthless Ruffian","Club / Mace proficiency, club and mace work with light blade rogue powers, add str mod to Rattling keyword powers with club or mace")
                           ,feat([ft("featureadd","rogue tactics")],"Cunning Sneak","No penalty for stealthing more than 2 squares, only -5 for running, may make stealth check after moving 3 squares")]))],"rogue tactics featpick")
                    ,feat([ft("featpick",FeatPick(0, "Weapon Talent",0,
                              [feat([ft(["shurikennameweaponsize","daggernameattack","parrying daggernameattack"],("",1))],"Rogue weapon talent","Increased damage die for shuriken, and +1 on attacks with a dagger"),
                               feat([MultiMenu([{"crossbows":feat([ft("crossbowattack",["",1])],"crossbows"),"slings":feat([ft("slingattack",["",1])],"slings")}],["+1 to attack rolls with ",""])],"Sharpshooter Talent")
                               ]))],"weapon talent featpick")
                    ,feat([],"Sneak Attack",["Deal an extra ",raiselist(1,[1,11,21,21]),"d",lambda x:6+x.featuretotal("sneakdice"),plus(lambda x:x.featuretotal("sneakbonus"))," damage on one attack each round when you have combat advantage"])
                    ,feat([ft("skillpick",SkillPick("rogue",4, "Rogue Skill")),ft(["stealth","thievery"],["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Dagger","Hand Crossbow","Shuriken","Sling","Short Sword"]
                    ,["Acrobatics","Athletics","Bluff","Dungeoneering","Insight","Intimidate","Perception","Stealth","Streetwise","Thievery"]),
           "Seeker" :charClass(12, 5, 7, [feat([ft(["ref","will"],["class",1])],"Save Bonus")
                    ,feat([basePowers["Inevitable Shot"]],"Inevitable Shot")
                    ,feat([ft("featpick",FeatPick(0, "Seeker's Bond",0,
                           [feat([ft("featureadd","seeker's bond"), basePowers["Encaging Spirits"]],"Bloodbond","Shift as a minor action while not wearing heavy armor")
                           ,feat([ft("featureadd","seeker's bond"),basePowers["Spirits' Rebuke"], ft(["heavy thrownattack","light thrownattack"],["",1]),ft("light armor",["light armor",STRMOD])],"Spiritbond","+1 to attack rolls with thrown weapons, thrown weapons return after attack, str for light armor AC")]))],"seeker's bond featpick")
                    ,feat([ft("skillpick",SkillPick("seeker",3, "Seeker Skill")),ft("nature",["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Simple Melee","Simple Ranged","Military Ranged"]
                    ,["Acrobatics","Athletics","Endurance","Heal","Insight","Intimidate","Nature","Perception","Stealth"]),
           "Shaman"  :charClass(12, 5, 7, [feat([ft(["fort","will"],["class",1])],"Save Bonus")
                    ,feat([basePowers["Call Spirit Companion"],basePowers["Healing Spirit"], basePowers["Speak with Spirits"]],"Shaman Powers","")
                    ,feat([ft("featpick",FeatPick(0, "Companion Spirit", 0,
                           [feat([ft("featureadd","companion spirit"),basePowers["Spirit's Shield"],powerList["shamanat-will1"]["Protecting Strike"]],"Protector Spirit",["Ally adjacent to spirit regains ",CONMOD," extra hp with second wind or your healing"])
                            ,feat([ft("featureadd","companion spirit"),basePowers["Spirit's Fangs"],powerList["shamanat-will1"]["Stalker's Strike"]],"Stalker Spirit",["Ally adjacent to spirit gains a +",INTMOD," bonus to damage rolls against bloodied enemies"])
                            ,feat([ft("featureadd","companion spirit"),basePowers["Spirit's Prey"],powerList["shamanat-will1"]["Claws of the Eagle"]],"Watcher Spirit","Enemies adjacent to spirit companion can't gain cover from other enemies; allies can treat them as their nearest enemy")
                            ,feat([ft("featureadd","companion spirit"),basePowers["World Speaker's Command"],powerList["shamanat-will1"]["Voice of Battle"]],"World Speaker Spirit",["Ally who provokes opportunity attacks entering/leaving squares next to spirit companion gain +",CONMOD," defense vs. those attacks"])]))],"companion spirit featpick")
                    ,feat([ft("at-willpowers",["",-1])],"Less at will choice")
                    ,feat([ft("skillpick",SkillPick("shaman",3, "Shaman Skill")),ft("nature",["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Simple Melee","Longspear"]
                    ,["Arcana","Athletics","Endurance","Heal","History","Insight","Nature","Perception","Religion"]),
           "Sorcerer"  :charClass(12, 5, 6, [feat([ft("will",["class",2])],"Save Bonus")
                    ,feat([ft("featpick",FeatPick(0, "Spell Source",0,
                           [feat([ft("featureadd","spell source"),specMenus["dragonSoul"],ft("arcanedamage",["",lambda x:x.mod("str")+raising(2,10)(x)-2]),ft("light armor",["light armor",STRMOD])],"Dragon Magic","")
                            ,feat([ft("featureadd","spell source"),ft("arcanedamage",["",lambda x:x.mod("dex")+raising(2,10)(x)-2])],"Storm Magic",["Gain resist ",raising(5,10)," thunder and lightning.  Your arcane powers ignore resistance up to this value while active."])
                            ,feat([ft("featureadd","spell source"),ft("arcanedamage",["",lambda x:x.mod("dex")+raising(2,10)(x)-2])],"Wild Magic",["Gain resist ",raising(5,10)," to a random element each day.  Your arcane powers ignore up to ",raising(5,10)," resistance of this element."])
                            ,feat([ft("featureadd","spell source"),ft("arcanedamage",["",lambda x:x.mod("str")+raising(2,10)(x)-2]),ft("light armor",["light armor",STRMOD])],"Cosmic Magic",["Your arcane powers ignore up to ",raising(5,10)," resistance of the type granted by your cosmic cycle."])]))],"spell source featpick")
                    ,feat([],"Arcane Power",[orfeat("",["+",lambda x:x.mod("str")+raising(2,10)(x)-2," damage with arcane powers; can use Str to determine AC"],"dragon magic")
                                            ,orfeat("",["+",lambda x:x.mod("dex")+raising(2,10)(x)-2," damage with arcane powers, if first attack each round is even, +1 AC, else make a saving throw."],"wild magic")
                                            ,orfeat("",["+",lambda x:x.mod("dex")+raising(2,10)(x)-2," damage with arcane powers, with natural 20 on attack roll, push 1 square and you can fly ",lambda x:x.mod("dex")+1," squares."],"storm magic")
                                            ,orfeat("",["+",lambda x:x.mod("str")+raising(2,10)(x)-2," damage with arcane powers, can use Str to determine AC"],"cosmic magic")])            
                    ,feat([],"Arcane Boon",["",orfeat("","First time bloodied in encounter, gain +2 to AC until the end of encounter","dragon magic")
                                              ,orfeat("","With nat 20 on attack for arcane power, slide target 1 square and knock it prone.  On nat 1, push all in 5 1 square.","wild magic")
                                              ,orfeat("","Lose resistance as interrupt to gain +4 all defenses until end of next turn; regain resistance after short rest","storm magic")
                                              ,orfeat("","Choose cycle each rest, go to next cycle when first bloodied.","storm magic")])
                    ,feat([],"1. Phase of the Sun",["",orfeat("",["At start of your turn, adjacent enemies take ",STRMOD," fire and radiant damage.  Resist ",raising(5,10)," cold."],"cosmic magic")])
                    ,feat([],"2. Phase of the Moon",["",orfeat("",["Gain a bonus to AC equal to the number of conscious enemies adjacent to you.  Resist ",raising(5,10)," psychic."],"cosmic magic")])
                    ,feat([],"3. Phase of the Stars",["",orfeat("",["Whenever an enemy's attack misses you, you can teleport ",STRMOD," squares as a free action.  Resist ",raising(5,10)," radiant."],"cosmic magic")])
                    ,feat([ft("skillpick",SkillPick("sorcerer",3, "Sorcerer Skill")),ft("arcana",["training",5])],"Class Skills")]
                    ,["Cloth","Simple Melee","Simple Ranged"]
                    ,["Arcana","Athletics","Bluff","Diplomacy","Dungeoneering","Endurance","History","Insight","Intimidate","Nature"]),
           "Swordmage" :charClass(15, 6, 8, [feat([ft(["will"],["class",2])],"Save Bonus")
                    ,feat([],"Swordbond","Meditate to bond with weapon, can call that weapon from 10 squares away as standard action, or repair it in 1 hour for free")
                    ,feat([ft("powerpick",PowerPick([basePowers["Aegis of Assault"], basePowers["Aegis of Shielding"], basePowers["Aegis of Ensnarement"]],0,31,"swordmage aegis")),ft("featureadd","swordmage aegis")],"Swordmage Aegis")
                    ,feat([ft("ac",["",lambda x:("heavy blade" in x.statret("weapongroups") or "light blade" in x.statret("weapongroups"))])],"Swordmage Warding","+1 AC, or +3 AC with a blade in one hand and the other hand free.  Must have a short rest to recover after falling unconscious.")
                    ,feat([ft("skillpick",SkillPick("swordmage",3, "Swordmage Skill")),ft("arcana",["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Simple Melee","Simple Ranged","Military Light Blades","Military Heavy Blades"]
                    ,["Arcana","Athletics","Diplomacy","Endurance","History","Insight","Intimidate"]),
           "Warden":charClass(17, 7, 9, [feat([ft(["fort","will"],["class",1])],"Save Bonus")
                    ,feat([ft("featpick",FeatPick(0, "Warden Guardian Might",0,
                           [feat([ft("light armor",["light armor",CONMOD])],"Earthstrength",["While in light armor, can use Con to determine AC; +",CONMOD," AC with second wind"])
                           ,feat([ft("light armor",["light armor",WISMOD])],"Lifespirit","While in light armor, can use Wis to determine AC; an ally in 5 squares of you can spend healing surge and make a saving throw with your second wind")
                           ,feat([ft("light armor",["light armor",CONMOD])],"Stormheart",["While in light armor, can use Con to determine AC; with second wind, slow each marked enemy and pull marked enemies in 2 squares 1 square"])
                           ,feat([ft("light armor",["light armor",WISMOD])],"Wildblood",["While in light armor, can use Wis to determine AC; marked enemies at -",WISMOD," to hit allies with second wind"])]))],"guardian might featpick")
                    ,feat([ft("power",[basePowers["Warden's Fury"],basePowers["Warden's Grasp"]])],"Nature's Wrath powers")
                    ,feat([],"Font of Life","At the start of your turn, make a sving throw against one effect that a save can end.")
                    ,feat([],"Nature's Wrath","Once during each turn, you can mark each adjacent enemy as a free action.")
                    ,feat([ft("skillpick",SkillPick("warden",3, "Warden Skill")),ft("nature",["training",5])],"Class Skills")]
                    ,["Cloth","Leather","Hide","Light Shield","Heavy Shield","Simple Melee","Military Melee","Simple Ranged"]
                    ,["Athletics","Dungeoneering","Endurance","Heal","Intimidate","Nature","Perception"]),
           "Warlock":charClass(12, 5, 6, [feat([ft(["ref","will"],["class",1])],"Save Bonus")
                    ,feat([ft("featpick",FeatPick(0, "Warlock Pact", 0
                            ,[feat([ft("addfeature","warlock pact"),powerList["warlockat-will1"]["Eyebite"]],"Fey Pact",["Teleport ",lambda x:3+x.featuretotal("mistystep")," squares when cursed enemy drops to 0"])
                             ,feat([ft("addfeature","warlock pact"),powerList["warlockat-will1"]["Hellish Rebuke"]],"Infernal Pact",["Gain ",lambda x:x.statret("level")+x.featuretotal("infernalpact")," temporary hit points when cursed enemy drops to 0"])
                             ,feat([ft("addfeature","warlock pact"),powerList["warlockat-will1"]["Dire Radiance"]],"Star Pact",["Gain a +",lambda x:1+x.featuretotal("starpact")," cumulative bonus to one d20 roll when cursed enemy drops to 0"])
                             ,feat([ft("addfeature","warlock pact"),powerList["warlockat-will1"]["Spiteful Glamor"],basePowers["Darkspiral Aura"]],"Dark Pact",["Gain 1 Darkspiral Aura point when a cursed enemy drops to 0.  Points reset to 0 after a short or extended rest."])
                             ,feat([ft("addfeature","warlock pact"),powerList["warlockat-will1"]["Eyes of the Vestige"]],"Vestige Pact","Pick vestige at during short rest or by daily power; gain vestige pact boon when when a cursed enemy drops to 0")]))],"warlock pact featpick")
                    ,feat([ft("power",[powerList["warlockat-will1"]["Eldritch Blast"]])],"Eldritch Blast")
                    ,feat([],"Vestige: King Elidyr",orfeat("",["Pact Boon: One adjacent ally gainst +2 to all defenses until end of your next turn"],"vestige pact"))
                    ,feat([],"Vestige: Zutwa",orfeat("","Pact Boon: Prime Shot bonus increases to +3 until end of your next turn","vestige pact"))
                    ,feat([],"Prime Shot","+1 on ranged attack rolls if no allies are closer to your target than you are.")
                    ,feat([],"Shadow Walk","If you move at least 3 squares from where you started on your turn, gain concealment")
                    ,feat([],"Warlock's Curse",["Curse nearest enemy as minor action, deal ",raising(1,10),"d",lambda x:6+x.featuretotal("cursedice"),plus(lambda x:x.featuretotal("cursebonus"))," extra damage against cursed foes"])
                    ,feat([ft("at-willpowers",["",-2])],"No at will choice")
                    ,feat([ft("skillpick",SkillPick("warlock",4, "Warlock Skill"))],"Class Skills")]
                    ,["Cloth","Leather","Simple Melee","Simple Ranged"]
                    ,["Arcana","Bluff","History","Insight","Intimidate","Religion","Streetwise","Thievery"]),
           "Warlord":charClass(12, 5, 7, [feat([ft(["fort","will"],["class",1])],"Save Bonus")
                    ,feat([ft("featpick",FeatPick(0,"Combat Style", 0
                            ,[feat([ft("proficiency","chainmail"),ft("proficiency","light")],"Armored Warlord","Proficiency with Chainmail and Light Shields")
                             ,feat([ft("feat",[militaryRanged]),ft(["and","bowattack","basic attackattack"],("stat change",lambda x:max(x.mod("dex"), x.mod("str"))-x.mod("dex"))),ft(["and","bowdamage","basic attackdamage"],("stat change",lambda x:max(x.mod("dex"), x.mod("str"))-x.mod("dex")))],"Archer Warlord","Proficiency with Military Ranged weapons; can use Str instead of Dex for basic attack with a bow")
                              ]))],"combat style featpick")
                    ,feat([ft("featpick",FeatPick(0,"Leadership Bonus", 0
                            ,[feat([ft("combatleader",("combatleader",2))],"Combat Leader",["Each ally in 10 squares that can see and hear you gains a +",lambda x:x.statret("combatleader")," power bonus to initiative"])
                              ,feat([ft("cannyleader",("cannyleader",2)),ft(["insight","perception"],["",lambda x:x.statret("cannyleader")])],"Canny Leader",["You and each ally in 10 squares that can see and hear you gains a +",lambda x:x.statret("cannyleader")," bonus to Insight and Perception checks"])
                              ]))],"leadership bonus featpick")
                    ,feat([ft("featpick",FeatPick(0,"Commanding Presence", 0
                            ,[feat([ft("addfeature","commanding presence")],"Inspiring Presence",["Ally who sees you & spends AP for an extra action regains ",lambda x:x.statret("level")/2+x.mod("cha")+x.featuretotal("inspiringpresencehp")," hp"])
                             ,feat([ft("addfeature","commanding presence")],"Tactical Presence",["Ally who sees you & spends an AP to attack gains a ",plus(lambda x:x.mod("int")/2+x.statret("tacticalpresenceatk"),1)," bonus to the attack"])
                             ,feat([ft("addfeature","commanding presence")],"Bravura Presence","Ally who attacks with AP gains basic attack or move action on a hit, or grants combat advantage on a miss")
                             ,feat([ft("addfeature","commanding presence")],"Resourceful Presence",["Ally who spends AP to attack gains +",lambda x:x.mod("int")+x.statret("level")/2+x.statret("resourcefuldmg")," damage.  If attack doesn't hit, ally gains +",lambda x:x.mod("cha")+x.statret("level")/2+x.statret("resourcefulhp")," temporary HP"])
                             ,feat([ft("addfeature","commanding presence")],"Insightful Presence",["Ally who spends AP for an extra action gains +",lambda x:max(x.mod("wis")/2, x.mod("cha")/2)," to all defenses until end of your next turn"])
                             ,feat([ft("addfeature","commanding presence")],"Skirmishing Presence",["Ally who spends AP to attack can use a free action to shift ",lambda x:max(x.mod("int"),x.mod("wis"))," square(s) before or after the attack"])]))],"commanding presence featpick")
                    ,feat([ft("power",[basePowers["Inspiring Word"]])],"Inspiring Word")
                    ,feat([ft("skillpick",SkillPick("warlord",4,"Warlord Skill"))],"Class Skills")]
                    ,["Cloth","Leather","Hide","Simple Melee","Military Melee","Simple Ranged"]
                    ,["Athletics","Diplomacy","Endurance","Heal","History","Intimidate"]),
           "Wizard" :charClass(10, 4, 6, [feat([ft("will",["class",2])],"Save Bonus")
                    ,feat([specMenus["implementMastery"]],"Implement Mastery")
                    ,feat([ft("power",[basePowers["Prestidigitation"],basePowers["Mage Hand"],basePowers["Light"],basePowers["Ghost Sound"]])],"Wizard At-wills")
                    ,feat([ft("feat",[allFeatList["Ritual Caster"]])],"Ritual Caster","Master and perform rituals")
                    ,feat([ft("powerpick",PowerPick(powerList["wizarddaily1"].values(),1, 15, "Spellbook Daily 1")),ft("powerpick",PowerPick(powerList["wizarddaily5"].values(),5, 19, "Spellbook Daily 5")),ft("powerpick",PowerPick(powerList["wizarddaily9"].values(),9, 25, "Spellbook Daily 9")),ft("powerpick",PowerPick(powerList["wizarddaily15"].values(),15, 29, "Spellbook Daily 15")),ft("powerpick",PowerPick(powerList["wizarddaily19"].values(),19, 31, "Spellbook Daily 19")),ft("powerpick",PowerPick(powerList["wizarddaily25"].values(),25, 31, "Spellbook Daily 25")),ft("powerpick",PowerPick(powerList["wizarddaily29"].values(),29, 31, "Spellbook Daily 29"))
                          ,ft("powerpick",PowerPick(powerList["wizardutility2"].values(),2, 31, "Spellbook Utility 2")),ft("powerpick",PowerPick(powerList["wizardutility6"].values(),6, 31, "Spellbook Utility 6")),ft("powerpick",PowerPick(powerList["wizardutility10"].values(),10, 31, "Spellbook Utility 10")),ft("powerpick",PowerPick(powerList["wizardutility16"].values(),16, 31, "Spellbook Utility 16")),ft("powerpick",PowerPick(powerList["wizardutility22"].values(),19, 31, "Spellbook Utility 22"))
                    ],"Spellbook","Holds an additional daily and utility spell of each level you can cast")
                    ,feat([ft("skillpick",SkillPick("wizard",3, "Wizard Skill")),ft("arcana",["training",5])],"Class Skills")]
                    ,["Cloth","Dagger","Quarterstaff"]
                    ,["Arcana","Diplomacy","Dungeoneering","History","Insight","Nature","Religion"])}