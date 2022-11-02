field = [int(i) for i in input('Введите кол-во строк, кол-во столбцов и кол-во мин через пробел').split()]

mines = []
for _ in range(field[2]):
	mines.append([int(j) - 1 for j in input('Введите расположение мины (первое - строка, второе - столбец): ').split()])

row = field[0]
col = field[1]

arr = [[0 for j in range(col)] for i in range(row)]

for i in mines:
	arr[i[0]][i[1]] = -1

for i in range(row):
	for j in range(col):
		if arr[i][j] != -1: 
			count = 0
			if i - 1 >= 0 and j - 1 >= 0 and arr[i-1][j-1] == -1: # верхний левый
				count += 1
			if i - 1 >= 0 and arr[i-1][j] == -1: # верхний
				count += 1
			if i - 1 >= 0 and j + 1 < col and arr[i-1][j+1] == -1: # верхний правый
				count += 1
			if j - 1 >= 0 and arr[i][j-1] == -1: # левый
				count += 1 
			if j + 1 < col and arr[i][j+1] == -1: # правый
				count += 1
			if i + 1 < row and j - 1 >= 0 and arr[i+1][j-1] == -1: # нижний левый
				count += 1
			if i + 1 < row and arr[i+1][j] == -1: # нижний
				count += 1
			if i + 1 < row and j + 1 < col and arr[i+1][j+1] == -1: # нижный правый
				count += 1
			if count == 0:
				arr[i][j] = '.'
			else:
				arr[i][j] = count

for i in mines:
	arr[i[0]][i[1]] = '*'

for i in arr:
	print(*i, sep='  ')