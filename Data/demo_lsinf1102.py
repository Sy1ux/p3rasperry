from sense_hat import SenseHat
import os
from fcts import *
import options

#options
opt = options.options()
message_file = opt[0]
caracters = opt[1]
r=opt[2]
w=opt[3]
p=opt[4]
c=opt[5]
cross=opt[6]
triangle=opt[7]
circle=opt[8]

#variables
crypted_message = ""
symbols1 = [circle,triangle]
symbols2 = [circle,triangle,cross]
symbols3 = [circle,cross]

sense = SenseHat()

#verifie la presance du message

###pas de message:
if file_exist(message_file) == False:
	write_message(caracters, message_file, symbols1)

###message present:
else:
	##menu
	to_do = menu(symbols2)
	sense.clear()

	if to_do == 0:#O decrypter
		read_message(message_file)
		if menu(symbols3) == 1: del_message(message_file)

	elif to_do == 1:
		#suprimmer le mesage
		del_message(message_file)

		#ecrire un message
		write_message(caracters, message_file, symbols1)

	else:
		#suprimmer le message
		del_message(message_file)

sense.clear()