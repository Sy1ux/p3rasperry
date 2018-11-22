from sense_hat import SenseHat 
from os import remove
from time import sleep

########################### FICHIERS
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
		 filename le nom du fichier dans lequel crire
	post: None
	"""
	with open(filename,"w") as file:
		file.write(message)


def read_file(filename):
	"""
	pre: filename le nom du fichier a lire
	post: le string contenant le message
	"""
	with open(filename,"r") as file:
		return file.readline()

def del_message(filename):
	"""
	suprimer un fichier
	"""
	remove(filename)

##################################### INTERFACE

def new_message_list(caracters,symbols):
	"""
	demande a l'utilisateur de crer un nouveau message
	pre: caracers la liste de tout les caracteres possibles
		 symbols la liste des "images" pour le menu de confirmation
	post: un string contenant le message en clair
	"""
	#creation variables
	sense = SenseHat()
	new_message = ["0"]
	index = 0
	push2 = 0
	sense.show_letter(new_message[index])
	
	while index >= 0:
		caracter = new_message[index]
		for event in sense.stick.get_events():
			if event.action == "pressed":
				#suprimer le dernier caractere
				if event.direction == "middle":
					if len(new_message) > 1:
						if push2 == 1:
							new_message = new_message[:-1]
							index = len(new_message)-1
							push2 = 0
						else:
							push2 = 1

				#choisir le caractere
				elif event.direction == "up":
					push2 = 0
					new_message[index] = caracters[up_index(caracter,caracters)]
				elif event.direction == "down":
					push2 = 0
					new_message[index] = caracters[down_index(caracter,caracters)]

				#se deplacer dans le message
				elif event.direction == "left":
					push2 = 0
					if index == 0: index = 1
					index -= 1
				elif event.direction == "right":
					push2 = 0
					if index == len(new_message)-1:
						new_message.append("0")
						index += 1
					else:
						index += 1

			#fin ecriture
			elif event.action == "held":
				if event.direction == "middle":
					string_message = ""
					for i in new_message:
						string_message += i
					sense.show_message(string_message)

					#demande de confirmation
					selected = 0
					sense.set_pixels(symbols[selected])
					selected = menu(symbols)
					if selected == 0:
						return string_message
			sense.show_letter(new_message[index])

def menu(menu_options):
	"""
	afiche un menu a l'ecran
	pre: menu_options la liste des "images" pour chaque option du menu
	post: l'index du choix fait dans le menu
	"""
	sense = SenseHat()
	menu_index = 0

	sense.set_pixels(menu_options[menu_index])
	while menu_index >= -10:
		for event in sense.stick.get_events():
			if event.action == "pressed":
				if event.direction == "middle":
					return menu_index
				elif event.direction == "up":
					menu_index += 1
					if menu_index == len(menu_options): menu_index = 0
					sense.set_pixels(menu_options[menu_index])
				elif event.direction == "down":
					if menu_index == 0: menu_index = len(menu_options)
					menu_index -= 1
					sense.set_pixels(menu_options[menu_index])

################ MANIPULATION INDEX

def get_index(caracter,caracters):
	"""
	donne le numro d'index de caracter dans la liste caracters
	"""
	for i,j in enumerate(caracters):
		if j == caracter:
			return i

def up_index(caracter,caracters):
	"""
	renvoie le numero suivant dans la liste caracters (boucle)
	"""
	new = get_index(caracter,caracters)
	if new == len(caracters)-1:
		return 0
	else:
		return new+1

def down_index(caracter,caracters):
	"""
	renvoie le numero precedent dans la liste caracters (boucle)
	"""
	new = get_index(caracter,caracters)
	if new == 0:
		return len(caracters)-1
	else:
		return new-1

###################### FONCTIONS GENERALES

def write_message(caracters,filename,symbols):
	"""
	ecrire un nouveau message
	"""
	sense = SenseHat()
	#entrer nouveau message
	message = new_message_list(caracters,symbols)

	#enregistrer sequance de mouvement et aproximer

	#cree la clef

	#encrypter le message + acher la clef et sauvguarder
	crypted_message = message

	#enregister le message
	save_message(crypted_message,filename)

def read_message(filename):
	"""
	lire un message existant
	"""
	sense = SenseHat()
	crypted_message = read_file(filename)
	print(crypted_message)

	#enregister sequance de mouvement

	#cree la clef

	#decrypter le message + acher et comparer les ach
	decrypted_message = crypted_message

	#afficher le message
	sense.show_message(decrypted_message)

