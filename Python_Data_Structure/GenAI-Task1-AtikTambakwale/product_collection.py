# create 6 product names list and create sample_product tuple variable
products= ["watch","mobile","laptop","table","book","bike"]

# product_name,price,category
sample_product = ("casio",1300,"fashion") 

# print 2nd and last product name
print(products[1])
print(products[len(products)-1])

# print append 2 product names like pen,cabinet
products.append("pen")
products.append("cabinet")

# print updated product names list
print(products)

# converted tuple variable into list variable 
converted_into_list_sample_product = list(sample_product)
# and print converted list variable
print(converted_into_list_sample_product)

# update price value 1350
converted_into_list_sample_product[1]=1350

# converted list into tuple again variable type
converted_into_tuple_smaple_product = tuple(converted_into_list_sample_product)
# print converted tuple variable
print(converted_into_tuple_smaple_product)
