from sense_hat import SenseHat

class Board:
    """
    classe de l'espace en 2D contenant les cases de coleurs
    (utiliser pour lister toutes les tiles)
    """
    class Tile:
        """
        définit les cases de couleurs par des coordonee dans un espace 2D et une couleur
        """
        def __init__(self,x,y,color,next = None):
            self.__x = x
            self.__y = y
            self.__color = color
            self.__next = next

        def next(self):
            return self.__next
        def set_next(self,next):
            self.__next = next
        def get_x(self):
            return self.__x
        def get_y(self):
            return self.__y
        def get_color(self):
            return self.__color
        def set_x(self,x):
            self.__x = x
        def set_y(self,y):
            self.__y = y

    def __init__(self):
        self.__first = None
        self.__lenth = 0

    def add(self,x,y,color):
        """
        rajouter une nouvelle tuile au tableau
        """
        tile = self.Tile(x,y,color,self.__first)
        self.__first = tile
        self.__lenth += 1

    def color(self,x,y):
        """
        obtenir la couleur d'une certaine case
        """
        other = self.__first
        while (other.get_x(),other.get_y()) != (x,y):
            other = other.next()
        return other.get_color()

    def move(self,selection_x,selection_y,direction):
        """
        deplacer toutes les cases d'une certaine ligne ou colone dans une 
        direction donnée
        """
        other = self.__first
        for i in range(self.__lenth):
            if direction == "up":
                if other.get_y() == selection_y:
                    other.set_x(other.get_x()+1)
            elif direction == "down":
                if other.get_y() == selection_y:
                    other.set_x(other.get_x()-1)
            elif direction == "right":
                if other.get_x() == selection_x:
                    other.set_y(other.get_y()+1)
            elif direction == "left":
                if other.get_x() == selection_x:
                    other.set_y(other.get_y()-1)
            if other.get_x() < 0:
                other.set_x(other.get_x()+6)
            elif other.get_x() > 5:
                other.set_x(other.get_x()-6)
            if other.get_y() < 0:
                other.set_y(other.get_y()+6)
            elif other.get_y() > 5:
                other.set_y(other.get_y()-6)
            other = other.next()

def wait_for_move():
    """
    attend une action de l'iutilisateur et la renvoie
    """
    sense = SenseHat()
    end = False
    while end == False:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                return event.direction

def screen(board,selection,selected):
    """
    met a jour l'ecran avec les donee du tableau
    """
    sense = SenseHat()
    white = (255,255,255)
    grey = (100,100,100)

    #met a jour toutes les couleurs en fonction des tiles aux coordonee choisies
    A = board.color(3,2)
    W = board.color(3,2)
    B = board.color(3,3)
    X = board.color(3,3)
    C = board.color(2,2)
    Y = board.color(2,2)
    D = board.color(2,3)
    Z = board.color(2,3)

    #modifie le contour de la case selectionee en fonction de si elle est enfoncee ou non
    if selected == True:
        if selection == (3,2): A = grey
        elif selection == (3,3): B = grey
        elif selection == (2,2): C = grey
        elif selection == (2,3): D = grey
    elif selected == False:
        if selection == (3,2): A = white
        elif selection == (3,3): B = white
        elif selection == (2,2): C = white
        elif selection == (2,3): D = white

    screen_pixels = [A,A,A,A,B,B,B,B,A,W,W,A,B,X,X,B,A,W,W,A,B,X,X,B,A,A,A,A,B,B,B,B,C,C,C,C,D,D,D,D,C,Y,Y,C,D,Z,Z,D,C,Y,Y,C,D,Z,Z,D,C,C,C,C,D,D,D,D]
    sense.set_pixels(screen_pixels)

def move_selection(selection_x,selection_y,direction):
    """
    deplace la case selectionnee par l'utilisateur
    """
    new_selection = [selection_x,selection_y]
    if direction == "up":
    	if selection_x == 2:
    		new_selection[0] += 1
    elif direction == "down":
    	if selection_x == 3:
    		new_selection[0] -= 1
    elif direction == "right":
    	if selection_y == 2:
    		new_selection[1] += 1
    elif direction == "left":
    	if selection_y == 3:
    		new_selection[1] -= 1
    return (new_selection[0],new_selection[1])

def color_lock():

    #definitions des couleurs de l'ecran
    red = (255,0,0)
    blue = (0,0,255)
    green = (0,255,0)
    yellow = (255,255,0)
    purple = (255,0,255)

    #proprietee initilales de toutes les tiles
    tiles_options = [(0,2,red),(0,3,red),(1,2,red),(1,3,red),(2,0,blue),(2,1,blue),(3,0,blue),(3,1,blue),(2,2,green),(2,3,green),(3,2,green),(3,3,green),(2,4,yellow),(2,5,yellow),(3,4,yellow),(3,5,yellow),(4,2,purple),(4,3,purple),(5,2,purple),(5,3,purple)]
    
    tiles_convertion = {}

    # cree un dictionaire de conversion
    for i in tiles_options:
        tiles_convertion[(i[0],i[1])] = ajouter_tup(l)

    screen(board,(3,2),False)
    selection = (3,2)
    selected = False
    moves = 0

    #mouvements des cases
    while moves < 7:
        while selected == False:
        	screen(board,(selection[0],selection[1]),False)
        	move = wait_for_move()

        	if move == "middle":
        		selected = True
        	else:
        		selection = move_selection(selection[0],selection[1],move)
        		screen(board,(selection[0],selection[1]),False)
        while selected == True:
        	screen(board,(selection[0],selection[1]),True)
        	move = wait_for_move()
        	if move == "middle":
        		selected = False
        	else:
        		board.move(selection[0],selection[1],move)
        		screen(board,(selection[0],selection[1]),True)
        		moves += 1
        		break

    return 

color_lock()