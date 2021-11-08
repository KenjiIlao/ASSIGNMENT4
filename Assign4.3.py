def getUserInput(): 
    money_leftFunc = int(input("How much money i have "))
    price_appleFunc = int(input("How much is an apple: "))
    amount = money_leftFunc // price_appleFunc
    money = money_leftFunc % price_appleFunc
    return money_leftFunc, price_appleFunc, amount, money

def displayOutpt (amount, money):
    print (f"You can buy {amount} apples and your change is {money}")

# Steps
# 1. ask the money_leftFunc, price_appleFunc, amount, money
money_leftFunc, price_appleFunc, amount, money = getUserInput()
#2.Display the amount and money
displayOutpt (amount,money)