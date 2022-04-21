#3. Create a regular expression that matches a street address
#consisting of a number with one or more digits followed
#by three words of one or more characters each.
#You must have an input prompt that I can enter an address in your program.

#Your street address should be separated by one space each.

#ex. 123 North Main Street.

#Based on what address was entered, the answer in the Shell says either

#Match or No Match

#If your address didn't produce the correct or no answer at all, you will
#not receive the full points for this problem.


import re

pattern = "[0-9]+\s[A-Za-z]+\s[A-Za-z]+\s[A-Za-z]+"

street = "12345 Tree Branch Street"

yourAddress = (input('Enter An Address: '))

print(re.findall(pattern, street))


def addressCheck():
    if yourAddress == street:
    
            print("Match")
    else:
            print("No Match")


addressCheck()



