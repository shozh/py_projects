direction = input('Шифрование или дешифрование:')
shift = int(input('Шаг сдвига:'))
en_alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97,123)]
ru_alphabet = [chr(i) for i in range(1040, 1104)]

shift = -shift if direction == 'дешифрование' else shift

text = input('Введите текст: ')

if text[0] in en_alphabet: 
	alphabet = en_alphabet
	size = 26
else:
	alphabet = ru_alphabet
	size = 32

shifted_letters = []
for letter in text:
	if letter.isalpha():
		if letter.isupper():
			shifted_letters.append(alphabet[(alphabet.index(letter) + shift) % size])
		else:
			shifted_letters.append(alphabet[(alphabet.index(letter) + shift) % size + size])
	else:
		shifted_letters.append(letter)
print(''.join(shifted_letters))