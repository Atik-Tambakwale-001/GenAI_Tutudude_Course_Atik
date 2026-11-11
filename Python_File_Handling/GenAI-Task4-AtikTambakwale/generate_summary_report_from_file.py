with open("GenAI-Task4-AtikTambakwale/sales_data.txt","r") as f:
    # read all sales values from sales_data.txt
    get_sale_amounts = f.readlines()

    # convert string sales amount into integer
    sale_amounts_list = []
    for sale_amt in get_sale_amounts:
         sale_amounts_list.append(int(sale_amt.strip()))

    # print all calculation from sales_data.txt
    print("The Original data :")
    print(sale_amounts_list)
    print("Total Sale : ",sum(sale_amounts_list))
    print("Highest Sale : ",max(sale_amounts_list))
    print("Lowest Sale : ",min(sale_amounts_list))
    print("Average Sale : ",(sum(sale_amounts_list)/len(sale_amounts_list)))
    