try:
    # ask user enter file name
    filename = input("Enter your filename:")
    # open file and read file and print first top three lines using while loop
    with open("GenAI-Task4-AtikTambakwale/"+filename,"r") as f:
        get_file_content=f.readlines()
        i=0
        while(i<3):
            print(get_file_content[i].strip())
            i+=1

# check file found or not
except FileNotFoundError:
    print("unable to find and open file")

# check file has a persmission issue or not
except PermissionError:
    print("file does not have read permission")
finally:
    print("File operation attempted")