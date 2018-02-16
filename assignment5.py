def sum_numbers(num_list):
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

# Set up logger
import logging
log_format = '%(levelname)s %(asctime)s %(message)s'
logging.basicConfig(filename='divlog.txt', format= log_format, datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logger = logging.getLogger()

def findextremes(num_list):
    """ returns the smallest and largest elements in an inputted list
    :param: num_list
    :returns: the smallest and largest elements in input num_list
    :raises: TypeError: Input list must not be empty
    :raises: ValueError: Numbers in list must be real numbers
    :raises: ImportError: Numpy must be installed in Env
    """

    # Make sure list criteria are met
    try:
        check_input(num_list)
    except ValueError:
        logging.error('Input must be a list composed of real, numeric entries')
        quit()
    except TypeError:
        logging.error('Input must be list with entries')
        quit()

    try:
        import numpy as np
    except ImportError:
        logging.error('Numpy must be installed in your local environment!')


    logger.info("# Find Minimum and Maximum")
    logger.debug('Input: %s', str(num_list))
    minimum = np.min(num_list)
    maximum = np.max(num_list)
    logging.info("# Return Minimum and Maximum")
    logging.debug('Output: %s',(minimum, maximum))


    return [minimum,maximum]


def contains_imaginary(num_list):
    import numpy as np
    is_real = np.isreal(num_list)
    if False in is_real:
        imaginary_elements = True
    else:
        imaginary_elements= False
    return imaginary_elements

def check_list(num_list):

    if type(num_list) == list:
        list_input = True
    else:
        list_input = False
    return list_input

def check_input(num_list):

    # Check that input is a list
    if check_list(num_list) == False:
        raise TypeError('Input must be a list')

    # Check that list has entries
    if len(num_list) == 0:
        raise TypeError('Input list is empty')

    # Check for imaginary numbers in list
    if contains_imaginary(num_list) == True:
        logging.error('Input list contains imaginary elements')
        raise ValueError('Input list contains imaginary elements!')

output = findextremes([1,2,3])
logger.debug('Output:%s', str(output))

def main(num_list):
    sum = sum_numbers(num_list)
    min_and_max = findextremes(num_list)

    return sum, min_and_max

print(main([1,2,3]))