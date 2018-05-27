#!/usr/bin/env python3.5
F=open("../files/os_list.txt", 'r')   # Open a file in read mode
F_read=F.read()
print("Output :\n", F_read)
F.close()  ## Close the file after reading
############################################################


F2 = open("../files/newfile", "w")  
'''
# 'w' creates new file or if existing file opened with 'w' it truncates it content (makes blablank)
'''
F = open("../files/os_list.txt", 'r') ## Open os_list.txt in 'r' mode in order to copy its content to newfile
F.seek(0)   ## Move the cursor to begining of the file to read file from beginging

F2.write(F.read())  # copy content of os_list.txt to newfile
F2.close()          # Close file after writing since file was opened in only write mode so it is not readable
F2 = open("../files/newfile", "r")
F2.seek(0)                 # Move cursor to begining 
F2_read = F2.read()
print("Content of newfile:\n", F2_read)
F2.close()
F.close()

####################################################

with open("../files/os_list.txt", 'a') as F3:
    F3.write("Windows2003\n")
'''
with open() closes file after completing operations and assigns to variable
useful in case of if you forget to close file
'''
F3 = open("../files/os_list.txt", "r")
F3.seek(0)
print(F3.read())
F3.close()

