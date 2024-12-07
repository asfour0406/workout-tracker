import os

def createTemplate(tempName):
    foldercontents = os.listdir("templates")
    for temp in foldercontents:
        if temp == tempName:
            print(f"already a template named:{tempName}")
        else:
            f = open(f"./template/{tempName}","w")
            
print(createTemplate("upper"))