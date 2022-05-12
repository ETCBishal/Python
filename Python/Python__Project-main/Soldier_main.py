'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''



import os

def soldier(path,file,format): # Format of your file can be any...
    os.chdir(path)
    i = 1
    
    files = os.listdir(path)
    # print(files)
    with open(file) as f:
        filelist = f.read().split("\n")
    
    for file  in files:
        if file not in filelist:
            os.rename(file, file.capitalize())
        
        if os.path.splitext(file)[1] == format:
                os.rename(file, f"{i}{format}")
                i+=1
            
            
               
soldier("c:path",
        "c:path of your python file", ".txt")
