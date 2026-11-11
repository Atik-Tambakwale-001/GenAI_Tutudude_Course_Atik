# create apply discount  function with default 5 percentage discount
def apply_discount(price,discount=5):
    # check if discount is not exceeds 60 percentage condition 
    if discount>60:
        return "Discount Not Exceeds Above 60%"
    
    # discount calculation logic
    return price*(discount/100)

#passing argument are 1000 price and 10 percentage
print(apply_discount(1000,10))

# passing only price argument to check default value
print(apply_discount(500))

# check not exceed 60 percentage discount 
print(apply_discount(2000,67))
