# define cart list variable
cart_list = []

# while for asking user enter a prices
while True:
    value = input("Enter price:")
    # check value is equal to "q" then break loop exited it
    if (value.lower()=="q"):
        print("Exit.......")
        break
    try:
        # convert string value into float type datatype
        price=float(value)

        # check given price is not negative number
        if(price<0):
            print("Negative price not allowed")

        # appending new price into cart list
        cart_list.append(int(price))

    # check value type error and create custom exception error message
    except ValueError as e:
        msg=str(e)
        if("Negative" in msg):
            print("Error:",msg)
        else:
            print("Invalid input,please enter a number")

# print total item count value and total item price value
print("Total Item:",len(cart_list))
print("Total Bill:",sum(cart_list))