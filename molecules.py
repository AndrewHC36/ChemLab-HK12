# BOND TYPE: 1: Single, 2: Double, 3: Triple, 4: Quadruple

MOLECULES = {
	"Water": [
		["H", (20, 20), 0, {}],
		["H", (140, 20), 1, {}],
        ["O", (80, 80), 2, {0:1, 1:1}]
    ],
	"Carbon Dioxide": [
		["O", (-10, 80), 0, {}],
		["O", (180, 80), 1, {}],
		["C", (80, 80), 2, {0:2, 1:2}],
	],
	"Ammonia": [
		["H", (20, 20), 0, {}],
		["H", (140, 20), 1, {}],
		["H", (80, 160), 2, {}],
		["N", (80, 80), 3, {0:1, 1:1, 2:1}],
	],
	"Hydrogen Gas": [
		["H", (20, 20), 0, {}],
		["H", (80, 20), 1, {0:1}],
	],
	"Oxygen Gas": [
		["O", (20, 20), 0, {}],
		["O", (20, 120), 1, {0:2}],
	],
	"Nitrogen Gas": [
		["N", (20, 20), 0, {}],
		["N", (20, 120), 1, {0:3}],
	],
	"Nitric Oxide" : [
		["O", (20, 20), 0, {}],
		["N", (80, 20), 1, {0:2}]
	],
	"Carbon Ring": [  # Benzene Ring
		["C", (20, 20), 0, {1:1}],
		["C", (120, -40), 1, {2:2}],
		["C", (220, 20), 2, {3:1}],
		["C", (220, 140), 3, {4:2}],
		["C", (120, 200), 4, {5:1}],
		["C", (20, 140), 5, {0:2}],
	],
	"Hydrogen Fluoride": [
		["H", (20, 20), 0, {}],
		["F", (20, 100), 1, {0:1}],
	],
	"Phosphine": [
		["H", (-40, -40), 0, {}],
		["H", (80, -40), 1, {}],
		["H", (20, 100), 2, {}],
		["P", (20, 20), 3, {0:1, 1:1, 2:1}],
	],
	"Hydrogen Sulfide": [
		["H", (80, -40), 0, {}],
		["H", (-40, -40), 1, {}],
		["S", (20, 20), 2, {0:1, 1:1}],
	],
	"Methane": [
		["H", (80, -40), 0, {}],
		["H", (-40, -40), 1, {}],
		["H", (80, 80), 2, {}],
		["H", (-40, 80), 3, {}],
		["C", (20, 20), 2, {0:1, 1:1, 2:1, 3:1}],
	],
	"Nitrogen Triiode":[
		["N",[20,20],0,{1:1,2:1,3:1}],
		["I",[20,80],1,{}],
		["I",[40,10],2,{}],
		["I",[0,10],3,{}]
	],
	"Phosphorus Fluoride":[
		["P",[20,20],0,{1:1,2:1,3:1,4:1,5:1}],
		["F",[-30,20],1,{}],
		["F",[70,20],2,{}],
		["F",[20,80],3,{}],
		["F",[70,-10],4,{}],
		["F",[-30,-10],5,{}],
	],
	"Sulfur Fluoride":[
		  ["S",[20,20],0,{1:1}],
		  ["F",[80,20],1,{}]
	],
	"Iodine Pentafluoride" : [
		["I",[20,20],0,{1:1,2:1,3:1,4:1,5:1}],
		["F",[-30,-40],1,{}],
		["F",[70,-40],2,{}],
		["F",[20,120],3,{}],
		["F",[100,40],4,{}],
		["F",[-60,40],5,{}],
	],
	"Sulfur Iodine Cycle" : [
	  ["S",[20,20],0,{1:1}],
	  ["I",[80,20],1,{}]
	],
	"Carbon Tetrafluoride" : [
	  ["C",[20,20],0,{1:1,2:1,3:1,4:1}],
	  ["F",[20,80],1,{}],
	  ["F",[20,-40],2,{}],
	  ["F",[80,20],3,{}],
	  ["F",[-40,20],4,{}]
	],
	"Carbon Tetraiodide" : [
	  ["C",[20,20],0,{1:1,2:1,3:1,4:1}],
	  ["I",[20,80],1,{}],
	  ["I",[20,-40],2,{}],
	  ["I",[80,20],3,{}],
	  ["I",[-40,20],4,{}]
	],
	"Nitrogen Trifluoride" : [
	  ["N",[20,20],0,{1:1,2:1,3:1}],
	  ["F",[20,120],1,{}],
	  ["F",[120,20],1,{}],
	  ["F",[-80,20],1,{}]
	],
	"Sulfur Monotride": [
	  ["S",[20,20],0,{1:1}],
	  ["N",[20,100],1,{}],
	],
	"Carbon Disulfide": [
	  ["C",[20,20],0,{1:1,2:1}],
	  ["S",[120,20],1,{}],
	  ["S",[-80,20],2,{}],
	],
	"Hydrogen Iodine": [
	  ["H",[20,20],0,{1:1}],
	  ["I",[20,100],1,{}]
	],
	"Oxygen Diflouride": [
	  ["O",[20,20],0,{1:1,2:1}],
	  ["F",[120,20],1,{}],
	  ["F",[-80,20],2,{}],
	],
	"Sulfur Oxide": [
	  ["O",[20,20],0,{1:1}],
	  ["S",[20,80],1,{}]
	],
	"Phosphorus Pentoxide": [
		["P",[20,20],0,{}],
		["P",[120,20],1,{}],
		["O",[70,-60],2,{0:1,1:1}],
		["O",[-40,-60],3,{0:1}],
		["O",[180,-60],4,{1:1}],
		["O",[20,120],5,{0:2}],
		["O",[120,120],6,{1:2}]
	],
	"Hydrogen":[["H",[20,20],0,{}]],
	"Carbon":[["C",[20,20],0,{}]],
	"Nitrogen":[["N",[20,20],0,{}]],
	"Flouride":[["F",[20,20],0,{}]],
	"Phosphorus":[["P",[20,20],0,{}]],
	"Sulfur":[["S",[20,20],0,{}]],
	"Iodine":[["I",[20,20],0,{}]],
	"Tetraphosphorus Trisulfide" : [
	  ["P",[20,20],0,{1:1,2:1,3:1}],
	  ["S",[-100,220],1,{4:1}],
	  ["S",[20,220],2,{5:1}],
	  ["S",[140,220],3,{6:1}],
	  ["P",[-100,420],4,{5:1}],
	  ["P",[20,340],5,{6:1}],
	  ["P",[140,420],6,{4:1}],
	],
	"Fluorine Gas": [
		["F", (20, 20), 0, {}],
		["F", (140, 20), 1, {0:1}],
	],


	"Random": [
		["H", (20, 20), 0, {}],
		["C", (100, 20), 0, {}],
		["N", (100, 100), 0, {}],
		["O", (20, 100), 0, {}],
		["F", (200, 200), 0, {}],
		["P", (200, 100), 0, {}],
		["S", (200, 20), 0, {}],
	]
}

