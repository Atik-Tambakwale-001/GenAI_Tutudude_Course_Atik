# ask user 3 product info data from input() method
# collecting product name and price and stored into list variable
i=1;product_info_list=[]
while(i<=3):
    product = input(f"Enter product name {i} : ")
    price = input(f"Enter product price {i} : ")
    product_info_list.append(product+"|"+price+"\n")
    i+=1

# writing file using collect product info data list
with open("GenAI-Task5-AtikTambakwale/products_data.txt","w") as f:
    for product_info in product_info_list:
        f.write(product_info)

# read a file products_data.txt data using readlines()
# print all products name and price using for loop
print("\n All Products info data : ")
with open("GenAI-Task5-AtikTambakwale/products_data.txt","r") as f1:
    get_all_product_info = f1.readlines()
    count=1
    for product_info in get_all_product_info:
        print(f"Product {count} name and price : {product_info}")
        count+=1
