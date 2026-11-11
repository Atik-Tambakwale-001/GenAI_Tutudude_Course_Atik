# import math_utils.py file functionality from task 1
import math_utils
# import math_utils.py file specific square root functionality from task 2
from math_utils import square
# import math_utils.py file functionality from task 2
import string_utils

import shop_package.discount as disc
import shop_package.billing as bil
from shop_package.billing import calculate_total

# asked user input of two number for testing function which imported from math_utils.py file
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

# testing each functionality and print output task 1
print("Addition of the numbers:",math_utils.add(num1,num2))
print("Substraction of two number:",math_utils.substract(num1,num2))
print("Given First number square :",square(num1))

# testing each functionality and print result for Task 2
text_input= input("Enter word:")

print("Capitalize word is: ",string_utils.capitalize_words(text_input))
print("Reverse word is: ",string_utils.reverse_string(text_input))
print("Word count is :",string_utils.word_character_length(text_input))

price=100
prices = [100,200,300]
discount = 10

# calling all functions from shop package like billing,discount 
print(f"The {price} price after discount:",disc.apply_discount(price,discount))
print(f"the {price} price after 50 flat discount:",disc.flat_discount(1000))

total_amt = calculate_total(prices)
print(f"Total calculation:",total_amt)
print(f"Total bill and add 5% tax :",bil.apply_tax(total_amt))