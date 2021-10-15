from sense_hat import SenseHat
import os

from fcts import *

#vérifie la présance du message
message_file = "message.txt"
caracters = ["0","1","2","3","4","5","6","7","8","9"]

###pas de message:
if fcts.file_exist(message) == False:
	#entrer nouveau message
	message = new_message(caracters)

	#enregistrer séquance de mouvement

	#cree la clef

	#encrypter le message

	#enregister le message
	save_message(message,message_file)


###message présent:
else:
	#enregister séquance de mouvement

	#cree la clef

	#décrypter le message

	#afficher le message

	#attendre suprimer ou conserver
	if:
		os.remove(message_file)
		
sense.show_message(str(get_position()), text_colour=[255, 0, 0])