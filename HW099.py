def positive_values(list_payment):
    
    new_list = filter(lambda x: x > 0, list_payment)
    return list(new_list)
    



