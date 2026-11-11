# define try except finally block
try:
    prices = [120,350,'abc',500,-200,800]
    # iterated give prices list
    total_amt=0
    for price in prices:

        # check price is not integer and float number or not
        if(not isinstance(price,(int,float))):
            print("Given price is not a number :",price)
        
        # check price is not negative number within prices list
        elif(price<0):
            print("negative price number not allowed :",price)

        # adding positive integer or float number into calculated total amount variable
        # print running total amount
        else:
            total_amt+=price
            print("running total price:",total_amt)
# capture type error exception during execution
except TypeError:
    print("error:Value is not a number")

# capture value error exception during execution
except ValueError:
    print("error:Negative price not allowed")

# print completion message
finally:
    print("operation complete")