from sense_hat import SenseHat

from fcts_steps import *

#importe les options
from options import *

#variables
crypted_message = ""
symbols1 = [circle,triangle] #menu de confirmation écriture
symbols2 = [circle,triangle,cross] #menu de choix lecture
symbols3 = [circle,cross] #choix post lecture

sense = SenseHat()
sense.low_light = True

#verifie la presance du message

###pas de message:
if file_exist(message_file) == False:
	write_message(caracters, message_file, symbols1, key_file, convert_list)

###message present:
else:
	##menu
	to_do = menu(symbols2)
	sense.clear()

	if to_do == 0:#O decrypter
		read_message(message_file, key_file, convert_list)
		if menu(symbols3) == 1: del_message(message_file)

	elif to_do == 1:
		#suprimmer le mesage
		del_message(message_file)

		#ecrire un message
		write_message(caracters, message_file, symbols1, key_file, convert_list)

	else:
		#suprimmer le message
		del_message(message_file)

sense.clear()