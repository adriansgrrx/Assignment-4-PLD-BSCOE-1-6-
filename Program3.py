#Create a program that which you will enter the amount of money you have.
#It will also ask for the price of an apple.
#Display tha maximum number of apples that you can buy and the remaining money that you will have
#You can buy  ______ apples and your change is ______ pesos.

#Greetings!
print("\nHi, good day! Would you like to buy some apples?")

def get_Questions():
    yourMoney = int(input("\nEnter the amount of money you have.\nPHP: ")) 
    applepPrice = int(input("\nHow much for an apple?\nPHP: "))
    return yourMoney , applepPrice

def get_Computation():
    maxApples = yourMoney // applePrice
    yourChange = yourMoney - maxApples * applePrice
    return maxApples , yourChange

def display(maxApples , yourChange):
    print(f"\nYou can buy {maxApples} apple(s) and your change is {yourChange} pesos.\n")

# Steps
# 1. Ask for the amount of money available and the price of an apple.
yourMoney , applePrice = get_Questions()
# 2. Compute for the maximum number of apple available for purchase and for the remaining money.
maxApples , yourChange = get_Computation()
# 3. Display.
display(maxApples , yourChange)