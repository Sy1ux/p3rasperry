from os import remove

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