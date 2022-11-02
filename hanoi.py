'''Ханойские башни '''
def hanoi(n, start, finish):
	if n == 1:
		print(start, '-', finish)
	else:
		tmp = 6 - start - finish
		hanoi(n - 1, start, tmp)
		print(start, '-', finish)
		hanoi(n - 1, tmp, finish)

hanoi(int(input()), 1, 3)