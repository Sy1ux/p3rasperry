def ajouter_tup (l):
    """
    Fonction qui permet de créer un tuple sur base d'une liste 'l'
    pre : 'l' est une liste contenant 3 éléments représentant des chiffres : -1, 0, 1.
    post : retourne un tuple avec les nouvelles valeurs modifiées de la liste.
    """
    l[2] += 1
    while l[2] > 1 :
        l[2] = -1
        l[1] += 1
    while l[1] > 1 :
        l[1] = -1
        l[0] += 1
    
    return (l[0],l[1],l[2]) 

def repertoire (lst):
    """
    Crée un dictionnaire sur base d'une liste de caractères 'lst'.
    pre : 'lst' est une liste de caractère déjà définie.
           La fonction 'ajouter_tup' est déjà définie.
    post : La fonction retourne un dictionnaire avec un tuple comme clé pour chaque caractère de la liste 'lst' comme valeur.
           La création des tuples se fait sur base du tuple précédant après avoir initialiser le premier { tuple : valeur } dans
           le dictionnaire.
    """
    d ={}
    l = [-1,-1,-1]     # Définition d'une liste de base
    d[(-1,-1,-1)] = 'a'    # Initialisation du premier { tuple : valeur } du dictionnaire
    for i in lst[1:] :
        d[ajouter_tup (l)] = i   # Création du dictionnaire complet sur base de la liste 'l' est la liste de caractère 'lst'.
    return d 


def letter (lst_tup,dict):
    """
    Crée une liste de lettres sur base d'une liste de tuples 'lst_tup' et un dictionnaire 'dict'.
    pre : 'lst_tup' est une liste de tuples, les tuples doivent exister comme clé dans le dictionnaire 'dict'.
    post : Pour chaque tuple de la liste 'lst_tup', la fonction trouve la valeur qui lui est assigée dans le dictionnaire 'dict' et
           l'enregistre dans une nouvelle liste 'lst_char'.
           La fonction retourne 'lst_char'.
    """ 
    lst_char = []
    for i in lst_tup:
        lst_char.append(dict[i])
    
    return lst_char

def create_key (lst_tup, dict):
    """
    Crée une clé à partir d'une liste de tuples 'lst_tup' et un dictionnaire 'dict'.
    pre : 'lst_tup' est une liste de tuples, les tuples doivent exister comme clé dans le dictionnaire 'dict'.
          La fonction 'letter' est déjà définie.
    post : La fonction crée une liste de caractère grâce à la fonction 'letter'.
           La fonction effectue un concaténation de tous les caractères de la liste crée, formant
           ainsi un string 'key' qu'elle retournera par la suite.
    """
    lst_str = letter (lst_tup,dict)
    key =''
    for i in lst_str:
        key += i
    
    return key