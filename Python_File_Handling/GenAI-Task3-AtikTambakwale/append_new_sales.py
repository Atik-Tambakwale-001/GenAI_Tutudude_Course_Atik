# define new sale amounts in the list variable
new_sales_amounts = [5000,2500,1700]

# Appending new sale amount with existing sales_data.txt file
with open("sales_data.txt","a") as f:
    for sale_amount in new_sales_amounts:
        f.write(str(sale_amount)+"\n")

# read sales_data.txt file
# get all sale amounts and print all sale amounts
# print total number of lines in sales_data.txt file
with open("GenAI-Task3-AtikTambakwale/sales_data.txt","r")as f1:
    all_sale_amounts = f1.readlines()
 
    sales_amounts_list = []
    for sale_amount in all_sale_amounts:
        sales_amounts_list.append(int(sale_amount.strip()))
 
    print(sales_amounts_list)
    print("total number of lines after appending : ",len(all_sale_amounts))