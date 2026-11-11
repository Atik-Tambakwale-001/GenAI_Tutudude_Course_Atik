# added new price into list variable using append() method
def add_price(price_list,price):
    price_list.append(price)
    return price_list

# check get average price from prices list using sum() and len() methods
def get_average_price(price_list):
    if(len(price_list)>0):
        return sum(price_list)/len(price_list)
    else:
        return 0

# check get maximum price in the list using max() and len() methods
def get_max_price(price_list):
    if(len(price_list)>0):
        return max(price_list)
    else:
        return "none"

# create price list which stored using while loop
price_list=[]
while True:
    # print price list and display menu options with input() method
    print(price_list)
    print("Menu options :\n1 -- Add Price\n2 -- Show Average Price\n3 -- Show Maximum Price\nq -- Quite\n")
    option = input("Enter menu option:").strip().lower()

    # option 1 for add new price into list with calling add_price() function and show menu options
    if(option =="1"):
        price = float(input("Add price to the list :"))
        add_price(price_list,price)
        continue

    # option 2 for get average prices from list with calling get_average_price() function and show menu options
    elif(option == "2"):
        average_price = get_average_price(price_list)
        print("The average price : ",average_price)
        continue

    # option 3 for get maximum price from list with calling get_max_price() function and show after menu options
    elif(option == "3"):
        max_price = get_max_price(price_list)
        print("The Maximum price from prices list: ",max_price)
        continue
    
    # option q for quit block of loop code 
    elif(option == "q"):
        break
    
    # if any option not matched then it show invalid option
    else:
        print("Invalid menu option. Please try again.")
        continue