def encode(pwd, message):  #encrypter le message
    """
    Crypte un texte en utilisant une cle de chiffrement, tous les deux fournis sous la forme d'une chaine de caracteres.
    L'algorithme utilise est le chiffrement de Vigenere.
    Attention : cette méthode est "craquee" depuis longtemps, mais elle illustre le fonctionnement d'un algorithme de chiffrement.

    :param (str) pwd: la cle de chiffrement
    :param (str) message: le texte a chiffrer
    :return (str): le texte chiffre
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
    Dechiffre le texte en utilisant la cle de dechiffrement, tous les deux fournis sous la forme d'une chaine de caracteres.
    L'algorithme utilise est le (de)chiffrement de Vigenere.
    Attention : cette methode est "craquee" depuis longtemps, mais elle illustre le fonctionnement d'un algorithme de (de-)chiffrement.

    :param (str) pwd: le mot de passe rentre par l'utilisateur
    :param (str) cipher_text: le texte crypte
    :return (str): le texte decrypte
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
    Hachage d'un mot de passe fourni en entree.
    Le resultat est une chaine de caracteres.
    Attention : cette technique de hachage n'est pas suffisante (hachage dit cryptographique) pour une utilisation en dehors du cours.

    :param (str) pwd: le mot de passe sous forme de chaine de caracteres
    :return (str): le résultat du hachage
    """
    def to_32(value):
        """
        Fonction interne utilisee par hashing.
        Convertit une valeur en un entier signe de 32 bits.
        Si value est un entier trop long de base, on en prend qu'une version diminuee.

        :param (int) value: valeur du caractere transforme par la valeur de hachage de cette iteration
        :return (int): entier signe de 32 bits representant value
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
    return "" #retourne la cle hache sous forme str