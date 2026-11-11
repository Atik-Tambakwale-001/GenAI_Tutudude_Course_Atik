# product list variable
products = ["watch","mobile","laptop","table","book","bike"]

product_dict = {
    "watch":1300,
    "mobile":15000,
    "laptop":65000,
    "table":4500,
    "book":350,
    "bike":78500
}

catalog=[
    ("watch",1300,"accessories"),
    ("mobile",15000,"electronics"),
    ("laptop",65000,"electronics"),
    ("table",4500,"furniture"),
    ("book",350,"stationery"),
    ("bike",78500,"vehicles")
]

category_to_product = {};total_number_products_list=[];
for product,price,category in catalog:
    if category in category_to_product.keys():
        list_product = category_to_product[category]
        list_product.append(product);
        category_to_product.update({category:list_product})
    else:
        category_to_product.update({category:[product]})

print(category_to_product["electronics"])