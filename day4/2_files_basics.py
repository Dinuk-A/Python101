#major function of working with python file handling is 'open()' ✅✅✅
#it gives a special file handler to work with opened file

file = open('file_handling_exs\\sample.txt','rt')
content1 = file.read()
print(content1)
file.close()                     #always close the file after using it for any task

# open() takes 2 params === file name(relative path if not in the same folder), and the opening mode ✅✅✅

# 4 main opening modes to handle files
# 1. 'r' === read, the default mode (if not mentioned in the open()), returns an error if file doesnt exist
# 2. 'w' === overwrite, create the file if desnt exist, returns the number of characters written
# 3. 'a' === append , add content at the end of the existing content, create file if doesnt exist
# 4. 'x' === create, create a specific file by given name, returns an error if already exists

# 2 main modes which way the file should be handle
# 1. 't' === as text, default mode
# 2. 'b' === as binary (images)

# read() for reading content ✅✅✅
#if the given file is not found, python will automatically create a new one

f = open('file_handling_exs\\sample.txt','rt')

# read all content
print('************reading all content************')
print(f.read())

#after above code, file pointer is at the end of the content
#since we need the same file to be read in multiple examples below,we need to reset the file pointer
f.seek(0)      

# read only first set of characters of a given amount
print('************reading first 8 characters************')
print(f.read(8))
f.seek(0)     

#only read the first line, call the same function multiple times to read more lines
print('************reading only line by line************')
print(f.readline())
print(f.readline())
f.seek(0)     

#looping through file
print("************')looping through file************')")
for x in f:
    print(x)
f.close()

# append ✅✅✅

# the new content will be appended to the end of last line, not in a new line
file2 = open('file_handling_exs\\myfile.txt','a')
file2.write('now file has new content, added by python')

#to add to a new line using '\n' or '\t'
file2.write('\nnow file has a new line, added by python')

file2.close()

# overwrite ✅✅✅
file2 = open('file_handling_exs\\myfile2.txt','w')
file2.write('previous content deleted, overwritten by python')


# create ✅✅✅
try:
    newFile = open('file_handling_exs\\newfile.txt','x')
except:
    #if the file already exist, this gives an error
    print('file is already existing')


# python 2_files_basics.py