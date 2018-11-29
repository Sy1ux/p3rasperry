from sense_hat import SenseHat 
from time import sleep

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
	sense.low_light = True
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
	sense.low_light = True
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



################ MANIPULATION INDEX ###################

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