def palindrome(string):
    i = 0
    j = -1
    result = True
    for ch in string:
        if string[i] != string[j]:
            result = False
        i += 1
        j -= 1
    return result

'''
# iterative solution:
# keep chopping off the head and tail of the string,
# and compare the two. If they are not equal, it's
# not a palindrome. Stop when the string gets too short.
def palindrome(string):
    while len(string) > 1:
        head = string[0]
        tail = string[-1]
        string = string[1:-1]
        if head != tail:
            return False
    return True

# recursive solution: equivalent to the above.
def palindrome(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and palindrome(string[1:-1])

# smarter solution:
# check if reversing the string gives the same string.
def palindrome(string):
    return string == string[::-1]
'''
v = "vanna"
a = "anna"
print(palindrome(a))
print(palindrome(v))
