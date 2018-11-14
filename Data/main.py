from sense_hat import SenseHat as sh
import os

#vérifie la présance du message
message_file = "message.txt"
caracters = ["0","1","2","3","4","5","6","7","8","9"]

###pas de message:
if fcts.file_exist(message) == False:
	#entrer nouveau message

	#enregistrer séquance de mouvement

	#cree la clef

	#encrypter le message

	#enregister le message


###message présent:
else:
	#enregister séquance de mouvement

	#cree la clef

	#décrypter le message

	#afficher le message

	#attendre suprimer ou conserver
	os.remove(message_file)