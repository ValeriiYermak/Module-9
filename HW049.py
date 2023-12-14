def discount_price(discount):

    def count_price(price):
        price = price * float(1 - discount)
        return price 
    return count_price
    
price = 100

cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)


print(cost_15(price))
print(cost_10(price)) 
print(cost_05(price))   