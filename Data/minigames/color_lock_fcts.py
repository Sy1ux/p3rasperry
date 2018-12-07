from sense_hat import SenseHat

class Board:
    class Tile:
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
        tile = self.Tile(x,y,color,self.first())
        self.__first = tile
        self.__lenth += 1

    def get_color(self,x,y):
        other = self.__first
        while (other.get_x(),other.get_y()) != (x,y):
            other = other.next()
        return other.get_color()

    def move(self,selection_x,selection_y,direction):
        other = self.first()
        for i in range(self.__lenth):
            if direction == "up":
                if other.get_y() == selection_y:
                    other.set_x(other.get_x()+2)
            elif direction == "down":
                if other.get_y() == selection_y:
                    other.set_x(other.get_x()-2)
            elif direction == "right":
                if other.get_x() == selection_x:
                    other.set_y(other.get_y()+2)
            elif direction == "left":
                if other.get_x() == selection_x:
                    other.set_y(other.get_y()-2)
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
    sense = SenseHat()
    end = False
    while end == False
        for event in sense.stick.get_events():
            if event.action == "pressed":
                return event.direction

def screen(board,selection,selected):
    sense = SenseHat()
    white = (255,255,255)
    grey = (100,100,100)

    A = board.get_color(3,2)
    W = board.get_color(3,2)
    B = board.get_color(3,3)
    X = board.get_color(3,3)
    C = board.get_color(2,2)
    Y = board.get_color(2,2)
    D = board.get_color(2,3)
    Z = board.get_color(2,3)

    if selected == True:
        if selection == 0: A = grey
        elif selection == 1: B = grey
        elif selection == 2: C = grey
        elif selection == 3: D = grey
    elif selected == False:
        if selection == 0: A = white
        elif selection == 1: B = white
        elif selection == 2: C = white
        elif selection == 3: D = white

    screen_pixels = [A,A,A,A,B,B,B,B,A,W,W,A,B,X,X,B,A,W,W,A,B,X,X,B,A,A,A,A,B,B,B,B,C,C,C,C,D,D,D,D,C,Y,Y,C,D,Z,Z,D,C,Y,Y,C,D,Z,Z,D,C,C,C,C,D,D,D,D]
    sense.set_pixels(screen_pixels)

def move_selection(selection_x,selection_y,direction):
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


