import re
def generator_numbers(string=""):

    pattern = (r'[0-9]+')
    numbers = re.findall(pattern, string)
    for i in numbers:
        yield i
    

def sum_profit(string):
    sum = 0
    func = generator_numbers(string)
    for i in func:
        sum += int(i)
    return sum





generator_numbers("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.")
# string="The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
# print (string)
# sum_profit(string)
# string="The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."    
# print (string)