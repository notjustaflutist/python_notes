"""
from http://greenteapress.com/thinkpython2/html/thinkpython2010.html
"""

fin = open('words.txt')  # file input
'''
line = fin.readline()
word = line.strip()
count = 0
for line in fin:
    word = line.strip()
    count += 1
    print(word)
print(count)
'''
"""
Write a program that reads words.txt and prints only the words 
with more than 20 characters (not counting whitespace).
"""

'''
count = 0
for line in fin:
    word = line.strip()
    if len(word) >= 20:
        print(word)
        count += 1
print(count)
'''

"""
Write a function called has_no_e that returns 
True if the given word doesn’t have the letter “e” in it.

Write a program that reads words.txt and prints only the 
words that have no “e”. 
Compute the percentage of words in the list that have no “e”.
"""


def has_no_e(word):
    """Returns True if word does not contain 'e' or 'E'."""
    return "e" not in word and "E" not in word


'''
for line in fin:
    word = line.strip()
    if has_no_e(word):
        print(word)
'''

"""
Write a function named avoids that takes a word and a string 
of forbidden letters, and that returns True if the word 
doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string 
of forbidden letters and then prints the number of words 
that don’t contain any of them. Can you find a combination 
of 5 forbidden letters that excludes the smallest number of words?
"""


def avoids(word, forbidden_letters):
    """Returns true if word does not contain letters in forbidden_letters."""
    '''
    letters = list(forbidden_letters)
    result = True
    for l in letters:
        if l in word:
            result = False
    '''
    for letter in word:
        if letter in forbidden_letters:
            return False
    return True


'''
forbidden_letters_string = str.lower(input("Enter letters to exclude: "))
count = 0
for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters_string):
        count += 1
        print(word)
print(count)
'''

"""
Write a function named uses_only that takes a word and a 
string of letters, and that returns 
True if the word contains only letters in the list. 
Can you make a sentence using only the letters acefhlo? 
Other than “Hoe alfalfa”?
"""


def uses_only(word, avail_letters):
    """Returns True if word is comprised of letters in avail_letters."""
    '''
    result = True
    spelling = list(word)
    for l in spelling:
        if l not in avail_letters:
            result = False
    return result
    '''
    for letter in word:
        if letter not in avail_letters:
            return False
    return True


'''
for line in fin:
    word = line.strip()
    if uses_only(word, "achlo"):
        print(word)
'''

"""
Write a function named uses_all that takes a word and a 
string of required letters, and that returns True if the 
word uses all the required letters at least once. How many words 
are there that use all the vowels aeiou? How about aeiouy?
"""


def uses_all(word, required_str):
    """Returns True if all letters in required_str are in word."""
    '''
    result = True
    required = list(required_str)
    for l in required:
        if l not in word:
            result = False
    return result
    '''
    '''
    for letter in required_str:
        if letter not in word:
            return False
    return True
    '''
    return uses_only(required_str, word)

'''
count = 0
for line in fin:
    word = line.strip()
    if uses_all(word, "aeiouy"):
        print(word)
        count += 1
print(count)
'''

"""
Write a function called is_abecedarian that returns 
True if the letters in a word appear in alphabetical order 
(double letters are ok). How many abecedarian words are there?
"""


def is_abecedarian(word):
    """Returns True if letters in word are in alphabetical order."""
    lword = str.lower(word)
    result = True
    for i in range(len(lword) - 1):
        if lword[i] > lword[i + 1]:
            result = False
    return result

'''
count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print(word)
        count += 1
print(count)
'''


