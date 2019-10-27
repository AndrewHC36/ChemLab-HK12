import pygame as p
from pygame.locals import *
import ctypes; ctypes.windll.user32.SetProcessDPIAware(); del ctypes

from chemistry import Base, Energy
from gui import Button, SearchBox, TextBox
from molecules import MOLECULES, INFO

p.init()

fps = 60
clock = p.time.Clock()

width, height = 1920, 1080
surface = p.display.set_mode( (width, height), p.FULLSCREEN )
#  surface = p.display.set_mode( (1000, 1000), )

"""
There are 3 main pages: Home, ChemLab, Explorer

Home - Intro, Help, Tutorial, etc.

ChemLab (Chemistry Laboratory) - Mix all the discovered chemicals into something new through reaction and processes

Explorer - Explore new molecules through the environment using the explorer, clicking an object can either give you
the molecule, a selection of molecule, or zoom into that object for further exploration
"""
PAGE = "ChemLab"
GO = []  # graphic object
GO_HOME = []  # graphic object @ home
GO_CLAB = []  # graphic object @ ChemLab
GO_EXPL = []  # graphic object @ Explorer
OBJECT = []  # this is list of chemical; automatically in the ChemLab

# button functions
def switch_home():
	global PAGE
	PAGE = "Home"

def switch_chemlab():
	global PAGE
	PAGE = "ChemLab"

def switch_explorer():
	global PAGE
	PAGE = "Explorer"

def add_molecules(name):
	OBJECT.append(Base(MOLECULES[name], name, [200, 200]))

def add_energy(name, color):
	OBJECT.append(Energy(name, color, [200, 100], [200, 200]))

molecules = {a.lower():[add_molecules, a] for a in MOLECULES}

energy = {
	"fire":[add_energy, "Fire", (255, 100, 0)],
	"pressure":[add_energy, "Pressure", (150, 220, 220)],
}

molecules.update(energy)

GO.append(Button([0, 0, 80, 30], (255, 200, 200), "Home", switch_home, fnt_size=18))
GO.append(Button([85, 0, 120, 30], (255, 200, 200), "ChemLab", switch_chemlab, fnt_size=18))
GO.append(Button([210, 0, 100, 30], (255, 200, 200), "Explorer", switch_explorer, fnt_size=18))

GO_CLAB.append(SearchBox([20, 150, 200, 30], molecules, "mol"))
GO_CLAB.append(TextBox([1500, 50, 420, 1030], (200, 200, 200), ["Empty"]))
# atom data: [atom id, pos, uniq id, bond[uniq_id]]

GO_HOME.append(TextBox([500, 30, 800, 1000], (200, 200, 200),
                       ["Welcome to the Chemistry Lab!",
                        "This is educational software to help people 'learn' chemistry",
                        "Got demotivated after spending three hours of modeling the molecules"
                        ]))

molc_info = []  # molecule info
event = []
app_loop = True
while app_loop:
	surface.fill( (255, 255, 255) )
	event = p.event.get()

	on_trg, off_trg = False, False
	for e in event:
		if e.type == QUIT:
			app_loop = False
		elif e.type == KEYDOWN:
			if e.key == K_ESCAPE: app_loop = False
		elif e.type == MOUSEBUTTONDOWN: on_trg = True
		elif e.type == MOUSEBUTTONUP: off_trg = True

	if PAGE == "ChemLab":
		for o in OBJECT:
			o.update( p.mouse.get_pos(), on_trg, off_trg, OBJECT )
			o.render( surface, )
			if o.SELECTED:
				if type(o) == Base:
					molc_info = INFO[o.MOLECULE]
				else:
					molc_info = INFO[o.name]

	for g in GO:
		g.update( p.mouse.get_pos(), on_trg, off_trg, event )
		g.render( surface, )

	if PAGE == "Home":
		for o in GO_HOME:
			o.update( p.mouse.get_pos(), on_trg, off_trg, event )
			o.render( surface, )
	elif PAGE == "ChemLab":
		for o in GO_CLAB:
			if type(o) == TextBox:
				o.txt = molc_info
			o.update( p.mouse.get_pos(), on_trg, off_trg, event )
			o.render( surface, )
	elif PAGE == "Explorer":
		for o in GO_EXPL:
			o.update( p.mouse.get_pos(), on_trg, off_trg, event )
			o.render( surface, )

	p.display.flip()
	clock.tick( fps )

p.quit()
quit()
