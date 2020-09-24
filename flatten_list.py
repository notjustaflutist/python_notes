def flatten(li):
    # I have no idea why this works
    flat_li = []
    for outer in li:
        flat_li += outer
    return flat_li


li = [
    [1, 1.1, 1.2],
    [2, 2.2, 2.3]
]

print(li)
print(flatten(li))

'''
# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]
'''