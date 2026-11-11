with open("GenAI-Task2-AtikTambakwale/sales_data.txt", "r") as f:
    read_file_content = f.read()
    print("The file content using read():")
    print(read_file_content + "\n")

    # Reset file pointer to the beginning of the file
    f.seek(0)
    readline_file_content = f.readline()
    print("The file content using readline():")
    print(readline_file_content + "\n")

    # Reset file pointer again before reading all lines into a list
    f.seek(0)
    readlines_file_content = f.readlines()
    print("The file content using readlines():")
    # define new list and each sale amounts string to integer using for loop
    # append() for adding after convert string to integer
    # remove new line string using strip() 
    file_content_list = []
    for sale_amount in readlines_file_content:
        file_content_list.append(int(sale_amount.strip()))
    print(file_content_list)
