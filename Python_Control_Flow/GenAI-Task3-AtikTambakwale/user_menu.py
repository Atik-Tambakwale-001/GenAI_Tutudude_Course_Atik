# store order amount into list variable
order_menu_list = []

# create while Loop with True Boolean value 
while True:
    # Display Menu Options and input menu option 
    print("Menu Option :")
    print("1 -- Add order amount to a running list")
    print("2 -- Show all orders and totals after applying discounts")
    print("q -- Quit")
    menu_option = input("Provide menu option: ")

    # 1 menu option for added order amount into order menu list 
    # variable with input() method and converted into integer from string
    if(menu_option == "1"):
        order_amount = int(input("Add order Amount to a running list : "))
        order_menu_list.append(order_amount)
        print("Order Amount added successfully!")
        continue

    # 2 menu option for show all order amount
    # After discount amount and it calculation
    # all order amounts total after discount 
    elif(menu_option == "2"):
        total_revenue_amount=0
        for order_item in order_menu_list:
            if(order_item>=2000):
                final_amount=order_item-(order_item*0.15)
                discount_amount = "15%"
            elif(1500<=order_item and order_item<2000):
                final_amount=order_item-(order_item*0.10)
                discount_amount = "10%"
            elif(1000<=order_item and order_item<1500):
                final_amount=order_item-(order_item*0.07)
                discount_amount = "7%"
            else:
                final_amount = order_item
                discount_amount = "0%"
            total_revenue_amount+=final_amount
            print(f"{order_item} --> {discount_amount} ---> {final_amount}")
        print("Total after discount: ",total_revenue_amount)
        continue

    # q option menu for exit loop
    elif(menu_option=="q"):
        print("Exit .........")
        break;
    # invalid menu option and re-show menu options
    else:
        print("Invalid option! Please try again.")
        continue