#nom des fichiers
message_file = "message.txt"
key_file = "key.txt"

#caracteres possibles
#caracters = ["_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","9","8","7","6","5","4","3","2","1","0"]
caracters = ["9","8","7","6","5","4","3","2","1","0"]
convert_list = ["A","d","D","e","i","l","m","M","n","r","S","v","x","y","X","Y","0","1","2","3","4","5","6","7","8","9"]

###couleurs

##fond
#menus
r = (150,0,0) #red
p = (80,0,150) #purple
c = (0,80,150) #cyan
#mouvements
o = (255,80,0) #orange
l = (70,255,70) #lime
#mot de passe
g = (0,255,0) #green
d = (255,0,0) #dark red

#symbole
w = (150,150,150) #white

###patern menu
# suprimer
shape1 = [
r,r,r,r,r,r,r,r,
r,w,r,r,r,r,w,r,
r,r,w,r,r,w,r,r,
r,r,r,w,w,r,r,r,
r,r,r,w,w,r,r,r,
r,r,w,r,r,w,r,r,
r,w,r,r,r,r,w,r,
r,r,r,r,r,r,r,r]

# editer
shape2 = [
c,c,c,c,c,c,c,c,
c,w,w,w,w,w,w,c,
c,w,c,c,c,c,w,c,
c,w,c,c,c,c,w,c,
c,w,c,c,c,c,w,c,
c,w,c,c,c,c,w,c,
c,w,w,w,w,w,w,c,
c,c,c,c,c,c,c,c]

# valider/lire
shape3 = [
p,p,p,p,p,p,p,p,
p,p,w,w,w,w,p,p,
p,w,p,p,p,p,w,p,
p,w,p,p,p,p,w,p,
p,w,p,p,p,p,w,p,
p,w,p,p,p,p,w,p,
p,p,w,w,w,w,p,p,
p,p,p,p,p,p,p,p]

#attente 1
shape4 = [
o,o,o,o,o,o,o,o,
o,o,w,o,w,o,o,o,
o,o,o,o,o,o,w,o,
o,w,o,o,o,o,o,o,
o,o,o,o,o,o,w,o,
o,w,o,o,o,o,o,o,
o,o,o,w,o,w,o,o,
o,o,o,o,o,o,o,o]

#attente 2
shape5 = [
o,o,o,o,o,o,o,o,
o,o,o,w,o,w,o,o,
o,w,o,o,o,o,o,o,
o,o,o,o,o,o,w,o,
o,w,o,o,o,o,o,o,
o,o,o,o,o,o,w,o,
o,o,w,o,w,o,o,o,
o,o,o,o,o,o,o,o]

#validation
shape6 = [
l,l,l,l,l,l,l,l,
l,w,l,l,l,l,w,l,
l,w,l,l,l,l,w,l,
l,w,l,l,l,l,w,l,
l,l,w,l,l,w,l,l,
l,l,w,l,l,w,l,l,
l,l,l,w,w,l,l,l,
l,l,l,l,l,l,l,l]

#correct
shape7 = [
g,g,g,g,g,g,g,g,
g,w,g,g,g,g,w,g,
g,w,g,g,g,g,w,g,
g,w,g,g,g,g,w,g,
g,g,w,g,g,w,g,g,
g,g,w,g,g,w,g,g,
g,g,g,w,w,g,g,g,
g,g,g,g,g,g,g,g]

#incrrect1
shape8 = [
d,d,d,d,d,d,d,d,
d,w,d,d,d,d,w,d,
d,d,w,d,d,w,d,d,
d,d,d,w,w,d,d,d,
d,d,d,w,w,d,d,d,
d,d,w,d,d,w,d,d,
d,w,d,d,d,d,w,d,
d,d,d,d,d,d,d,d]

#incorrect2
shape9 = [
w,w,w,w,w,w,w,w,
w,d,w,w,w,w,d,w,
w,w,d,w,w,d,w,w,
w,w,w,d,d,w,w,w,
w,w,w,d,d,w,w,w,
w,w,d,w,w,d,w,w,
w,d,w,w,w,w,d,w,
w,w,w,w,w,w,w,w]