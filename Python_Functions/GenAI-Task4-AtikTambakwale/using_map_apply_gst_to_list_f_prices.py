prices = [100,250,400,1200,50]
print("Original Prices: ")
print(prices)

# calculate gst with price list using map() method 
# apply logic with lambda function with map() method
# covert into list and print new gst price list
price_with_gst = list(map(lambda price:price+(0.18*price),prices))
print("Price after GST:")
print(price_with_gst)