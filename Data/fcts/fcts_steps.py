from sense_hat import SenseHat

from fcts_ui import *
from fcts_key import *
from fcts_file import *

def write_message(caracters,filename,symbols):
	"""
	ecrire un nouveau message
	"""
	sense = SenseHat()
	sense.low_light = True
	#entrer nouveau message
	message = new_message_list(caracters,symbols)

	#enregistrer sequance de mouvement et aproximer

	#creer dictionaire de convertion
	convert_dict = repertoire(convert_lst)

	#cree la clef
	key = create_key(mooves, convert_dict)

	#encrypter le message + acher la clef et sauvguarder
	crypted_message = message

	#enregister le message
	save_message(crypted_message,filename)

def read_message(filename):
	"""
	lire un message existant
	"""
	sense = SenseHat()
	sense.low_light = True

	#lecture du messsage cripté
	crypted_message = read_file(filename)

	#enregister sequance de mouvement
	mooves = [(0,0,0),(0,0,0),(0,0,0)]

	#creer dictionaire de convertions
	convert_dict = repertoire(convert_lst)

	#cree la clef
	key = create_key(mooves, convert_dict)

	#decrypter le message + acher et comparer les ach
	decrypted_message = crypted_message

	#afficher le message
	sense.show_message(decrypted_message)