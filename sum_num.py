def sum_numbers(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num
    return sum


def MaxDiff(num_list):
    """ returns the MaxDiff value

    :param:  num_list: list of values
    :param:  i : the index in num_list
    :param:  j : the index i + 1 in num_list
    :returns: return the max diff between two adjacent value from input num_list
    :raises: ImportError
    :raises: TypeError
    :raises: ValueError
    """

    try:
        import logging
    except ImportError:
        logging.error("No such file")
        print("No Imported file")

    logging.basicConfig(filename='divlog.txt', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    if len(num_list) == 0:
        logging.warning('This is not a list')

    try:
        max_diff = num_list[1] - num_list[0]
        i = 0
        j = i + 1
        for i in num_list:
           for j in num_list:
              if (j-i > max_diff):
                  max_diff = j - i
        return max_diff
    except TypeError:
        pass
    except ValueError:
        pass
    logging.info('Status quo')

def find_extremes(num_list):
    Minimum = min(num_list)
    Maximum = max(num_list)
    return (Minimum, Maximum)
