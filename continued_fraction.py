''' Finite simple continued fraction '''

numerator, denominator = map(int, input().split('/'))
continued_frac = []

while denominator:
	continued_frac.append(numerator // denominator)
	numerator, denominator = denominator, numerator % denominator

print(*continued_frac)