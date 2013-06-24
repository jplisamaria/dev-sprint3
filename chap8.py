# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name:Lisa-Maria Mehta

def rotate_letter (letter, n):
	"""Takes a letter and an integer n as input, and returns letter
	n places away from original letter."""
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
	"""Takes a word and an integer n as input.  Calls rotate_letter
	and returns a word with each letter n places away from
	original letters."""
	new_word = ""
	for char in word:
		new_word = new_word +rotate_letter(char, n)
	return new_word

print rotate_word('Cheer' , 7)
print rotate_word('melon' , -10)
print rotate_word('Melon.head' , -10)
print rotate_word('sLEEp' , 9)

