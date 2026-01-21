car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")
print("\nIs car == 'audi'? I predict False.")
print(car == "audi")


def check_score(alien_colour: str):
    """
    Docstring for stage_of_life
    this function uses an if statement to verify whether or not the
    gamer guessed the correct colour of the alien that was shot down
    :param alien_colour: is a variable that stores the gamer's choice of colour
    :type alien_colour: str
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
    Determines the life stage of a person based on age.
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
    this function decides whethe or not the fruit the user is asking for is
    one of the fruits the likes
    :param fruit: input collected from user based on what
    fruit they want to purchase
    :type fruit: str
    """
    fruit_list = ["oranges", "Bananas", "Apples"]
    if fruit in fruit_list:
        print(f"you really like {fruit}")
    else:
        print(f"{fruit} is not part of the fruits you like")


fruit = input("what fruits do you want?")
affinity_fruits(fruit)


def user_greeting(usernames: str):
    """
    Docstring for user_greeting

    :param usernames: Description
    :type usernames: str
    """
    usernames = ["Admin", "habeeb", "nafist", "fatimah", "aisha"]
    for name in usernames:
        if name == "Admin":
            print("Hello admin, would you like to see a status report?")
            break
        else:
            print("welcome back user")


name = input("enter your user name: ")
user_greeting(name)
