def sum_numbers(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num
    return sum


def MaxDiff(num_list):
    max_diff = num_list[1] - num_list[0]
    i = 0
    j = i + 1
    for i in num_list:
        for j in num_list:
            if (j-i > max_diff):
                max_diff = j - i
    return max_diff


def find_extremes(num_list):
    Minimum = min(num_list)
    Maximum = max(num_list)
    return (Minimum, Maximum)
