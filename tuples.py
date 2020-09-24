# tuples are immutable

t = ("Max", 28, "Boston")  # also, t = "Max", 28, "Boston" (parenthesis optional)
t_using_function = tuple(["Max", 3])
print(t)
print(t_using_function)
print(type(t_using_function))

one_element_tuple = "Max",
print(type(one_element_tuple))

item = t[0]  # access item in tuple (or negative index)
print(item)

# iterate over a tuple
for i in t:
    print(i)

