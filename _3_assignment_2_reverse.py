# Write a Python program to reverse a string.



# ﻿Sample String : "1234abcd"

# Expected Output : "dcba4321"


def reverse(string):
    string = string[::-1]
    return string

string = input("Enter the Strings to be reversed: ")
print("The original string is: ",string)
print("The reversed string using extended slice operator is: ",reverse(string))