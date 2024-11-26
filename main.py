import os
import datetime
#art
copy =  open("./art/divider","r")
divider = copy.read()
copy =  open("./art/workout","r")
workout = copy.read()
copy =  open("./art/main","r")
menu = copy.read()


# date
with open("./logs/lastOpened","r") as lastopened:
    old = lastopened.read()
    
now = datetime.date.today()
with open("./logs/lastOpened", "w") as f:
    f.write(str(now))
os.system('clear')
menuInfo = (f"Last opened : {old}         by Ali Alasfour")
#printing menu

print(workout,"\n",divider,"\n",menuInfo,"\n",divider)
print(menu)
