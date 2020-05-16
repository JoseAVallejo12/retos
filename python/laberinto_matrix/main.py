#!/usr/bin/python3
if __name__ == "__main__":
    from matrices import matrix
    from dir_control import dir

    start = (3,5)
    fin = (5,5)
    mtx = matrix(1)

	'''
	for n in range(1,4):
		a = matrix(n)
		pass
		for i in a:
			print(i)
		print("")
	'''
    dir_mov = dir(start, fin)
    print(dir_mov)