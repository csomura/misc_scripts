def hanoi(depth,start,middle,end):
	if depth > 1:
		hanoi(depth-1,start,end,middle)
		hanoi(1,start,middle,end)
		hanoi(depth-1,middle,start,end)
	else:
		print("moving the top of %s to the top of %s" % (start,end))
	
