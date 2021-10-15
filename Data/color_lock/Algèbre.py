A = [1.0,2.0]
B = [3.0,4.0]
C = [1.0,2.0,3.0]
D = [[1.0,2.0],[3.0,4.0]]
E = [[1.0,2.0,3.0],
     [4.0,5.0,6.0]]


def multiply(M_A,M_B):
    #calcul de compatibilité des 2 matrices
    #Cette fonction ne marhce pas pour les matrices d'une seule ligne
    if M_A[0] is list:
        #Alors M_A est une liste de liste
        L_A = len(M_A[0])
        C_A = len(M_A)
    else:
        #Alors M_A est une liste
        C_A = len(M_A)
        L_A = 1
    
    if type(M_B[0]) == type([]):
        #Alors M_A est une liste de liste
        C_B = len(M_B[0])
        L_B = len(M_B)
    else:
        #Alors M_B est une liste
        C_B = len(M_B)
        L_B = 1
    if C_A==L_B:
        r = []
        M = []
        for i in range (len(M_A)):
            #parcours de ligne
            for j in range (len(M_B[0])) :
                res= 0
                for k in range (len(M_B)) :
                    res = res + (M_A[i][k] * M_B[k][j])
                r.append(res)
            M.append(r)
            r=[]
            #vidage de la ligne 
        return M
    else:
        raise ValueError("Dimension mismatch")
