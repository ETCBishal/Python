'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''




import os

  
def move(folderName, files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")
      
def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files = os.listdir()
files.remove("Wrapper.py")

# Create the file if not exist otherwise it wiil execute other lines
CreateIfNotExist("Images") 
CreateIfNotExist("Audios")
CreateIfNotExist("Others")
###################################################################

ImgEXT = [".jpg",".png",".jpeg",".gif"]
AudioEXT = [".wav",".mp3",".dsd",".flac"]
images = [file for file in files if os.path.splitext(file)[1].lower() in ImgEXT]
audios = [file for file in files if os.path.splitext(file)[1].lower() in AudioEXT]

Others = [".txt", ".py"]   # You can put any type of extention here or just leve it empty
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in ImgEXT) and (ext not in AudioEXT) and os.path.isfile(file):
        Others.append(file)
others = [file for file in files if os.path.splitext(file)[1].lower() in Others]
move("Images",images)
move("Audios",audios)
move("Others",others)