# ENERGY = {
# 	"Fire": [(255,100,0)]
#
# }

INFO = {
	"Water": [
		"Has a high specific heat",
		"which means it uses a lot",
		"of energy to only heat a",
		"the water only a little bit",
    ],
	"Carbon Dioxide": [
		"Produced by burning carbon-based plants",
		"or literally any living things!",
		"It is poisonous when in mass",
		"to animals or cells that does",
		"not use CO2 as a reactant",
    ],
	"Ammonia": [
		"Like bleach, it is used in cleaner product.",
    ],
	"Hydrogen Gas": [
		"Flammable gas!",
		"Used in balloon in the old days.",
	],
	"Oxygen Gas":[
		"The gas we and the animals breathe in!",
	],
	"Nitrogen Gas":[
		"Essential for plant growth. Also ease",
		"us for breathing air since breathing",
		"in pure Oxygen actually is painful!"
	],
	"Carbon Ring":[
		"Carbon Ring"
	],
	"Hydrogen Floride" : [
	  "Mainly used for carving windows",
	  "It is very commonly used"
	],
	"Phosphine" : [
	  "A very useful thing to kill bug"
	],
	"Hydrogen Sulfide" : [
	  "Poison, you died"
	],
	"Hydrogen Iodine" : [
	  "Used to clean things",
	  "mainly used in hospitals",
	  "for patients to clean their hands"
	],
	"Nitric Oxide" : [
	  "Contained in the human body",
	  "a substance human body uses to",
	  "control blood all over the body"
	],
	"Oxygen Diflouride" : [
	  "Toxic"
	],
	"Phosphorus Pentoxide" : [
	  "used to make dryers",
	  "which are things that clear",
	  "water on clothes and stuff"
	],
	"Sulfur Oxide" : [
	  "used to obtain food for a",
	  "really long time, almost",
	  "any none nature food one",
	  "eats contains this in it"
	],
	"Iodine Pentoxide" : [
	  "using this will convert the",
	  "carbon monoxide into carbon",
	  "dioxide in an area"
	],
	"Carbon Nitride" : [
	  "a very new discovery, many",
	  "were really impressed after",
	  "the discovery of this substance",
	  "the hardest stone on earth is",
	  "diamond, and carbon nitride is",
	  "harder than diamond"
	],
	"Carbon Tetrafluoride" : [
	  "Used to make insulator, which",
	  "is very useful since all your",
	  "phones or computers' chargers",
	  "have to be made out of insulator"
	],
	"Carbon Disulfide" : [
	  "Can be used to make fibers",
	  "which care used to make clothes"
	],
	"Carbon Tetraiodide" : [
	  "Used to combine certain chemical",
	  "substances"
	],
	"Nitrogen Trifluoride" : [
	  "used to make electric circuit",
	  "in phones, computers, and tv"
	],
	"Sulfur Monitride" : [
	  "used to merge metals into",
	  "different another metal"
	],
	"Nitrogen Triiodide" : [
	  "Very easily to explode",
	  "You can make homemade",
	  "bombs or fireworks with it"
	],
	"Phosphorus Fluoride" : [
	  "Poison, you died"
	],
	"Sulfur Floride": [
	  "used to make chips for",
	  "computers, phones, and",
	  "many other electric devices"
	],
	"Iodine Pentafluoride" : [
	  "used to make batteries"
	],
	"Tetraphosphorus Trisulfide": [
	  "used to make fireworks and",
	  "matches"
	],
	"Sulfur Iodine Cycle" : [
	  "used to make oxygen and hydrogen"
	],
	"Hydrogen" : [
	  "when mixed with oxygen, can",
	  "create extreme heat to cut",
	  "metals, used for manufacture"
	],
	"Carbon": [
	  "makes up the basic matter",
	  "of life, all life on earth",
	  "are called carbon based life"
	],
	"Nitrogen" : [
	  "Essential element for plant",
	  "to live and grow"
	],
	"Fluoride" : [
	  "mainly used to make medicine"
	],
	"Phosphorus" : [
	  "essential for human life, having",
	  "too less or too much of it will",
	  "cause sickness"
	],
	"Sulfur" : [
	  "used to make gunpowder"
	],
	"Iodine" : [
	  "essential for life on earth, human",
	  "take in sulfur by eating salt"
	],
	"Methane": [
		"Fuel used in factory for electricity.",
		"Effects the atmosphere in the Earth",
		"to be warmer",
	],
	"Fire": [
		"To burn chemicals and other flammable objects."
	],
	"Pressure": [
		"To make gas, liquid, or solid molecules",
		"to come more tightly pack. Since it is",
		"more tightly pack, some reaction can",
		"occur due to more contact.",
	],
	"Fluorine Gas": [
		"Main application is to make fluoride"
	]
}

PROCESS = {

}

REACTION = [
	[["Hydrogen Gas", "Hydrogen Gas", "Oxygen Gas"], ["Water", "Water"]],
	[["Methane", "Oxygen Gas", "Oxygen Gas", "Fire"], ["Carbon Dioxide", "Water", "Water"]],
	[["Nitrogen Gas", "Hydrogen Gas", "Hydrogen Gas", "Hydrogen Gas", "Pressure"], ["Ammonia", "Ammonia"]],
	[["Fluorine Gas", "Fluorine Gas", "Fluorine Gas", "Nitrogen Gas",], ["Nitrogen Trifluoride", "Nitrogen Trifluoride"]],
]
