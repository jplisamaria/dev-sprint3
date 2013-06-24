# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name:Lisa-Maria Mehta

def rotate_letter (letter, n):
	rotation_factor = n % 26
	new_letter_ord = ord(letter) + rotation_factor
	if letter.isupper():
		if new_letter_ord <=90:
			return chr(new_letter_ord)
		else:
			return chr(new_letter_ord - 26)
	elif letter.islower():
		if new_letter_ord <=122:
			return chr(new_letter_ord)
		else:
			return chr(new_letter_ord - 26)
	else:
		return letter

def rotate_word (word, n):
	new_word = ""
	for char in word:
		new_word = new_word +rotate_letter(char, n)
	return new_word

def reverse (name):
	nickname = ""
	for i in range(len(name)):
		nickname = nickname + name[-i-1]
	return nickname

def fix_capitalization():
	pass

print rotate_word('Cheer' , 7)
print rotate_word('melon' , -10)
print rotate_word('Melon.head' , -10)
print rotate_word('sLEEp' , 9)
print reverse ('aira-masil')


