from color_lock_fcts import *

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
purple = (255,0,255)

tiles_options = [(0,2,red),(0,3,red),(1,2,red),(1,3,red),(2,0,blue),(2,1,blue),(3,0,blue),(3,1,blue),(2,2,green),(2,3,green),(3,2,green),(3,3,green),(2,4,yellow),(2,5,yellow),(3,4,yellow),(3,5,yellow),(4,2,purple),(4,3,purple),(5,2,purple),(5,3,purple)]

b = Board()
for i in tiles_options:
    b.add(i[0],i[1],i[2])

screen(3,2,False)
selection = (3,2)
selected = False

for i in range(5):
	while selected == False:
		move = wait_for_move()
		if move == "middle":
			selected = True
		else:
			selection = move_selection(selection[0],selection[1],move)
			screen(selection[0],selection[1],False)
	while selected == True:
		move = wait_for_move()
		if move == "middle":
			selected = False
		else:
			b.move(selection[0],selection[1],move)
			break