def divs(num):
	divs = {1, num}
	for div in range(2, int(num**0.5)+1):
		if num % div == 0: divs |= {div, num//div}
	return divs

def is_prime(num):
	if num % 2 == 0: return False
	div = 3
	while div**2 <= num:
		if num % div == 0:
			return False
		div += 2
	return True

from math import ceil, sqrt

def div_count(num):
	k = 2
	for div in range(2, ceil(sqrt(num))):
		if num % div == 0:
			k += 2
	if (div+1)**2 == num:
		k += 1
	return k