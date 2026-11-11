# get discount price after calculate discount percentage
def apply_discount(price,percent):
    return price*(percent/100)

#get flat price after calculate 50 flat value
def flat_discount(price):
    return price-50