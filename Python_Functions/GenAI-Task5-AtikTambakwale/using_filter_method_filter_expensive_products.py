# Given price list
prices = [100,250,400,1200,50,2000,850]
print("Origina List :\n",prices)

# check prices which are greater then 500 and convert into list and print it
prices_greater_list = list(filter(lambda price:price>500,prices))
print("List of prices greater then 500 :\n",prices_greater_list)

# check prices which are less then and equal to 500 and convert into list and print it
prices_less_list = list(filter(lambda price:price<=500,prices))
print("List of prices less then and equal to 500 :\n",prices_less_list)