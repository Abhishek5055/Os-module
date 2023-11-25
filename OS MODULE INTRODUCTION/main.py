import os

if(not os.path.exists("data")):
    os.mkdir("data")        #data name directory created
for i in range(0,3):
    os.mkdir(f"data/Day{i+1}")      #here it creates a file starting from 1 to 3