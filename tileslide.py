#3x3 tile slide puzzle, solve it!
import time


#make tile object
class tile():
	def __init__(self):
		a = 1+1
		
	def initialize(self, x,y,num):
		self.x = x
		self.y = y
		self.num = num
	def changecoord(self,x,y):
		self.x = x
		self.y = y
		

#make space object
class space():
	def __init__(self):
		a = 1+1
		self.num = "_"
		
	def initialize(self, x,y):
		self.x = x
		self.y = y
	def changecoord(self,x,y):
		self.x = x
		self.y = y

#initialize puzzle
tile_list = []
a = tile()
a.initialize(1,1,5)
b = tile()
b.initialize(2,1,4)
c = tile()
c.initialize(1,2,3)
d = tile()
d.initialize(2,2,2)
e = tile()
e.initialize(3,2,1)
f = tile()
f.initialize(1,3,6)
g = tile()
g.initialize(2,3,7)
h = tile()
h.initialize(3,3,8)
j = space()
j.initialize(3,1)
tile_list = [a,b,c,d,e,f,g,h,j]
		
		


#whenver you press an arrow key, if you can, you move the space object in the direction and swap it with whatever number is there
def move(tiles):
	#get coordinates of blank
	for tile in tiles:
		if tile.num == "_":
			blankx = tile.x
			blanky = tile.y
			blanktile = tile
			swapx = blankx
			swapy = blanky
	
	dir = str(raw_input("what direction? (wasd) "))
	if dir not in "wasd":
		print("bad direction! use wasd!")
		swapx = blankx
		swapy = blanky
	if dir == "a": 
		swapx = blankx + 1
		swapy = blanky
	if dir == "s":
		swapx = blankx
		swapy = blanky - 1
	if dir == "d":
		swapx = blankx - 1
		swapy = blanky
	if dir == "w":
		swapx = blankx
		swapy = blanky + 1	
		
		
	if swapx in range(1,4) and swapy in range(1,4):
		#swap is legal!
		for tile in tiles:
			if tile.x == swapx and tile.y == swapy:
				swaptile = tile
		swaptile.changecoord(blankx, blanky)
		blanktile.changecoord(swapx,swapy)


#print 
def print_state(tile_list):
	for row in range(1,4):
		thisstr = ""
		for col in range (1,4):
			for tile in tile_list:
				if tile.x == col and tile.y == row:
					thisstr = thisstr + str(tile.num)
		print thisstr
	
	

#check if you are done 
def done_check(tiles):
	goodcount = 0
	for tile in tiles:
		expected_pos = tile.x + 3*(tile.y-1)
		real_pos = tile.num
		if real_pos == "_":
			real_pos = 9
		if expected_pos == real_pos:
			goodcount += 1

	if goodcount == 9:
		return 1
	else:
		return 0 

#record time 


#do the thing
start_time = time.time()
while done_check(tile_list) == 0:
	print_state(tile_list)
	move(tile_list)
total_time = time.time()-start_time
print ("done! final time: %s" %total_time)
