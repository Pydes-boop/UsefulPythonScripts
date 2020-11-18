# Python code to rename multiple  
# files in a directory or folder 
# specifically: renaming Folders to add Spaces between Upercase Letters
  
# importing os module 
import os
import re
path = '/Users/Dani/Documents/PythonTest'
files = os.listdir(path)
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir(path)): 
        src = path + '/' + filename
        dst = path + '/' + re.sub(r"(\w)([A-Z])", r"\1 \2", filename)
          
        # rename() function will 
        # rename all the files 
        print('renaming: ' + src + ' to ' + dst)
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 