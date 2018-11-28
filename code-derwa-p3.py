#encrypter le message +hacher lambda clé et la sauvegarder
#décrypter le message + hacher et comparer les hach


def encode(pwd, message):  #encrypter le message
    """
    Crypte un texte en utilisant une clé de chiffrement, tous les deux fournis sous la forme d'une chaine de caractères.
    L'algorithme utilisé est le chiffrement de Vigenère.
    Attention : cette méthode est "craquée" depuis longtemps, mais elle illustre le fonctionnement d'un algorithme de chiffrement.

    :param (str) pwd: la clé de chiffrement
    :param (str) message: le texte à chiffrer
    :return (str): le texte chiffré
    """
    key = pwd
    enc = []
    for i, e in enumerate(message):
        key_c = key[i % len(key)]
        enc_c = chr((ord(e) + ord(key_c)) % 256)
        enc.append(enc_c)
    return ("".join(enc).encode()).decode() #retourne le message crypter

def decode(pwd, cipher_text):
    """
    Déchiffre le texte en utilisant la clé de déchiffrement, tous les deux fournis sous la forme d'une chaine de caractères.
    L'algorithme utilisé est le (dé)chiffrement de Vigenère.
    Attention : cette méthode est "craquée" depuis longtemps, mais elle illustre le fonctionnement d'un algorithme de (dé-)chiffrement.

    :param (str) pwd: le mot de passe rentré par l'utilisateur
    :param (str) cipher_text: le texte crypté
    :return (str): le texte décrypté
    """
    key = pwd
    dec = []
    for i, e in enumerate(cipher_text):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(e) - ord(key_c)) % 256)
        dec.append(dec_c)
    return str("".join(dec))


def hashing(pwd):  #Hach un mot de passe de type str
    """
    Hachage d'un mot de passe fourni en entrée.
    Le résultat est une chaîne de caractères.
    Attention : cette technique de hachage n'est pas suffisante (hachage dit cryptographique) pour une utilisation en dehors du cours.

    :param (str) pwd: le mot de passe sous forme de chaîne de caractères
    :return (str): le résultat du hachage
    """
    def to_32(value):
        """
        Fonction interne utilisée par hashing.
        Convertit une valeur en un entier signé de 32 bits.
        Si value est un entier trop long de base, on en prend qu'une version diminuée.

        :param (int) value: valeur du caractère transformé par la valeur de hachage de cette itération
        :return (int): entier signé de 32 bits représentant value
        """
        value = value % (2 ** 32)
        if value >= 2**31:
            value = value - 2 ** 32
        value = int(value)
        return value 

    if pwd:
        x = ord(pwd[0]) << 7
        m = 1000003
        for c in pwd:
            x = to_32((x*m) ^ ord(c))
        x ^= len(pwd)
        if x == -1:
            x = -2
        return str(x)
    return "" #retourne la clé haché sous forme str

def read_file(filename):
	"""
	pre: filename le nom du fichier a lire
	post: le string contenant le message
	"""
	with open(filename,"r") as file:
            return file.readline()
        
def save_message(message, filename):
	"""
	pre: message le string a stocker dans un fichier
		 filename le nom du fichier dans lequel crire
	post: None
	"""
	with open(filename,"w") as file:
                file.write(message)
                

def encrypted_hashed (message,pwd,file_message,file_old):   #fonction générale pour encrypter le message et hacher la clé et la sauvegarder.

    def encrypted_message(message,pwd,file_message):  #encrypter le message et le sauvegarder dans un fichier "filename"
        crypted_message=encode(pwd, message) # sauvegarde dans une variable le message crypter 
        save_message(crypted_message,filename_message)#sauvegarde le message crypter dans le fichie .txt
    
    def hashed_key(pwd,file_old): #Hacher la clé 'pwd' et la sauvegarde dans un fichier "filename"
        hashed_message=hashing(pwd) #Sauvegarde le mdp hacher en type str
        save_message(hashed_message, filename) #sauvegarde le mdp hacher dans un fichier
        
    encrypted_message(message,pwd)
    hashed_key(pwd,filename)
        

def decrypt_compare(file_old,file_message,pwd):
    
    def compare(pwd,file_old):
        hashed_message_new = hashing(pwd)
        hashed_message_old =read_file(file_old)
        if hashed_message_old == hashed_message_new:
            return True
        return false

    if compare(file_old) == True : #si la clé hacher de base (créer par celui qui a écrit le message)est equivalente à la clé généré par la suite de mouvement de celui qui veut lire le message --> donc la suite de mouvement est bonne
        crypted_message_from_txt=readfile(file_message) 
        decrypted_message = decode(pwd,crypted_message_from_txt) #décrypter le message
        print(decrypted_message) #type str
    else :
        print("Le mots de passe est mauvais, veuillez réesayer")
    
    

    

    
"""#encrypter le message +hacher lambda clé et la sauvegarder
   
message_from_txt = read_file(message_file)     #lis le fichier .txt pour en sortir le message non crypter et le stocket dans la variable afin de l'utilser dans la fonction ''encode''
crypted_message=encode(pwd, message_from_txt)     # sauvegarde dans une variable le message crypter (pwd encore à définir)
save_message(crypted_message,message_file)       #sauvegarde le message crypter dans le fichie .txt
hashed_message=hashing(pwd)     #Sauvegarde le mdp hacher en type str (pwd reste a définir voir code de samy)
save_message(hashed_message, filename)     #sauvegarde le mdp hacher dans un fichier (nom qui reste a determiner -> voir code samy)


#décrypter le message + hacher et comparer les hach
hashed_message_new = hashing(pwd) #Sauvegarde la haching de la clé génére par la suite de mouvement dans une variable

if compare(filename) == True : #si la clé hacher de base (créer par celui qui a écrit le message)est equivalente à la clé généré par la suite de mouvement de celui qui veut lire le message --> donc la suite de mouvement est bonne
    crypted_message_from_txt=readfile(message_file) 
    decrypted_message = decode(pwd,crypted_message_from_txt) #décrypter le message
    print(decrypted_message) #type str
else :
    print("Le mots de passe est mauvais, veuillez réesayer")"""







