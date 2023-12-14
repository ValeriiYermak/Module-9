from functools import reduce


def sum_numbers(numbers):
    
    result = reduce((lambda x, y: x + y), numbers)
    return(result)