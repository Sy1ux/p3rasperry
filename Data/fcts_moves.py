from sense_hat import SenseHat
from time import sleep

def get_position():
	"""
	retourne l'orientation actuelle du raberry
	pre: None
	post: un tuple (x,y,z) a l'acceleration subie par chacun des axes
	"""
	sense = SenseHat()
	acc = sense.get_accelerometer_raw()
	x = int(round(acc["x"],0))
	y = int(round(acc["y"],0))
	z = int(round(acc["z"],0))
	return (x,y,z)

def countdown(time,col1,col2):
	"""
	afiche un decompte a l'ecran
	pre: time le temps du decompte
		 col1 et col2 les couleurs des chifres et du font (sont inversee toutes les 0.5s)
	post: None
	"""
	sense = SenseHat()
	time2 = time
	while time2 > 0:
		sense.show_letter(str(time2),col1,col2)
		sleep(0.5)
		sense.show_letter(str(time2),col2,col1)
		sleep(0.5)
		time2 -= 1

def get_moves(lenth,col1,col2):
	"""
	optien une liste de positions de la longueure voulue
	pre: lenth le nombre de positions voulue
		 col1 et col2 les couleurs du countdown
	"""
	moves = []
	countdown(5,col1,col1)
	for i in range(lenth):
		countdown(4,col1,col2)
		moves.append(get_position())
		sleep(1)
	return moves



