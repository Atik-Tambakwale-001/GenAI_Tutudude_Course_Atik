prices = {
    "Mouse":500,
    "Keyboard":800,
    "Monitor":7000,
    "Pendrive":400,
    "Camera":5000
}

# ask percentage value from user using input method
input_percentage = int(input("Enter discount percentage number: "))

# write discount price into discount_report.txt file
item_count=0;average_discounted_price=0
with open("GenAI-Task7-AtikTambakwale/discount_report.txt","w") as f:
    for product in prices:
        actual_price = prices[product]
        discounted_price = int(actual_price*(input_percentage/100))
        f.write(product+"|"+str(actual_price)+"|"+str(discounted_price)+"\n")
        average_discounted_price+=discounted_price
        item_count+=1

# read discount_report.txt file and print it
with open("GenAI-Task7-AtikTambakwale/discount_report.txt","r") as f1:
    get_product_prices=f1.read()
    print(get_product_prices)

print("Total Item : ",item_count)
print("Average Discounted Price : ",int(average_discounted_price/item_count))