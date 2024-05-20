#Activity1
print("*******************this will contain all actiities of portfolio 5******************* \n**********************       lets start       *****************")
print("start of activity1")
#import math for pi value
import math
#class creation
class Circle:
    def __init__(self, radius):
        self.radius = radius
    #defining compute area method
    def compute_area(self):
        return math.pi * self.radius ** 2
    #defining compute primeter method
    def compute_perimeter(self):
        return 2 * math.pi * self.radius

while True:
# test class and methods:
    circle = Circle(float(input("enter radius=")))
    print(f"Area= {circle.compute_area()}")
    print(f"Perimeter= {circle.compute_perimeter()}")
    s=input("if you want to try again activity1 press y else press any other key to move to next activity= ")
    if(s=='y'):
        
        continue
    else:
        break
print("end of activity 1")

print("\n\n start of activity 2")
#class creation
class IntegerToRoman:
    def __init__(self, num):
        self.num = num
#method definition for conversion
    def convert_to_roman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while self.num > 0:
            for _ in range(self.num // val[i]):
                roman_num += syms[i]
                self.num -= val[i]
            i += 1
        return roman_num

# testing class and method:
while True:
    test = IntegerToRoman(int(input("enter your number to convert to Roman Numeral =")))
    print(f"Integer: {test.num} => Roman Numeral: {test.convert_to_roman()}")
    s=input("if you want to try again activity2 press y else press any other key to move to next activity= ")
    if(s=='y'):
        
        continue
    else:
        break
print("end of activity 2")

print("\n\nstart of acivity 3")
#class creation,  list objet creation and class methods creation
class ListManager:
    def __init__(self):
        self.my_list = []

    def add_element(self, element):
        self.my_list.append(element)
        print("Element added successfully.")


    def display_list(self):
        if not self.my_list:
            print("List is empty.")
        else:
            print("Elements in the list:")
            for element in self.my_list:
                print("*",element)

    def remove_element(self, element):
            if element in self.my_list:
                self.my_list.remove(element)
                print("Element removed successfully.")
                self.display_list()
            else:
                print("Element not found in the list.")



# Function to take user input and perform operations
def main():
    list_manager = ListManager()

    while True:
        print("\nUpdated list",list_manager.my_list)
        print("Menu:")
        print("1. Add Element")
        print("2. Remove Element")
        print("3. Display List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            element = input("Enter element to add: ")
            list_manager.add_element(element)
        elif choice == '2':
            if list_manager.my_list:

                while True:
                    list_manager.display_list()
                    element = input("Enter element to remove: ")
                    list_manager.remove_element(element)
                    
                    if list_manager.my_list:
                        a=input("if want to remove something else press y or else press any key for main menu= ")
                        if a=='y':
                           continue
                        else:
                           break
                    else:
                           break
            else:
                print("list is already empty nothing to remove")   
        elif choice == '3':
            list_manager.display_list()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    print("Final List:")
    list_manager.display_list()
#test class and its methods
while True:
    main()
    m= input("enter y to try again activity 3 else press any key to exit= ")
    if m=='y':
        continue
    else:
        break


print("end of activity 3")
print("thanks for running my program")