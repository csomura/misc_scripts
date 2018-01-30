import random

returnstring = "lazy"

def check(sub,main):
	#s=index of sub
	#m=index of main
	s = 0
	m = 0
	while 1:
		if sub[s] == main[m]:
			s += 1
			m += 1
		else:
			m += 1
		if s == len(sub):
			return 1
		if m == len(main):
			return 0
def getwords(sub):
	count = 0
	f = open("/usr/share/dict/words")
	for line in f.readlines():
		if check(sub,line) == 1:
			print line.rstrip()
			count += 1
	return count

def get_rand_string():
	returnstring = random.choice("abcdefghijklmnopqrstuvwxyz")+random.choice("abcdefghijklmnopqrstuvwxyz")+random.choice("abcdefghijklmnopqrstuvwxyz")
	return(returnstring)
	
def solve_last_word():
	getwords(returnstring)

	
print"getwords(sub)"
print"get_rand_string()"
print"solve_last_word()"
