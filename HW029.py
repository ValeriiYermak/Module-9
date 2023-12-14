DEFAULT_DISCOUNT = 0.05

def get_discount_price_customer(price, customer):

    for _ in customer.items():
        if customer.get("discount") is None:
            discount = DEFAULT_DISCOUNT
            price = price * float(1 - discount)
        else:
            discount = float(customer.get("discount"))
            price = price * float(1 - discount)
        print(price)
        return price


get_discount_price_customer(10, {"name":"Stepan"})


#{"name":"Stepan", "discount": 0.15}