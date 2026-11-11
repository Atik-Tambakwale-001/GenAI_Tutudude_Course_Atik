# create function for calculated factorial number with n number parameter
def factorial(n):
    # check zero number and return error message it
    if(n==0):
        return "zero can't be calculated factorial number"
    
    # check 1 number value and return same return 1 number
    elif(n==1):
        return 1;

    # check negative number and return error message
    elif(n<0):
        return "negative number can't be calculated factorial number"

    # check given number more than 1 numbe value for calculate factorial number
    elif(n>1):
       return n*factorial(n-1)

# calling factorial function with 5 number integer argument
print(factorial(5))

# calling factorial function with zero number integer argument
print(factorial(0))

# calling factorial function with negative number integer argument
print(factorial(-3))