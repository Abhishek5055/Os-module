import os
folders = os.listdir("data")

print(folders)

for folder in folders:
    print(folder)       #it will print all tutorial folder
    print(os.listdir(f"data/{folder}")) #it will print tutorial folder file