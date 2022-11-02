'''Реализация некоторых встроенных функций'''

def filter(function, items):
	result = []
	for item in items:
		if function(item):        
			result.append(item)
	return result

def map(function, items):
	result = []
	for item in items:
		new_item = function(item)
		result.append(new_item)
	return result

def reduce(operation, items, initial_value):
	acc = initial_value
	for item in items:
		acc = operation(acc, item)
	return acc

def all(iterable):
	for item in iterable:
		if not item:
			return False
	return True

def any(iterable):
	for item in iterable:
		if item:
			return True
	return False

def zip(*iterables):
	length = min(map(len, iterables))
	result = []
	for index in range(length):
		new_item = tuple(map(lambda item: item[index], iterables))
		result.append(new_item)
	return result

def enumerate(iterable, start=0):
	result = []
	for index in range(len(iterable)):
		new_item = (index + start, iterable[index])
		result.append(new_item)
	return result