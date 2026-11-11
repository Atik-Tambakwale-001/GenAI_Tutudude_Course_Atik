order_amount = int(input("Enter your order Amount:"))

if(isinstance(order_amount,int)):
    if(order_amount>=2000):
        final_amount=order_amount-(order_amount*0.15)
        print("After Discount 15%,The Final Amount : ",final_amount)
    elif(1500<=order_amount and order_amount<2000):
        final_amount=order_amount-(order_amount*0.10)
        print("After Discount 10%,The Final Amount : ",final_amount)
    elif(1000<=order_amount and order_amount<1500):
        final_amount=order_amount-(order_amount*0.07)
        print("After Discount 7%,The Final Amount : ",final_amount)
    else:
        final_amount = order_amount
        print("No Discount,The Final Amount : ",final_amount)
    print("added 5% Tax ,Total Amount : ",(final_amount+(final_amount*0.05)))
else:
    print("Your entered not valid integer value ,Kindly Enter Integer Number")
