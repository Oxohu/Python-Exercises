car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")
print("\nIs car == 'audi'? I predict False.")
print(car == "audi")


def check_score(alien_colour: str):
    """
    this function uses an if statement to verify whether or not the
    gamer guessed the correct colour of the alien that was shot down
    alien_colour  is a variable that stores the gamer's choice of colour
    """
    if alien_colour == "green":
        print("you just earned 5 points")
    elif alien_colour == "yellow":
        print("you just earned 10 points")
    elif alien_colour == "red":
        print("you just earned 15 points")
    else:
        print("you got the alien colours wrong")


alien_colour = "red"
check_score(alien_colour)


def stage_of_life(age: int):
    """
    Docstring for stage_of_life

    :param age: input to be collected from user
    :type age: int
    """
    if age < 2:
        print("you are a child")
    elif age >= 2 and age < 4:
        print("you are a toddler")
    elif age >= 4 and age < 13:
        print("you are a kid")
    elif age >= 13 and age < 20:
        print("you are a teenager")
    elif age >= 20 and age < 65:
        print("you are an adult")
    else:
        print("you are an elder")


age = int(input("how old are you? "))
stage_of_life(age)


def affinity_fruits(fruit: str):
    """
    Docstring for affinity_fruits
    
    :param fruit: Description
    :type fruit: str
    """
    fruit_list = ["oranges", "Bananas", "Apples"]
    if fruit in fruit_list:
        print(f"you really like {fruit}")
    else:
        print(f"{fruit} is not part of the fruits you like")

fruit = input("what fruits do you want?")
affinity_fruits(fruit)

