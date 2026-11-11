
order_amount_list = [1200,2500,800,1750,3000]
total_revenue_amount = 0;
for order_amount in order_amount_list:
    if(isinstance(order_amount,int)):
        if(order_amount>=2000):
            final_amount=order_amount-(order_amount*0.15)
            discount_amount = "15%"
        elif(1500<=order_amount and order_amount<2000):
            final_amount=order_amount-(order_amount*0.10)
            discount_amount = "10%"
        elif(1000<=order_amount and order_amount<1500):
            final_amount=order_amount-(order_amount*0.07)
            discount_amount = "7%"
        else:
            final_amount = order_amount
            discount_amount = "0%"
        total_revenue_amount+=final_amount
        print(f"{order_amount} --> {discount_amount} ---> {final_amount}")
    else:
        print("Your entered not valid integer value ,Kindly Enter Integer Number")
print("The Total Revenue Amount After Discounts :",total_revenue_amount)