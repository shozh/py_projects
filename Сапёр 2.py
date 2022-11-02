row, col, mine = (int(i) for i in input().split())

a = [[0 for j in range(col)] for i in range(row)]

for _ in range(mine):
	i, j = (int(i) -1 for i in input().split())
	a[i][j] = '*'

for i in range(row):
	for j in range(col):
		if a[i][j] == 0:
			for di in range(-1, 2):
				for dj in range(-1, 2):
					if 0 <= i + di < row and 0 <= j + dj < col and a[i+di][j+dj] == '*':
						a[i][j] += 1

for i in range(row):
	for j in range(col):
		if a[i][j] == 0:
			a[i][j] = '.'

for i in a:
	print(*i, sep='  ')