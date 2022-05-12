import os

'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''

def detectBinod(item):
    with open(item,"r") as f:   # Opening the file in reading mode 
        cont = f.read()
        if "binod" in cont.lower(): # Checking the presence of Bind in the specified file by converting the content of the file in lowercase
                                    #                                      -----
                                    # Because Binod can be Binod --> BiNoD      |
                                    #                      Binod --> bInOD      |  Esistance of Binod in Different form   
                                    #                      Binod --> BINOD      | 
                                    #                      Binod --> binod      |
                                    #                                      -----
            return True
        else:
            return False
        
NO_OF_FILE_WITH_BINOD = 0
if __name__ == "__main__":
    myContent = os.listdir()  # Listing the all the content of the directory
    for item in myContent:
        if item.endswith(".txt"):  # Searching Binod in files which endswith(.txt) only 
            print(f"\nSearching Binod in {item}")
            
            flag = detectBinod(item)
            
            if (flag):
                print(f"******* Binod Detected in {item} *******")
                NO_OF_FILE_WITH_BINOD +=1
                flag+=1     
                
            else:
                print(f"!!!! Binod Not Found in {item} !!!!")
             
    
    print("\n##### Binod Detector Summary #####")   
    
    if flag>1:  # If file is more than 1 then printing plural of the file(files)
        print(f"{NO_OF_FILE_WITH_BINOD} files with Binod Hidden in them")
        
    elif flag==1:   # If file is equal to 1 the printing singular of file(file)
        print(f"{NO_OF_FILE_WITH_BINOD} file with Binod Hidden in them")
    else:     # Other wise printing [No file found Binod hidden in them ]
        
        print("NO SUCH FILE: No such file find with Binod")
        
