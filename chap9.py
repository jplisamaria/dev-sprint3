# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name:Lisa-Maria


# ******************
# ** Exercise 9.1 **
# ******************
# Words longer than 20 characters
# -------------------------------

def find_longwords(fin):
	'''Takes a file, and checks for words > 20 chars.'''
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print word
	return

# Main Program
# ------------
fin = open('words.txt')
print
print 'Words longer than 20 letters'
print '----------------------------'
find_longwords(fin)



# ******************
# ** Exercise 9.2 **
# ******************
# Has no 'e'
# ----------

def has_no_e(word):
	'''Checks individual word to see if it has an "e".'''
	for i in range (len(word)):
		if word[i] == 'e':
			return False
	return True

def info_words_with_no_e(fin):
	'''Takes a file.  Runs "has_no_e". Prints some statistical info.'''
	all_words = 0.0
	no_e_words = 0.0

	for line in fin:
		word = line.strip()
		all_words = all_words +1
		if has_no_e(word):
			no_e_words = no_e_words +1
#			print word
	print 'Total number of words =', all_words
	print "Total number of words without 'e'=", no_e_words
	print "Percentage of words with no 'e'=", (no_e_words)*100/all_words , "%"

# Main Program
# ------------
fin = open('words.txt')
print
print
print 'Words with no e'
print '---------------'
info_words_with_no_e(fin)



# ******************
# ** Exercise 9.3 **
# ******************
# Forbidden letters
# -----------------

def avoids(word,bad_letters):
	'''Checks individual word to see if it has forbidden letters.'''
	for letter in word:
		if letter in bad_letters:
			return False
	return True

def find_words_without_forbidden_letters(fin, bad_letters):
	'''Takes a file, and runs "avoids".  Gives some statistical info.'''
	all_words = 0.0
	no_bad_letters = 0.0
	for line in fin:
		all_words = all_words +1
		word = line.strip()
		if avoids(word, bad_letters):
			no_bad_letters = no_bad_letters + 1
#			print word
	print 'Total number of words =', all_words
	print "Total number of words without forbidden letters=", no_bad_letters
	print "Percentage of words with no forbidden letters=", (no_bad_letters)*100/all_words , "%"	

def get_bad_letters():
	'''Gets user input for 5 "forbidden" letters.'''
	print "Enter 5 forbidden letters:"
	return raw_input()

# Main Program
# ------------
fin = open('words.txt')
print
print
bad_letters = get_bad_letters()
print 'Words without', bad_letters
print '-------------------------------'
find_words_without_forbidden_letters(fin, bad_letters)



# ******************
# ** Exercise 9.4 **
# ******************
# Find words that use only certain letters
# ----------------------------------------

def uses_only(word,good_letters):
	'''Checks individual word to see if it has only allowable letters.'''
	for letter in word:
		if letter not in good_letters:
			return False
	return True

def find_words_using_only(fin, good_letters):
	'''Takes a file, and runs "uses_only".  Gives some statistical info.'''
	all_words = 0.0
	uses_only_words = 0.0
	for line in fin:
		all_words = all_words +1
		word = line.strip()
		if uses_only(word, good_letters):
			uses_only_words = uses_only_words + 1
			print word
	print 'Total number of words =', all_words
	print "Total number of words using only allowably letters=", uses_only_words
	print "Percentage of words using only allowable letters=", (uses_only_words)*100/all_words , "%"	

def get_good_letters():
	'''Gets user input for allowable letters.'''
	print "Enter allowable letters letters:"
	return raw_input()

# Main Program
# ------------
fin = open('words.txt')
print
print
good_letters = get_good_letters()
print 'Words with allowable letters', good_letters
print '-------------------------------'
find_words_using_only(fin, good_letters)