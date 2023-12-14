from functools import reduce


def amount_payment(payment):
    
    new_list = filter(lambda x: x > 0, payment)
    result = reduce((lambda x, y: x + y), new_list)
    return(result)