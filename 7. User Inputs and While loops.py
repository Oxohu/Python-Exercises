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


def add_pizza_toppings():
    topping = ""
    while topping != 'quit':
        topping = input("Enter a topping (or 'quit' to stop): ")

        if topping != 'quit':
            print(f"I'll add {topping} to your pizza.")


def add_pizza_toppings_with_break():
    while True:
        topping = input("Enter a topping (or 'quit' to stop): ")

        if topping == 'quit':
            break
        print(f"I'll add {topping} to your pizza.")


def infinite_loop():
    while True:
        print("This loop will run forever.")



def make_sandwiches(sandwich_orders):
    finished_sandwiches = []

    while sandwich_orders:
        sandwich = sandwich_orders.pop(0)
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)

    print("\nSandwiches made:")
    for sandwich in finished_sandwiches:
        print(sandwich)


def make_sandwiches_no_pastrami(sandwich_orders):
    finished_sandwiches = []

    print("\nSorry, the deli has run out of pastrami.")

    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    while sandwich_orders:
        sandwich = sandwich_orders.pop(0)
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)

    print("\nSandwiches made:")
    for sandwich in finished_sandwiches:
        print(sandwich)


def dream_vacation_poll():
    dream_vacations = {}

    while True:
        name = input("\nWhat is your name? ")
        place = input("If you could visit one place in the world, where would you go? ")

        dream_vacations[name] = place

        another = input("Would you like to let another person respond? (yes/no): ")
        if another.lower() == 'no':
            break

    print("\nPoll results:")
    for name, place in dream_vacations.items():
        print(f"{name} would like to visit {place}.")


sandwich_orders_1 = ['tuna', 'chicken', 'pastrami', 'egg', 'beef']
make_sandwiches(sandwich_orders_1)

sandwich_orders_2 = [
    'tuna', 'pastrami', 'chicken',
    'pastrami', 'egg', 'pastrami', 'beef'
]
make_sandwiches_no_pastrami(sandwich_orders_2)

dream_vacation_poll()
