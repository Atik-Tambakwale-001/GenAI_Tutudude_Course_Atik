# define price amount with 100 value
price = 100
print("The Given price : ",price)

# create gst calculation with lambda function
gst_amt = lambda price:price+(0.18*price)
print("given price with 18% gst :",gst_amt(price))

# create compute final price with gst and discount together
discount_amt = lambda price,discount:price+gst_amt(price)+(discount/100)
print("Compute final price discount amount after GST + 10% discount : ",discount_amt(price,10))
