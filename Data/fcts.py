def file_exist(filename):
	"""
	pre: le nom complet d'un fichier
	post: True ou False selon l'existance du fichier
	"""
	try:
		with open(filename, "r") as file:
			return True
	except:
		return False


def save_message(message, filename):
	"""
	pre: message le string a stocker dans un fichier
		 filename le nom du fichier dans lequel écrire
	post: None
	"""
	with open(filename,"w") as file:
		file.write(message)


def read_message(filename):
	"""
	pre: filename le nom du fichier a lire
	post: le string contenant le message
	"""
	with open(filename,"r") as file:
		return file


def new_message(caracters):
	"""
	demande a l'utilisateur de créer un nouveau message
	"""
	sense = SenseHat()
	new_message = ["0"]
	index = 0
	
	while True:
		caracter = new_message[index]
		event = sense.stick.wait_for_event()
		if event.action == "pressed":
			break #s'active tout seul?
		elif event.direction == "up":
			new_message[index] = caracters[up_index(caracter,caracters)]
		elif event.direction == "down":
			new_message[index] = caracters[down_index(caracter,caracters)]
		elif event.direction == "left":
			index -= 1
		elif event.direction == "right":
			new_message.append("0")
			index += 1
		sense.show_letter(new_message[index])

	return new_message


def get_index(caracter,caracters):
	"""
	donne le numéro d'index de caracter dans la liste caracters
	"""
	for i,j in enumerate(caracters):
		if j == caracter:
			return i

def up_index(caracter,caracters):
	"""
	"""
	new = get_index(caracter,caracters)
	if new == len(caracters):
		return 0
	else:
		return new+1

def down_index(caracter,caracters):
	"""
	"""
	new = get_index(caracter,caracters)
	if new == 0:
		return len(caracters)
	else:
		return new-1


def get_position():
	set_imu_config(False,True,True)
	orientation = sense.get_orientation_degrees()
	accel = sense.get_accelerometer_raw()
	

