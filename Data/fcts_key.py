def ajouter_tup (l):
    """
    Fonction qui permet de creer un tuple sur base d'une liste 'l'
    pre : 'l' est une liste contenant 3 elements representant des chiffres : -1, 0, 1.
    post : retourne un tuple avec les nouvelles valeurs modifiees de la liste.
    """
    l[2] += 1
    while l[2] > 1 :
        l[2] = -1
        l[1] += 1
    while l[1] > 1 :
        l[1] = -1
        l[0] += 1
    
    return (l[0],l[1],l[2]) 

def repertoire(lst):
    """
    Cree un dictionnaire sur base d'une liste de caracteres 'lst'.
    pre : 'lst' est une liste de caractere deja definie.
           La fonction 'ajouter_tup' est deja definie.
    post : La fonction retourne un dictionnaire avec un tuple comme cle pour chaque caractere de la liste 'lst' comme valeur.
           La creation des tuples se fait sur base du tuple precedant apres avoir initialiser le premier { tuple : valeur } dans
           le dictionnaire.
    """
    d ={}
    l = [-1,-1,-1]     # Definition d'une liste de base
    d[(-1,-1,-1)] = 'a'    # Initialisation du premier { tuple : valeur } du dictionnaire
    for i in lst:
        d[ajouter_tup (l)] = i   # Creation du dictionnaire complet sur base de la liste 'l' est la liste de caractere 'lst'.
    return d 

def letter (lst_tup,dic):

    """
    Cree une liste de lettres sur base d'une liste de tuples 'lst_tup' et un dictionnaire 'dict'.
    pre : 'lst_tup' est une liste de tuples, les tuples doivent exister comme cle dans le dictionnaire 'dict'.
    post : Pour chaque tuple de la liste 'lst_tup', la fonction trouve la valeur qui lui est assigee dans le dictionnaire 'dict' et
           l'enregistre dans une nouvelle liste 'lst_char'.
           La fonction retourne 'lst_char'.
    """ 
    lst_char = []
    for i in lst_tup:
        lst_char.append(dic[i])

    return lst_char

def create_key (lst_tup,caract):
    """
    Cree une cle a partir d'une liste de tuples 'lst_tup' et un dictionnaire 'dict'.
    pre : 'lst_tup' est une liste de tuples, les tuples doivent exister comme cle dans le dictionnaire 'dico'.
           'caract' est une liste de caracteres.
          La fonction 'repertoire' est deja definie.
          La fonction 'letter' est deja definie.
    post : La fonction cree une liste de caractere grace a la fonction 'letter'.
           La fonction effectue un concatenation de tous les caracteres de la liste cree, formant
           ainsi un string 'key' qu'elle retournera par la suite.
    """
    dico = repertoire(caract)
    lst_str = letter (lst_tup, dico)
    key =''
    for i in lst_str:
        key += i
    return key