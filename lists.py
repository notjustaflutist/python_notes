my_list = ["banana", "cherry", "apple"]
print(my_list)

# can create empty list this way
my_list2 = list()
print(my_list2)

# lists can contain different data types
my_list3 = [5, True, "apple", "apple"]
print(my_list3)

item = my_list[0]
print(item)

item2 = my_list[-1]
print(item2)

# iterate over list
for i in my_list:
    print(i + " :) ")

# check for item in list
if "apple" in my_list3:
    print("yes")
else:
    print("no")

# returns number of elements in list
print(len(my_list3))

# append item
print(my_list3)
my_list3.append("lemon")
print(my_list3)

# insert at position (index, item)
my_list3.insert(3, "potato")
print(my_list3)

# remove items from list
a = my_list3.pop()  # returns and removes last item in list
print(a)
print(my_list3)
my_list.remove("banana")
print(my_list)

my_list2.clear()
print(my_list2)

my_list3.reverse()
my_list.sort()  # changes the original list
new_list = sorted(my_list)
print(my_list)
print(new_list)

my_list4 = [0] * 5
print(my_list4)

my_list5 = my_list4 + my_list3
print(my_list5)

# slice [start index : stop index : step index]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = nums[1:5]
print(a)

b = nums[::2]
print(b)

c = nums[::-1]  # reverses a list
print(c)

d = nums[::]
print(nums)
print(d)

# lists copied to additional variables directly reference the same object
e = nums.copy()  # copies list
f = list(nums)  # copies list
g = nums [:]  # copies list

# list comprehensions
# [expression for value in list if condition]
li = [1, 2, 3, 4, 5]
licomp = [i * i for i in li]
print(licomp)

