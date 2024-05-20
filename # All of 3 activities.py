# All of 3 activities
#Activity 3
print("welcome to Sales tax Calculator")
"""input projected total sales amount"""
totalSale= float(input("enter you projected annual total sale"))
"""calculate profit from the given total sale amount (23% of total sale)"""
annualProfit= totalSale*0.23
"""display calculated profit"""
print(f'("your total annaul profict is"+ {annualProfit : .2f})')




#Activity 4
print("welcome to Oder Bill calculator")
salesTaxRate= 0.07 #as givven initialize and assign 7% rate
subtotal=0.00 # initialize and assign 0 subtotal so we can use it later
for i in range(1,6): #loop to getting items price and calculating subtotal
    price=float(input(f'enter price of your item no {[i]}= ')) #items price
    subtotal +=price #calculate subtotal

saleTax=subtotal * salesTaxRate #calculate sale Tax
total= saleTax*subtotal #calculate total

#display the bill including subtotal, saletax amount, total

print(f'{"the subtotal of your order is "}{subtotal : .2f}{"$"}')
print(f'{"the amount of sales tax (sale tax rate 7%) applied to your order is "}{saleTax : .2f}{"$"}')
print(f'{"the total amount of your order is "}{total : .2f}{"$"}')



#Activity 5
print("welcome to land calculator")
squreFeetPerAcer=43560 #initialize and assign per acres value 
totalSqureFeet=float(input("enter amount of total sure feet you have"))# get input of total aqure feet of tract
numberOfAcres= totalSqureFeet/squreFeetPerAcer # calculate number of aces provided by user

print(f'the provided land {totalSqureFeet}squre feet is = {numberOfAcres}Acers') #display number of acers calculated

