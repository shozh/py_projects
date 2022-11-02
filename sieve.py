'''Sieve of Eratosthenes'''

def sieve(n: int) -> list[bool]:
	a = [True] * n
	a[0] = a[1] = False

	i = 2
	while i * i < n:
		if a[i]:
			for j in range(i * i, n, i):
				a[j] = False
		i += 1
	return a