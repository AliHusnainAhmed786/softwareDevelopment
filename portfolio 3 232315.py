print ("start of activity 1")
#EVEN NUMBER LIST UP TO 20
even_numbers = list(range(2, 21, 2))

# Display the first 3 elements
print("First 3 elements:")
for i in range(3):
    print(even_numbers[i])

# Display COMPLETE EVEN NUMBER LIST
print("All numbers in the list:")
for num in even_numbers:
    print(num, end=" ")

# Calculate and display the average of the even numbers
average = sum(even_numbers) / len(even_numbers)
print("\nAverage of the even numbers:", average)


print ("end of activity 1")



print ("\n\nstart of activity 2")

# given list of 5 numbers
numbers = [1, 2, 3, 4, 5]

# Print the first 3 elements using slice expression
print("First 3 elements:", numbers[:3])

# Change the elements in the list to be twice the previous value
for i in range(len(numbers)):
    numbers[i] *= 2

# Display the new list
print("List after multiplying each element by 2:", numbers)

# Display the minimum and maximum value in the list
print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))

print ("end of activity 2")



print ("\n\nstart of activity 3")

# Define the initial lists
summer = ['Dec', 'Jan', 'Feb']
autumn = ['Mar', 'Apr', 'May']
winter = ['Jun', 'Jul', 'Jul', 'Aug']
spring = ['Oct', 'Nov']

# Remove the excess month 'Jul' from the list winter
winter.remove('Jul')
# Add month 'Sep' at the beginning of the spring list
spring.insert(0, 'Sep')

# Create the MonthsISleep list containing all months from 'Feb' to 'Nov'
MonthsISleep = summer[2:] + autumn + winter + spring
# Create the MonthsIParty list containing the remaining 2 months
MonthsIParty = [summer[0],summer[1]]

# Display elements from both lists: MonthsISleep and MonthsIParty
print("Months I Sleep:", MonthsISleep)
print("Months I Party:", MonthsIParty)

# Display the elements of list summer in reverse order
print("Summer in reverse order:", summer[::-1])
print("end of activity 3")