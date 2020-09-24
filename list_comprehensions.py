# new_list = [expression for member in iterable (if conditional)]

squares = [i * i for i in range(10)]
print(squares)


'''
Writing short code
Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a single line of code.

# using a list comprehension
def convert(ns):
    return [str(n) for n in ns]

# using map
def convert(ns):
    return list(map(str, ns))
'''


'''
# ugly but understandable solution
def zap(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result

# concise solution with list comprehensions
def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]

'''

'''
Rather than creating an empty list and adding each element to the end, you simply define the list and its contents at 
the same time by following this format:

new_list = [expression for member in iterable]
Every list comprehension in Python includes three elements:

expression is the member itself, a call to a method, or any other valid expression that returns a value. In the example 
above, the expression i * i is the square of the member value.
member is the object or value in the list or iterable. In the example above, the member value is i.
iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the 
example above, the iterable is range(10).
Because the expression requirement is so flexible, a list comprehension in Python works well in many places where you 
would use map(). You can rewrite the pricing example with its own list comprehension:
'''