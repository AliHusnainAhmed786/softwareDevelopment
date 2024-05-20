#Activity 2 
#Ticket price checker
#user input age
age = int(input("Enter your age: "))

#chek age is less than 18 or less than 5 or greater than 18
if age < 18:
    if age < 5:
        print("enjoy Free for Babies.")
    else:
        print("you have to pay half ticket price (Ticket price is half for minors)")
else:
    print("you have to pay Full ticket price.")
