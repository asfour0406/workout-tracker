import os
from datetime import *
now = str(date.today())
def selectfunc(choice):
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            exit()


# this needs fixed
def createTemplate(tempName):
    foldercontents = os.listdir("templates")
    for temp in foldercontents:
        if temp == tempName:
            print(f"already a template named:{tempName}")
        else:
            f = open(f"./template/{tempName}","w")
def trackweight(current):
#    find last line in the file.
    with open("logs/weight","r") as f:
        for line in f:
            pass  # Iterate through the file until the last line
        word = ""
        for x in line:
         var = 0
         if x[0] !="/":
             word = word+x[0]
             var+=1
         else:
             break
    last = (word) 
     # check if weight was already tracked for the day
    if last == now:
        print("You already tracked your weight today!")
    else:
    # writing the time and weight
        with open("logs/weight", "a") as f:
            f.write(f"{now}/{str(current)}\n")  # Append timestamp with newline
trackweight(133)
