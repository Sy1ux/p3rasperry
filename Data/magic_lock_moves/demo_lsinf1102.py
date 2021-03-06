from sense_hat import SenseHat

from fcts_steps import *

#importe les options (uniquement des variables)
from options import *

#variables
crypted_message = ""
symbols1 = [shape3,shape2] #menu de confirmation ecriture
symbols2 = [shape3,shape2,shape1] #menu de choix lecture
symbols3 = [shape3,shape1] #choix post lecture
symbols4 = [shape6,shape4,shape5] #mouvements, attente et validation
symbols5 = [shape7,shape8,shape9,shape10] #erreur, coorect

sense = SenseHat()
sense.low_light = True

#verifie la presance du message

###pas de message:
if file_exist(message_file) == False:
	write_message(caracters, message_file, symbols1, key_file, convert_list,symbols4)

###message present:
else:
	##menu
	to_do = menu(symbols2)
	sense.clear()

	if to_do == 0:#O decrypter
		if read_message(message_file, key_file, convert_list,symbols4,symbols5) == True:
			if menu(symbols3) == 1: del_message(message_file)

	elif to_do == 1:
		#suprimmer le mesage
		del_message(message_file)

		#ecrire un message
		write_message(caracters, message_file, symbols1, key_file, convert_list,symbols4)

	else:
		#suprimmer le message
		del_message(message_file)

sense.clear()