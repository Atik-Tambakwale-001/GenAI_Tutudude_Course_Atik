# product list variable
products = ["watch","mobile","laptop","table","book","bike"]

# create short parallel list categories with same length of product list
categories = ["Accessories","Electronics","Electronics","Furniture","Stationery","Vehicles"]

# converted categories list variable into categories_set tuple variable
# print the categories_set tuple variable
categories_set = set(categories)
print(categories_set)

# adding categories value and show how set variable is ignored.
categories_set.add("Accessories")
print(categories_set)

print("Electronics" in categories_set)  # it return  True boolean value
print("Clothing" in categories_set)     # it return False boolean value

print(len(categories_set))