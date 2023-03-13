# Maze generator -- Randomized Prim Algorithm

#to je koda, ki sem jo kopiral z githuba, na povezavi 

# Imports
import random
import time
from colorama import init
from colorama import Fore, Back, Style
from inp import height, width


#najprej koda poisce, koliko celic obkrooza celico, v kateri je zacela
def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == ' '):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == ' '):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == ' '):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == ' '):
		s_cells += 1

	return s_cells


# glavna koda
# glavne spremenljivke
wall = 'w'
cell = ' '
warp = 's'
unvisited = 'u'
maze = []

# funkcije
def printMaze(maze):
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")

			elif (maze[i][j] == ' '):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")
			
		print('\n')

# oznaci vse celice kot 'unvisited' (neobiskane)
for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

# izbere nakljucno tocko in tam zacne
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1

# oznaci jo kot celico in oznaci ostale celice okoli nje
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# oznaci stene v labirintu (krog in krog)
maze[starting_height-1][starting_width] = 'w'
maze[starting_height][starting_width - 1] = 'w'
maze[starting_height][starting_width + 1] = 'w'
maze[starting_height + 1][starting_width] = 'w'

while (walls):
	# izbere nakljucno steno
	rand_wall = walls[int(random.random()*len(walls))-1]

	# preveri, ce je leva stena (na najbolj levi strani)
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == ' '):
			# najde stevilo celic, ki jo obkrozajo
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				# oznaci novo pot
				maze[rand_wall[0]][rand_wall[1]] = ' '

				# oznaci nove stene
				# zgornja celica
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != ' '):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				# spodnja celica (glede na zacetno)
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != ' '):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				# najbolj leva celica (glede na zacetno)
				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != ' '):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
			

			# unici steno
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# preveri, ce je zgornja stena
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == ' '):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# oznaci nov celico
				maze[rand_wall[0]][rand_wall[1]] = ' '

				# oznaci stene
				# zgorja celica (glede na izbrano)
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != ' '):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				# leva celica (glede na izbrano)
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != ' '):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				# desna celica (glede na izbrano)
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != ' '):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# unici stene
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# preveri spodnjo steno
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == ' '):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# nova pot
				maze[rand_wall[0]][rand_wall[1]] = ' '




				# -II-
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != ' '):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != ' '):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != ' '):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# -II-
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	# PREVERI NAJBOLJ DESNO STENO
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == ' '):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# -II-
				maze[rand_wall[0]][rand_wall[1]] = ' '

				# -II-
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != ' '):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != ' '):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != ' '):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			# UNICI STENP
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# 'cleanup'
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)

# oznaci preostale 'neobiskane celice' kot stene
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'u'):
			maze[i][j] = 'w'

# vpelje random
import random

# postavi portal = izhod
# torej tukaj sem naredl tako, da ce je igralec izbral lahko verzijo ima samo en izhod, ce pa ima tezjo ali legendarno, pa ima 2 mozna izhoda, ki pa sta nakljucno dolocena
if height == 20:
	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == ' '):
			maze[height-1][i] = 's'
			break
else:
		start_col = random.randint(0, width-1)
		maze[height-2][start_col] = 's'
		maze[start_col][width-2] = 's'

# tukaj se postavim igralcev lik na zacetek labirinta
for i in range(0, width):
	if (maze[1][i] == ' '):
		maze[1][i] = 'p'
		break


# tukaj nastavim listo WORLD_MAP, da naj bo enaka generiranemu labirintu
WORLD_MAP = maze