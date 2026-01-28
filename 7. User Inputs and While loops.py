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
    """
    This function prompts users to enter toppings they would like to add to their pizza.
    """
    toppings = []
    topping = ""

    while topping != 'quit':
        topping = input("Enter a topping (or 'quit' to stop): ")
        if topping != 'quit':
            toppings.append(topping)

    return toppings


toppings = add_pizza_toppings()
for topping in toppings:
    print(f"I'll add {topping} to your pizza.")


def add_pizza_toppings_with_break():
    toppings = []

    while True:
        topping = input("Enter a topping (or 'quit' to stop): ")
        if topping == 'quit':
            break
        toppings.append(topping)

    return toppings


toppings = add_pizza_toppings_with_break()
for topping in toppings:
    print(f"I'll add {topping} to your pizza.")


def infinite_loop():
    return "This loop will run forever."


print(infinite_loop())


def make_sandwiches(sandwich_orders):
    finished_sandwiches = []

    while sandwich_orders:
        sandwich = sandwich_orders.pop(0)
        finished_sandwiches.append(sandwich)

    return finished_sandwiches


sandwich_orders = ['tuna', 'chicken', 'pastrami', 'egg', 'beef']
finished = make_sandwiches(sandwich_orders)
for sandwich in finished:
    print(f"I made your {sandwich} sandwich.")


def make_sandwiches_no_pastrami(sandwich_orders):
    finished_sandwiches = []

    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    while sandwich_orders:
        sandwich = sandwich_orders.pop(0)
        finished_sandwiches.append(sandwich)

    return finished_sandwiches


sandwich_orders = [
    'tuna', 'pastrami', 'chicken',
    'pastrami', 'egg', 'pastrami', 'beef'
]
print("\nSorry, the deli has run out of pastrami.")
finished = make_sandwiches_no_pastrami(sandwich_orders)
for sandwich in finished:
    print(f"I made your {sandwich} sandwich.")


def dream_vacation_poll():
    dream_vacations = {}

    while True:
        name = input("\nWhat is your name? ")
        place = input("If you could visit one place in the world, where would you go? ")

        dream_vacations[name] = place

        another = input("Would you like to let another person respond? (yes/no): ")
        if another.lower() == 'no':
            break

    return dream_vacations


poll_results = dream_vacation_poll()
print("\nPoll results:")
for name, place in poll_results.items():
    print(f"{name} would like to visit {place}.")
