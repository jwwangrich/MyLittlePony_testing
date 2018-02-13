def sum_numbers(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num
    return sum


def MaxDiff(num_list):
    max_diff = num_list[1] - num_list[0]
    for i in num_list:
        for j+1 in num_list:
            if (num_list[j] - num_list[i] > max_diff):
                max_diff = num_list[j] - num_list[i]
    return max_diff
