def rental_car() -> str:
    """
    this function prompts the user for input on the type of car they 
    want to rent

    :return: message informing the user that the rental car they want will be checked for
    rtype: str
    """
    car_type = input("what type of rental car would you like? ")
    return car_type

car = rental_car()
print(f"let me see if I can find you a {car}")

def dinner_group() -> str:
    """
    this code uses input from the user to decide if there is a table available
    for them or if they have to  wait a while befor getting a table that can suffice
    for the amount of people they invited to the dinner party
    
    :return: A message indicating table availability.
    :rtype: str
    """
    people_seating = int(input("How many people are in your dinner group? "))
    if people_seating < 8:
        return ("there is a table available for you now")
    elif people_seating > 8:
        return ("you have to wait a while to get a table")
    else:
        return ("you have just the perfect number of people")
    
print(dinner_group())


def multiple_of_ten() -> bool:
    """
    the function takes in an input from the user and confirms if it is
    a multiple of 10 or not by untilizing the modulus operation
    
    :return: boolean confirming if the number is a multiple of 10 or not
    :rtype: bool
    """
    prompt = "You are to provide me with a number and i'll confirm if it \n is a multiple of 10 or not"
    prompt +="\n Enter Number here"
    number = int(input(prompt))
    if number % 10 == 0:
        return True
    else:
        return False

print(multiple_of_ten())


while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")


while True:
    age = input("Enter your age (or 'quit' to stop): ")

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")


topping = ""
while topping != 'quit':
    topping = input("Enter a topping (or 'quit' to stop): ")

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")


topping = ""
while topping != 'quit':
    topping = input("Enter a topping (or 'quit' to stop): ")

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")

while True:
    topping = input("Enter a topping (or 'quit' to stop): ")

    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")


while True:
    print("This loop will run forever.")
