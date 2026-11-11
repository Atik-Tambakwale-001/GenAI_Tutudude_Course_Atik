products = {
    "watch":1300,
    "mobile":15000,
    "laptop":65000,
    "table":4500,
    "book":350,
    "bike":78500
}
print(products)

products["pen"]=10
print(products)

products["book"]=300
print(products)

del products["pen"]
print(products)

print(sum(products.values())/len(products))