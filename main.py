# import 
import os
from datetime import *
import function


# setting time
now = str(date.today())
#art
copy =  open("./art/divider","r")
divider = copy.read()
copy =  open("./art/workout","r")
workout = copy.read()
copy =  open("./art/main","r")
menu = copy.read()
#menu
def printmenu():
    #printing menu
    os.system('clear')
    print(workout,"\n",divider,"\n",menuInfo,"\n",divider)
    print(menu)

# date
with open("./logs/lastOpened","r") as lastopened:
    old = lastopened.read()

# defining menu info
os.system('clear')
menuInfo = (f"Last opened : {old}         by Ali Alasfour")


#writing now to last opened
with open("./logs/lastOpened", "w") as f:
    f.write(str(now))


# def main():
# print(now)
while(True):
    printmenu()
    choice = int(input())

