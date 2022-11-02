'''Алгоритм Евклида'''

''' def gcd(a, b):
	if max(a, b) % min(a, b) == 0:
		return min(a, b)
	return gcd(max(a, b) % min(a, b), min(a, b))
'''

def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a, b)