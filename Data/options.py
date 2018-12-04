#nom des fichiers
message_file = "message.txt"
key_file = "key.txt"

#caracteres possibles
#caracters = ["_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","9","8","7","6","5","4","3","2","1","0"]
caracters = ["9","8","7","6","5","4","3","2","1","0"]
convert_list = ['A', 'd', 'D', 'e' , 'i', 'l', 'm', 'M', 'n', 'r', 'S', 'v','x','y','X', 'Y', '0','1','2','3','4','5','6','7','8','9']

###couleurs menu

#fond
r = (150,0,0) #red
p = (80,0,150) #purple
c = (0,80,150) #cyan

#symbole
w = (150,150,150) #white

#compte a rebours
col1 = (150,150,150) #white
col2 = (255,255,0) #orange

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