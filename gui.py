# GUI and other misc. file
import pygame as p

ALPHA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NUMBER = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

class Button:
	SELECTED = False

	def __init__(self, size, color, txt, fnc, fnt_size=24):
		self.size = size
		self.color = color
		self.txt = txt
		self.fnc = fnc  # function to execute when clicked
		self.fnt_size = fnt_size

	def render( self, surf ):
		p.draw.rect(surf, self.color, self.size)

		fnt = p.font.SysFont( 'arial', self.fnt_size )
		txt = fnt.render( self.txt, False, (0, 0, 0) )
		textRect = txt.get_rect()
		surf.blit( txt, [self.size[0]+self.size[2]/2-textRect[2]/2, self.size[1]+self.size[3]/2-textRect[3]/2] )

	def update( self, mpos, on_trig, off_trig, e):

		if self.size[0] < mpos[0] < self.size[0]+self.size[2] and \
				self.size[1] < mpos[1] < self.size[1]+self.size[3] and \
				on_trig and not self.SELECTED:
			self.SELECTED = True
			self.fnc()

		if off_trig:
			self.SELECTED = False
			self.OFS = [None, None]


class SearchBox:
	SELECTED = False
	PADX = 5  # padding at the beginning of the text
	PADY = 5
	CURSOR_TIMER = 0  # cursor loop counter; updates per each loop
	CURSOR = 30  # cursor blink time (if CURSOR_TIMER == CURSOR)
	CURSOR_BLINK = False
	CURSOR_LOC = 0  # cursor location by characters
	AT = False  # this is when the user is at the searchbox even when its not clicking

	def __init__( self, size, lst, default_val ):
		self.size = size
		self.lst = lst  # query data
		self.defualt_val = default_val
		self.selc = []

	def render( self, surf ):
		p.draw.rect( surf, (220, 220, 255) if self.AT else (220, 220, 220), self.size )

		fnt = p.font.SysFont( 'mono', 18 )
		txt = fnt.render( self.defualt_val, False, (0, 0, 0) )
		textRect = txt.get_rect()
		surf.blit( txt, [self.size[0]+self.PADX, self.size[1]+self.size[3]/2-textRect[3]/2] )

		if self.CURSOR_BLINK and self.AT:
			fnt = p.font.SysFont( 'mono', 18 )
			txt = fnt.render( self.defualt_val[0:self.CURSOR_LOC], False, (0, 0, 0) )
			textRect = txt.get_rect()
			locx = textRect[2]+self.PADX+self.size[0]
			p.draw.rect(surf, (0, 0, 0), (locx, self.size[1], 2, 20))

		posy = self.size[1]+self.PADY+self.size[3]
		if len(self.selc) > 0:  # single selected item will automatically be executed
			for s in self.selc:
				fnt = p.font.SysFont( 'arial', 18 )
				txt = fnt.render( s, False, (0, 0, 0) )
				textRect = txt.get_rect()
				surf.blit( txt, [self.size[0]+self.PADX, posy] )
				posy += textRect[3]+self.PADY


	def update( self, mpos, on_trig, off_trig, event, ):
		self.CURSOR_TIMER += 1

		for e in event:
			if e.type == p.KEYDOWN and self.AT:
				if e.key == p.K_LEFT and self.CURSOR_LOC > 0:
					self.CURSOR_LOC -= 1
					self.CURSOR_BLINK = True
				elif e.key == p.K_RIGHT and self.CURSOR_LOC < len(self.defualt_val):
					self.CURSOR_LOC += 1
					self.CURSOR_BLINK = True
				elif e.key == p.K_BACKSPACE and self.CURSOR_LOC > 0:
					char = [s for s in self.defualt_val]
					del char[self.CURSOR_LOC-1]
					self.defualt_val = "".join( char )
					self.CURSOR_LOC -= 1
				elif e.key == p.K_RETURN:  # user click enter to query
					self.selc = []
					for l in self.lst:
						if self.defualt_val in l:
							self.selc.append(l)
					if len(self.selc) == 1:
						if self.defualt_val == self.selc[0]:
							par = self.lst[self.defualt_val][1:]
							self.lst[self.defualt_val][0](*par)
				elif chr(e.key) in ALPHA+[" "]:
					character = chr(e.key)
					char = [s for s in self.defualt_val]
					char.insert( self.CURSOR_LOC, character)
					self.defualt_val = "".join(char)
					self.CURSOR_LOC += 1

		if self.CURSOR_TIMER == self.CURSOR:
			self.CURSOR_BLINK = not self.CURSOR_BLINK
			self.CURSOR_TIMER = 0

		if self.size[0] < mpos[0] < self.size[0]+self.size[2] and \
				self.size[1] < mpos[1] < self.size[1]+self.size[3] and \
				on_trig and not self.SELECTED:
			self.SELECTED = True
			self.AT = True
		elif on_trig and not self.SELECTED:
			self.AT = False
			self.selc = []

		if off_trig:
			self.SELECTED = False
			self.OFS = [None, None]

class TextBox:
	SELECTED = False
	PADY = 5

	def __init__( self, size, color, text: list ):
		self.size = size
		self.color = color
		self.txt = text

	def render( self, surf ):
		p.draw.rect( surf, self.color, self.size )
		posy = self.size[1]+self.PADY
		for ind, t in enumerate(self.txt):
			fnt = p.font.SysFont( 'arial', 18 )
			txt = fnt.render( t, False, (0, 0, 0) )
			textRect = txt.get_rect()
			surf.blit( txt, [self.size[0]+self.size[2]/2-textRect[2]/2, posy] )
			posy += textRect[3]+self.PADY

	def update( self, mpos, on_trig, off_trig, e ):
		pass
