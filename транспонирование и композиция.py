# Траспонирование матрица и композиция одной и той же функции

matrix =[[1, 2, 3,], [4, 5, 6], [7, 8, 9]]

for row in matrix:
	print(*row)

def transpose(matrix):
	transposed_matrix = [list(tpl) for tpl in zip(*matrix)][::-1]
	return transposed_matrix

def repeater(function, power):
	def tmp(x):
		for _ in range(power):
			x = function(x)
		return x
	return tmp

matrix = repeater(transpose, 2)(matrix)

for row in matrix:
	print(*row)