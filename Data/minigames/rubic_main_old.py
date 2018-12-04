red = (0,0,0)
blue = (0,0,0)
yellow = (0,0,0)
green = (0,0,0)
orange = (0,0,0)
purple = (0,0,0)

"""
screen = 
[na,na,na,na,nb,nb,nb,nb
,na,a , a,na,nb,b ,b ,nb
,na,a , a,na,nb,b ,b ,nb
,na,na,na,na,nb,nb,nb,nb
,nc,nc,nc,nc,nd,nd,nd,nd
,nc,c ,c ,nc,nd,d ,d ,nd
,nc,c ,c ,nc,nd,d ,d ,nd
,nc,nc,nc,nc,nd,nd,nd,nd]
"""

class face():
	"""
	classe de tout les cases du cube, 4 cases par faces et 6 faces
	"""
	def __init__(self,x,y,color):
		"""
		une face est definie par ses coordonees dans la representation 2D du cube et sa couleur
		"""
		self.__x = x
		self.__y = y
		self.__color = color

	def tp(self,x,y):
		"""
		deplace la cases choisie aux coordonee donees
		"""
		self.__x = x
		self.__y = y

	def coordonate(self):
		"""
		renvoie un tuple des coordonee de la case
		"""
		return(self.x,self.y)

	def new_x(self,x):
		self.__x = x

	def new_y(self,y):
		self.__y = y

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_color(self,x,y):
		"""
		renvoie la couleur de la case
		"""
		for i in items:
			if self.coordonate() == (x,y):
				return self.__color

def moove_up(x,y):
	for i in items:
		if i.get_x() == y:
			i.new_y(i.get_y()-2)
		if y == 5:
			if i.get_x() == 2:
				i.new_y(i.get_y()+2)
		if y == 6:
			if i.get_x() == 1:
				i.new_y(i.get_y()+2)
		tp(i)

def moove_down(x,y):
	for i in items:
		if i.get_x() == y:
			i.new_y(get_y()-2)
		if y == 5:
			if i.get_x() == 2:
				i.new_y(get_y()+2)
		if y == 6:
			if i.get_x() == 1:
				i.new_y(get_y()+2)
		tp(i)

def moove_right(x,y):
	for i in items:
		if i.get_y() == x:
			i.new_x(get_x()+2)
			if i.get_x() > 8:
				i.new_x(get_x()-8)

def moove_left(x,y):
	for i in items:
		if i.get_y() == x:
			i.new_x(get_x()-2)
			if i.get_x() < 1:
				i.new_x(get_x()+8)

def tp(obj):
	"""
	teleporte les cases du cube qui dépasse de la representation en 2D vers leurs points correspondants
	"""
	#up
	if obj.coordonate() == (5,0): ogj.tp(2,3)
	elif obj.coordonate() == (5,-1): ogj.tp(2,4)
	if ogj.coordonate() == (2,5): ogj.tp(5,6)
	elif ogj.coordonate() == (2,6): ogj.tp(5,5)

	if ogj.coordonate() == (6,0): ogj.tp(1,3)
	elif ogj.coordonate() == (6,-1): ogj.tp(1,4)
	if ogj.coordonate() == (1,5): ogj.tp(6,5)
	elif ogj.coordonate() == (1,6): ogj.tp(6,6)

	#down
	if ogj.coordonate() == (6,7): ogj.tp(1,4)
	elif ogj.coordonate() == (6,8): ogj.tp(1,3)
	if ogj.coordonate() == (1,2): ogj.tp(6,1)
	elif ogj.coordonate() == (1,1): ogj.tp(6,2)

	if ogj.coordonate() == (5,7): ogj.tp(2,3)
	elif ogj.coordonate() == (5,8): ogj.tp(2,4)
	if ogj.coordonate() == (2,1): ogj.tp(5,2)
	elif ogj.coordonate() == (2,2): ogj.tp(5,1)

	
def screen():
	print("####{}{}##\n".format(get_color(5,1),get_color(6,1))+
	  "####{}{}##\n".format(get_color(5,2),get_color(6,2))+
	  "{}{}{}{}{}{}{}{}\n".format(get_color(1,3),get_color(2,3),get_color(3,3),get_color(4,3),get_color(5,3),get_color(6,3),get_color(7,3),get_color(8,3))+
	  "{}{}{}{}{}{}{}{}\n".format(get_color(1,4),get_color(2,4),get_color(3,4),get_color(4,4),get_color(5,4),get_color(6,4),get_color(7,4),get_color(8,4))+
	  "####{}{}##\n".format(get_color(5,5),get_color(6,5))+
	  "####{}{}##\n".format(get_color(5,6),get_color(6,6)))

#creation des 6 faces du cube
f1 = face(1,3,"r")
f2 = face(1,4,"r")
f3 = face(2,3,"r")
f4 = face(2,4,"r")

f5 = face(3,3,"b")
f6 = face(3,4,"b")
f7 = face(4,3,"b")
f8 = face(4,4,"b")

f9 = face(5,1,"y")
f10 = face(5,2,"y")
f11 = face(6,1,"y")
f12 = face(6,2,"y")

f13 = face(5,3,"g")
f14 = face(5,4,"g")
f15 = face(6,3,"g")
f16 = face(6,4,"g")

f17 = face(5,5,"o")
f18 = face(5,6,"o")
f19 = face(6,5,"o")
f20 = face(6,6,"o")

f21 = face(7,3,"p")
f22 = face(7,4,"p")
f23 = face(8,3,"p")
f24 = face(8,4,"p")


items = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24]

screen()

moove((3,5),"up")

screen()

moove((3,5),"right")

screen()