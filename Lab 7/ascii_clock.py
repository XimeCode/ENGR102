#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ximena Yepez
# Melanie Barrientos
# Sophia Treviño
# 
# Section: Section 548
# Assignment: LAB: Topic 8 (team)
# Date: 20/11/25
#

#read user input, clock type, and preffered_character
while True:
    user_input = input("Enter the time: ")
    parts = user_input.split(":")
    
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        print("Invalid! Try again.")
        continue

    hour = int(parts[0])
    minute = int(parts[1])
    
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        print("Invalid! Try again.")
        continue

    break  # valid time entered, exit loop

clock_type = input("Choose the clock type (12 or 24): ")

chars_permitted = "abcdeghkmnopqrsuvwxyz@$&*="

original_input = user_input

#if no character entered, use the digits themselves
while True:
    char = input("Enter your preferred character: ")
    if char == "":  # default to digits themselves
        digits_as_chars = True
        break
    elif char in chars_permitted:
        digits_as_chars = False
        break
    else:
        print("Character not permitted! Try again: ")

original_hour = hour
original_minute = minute

#convert military time to standard if clock type = 12
if clock_type == "12":
    parts = user_input.split(":")
    hour = int(parts[0])
    minute = parts[1]

    if hour == 0:
        converted_hour = 12
    elif hour > 12:
         converted_hour = hour - 12
    else:
         converted_hour = hour 

    user_input = f"{converted_hour}:{int(minute):02d}"

#define digit, colon, and AM/PM patterns using dictionary
digit_patterns = {
    '0': [
        '***',
        '* *',
        '* *',
        '* *',
        '***'
    ],
    '1': [
        ' * ',
        '** ',
        ' * ',
        ' * ',
        '***'
    ],
    '2': [
        '***',
        '  *',
        '***',
        '*  ',
        '***'
    ],
    '3': [
        '***',
        '  *',
        '***',
        '  *',
        '***'
    ],
    '4': [
        '* *',
        '* *',
        '***',
        '  *',
        '  *'
    ],
    '5': [
        '***',
        '*  ',
        '***',
        '  *',
        '***'
    ],
    '6': [
        '***',
        '*  ',
        '***',
        '* *',
        '***'
    ],
    '7': [
        '***',
        '  *',
        '  *',
        '  *',
        '  *'
    ],
    '8': [
        '***',
        '* *',
        '***',
        '* *',
        '***'
    ],
    '9': [
        '***',
        '* *',
        '***',
        '  *',
        '***'
    ],
    ':': [
        ' ',
        ':',
        ' ',
        ':',
        ' '
    ],
    'A': [
    ' A ',
    'A A',
    'AAA',
    'A A',
    'A A'
    ],
    'M': [
        'M   M',
        'MM MM',
        'M M M',
        'M   M',
        'M   M'
    ],
    'P': [
        'PPP',
        'P P',
        'PPP',
        'P  ',
        'P  '
    ]

}

#initialize lines for numbers, colon, and if applicable AM/PM
line_1 = []
line_2 = []
line_3 = []
line_4 = []
line_5 = []


#call patterns for characters
for i in user_input:
    current_char = i if digits_as_chars else char
    if i in digit_patterns:
        pattern = digit_patterns[i]
        line_1.append(pattern[0].replace('*', current_char))
        line_2.append(pattern[1].replace('*', current_char))
        line_3.append(pattern[2].replace('*', current_char))
        line_4.append(pattern[3].replace('*', current_char))
        line_5.append(pattern[4].replace('*', current_char))

#AM/PM display logic
if clock_type == "12":
    original_hour = int(original_input.split(":")[0])
    suffix = "AM" if original_hour < 12 else "PM"
    for letter in suffix:
        pattern = digit_patterns[letter]
        line_1.append(pattern[0])
        line_2.append(pattern[1])
        line_3.append(pattern[2])
        line_4.append(pattern[3])
        line_5.append(pattern[4])


print(' '.join(line_1))
print(' '.join(line_2))
print(' '.join(line_3))
print(' '.join(line_4))
print(' '.join(line_5))