def largest_difference(num_list):
    max_num = max(num_list[0], num_list[1])
    min_num = min(num_list[0], num_list[1])
    for i in range(2, len(num_list)):
        if num_list[i] > max_num:
            max_num = num_list[i]
            print("current max: "+ str(max_num))

        if num_list[i] < min_num:
            min_num = num_list[i]
            print("current min: " + str(min_num))

    return max_num - min_num


# short solution
def largest_differences(numbers):
    return max(numbers) - min(numbers)


nums = [1, 2, 3, 4, 5, 6]
print(largest_difference(nums))
print(largest_differences(nums))