# molecules for each chemistry

import pygame as p
from molecules import REACTION, MOLECULES

# non-metal atoms defined
NON_METALS = {
	# Atom ID: [Atom Name, Size, Colour]
	"H": ["Hydrogen", 25, (200, 200, 200)],
	"C": ["Carbon", 37, (100, 100, 100)],
	"N": ["Nitrogen", 38, (150, 100, 150)],
	"O": ["Oxygen", 40, (255, 0, 0)],
	"F": ["Fluorine", 43, (100, 200, 200)],
	"P": ["Phosphorus", 48, (240, 100, 50)],
	"S": ["Sulfur", 50, (255, 200, 0)],
	# =========================================
	"Cl": ["Chlorine", 30, (200, 200, 200)],
	"Se": ["Selenium", 30, (200, 200, 200)],
	"Br": ["Bromine", 30, (200, 200, 200)],
	"I": ["Iodine", 30, (200, 200, 200)],
}

MOLECULE = {
	"Glucose": {"C":6, "H":12, "O":6},
}


class Base:
	POSITION = [None, None]
	ATOM_DATA = []  # atom data [atom id, relative pos, id, bond, bond_type (single, double, triple, quadruple)]
	MOLECULE = ""  # molecule name
	SELECTED = False
	OFS = [None, None]  # offset when dragging

	def __init__(self, atom_data, mol, pos,):
		# [[atom id, position, bonded[]]]
		self.ATOM_DATA = atom_data
		self.POSITION = pos
		self.MOLECULE = mol
		pos = [a[1] for a in atom_data]
		# print(pos)
		posx, posy = zip(*pos)
		self.max_size = [max(posx), max(posy)]  # width, length, maximum size

	def _update( self, mouse_pos, on_trig, off_trig, atom, obj):
		clicked = True in [o.SELECTED for o in obj]

		if self.SELECTED:
			self.POSITION[0] = mouse_pos[0]+self.OFS[0]
			self.POSITION[1] = mouse_pos[1]+self.OFS[1]

		if mouse_pos[0]-NON_METALS[atom[0]][1] < self.POSITION[0]+atom[1][0] < mouse_pos[0]+NON_METALS[atom[0]][1] and \
				mouse_pos[1]-NON_METALS[atom[0]][1] < self.POSITION[1]+atom[1][1] < mouse_pos[1]+NON_METALS[atom[0]][1] and \
				on_trig and not self.SELECTED and not clicked:
			self.SELECTED = True
			self.OFS = [self.POSITION[0]-mouse_pos[0], self.POSITION[1]-mouse_pos[1]]

		if off_trig:
			self.SELECTED = False
			self.OFS = [None, None]

	def _single_atom( self, surf, atom ):
		p.draw.circle( surf, NON_METALS[atom[0]][2], [self.POSITION[0]+atom[1][0], self.POSITION[1]+atom[1][1]],
		               NON_METALS[atom[0]][1] )

		fnt = p.font.SysFont( 'times', int(NON_METALS[atom[0]][1]/1.5), bold=True)
		txt = fnt.render( atom[0], False, (0, 0, 0) )
		textRect = txt.get_rect()
		surf.blit( txt, [self.POSITION[0]+atom[1][0]-textRect[2]/2, self.POSITION[1]+atom[1][1]-textRect[3]/2] )

	def _bonds( self, surf, atom, ):
		atom_spec = []  # atom data got from specified atoms to render bond
		bond_type = atom[3]
		for adt in self.ATOM_DATA:
			if adt[2] in list(atom[3]):
				atom_spec.append( adt )

		for aext in atom_spec:  # iterating to the specified atom to render bond with
			bond = bond_type[aext[2]]
			if bond == 1:
				p.draw.line(surf, (0,0,0), [self.POSITION[0]+atom[1][0], self.POSITION[1]+atom[1][1]],
						[self.POSITION[0]+aext[1][0], self.POSITION[1]+aext[1][1]], 4)
			elif bond == 2:
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0]-4, self.POSITION[1]+atom[1][1]-4],
				             [self.POSITION[0]+aext[1][0]-4, self.POSITION[1]+aext[1][1]-4], 4 )
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0]+4, self.POSITION[1]+atom[1][1]+4],
				             [self.POSITION[0]+aext[1][0]+4, self.POSITION[1]+aext[1][1]+4], 4 )
			elif bond == 3:
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0]-8, self.POSITION[1]+atom[1][1]-8],
				             [self.POSITION[0]+aext[1][0]-8, self.POSITION[1]+aext[1][1]-8], 4 )
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0], self.POSITION[1]+atom[1][1]],
				             [self.POSITION[0]+aext[1][0], self.POSITION[1]+aext[1][1]], 4 )
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0]+8, self.POSITION[1]+atom[1][1]+8],
				             [self.POSITION[0]+aext[1][0]+8, self.POSITION[1]+aext[1][1]+8], 4 )
			elif bond == 4:
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0]-12, self.POSITION[1]+atom[1][1]-12],
				             [self.POSITION[0]+aext[1][0]-12, self.POSITION[1]+aext[1][1]-12], 4 )
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0]-4, self.POSITION[1]+atom[1][1]-4],
				             [self.POSITION[0]+aext[1][0]-4, self.POSITION[1]+aext[1][1]-4], 4 )
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0]+4, self.POSITION[1]+atom[1][1]+4],
				             [self.POSITION[0]+aext[1][0]+4, self.POSITION[1]+aext[1][1]+4], 4 )
				p.draw.line( surf, (0, 0, 0), [self.POSITION[0]+atom[1][0]+12, self.POSITION[1]+atom[1][1]+12],
				             [self.POSITION[0]+aext[1][0]+12, self.POSITION[1]+aext[1][1]+12], 4 )

	def _collision_mixer( self, molc_obj, off_trig ):
		if off_trig:
			COLLIDED = []
			for ind, i in enumerate(molc_obj):
				COLLIDE_TO = []  # collision to the object /i/
				for k in molc_obj[:ind]:
					if (i.POSITION[0] < k.POSITION[0] < i.POSITION[0]+i.max_size[0] and
							i.POSITION[1] < k.POSITION[1] < i.POSITION[1]+i.max_size[1]) or \
							(k.POSITION[0] < i.POSITION[0] < k.POSITION[0]+k.max_size[0] and
							 k.POSITION[1] < i.POSITION[1] < k.POSITION[1]+k.max_size[1]):
						COLLIDE_TO.append(k)
				if len(COLLIDE_TO) > 0:
					COLLIDE_TO.append(i)
					COLLIDED.append(COLLIDE_TO)
			return COLLIDED

	def _mix_reactant( self, collided, lst ):
		if collided not in [[], None]:
			for reactant in collided:
				reactant_lcl = reactant.copy()
				name_mn = []
				for n in reactant_lcl:
					if type(n) == Base: name_mn.append(n.MOLECULE)
					elif type(n) == Energy: name_mn.append(n.name)
				for req in REACTION:
					name = name_mn.copy()
					PASSED = True
					for a in req[0]:
						if a in name:
							name.remove(a)
						else:  # requirement /a/ is not in the reactant
							PASSED = False
							break

					if len(name) == 0 and PASSED:  # to prevent confusion, we'll only allow if the requirement strictly matched
						print("PASSED")
						for res in req[1]:
							lst.append(Base(MOLECULES[res], res, [200, 200]))
						for r in reactant:
							lst.remove(r)

	def update( self, mpos, on_trig, off_trig, obj ):
		collided = self._collision_mixer(obj, off_trig)
		self._mix_reactant(collided, obj)

		for atm in self.ATOM_DATA:
			self._update(mpos, on_trig, off_trig, atm, obj)

	def render( self, surf ):
		if self.ATOM_DATA is not None:
			for atm in self.ATOM_DATA:
				self._bonds( surf, atm )  # draw the bonds
			for atm in self.ATOM_DATA:
				self._single_atom( surf, atm )  # draws the atoms


