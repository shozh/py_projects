def is_valid(number, a, b):
	''' Проверяет входит ли введенное число в заданный интервал'''

	return a <= number <= b        

def min_count_guess(number):
	''' За какое минимальное количество попыток можно угадать число. '''
	i = 1
	while 2 ** i < number: 
		i += 1
	return i

def guesser(a, b):
	''' Сама система угадывание на промежутке'''

	from random import randint
	print('Числа загадано, попробуйте отгадать.')
	r = randint(a, b)
	count = 0

	while True:    
		n = int(input(f'Введите число от {a} до {b}: '))

		if not is_valid(n, a, b):
			print('Число вне диапозона.')
			continue
		if n > r:
			print('Не то. Попробуйте ввести число поменьше')
		if n < r:
			print('Не то. Попробуйте ввести число побольше')
		count += 1
		if n == r:
			print('Вы угадали. Загаданное число:', n)
			print('Всего попыток', count)
			print('100% число можно было угадать за', min_count_guess(b - a))
			break

def continue_game():
	''' Возращает игру заного, если человек ввел положительный ответ'''

	ans = input('Если хотите еще сыграть в игру, напишите \'д\', а если не хотите, - \'н\'\n')
	while True:
		if ans not in ('y', 'д', 'n', 'н', 'yes', 'no', 'да', 'нет'):
			ans = input('Напишет корректнее: ')
		elif ans in ('n', 'н', 'no', 'нет'):
			print('До новых встреч!')
			return False
		else:
			return True

def game():
	print('Добро пожаловать в числовую угадайку. \nЕсли хотите сыграть в нее, напишите \'д\', а если не хотите, - \'н\'.\n')
	ans = input()
	if ans not in ('yes', 'y', 'д', 'да'):
		return False

	while True:
		edges = [int(i) for i in input('Введите промежутки интервала, через пробел: ').split()]
		while len(edges) != 2 or edges[0] == edges[1]:
			print('Некорректные данные промежутков. Ввод должен содержать два неравных числа, написанных через пробел\n')
			edges = [int(i) for i in input('Введите промежутки интервала, через пробел: ').split()]
		if edges[0] > edges[1]:
			edges[1], edges[0] = edges[0], edges[1]

		guesser(edges[0], edges[1])

		if continue_game():
			continue
		else:
			break

game() # вызов функции игры