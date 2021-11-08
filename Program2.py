# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25
# Display the output in the following format.
# The total amount is _____.

#Greetings!
print("\nHi, good day! Would you like to buy some apples and oranges?")

def get_Questions():
    appleQuestion = int(input("\nHow many apples do you want to buy?: "))
    orangeQuestion = int(input("\nHow many oranges do you want to buy?: "))
    return appleQuestion , orangeQuestion

def get_Prices():
    applePrice = 20
    orangePrice = 25
    return applePrice , orangePrice

def get_GrandTotal():
    totalApples = appleQuestion * applePrice 
    totalOranges = orangeQuestion * orangePrice 
    totalPrice = totalApples + totalOranges
    return totalApples, totalOranges, totalPrice

def display(totalPrice):
    print(f"\nThe total amount is {totalPrice:,.0f} PHP.\n")

# Steps
# 1. Ask for the quantity of the apple and oranges to be purchase.
appleQuestion , orangeQuestion = get_Questions()
# 2. Define the price of an apple and orange.
applePrice , orangePrice =  get_Prices()
# 3. Compute for the total price of apples and oranges to be purchase.
totalApples, totalOranges, totalPrice = get_GrandTotal()
# 4. Display
display(totalPrice)