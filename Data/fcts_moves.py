from sense_hat import SenseHat
from time import sleep
from time import time

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

def wait_for_move(symbols):
	sense = SenseHat()
	sense.set_pixels(symbols[1])
	start = time()
	end = False
	while end == False
		for event in sense.stick.get_events():
			if event.action == "pressed":
				if event.direction == "middle":
					return
		if time()-start < 1:
			sense.set_pixels(symbols[0])
		elif time()-start >= 2:
			sense.set_pixels(symbols[1])
			start = time() 

def get_moves(lenth,col1,col2,symbols):
	"""
	optien une liste de positions de la longueure voulue
	pre: lenth le nombre de positions voulue
		 col1 et col2 les couleurs du countdown
	"""
	moves = []
	for i in range(lenth):
		wait_for_move(symbols[1:])
		sense.set_pixels(symbols[0])
		moves.append(get_position())
		sleep(0.1)
	return moves



