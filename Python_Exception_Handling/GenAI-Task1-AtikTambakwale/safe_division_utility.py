
try:
    # create two input value like numerator and denominator number
    numerator = float(input("Enter Numerator:"))
    denominator = float(input("Enter Denominator:"))
    result = numerator/denominator

# check given input value is validation number or not
except ValueError:
    print("please check,given is invalidated input value")

# check denominator number is zero or not
except ZeroDivisionError:
    print("given denominator number is zero")

# if error not occur then it result will be print
else:
    print("the result :",result)
    
# print operation completed message it will print anyway come error or not
finally:
    print("operation Complete")