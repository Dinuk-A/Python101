#we can also open a file using 'with' keyword , in that way we dont have to manually close the file ✅

with open('file_handling_exs\\sample.txt','rt') as f:
    print(f.read())
    
# for more actions > import os module 
import os

#check existence before any action ✅✅
#rename a file ✅
if os.path.exists('file_handling_exs\\newfile2.txt'):
    os.rename('file_handling_exs\\newfile2.txt' , 'file_handling_exs\\renamedfile.txt')    
else:
        print('file does not exist')

# delete a file ✅
if os.path.exists('file_handling_exs\\newfile.txt'):
    os.remove('file_handling_exs\\newfile.txt')
else:
    print('file does not exist')
    
#delete a folder, we can only delete empty folders ✅
if os.path.exists('file_handling_exs\\folderToDelete'):
    os.rmdir('file_handling_exs\\folderToDelete')
else:
    print('folder does not exist')

# python 3_files_adv.py