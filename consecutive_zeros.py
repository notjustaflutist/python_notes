def consecutive_zeros(bin_string):
    count = 0
    max_count = 0
    for n in bin_string:
        if n == "1":
            count = 0
        elif n == "0":
            count += 1
            if count > max_count:
                max_count = count
    return max_count


s = "000100100000101"
print(consecutive_zeros(s))

'''
# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
'''