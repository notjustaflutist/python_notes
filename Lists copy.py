lucky_numbers = [12, 3, 4, 5, 34]
# 1:12 in Learn Python course for beginners
friends = ["dod", "fod", "tod", "glod"]

print(friends)
# extend function (concats lists)
friends.extend(lucky_numbers)
print(friends)
friends.append("bob")
print(friends)
friends.insert(1, "rod")
print(friends)
friends.remove("dod")
friends.clear()
friends.append("egg")
friends.append("toast")
friends.extend(lucky_numbers)
print(friends)
friends.pop()

print(friends)
print(friends.index("egg"))
print(friends.count("egg"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
num = lucky_numbers.copy()
print(num)
lucky_numbers.insert(2, 48)
print(lucky_numbers)


