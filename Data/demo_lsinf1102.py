from sense_hat import SenseHat
import os

from fcts_steps import *
import options

#atributions des obtions
opt = options.options()

#nom des fichiers
message_file = opt[0]
key_file = opt[9]

#listes de caracteres
caracters = opt[1]

#couleurs
r=opt[2]
w=opt[3]
p=opt[4]
c=opt[5]

#symboles
cross=opt[6]
triangle=opt[7]
circle=opt[8]

#variables
crypted_message = ""
symbols1 = [circle,triangle]
symbols2 = [circle,triangle,cross]
symbols3 = [circle,cross]

sense = SenseHat()
sense.low_light = True

#verifie la presance du message

###pas de message:
if file_exist(message_file) == False:
	write_message(caracters, message_file, symbols1, key_file)

###message present:
else:
	##menu
	to_do = menu(symbols2)
	sense.clear()

	if to_do == 0:#O decrypter
		read_message(message_file, key_file)
		if menu(symbols3) == 1: del_message(message_file)

	elif to_do == 1:
		#suprimmer le mesage
		del_message(message_file)

		#ecrire un message
		write_message(caracters, message_file, symbols1, key_file)

	else:
		#suprimmer le message
		del_message(message_file)

sense.clear()