class Energy:
	SELECTED = False
	OFS = [None, None]  # offset when dragging

	def __init__( self, name, color, size, pos,):
		self.POSITION = pos  # position
		self.max_size = size
		self.name = name  # the energy name
		self.color = color

	def _update( self, mouse_pos, on_trig, off_trig, obj ):
		clicked = True in [o.SELECTED for o in obj]

		if self.SELECTED:
			self.POSITION[0] = mouse_pos[0]+self.OFS[0]
			self.POSITION[1] = mouse_pos[1]+self.OFS[1]

		if self.POSITION[0] < mouse_pos[0] < self.POSITION[0]+self.max_size[0] and \
				self.POSITION[1] < mouse_pos[1] < self.POSITION[1]+self.max_size[1] and \
				on_trig and not self.SELECTED and not clicked:
			self.SELECTED = True
			self.OFS = [self.POSITION[0]-mouse_pos[0], self.POSITION[1]-mouse_pos[1]]

		if off_trig:
			self.SELECTED = False
			self.OFS = [None, None]

	def _collision_mixer( self, molc_obj, off_trig ):
		if off_trig:
			COLLIDED = []
			for ind, i in enumerate( molc_obj ):
				COLLIDE_TO = []  # collision to the object /i/
				for k in molc_obj[:ind]:
					if (i.POSITION[0] < k.POSITION[0] < i.POSITION[0]+i.max_size[0] and
					    i.POSITION[1] < k.POSITION[1] < i.POSITION[1]+i.max_size[1]) or \
							(k.POSITION[0] < i.POSITION[0] < k.POSITION[0]+k.max_size[0] and
							 k.POSITION[1] < i.POSITION[1] < k.POSITION[1]+k.max_size[1]):
						COLLIDE_TO.append( k )
				if len( COLLIDE_TO ) > 0:
					COLLIDE_TO.append( i )
					COLLIDED.append( COLLIDE_TO )
			return COLLIDED

	def _mix_reactant( self, collided, lst ):
		if collided not in [[], None]:
			for reactant in collided:
				reactant_lcl = reactant.copy()
				name = []
				for n in reactant_lcl:
					if type(n) == Base: name.append( n.MOLECULE )
					elif type(n) == Energy: name.append( n.name )
				for req in REACTION:
					PASSED = True
					for a in req[0]:
						if a in name:
							name.remove( a )
						else:  # requirement /a/ is not in the reactant
							PASSED = False
							break
					if len(name) == 0 and PASSED:  # to prevent confusion, we'll only allow if the requirement strictly matched
						for res in req[1]:
							lst.append( Base( MOLECULES[res], res, [200, 200] ) )
						for r in reactant:
							lst.remove( r )

	def update( self, mpos, on_trig, off_trig, obj ):
		collided = self._collision_mixer( obj, off_trig )
		self._mix_reactant( collided, obj )

		self._update( mpos, on_trig, off_trig, obj )

	def render( self, surf ):
		p.draw.rect( surf, self.color, self.POSITION+self.max_size )
		fnt = p.font.SysFont( 'times', 18, bold=True )
		txt = fnt.render( self.name, False, (0, 0, 0) )
		textRect = txt.get_rect()
		surf.blit( txt,
		           [self.POSITION[0]+self.max_size[0]/2-textRect[2]/2, self.POSITION[1]+self.max_size[1]/2-textRect[3]/2] )
