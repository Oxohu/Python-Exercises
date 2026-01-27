def rental_car() -> str:
    """
    this function prompts the user for input on the type of car they 
    want to rent

    return input on the user's choice
    rtype: str
    """
    car_type = input("what type of rental car would you like?")
    return car_type

car = rental_car()
print(f"let me see if I can find you a {car}")

