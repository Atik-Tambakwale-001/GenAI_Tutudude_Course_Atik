# create sales amounts list varible
sales = [1200,450,980,1500,3000]

# open sales_data.txt file
# write each sales amount into file using for loop
file = open("./sales_data.txt","w")
for sale_value in sales:
    # write sale amount with each new lines
    file.write(str(sale_value)+"\n")
file.close()

# re-open sales_data.txt file 
file2 = open("./sales_data.txt","r")
# read file content 
file_content = file2.read()
# stored into variable and print it
print(file_content)
file2.close()

# open sales_data.txt file
# write each sales amount into file using for loop
file = open("./sales_data.txt","w")
for sale_value in sales:
    # write sale amount with each seperated comma (,)
    file.write(str(sale_value)+",")
file.close()

# re-open sales_data.txt file 
file2 = open("./sales_data.txt","r")
# read file content 
file_content = file2.read()
# stored into variable and print it
print(file_content)
file2.close()