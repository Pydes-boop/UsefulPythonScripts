# Python code to rename multiple  
# files in a directory or folder 
# specifically: renaming Folders to add Spaces between Upercase Letters
  
# importing os module 
import os
import re

# Hardcoded this Path because it probably doesnt exist on your System so you dont fuck shit up by executing it
path = 'C:/Users/Dani/Documents/Blender/Textures'
files = os.listdir(path)
  
# Main Function
def main():
    addUnderscores()


# Function to add Underscores
def addUnderscores(): 
  
    for count, filename in enumerate(os.listdir(path)): 
        src = path + '/' + filename
        dst = path + '/' + re.sub(r"(\w)([A-Z])", r"\1_\2", filename)
        #dst2 --> removing double Underscores
        dst2 = re.sub('_+', '_', dst)

        #call renameColor Function with our Folder before we rename the Folder
        renameColor(src)

        #remanes and adds Underscores between Upercase Letters
        os.rename(src, dst) 

        #remove double Underscores
        os.rename(dst, dst2)
        

# Function for renaming .._basecolor.jpg to .._color.jpg
def renameColor(colorPath):
    for count, filename in enumerate(os.listdir(colorPath)):
        src = colorPath + '/' + filename
        dst = colorPath + '/' + re.sub('basecolor', 'color', filename)

        os.rename(src, dst)

  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling function s
    main()