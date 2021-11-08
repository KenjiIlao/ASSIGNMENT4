print("the price of apple is 20")
apple = 20
print("the price of orange is 25")
orange = 25

def getUserInput():
    apples = int(input("the total of apples that i want to buy: "))
    oranges = int(input("the total of oranges that i want to buy: "))
    amount = apples * apple + orange * oranges
    return apples, oranges, amount

def displayOutpt (amount):
    print (f"the total amount is {amount}")

# Steps
# 1. ask the apples,oranges and the amount
apples, oranges, amount =getUserInput()
#2. display the amount
displayOutpt (amount)