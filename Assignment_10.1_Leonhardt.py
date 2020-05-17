#Cord Leonhardt
#Assignment 10.1
#May 16,2020

#import os library
import os

#create varible for user to choose the directory name
directory = input("Please enter an existing directory that you would like to save the file: ")

#validate the directory is valid before asking for additional information from user
#if directory is invalid, exit program

while True:
  
    if os.path.isdir(directory):
        break
    else: 
        print("This is not a valid directory")
        exit()
    
#prompt user for additional input 
filename = input("Please enter the filename you would like to save as: ")
user_name = input("Please enter your name : ")
user_address = input("Please enter your address : ")
user_phone_number = input("Please enter your phone number : ")


#write to the user defined file by calling open()

with open(filename, 'w') as file_object:
    #insert user defined data comma separated
    file_object.write(user_name+','+user_address+','+user_phone_number+'\n')

#close file after writing is completed
file_object.close()

#Display the file contents to the user for validation purposes
print("")
print("Your file contains the following, please validate:")

#open user defined filename, read, then print results
with open(filename) as file_object:
    contents = file_object.read()
print(contents)
    
