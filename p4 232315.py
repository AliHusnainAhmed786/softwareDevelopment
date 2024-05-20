#activiy 1

print("start of activity 1")

def add_ing_or_ly(string): # defining funtion
    if len(string) < 3: #hek if string lenght is less than two words
        return string
    elif string.endswith('ing'): #hek if string already hae ing
        return string + 'ly'
    else: #if string doesn't hae ing at end then add ing
        return string + 'ing'


# Test funtion

while True:
    print("expeted result=",add_ing_or_ly(input("enter your letter= ")))
    user_input = input("Try again a1? (y for again/any other key for next activity): ")
    if user_input.lower() == 'y':

        continue
    else:
        break 
print("end of activity 1")

print("\n\nstart of ativity 2")
#Ativity 2
def count_z_in_string(string):
    count = 0
    for char in string:
        if char == 'z':
            count += 1
    return count

#test_method
while True:
    print("The number of 'z's in the string is=" ,count_z_in_string(input("enter your sentance=")))
    user_input = input("Try again a2? (y for again/any other key for next activity): ")
    if user_input.lower() == 'y':

        continue
    else:
        break 
print("end of activity 2")

print("\n\nstart of activity 3")
#Activity 3
import string #importing string to use string funtions

def count_character_types(input_string):#define method for ount character types in string
    lower_count = sum(1 for char in input_string if char.islower())
    upper_count = sum(1 for char in input_string if char.isupper())
    digit_count = sum(1 for char in input_string if char.isdigit())
    special_count = sum(1 for char in input_string if char in string.punctuation)

    return lower_count, upper_count, digit_count, special_count

#testing method
while True:
    input_string = input("Enter a string= ")#get input string from user
    lower, upper, digits, special = count_character_types(input_string)

    print(f"Lowercase letters: {lower}")
    print(f"Uppercase letters: {upper}")
    print(f"Digits: {digits}")
    print(f"Special symbols: {special}")
    user_input = input("Try again a3? (y for again/any other key for next activity): ")
    if user_input.lower() == 'y':

        continue
    else:
        break 
print("end of activity 3")

print("\n\nstart of activity 4")
#Activity 4
#defining function
def first_and_last_two_chars(input_string):
    if len(input_string) < 2:
        return ""
    else:
        return input_string[:2] + input_string[-2:]

# Test function
while True:
    print(f"expected String with first and last two chars=", first_and_last_two_chars(input("enter your string=")))
    user_input = input("Try again a4? (y for again/any other key for next activity): ")
    if user_input.lower() == 'y':
        continue
    else:
        break 
print("end of activity 4")