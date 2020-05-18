#!/usr/bin/python3
if __name__ == "__main__":
    from matrices import matrix
    from dir_control import dir
    from find_route import f

    start = (3, 5)
    fin = (5, 5)
    mtx = matrix(1)

    dir_mov = dir(start, fin)
    print(dir_mov)
