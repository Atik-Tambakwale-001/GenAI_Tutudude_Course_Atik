import os.path
# ask user for file name using input() method
file_name = input("Enter File name : ")

# check file exist or not using os.path.exist()
if(os.path.exists("GenAI-Task6-AtikTambakwale/"+file_name)):
    
    # after exist then read,print file content
    with open("GenAI-Task6-AtikTambakwale/"+file_name,"r") as f:
        file_content = f.read()
        print(file_content)
else:
    print("File not found. Please Check the filename")