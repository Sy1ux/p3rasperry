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
	def __init__(self,x,y,color):
		 self.x = x
		 self.y = y
		 self.color = color

	def coordonate(self):
		return(self.x,self.y)

def move(selection,direction):
	if direction == "up":
		for i in items:
			if i.x == selection[1]:
				i.y -= 2
			if selection[1] == 5:
				if i.x == 2:
					i.y += 2
			if selection[1] == 6:
				if i.x == 1:
					i.y += 2
			tp(i)
	elif direction == "down":
		for i in items:
			if i.x == selection[1]:
				i.y -= 2
			if selection[1] == 5:
				if i.x == 2:
					i.y += 2
			if selection[1] == 6:
				if i.x == 1:
					i.y += 2
			tp(i)
	elif direction == "right":
		for i in items:
			if i.y == selection[0]:
				i.x += 2
				if i.x > 8:
					i.x -=8
	elif direction == "left":
		for i in items:
			if i.y == selection[0]:
				i.x -= 2
				if i.x < 1:
					i.x += 8

def get_color(coord):
	for i in items:
		if i.coordonate() == coord:
			return i.color

def tp(i):
	#up
	if i.coordonate() == (5,0):
		i.x = 2
		i.y = 3
	elif i.coordonate() == (5,-1):
		i.x = 2
		i.y = 4
	if i.coordonate() == (2,5):
		i.x = 5
		i.y = 6
	elif i.coordonate() == (2,6):
		i.x = 5
		i.y = 5

	if i.coordonate() == (6,0):
		i.x = 1
		i.y = 3
	elif i.coordonate() == (6,-1):
		i.x = 1
		i.y = 4
	if i.coordonate() == (1,5):
		i.x = 6
		i.y = 5
	elif i.coordonate() == (1,6):
		i.x = 6
		i.y = 6

	#down
	if i.coordonate() == (6,7):
		i.x = 1
		i.y = 4
	elif i.coordonate() == (6,8):
		i.x = 1
		i.y = 3
	if i.coordonate() == (1,2):
		i.x = 6
		i.y = 1
	elif i.coordonate() == (1,1):
		i.x = 6
		i.y = 2

	if i.coordonate() == (5,7):
		i.x = 2
		i.y = 3
	elif i.coordonate() == (5,8):
		i.x = 2
		i.y = 4
	if i.coordonate() == (2,1):
		i.x = 5
		i.y = 2
	elif i.coordonate() == (2,2):
		i.x = 5
		i.y = 1

"""		
def screen():
	print("####{}{}##\n".format(get_color((5,1)),get_color((6,1)))+
	  "####{}{}##\n".format(get_color((5,2)),get_color((6,2)))+
	  "{}{}{}{}{}{}{}{}\n".format(get_color((1,3)),get_color((2,3)),get_color((3,3)),get_color((4,3)),get_color((5,3)),get_color((6,3)),get_color((7,3)),get_color((8,3)))+
	  "{}{}{}{}{}{}{}{}\n".format(get_color((1,4)),get_color((2,4)),get_color((3,4)),get_color((4,4)),get_color((5,4)),get_color((6,4)),get_color((7,4)),get_color((8,4)))+
	  "####{}{}##\n".format(get_color((5,5)),get_color((6,5)))+
	  "####{}{}##\n".format(get_color((5,6)),get_color((6,6))))
"""

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