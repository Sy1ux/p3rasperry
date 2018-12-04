from sense_hat import SenseHat
from time import sleep

def get_position():
	sense = SenseHat()
	acc = sense.get_accelerometer_raw()
	x = int(round(acc["x"],0))
	y = int(round(acc["y"],0))
	z = int(round(acc["z"],0))
	return (x,y,z)

def countdown(time,col1,col2):
	sense = SenseHat()
	time2 = time
	while time2 > 0:
		sense.show_letter(str(time2),col1,col2)
		sleep(0.5)
		sense.show_letter(str(time2),col2,col1)
		sleep(0.5)
		time2 -= 1

def get_moves(lenth,col1,col2):
	moves = []
	countdown(5,col1,col1)
	for i in range(lenth):
		countdown(4,col1,col2)
		moves.append(get_position())
		sleep(1)
	return moves



