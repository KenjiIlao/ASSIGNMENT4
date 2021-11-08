
def getUserInput():
    name_ = input("Name: ")
    age_ = int(input("Age: "))
    add_ = input("Address:")
    return name_, age_, add_

def display(name_, age_, add_):
    print(f"Hi, My name is {name_} I am {age_} years old and I live in {add_}.")


#steps
#1. ask my name, age and address
name, age, add = getUserInput()
#2. display my name, age and address
display(name, age, add) 