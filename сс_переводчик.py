'''Перевод числа из одной СС в другую'''

def translate(num, base, new_base):
	decimal = int(str(num), base)
	result = ''
	while decimal:
		result += '0123456789ABCDEF'[decimal%new_base]
		decimal //= new_base
	return result[::-1]