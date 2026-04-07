# Working With Files & Folders(Directories)

# Use Persistent Storage 

# syntax - 1
file = open("14_file_manage/file.txt","r")
print(file)
# NOTE: Here we need to "explicitly close" files after operations are performed
print(file.closed) # still open 
file.close() # explicitly close 
print(file.closed) # now closed

print("=" * 20)

# syntax - 2
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data) 
print(file_data.closed) # implicitly closed

# Reading Data From File - whole file
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())
    
# Reading Data From File - character wise 
with open("14_file_manage/file.txt","r") as file_data:
    for char in file_data.read():
        print(char)
        
# Reading Data From File - word wise 
with open("14_file_manage/file.txt","r") as file_data:
    for char in file_data.read().split():
        print(char)
        
# Reading Data From File - line wise 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readline())
    
# Reading Data From File - multiple line wise 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readlines())
    
# Reading Data From File - multiple line wise 
with open("14_file_manage/file.txt","r") as file_data:
    list_data = file_data.readlines()
    for line in list_data:
        print(line.strip())
        
# Write data To File - use write 'w' mode 
# Using Write We Can create file 
with open("14_file_manage/write.txt","w") as file_data:
    print(file_data)

# Write data To File    
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("Good Morning")
    
# Write data To File multiple lines   
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['Hello there\n', 'next line '])
    
# Append data 'a' mode
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("Good Morning \n")

# Append data 'a' mode
with open("14_file_manage/write.txt","a") as file_data:
    file_data.writelines(['Hello there\n', 'next line '])
    
# Create Folder / Directory
directory_name = "14_file_manage/students_data"
# os.mkdir(directory_name) # NameError: name 'os' is not defined. Did you forget to import 'os'?
import os
# os.mkdir(directory_name)

# Create Folder / Directory
directory_name = "14_file_manage/students_data"
# os.mkdir(directory_name) # NameError: name 'os' is not defined. Did you forget to import 'os'?
import os
if not os.path.exists(directory_name):
    os.mkdir(directory_name)

# Create file in students_data directory 
with open("14_file_manage/students_data/student.txt","w") as file_data:
    print(file_data)
    
# Delete File 
# os.remove("14_file_manage/student.txt")
if os.path.exists("14_file_manage/student.txt"):
    os.remove("14_file_manage/student.txt")

# Delete Folder - Empty 
# directory_name = "14_file_manage/empty_dir"
# directory_name = "14_file_manage/students_data" # OSError: [Errno 66] Directory not empty: '14_file_manage/students_data'

directory_name = "14_file_manage/empty_dir"
os.rmdir(directory_name)

# Delete Folder - NonEmpty 
import shutil
directory_name = "14_file_manage/students_data"
shutil.rmtree(directory_name)
