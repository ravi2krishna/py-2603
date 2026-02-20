# Working With CSV Files 

import csv

# Read Data From CSV File 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)
        
print("=" * 50)       

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[-1] == "Hyderabad":
            print(row)

print("=" * 50)       

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs  
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[1].endswith("@tcs.com"):
            print(row)

print("=" * 50)  

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs  
with open("14_file_manage/students.csv","r") as file_data:
    
    
    csv_reader = csv.reader(file_data)
    headers = next(csv_reader)
    # The 'headers' variable now contains the first row as a list
    print(f"Headers: {headers}")
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[1].endswith("@tcs.com"):
            print(row)

print("=" * 50) 

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[-1] == "Hyderabad":
            print(row)

print("=" * 50)

# Using DictionaryReader 
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        print(row)
    
print("=" * 50)

# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row['address'] == "Hyderabad":
            print(row)
    
print("=" * 50)

# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row['address'] == "Hyderabad":
            print(row)
    
print("=" * 50)

# Writing Data 

with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerows([['Ravi', 'ravi186@tcs.com', '9876055200', 'Bangalore'],
['Ramu', 'ramu661@tcs.com', '9833214959', 'Bangalore'],
['Deepak', 'deepak641@tcs.com', '9369382025', 'Chennai']])
    
with open("14_file_manage/emp.csv","a") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerows([['Balu', 'balu89@tcs.com', '9920062079', 'Chennai'],
['Naveen', 'naveen244@tcs.com', '9756439364', 'Kolkata'],
['Naresh', 'naresh190@tcs.com', '9942925292', 'Mumbai'],
['Balu', 'balu275@tcs.com', '9168624926', 'Mumbai'],
['Hari', 'hari478@tcs.com', '9564137451', 'Jaipur']])

# DictWriter
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/demo.csv","w") as file_data:
    csv_writer = csv.DictWriter(file_data,fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'Santosh', 'email': 'santosh579@outlook.com', 'mobile': '9718726887', 'address': 'Hyderabad'})
    csv_writer.writerows([{'name': 'Suresh', 'email': 'suresh602@gmail.com', 'mobile': '9578381099', 'address': 'Hyderabad'},
{'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'},
{'name': 'Santosh', 'email': 'santosh579@outlook.com', 'mobile': '9718726887', 'address': 'Hyderabad'}])