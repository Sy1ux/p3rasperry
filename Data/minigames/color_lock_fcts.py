class tile():
	def __init__(self,x,y,color):
		self.__x = x
		self.__y = y
		self.__color = color

	def __str__(self):
		return str(self.__color)

	def get_x(self):
		x = self.__x
		return x

	def get_y(self):
		y = self.__y
		return y

	def move_x(self,move):
		self.__x += move

	def move_y(self,move):
		self.__y += move

	def coord(self):
		x = self.__x
		y = self.__y
		return (x,y)

	def get_color(self):
		return self.__color
def tp():
	for i in tiles:
		if i.get_x() < 0:
			i.move_x(6)
		elif i.get_x() > 5:
			i.move_x(-6)
		if i.get_y() < 0:
			i.move_y(6)
		elif i.get_y() > 5:
			i.move_y(-6)

def move(x,y,direction):
	for i in tiles:
		if direction == "N":
			if i.get_y() == y:
				i.move_x(2)
		elif direction == "S":
			if i.get_y() == y:
				i.move_x(-2)
		elif direction == "E":
			if i.get_x() == x:
				i.move_y(2)
		elif direction == "W":
			if i.get_x() == x:
				i.move_y(-2)
	tp()

#cree les tiles
t1 = tile(0,2,red)
t2 = tile(0,3,red)
t3 = tile(1,2,red)
t4 = tile(1,3,red)

t5 = tile(2,0,blue)
t6 = tile(3,0,blue)
t7 = tile(2,1,blue)
t8 = tile(3,1,blue)

t9 = tile(2,2,green)
t10 = tile(3,2,green)
t11 = tile(2,3,green)
t12 = tile(3,3,green)

t13 = tile(2,4,yellow)
t14 = tile(2,5,yellow)
t15 = tile(3,4,yellow)
t16 = tile(3,5,yellow)

t17 = tile(4,2,purple)
t18 = tile(5,2,purple)
t19 = tile(4,3,purple)
t20 = tile(5,3,purple)

#liste des tiles
tiles = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20]