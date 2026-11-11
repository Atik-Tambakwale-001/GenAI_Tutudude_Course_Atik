# create age check functionality with error message
def check_age(age):
    # condition for check age should be 1 to 120 number
    if(age<1 or age>120):
        print("Age must be between 1 and 120")
        return False
    return True

try:
    # asked user enter age number
    age = int(input("Enter your age:"))

    # calling check_age function with age
    # if it is return true it will print success message with age number  
    if(check_age(age)):
        print("entered age is:",age)

except TypeError:
    print("Entered age number is invalid")

except ValueError:
    print("Entered age number is not correct value")

finally:
    print("operation complete")