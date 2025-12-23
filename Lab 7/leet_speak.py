# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB Topic 8
# Date: 20/11/2025
#

#take a string of text
text = input("Enter some text: ")

# create a dictionary
leet_speak = {"a": "4", "e": "3", "o": "0", "s": "5", "t": "7"}

listed_text = list(text)

#check for key in word and receive the index 
for index, char in enumerate(listed_text): 
     #convert to lowercase for dictionary use
    if char.lower() in leet_speak:
        conversion = leet_speak[char.lower()]
        listed_text[index] = conversion

#join string after converting
new_text = "".join(listed_text)

print(f'In leet speak, "{text}" is: \n{new_text}')





    





