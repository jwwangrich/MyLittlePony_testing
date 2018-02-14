def sum_numbers(num_list=[]):
    """ returns the sum of numbers in an inputted list

    :param numlist: list of values – each entry will be added up
    :returns: sum of each entries from input num_list
    :raises: TypeError
    :raises: ValueError
    :raises: ImportError
    """

    try:
        import logging
    except ImportError:
        logging.error("There is an ImportError")
        print("Requested import file does not exist.")

    logging.basicConfig(filename='divlog.txt', format= '%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    
    if len(num_list) == 0:
        logging.warning("num_list is empty")
    
    sum = 0
    try:
        for num in num_list:
            sum = sum + num
    except TypeError:
        logging.error("There is a TypeError")
        print("num_list must be a list containing variable type entries.")
    except ValueError:
        logging.error("There is a ValueError")
        print("The entries list must consist only of real numbers.")

    logging.info("All entries successfully added up.")

    return sum
