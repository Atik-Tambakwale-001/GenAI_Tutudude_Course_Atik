def process_price(prices_list):
    # create code which get prices list with 10 % discount list 
    discounted_prices_list = list(map(lambda price:price+(price*0.10),prices_list))
    
    # create below code filter() method to get filter list price above 300 price list
    discounted_prices_above_list = list(filter(lambda discount_price:discount_price>300,discounted_prices_list))

    # return both list for print it
    return [discounted_prices_list,discounted_prices_above_list]

# calling process_price function with given list
given_list = [100,500,900,50,750]
process_lists = process_price(given_list)

print("Given Original list:\n",given_list)
print("Apply 10% discount to all prices list:\n",process_lists[0])
print("Only Discounted prices list that are above 300:\n",process_lists[1])