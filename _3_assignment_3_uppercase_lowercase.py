# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.



# ﻿Sample String : 'The quick Brow Fox'

# Expected Output :

# No. of Upper case characters : 3

# No. of Lower case Characters : 12

def string_test(s):
    d={"upper_case":0, "lower_case":0}
    for i in s:
        if i.isupper():
           d["upper_case"]+=1
        elif i.islower():
           d["lower_case"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["upper_case"])
    print ("No. of Lower case Characters : ", d["lower_case"])

string_test('The quick Brow Fox')