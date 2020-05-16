#!/usr/bin/python3
#@a: is a tuple with current coordenates.
#@b: is a tuple with end coordenates.
def dir(a, b):
	x = b[0] - a[0]
	y = b[1] - a[1]

	#validate direction mov in x
	if x < 0:
		x = -1
	elif x > 0:
		x = 1
	else:
		x = 0

	#validate direction mov in y
	if y < 0:
		y = -1
	elif y > 0:
		y = 1
	else:
		y = 0
	
	#return tuple
	return (x, y)
	
