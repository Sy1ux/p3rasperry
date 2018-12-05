from sense_hat import SenseHat

from fcts_ui import *
from fcts_key import *
from fcts_file import *
from fcts_crypt import *
from fcts_moves import *

def write_message(caracters,filename,symbols,filename2,convert_list):
	"""
	ecrire un nouveau message
	"""
	sense = SenseHat()
	sense.low_light = True

	#entrer nouveau message
	message = new_message_ui(caracters,symbols)

	#enregistrer sequance de mouvement et aproximer
	moves = get_moves(5,(150,150,150),(255,180,0))
	print(moves)

	#cree la clef
	key = create_key(moves, convert_list)

	#sauvgarder la clef achee
	save_message(hashing(key),filename2)

	#crypter le message
	crypted_message = encode(key, message)

	#enregister le message
	save_message(crypted_message,filename)

def read_message(filename,filename2,convert_list):
	"""
	lire un message existant
	"""
	sense = SenseHat()
	sense.low_light = True

	#lecture du messsage cripte
	crypted_message = read_file(filename)

	#enregister sequance de mouvement
	moves = get_moves(5,(150,150,150),(255,180,0))
	print(moves)

	#cree la clef
	key = create_key(moves, convert_list)

	#acher et comparer la clef
	if hashing(key) != read_file(filename2):

		return

	#decrypter le message
	decrypted_message = decode(key, read_file(filename))

	#afficher le message
	sense.show_message(decrypted_message)