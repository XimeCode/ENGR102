# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB Topic 7
# Date: 28/10/2025
#


name = (input("What is your name? "))

#convert name to list for to check character by character
letters = list(name)

first_vowel = len(letters) 
for i in range(len(letters)):
    if letters[i] in "AEIOUaeiou": #Store index of first vowel
        first_vowel = i 
        break

#handles constantant starting names 
if len(letters) > 1 and letters[0] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
    remaining_letters = letters[first_vowel:] #slices word and uses everything from first vowel onward for rhyming

    first_rhyme = "Bo-B" + "".join(remaining_letters)
    print(f"{name}, {name}, {first_rhyme}")

    second_rhyme  = "Fo-F" + "".join(remaining_letters)
    print(f"Banana-Fana {second_rhyme}")

    third_rhyme= "Mo-M" + "".join(remaining_letters)
    print(f"Me Mi {third_rhyme}")
    print(f"{name}!")

#handles names with first indexes as vowels
elif letters[0] in "AEIOUaeiou": 
    letters[0] = letters[0].lower() 
    first_rhyme = "Bo-B" + "".join(letters)
    print(f"{name}, {name}, {first_rhyme}")

    second_rhyme = "Fo-F" + "".join(letters)
    print(f"Banana-Fana {second_rhyme}")

    third_rhyme = "Mo-M" + "".join(letters)
    print(f"Me Mi {third_rhyme}")
    print(f"{name}!")

    




