words = input().split()
alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97,123)]
shifted_text = []

for word in words:

	word_without_punctuation = ''
	for letter in word:
		if letter.isalpha():
			word_without_punctuation += letter
	shift = len(word_without_punctuation)

	shifted_letters = []
	for letter in word:
		if letter.isalpha():
			if letter.isupper():  
				shifted_letters.append(alphabet[(alphabet.index(letter) + shift) % 26])
			else:
				shifted_letters.append(alphabet[(alphabet.index(letter) + shift) % 26 + 26])
		else:
			shifted_letters.append(letter)
	
	shifted_word = ''
	for letter in shifted_letters:
		shifted_word += letter

	shifted_text.append(shifted_word)

print(*shifted_text)