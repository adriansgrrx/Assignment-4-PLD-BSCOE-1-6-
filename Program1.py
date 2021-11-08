# Create a program that will ask for name, age and address
# Display those details in the following format
# Hi my name is _____ . I am ______ years old and I live in _______.

#
print("\nPlease state some of your personal information.")

def get_NameAgeAddresss():
    _name = input("\nEnter your name: ")
    _age = int(input("\nEnter your age: "))
    _address = input("\nEnter your address: ")
    return _name, _age, _address

def display (name, age, address):
    print(f"\nHi my name is {name}. I am {age} years old and I live in {address}.\n")

# Steps
# 1. Ask for name, age and address
name, age, address = get_NameAgeAddresss()
# 2. Display
display (name, age, address)