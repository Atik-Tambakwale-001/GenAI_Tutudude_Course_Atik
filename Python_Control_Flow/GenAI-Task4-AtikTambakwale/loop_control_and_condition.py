# the given daily sales values into list variable
list_daily_sales = [200,150,0,400,50,-1,300]

# total_sales variable for store total sale amount
total_sales = 0

# iterate through it with for loop amd given daily sale list 
for sale_value in list_daily_sales:
    # check negitive value and break for stop loop
    if sale_value == -1:
        print("processing loop due corrupted data value like ",sale_value)
        break
    
    # check zero value with continue for skip loop
    elif sale_value == 0:
        print("skipping adding to revenue")
        continue

    # check positive integer numbers and greater than zero amount
    elif sale_value > 0:
        
        # adding each sale value
        total_sales+=sale_value

        # print running time sale value and total_value
        print("adding sales value: ",sale_value)
        print("Running total sale value : ",total_sales)

print("The Final Total Daily sales : ",total_sales)