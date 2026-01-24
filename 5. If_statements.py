car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")


def check_score(alien_colour: str) -> str:
    """
    This function uses an if statement to verify whether or not the
    gamer guessed the correct colour of the alien that was shot down.
    """
    if alien_colour == "green":
        return "You just earned 5 points"
    elif alien_colour == "yellow":
        return "You just earned 10 points"
    elif alien_colour == "red":
        return "You just earned 15 points"
    else:
        return "You got the alien colours wrong"


alien_colour = "red"
result = check_score(alien_colour)
print(result)


def stage_of_life(age: int) -> str:
    """
    Determines the life stage of a person based on age.
    """
    if age < 2:
        return "You are a child"
    elif age < 4:
        return "You are a toddler"
    elif age < 13:
        return "You are a kid"
    elif age < 20:
        return "You are a teenager"
    elif age < 65:
        return "You are an adult"
    else:
        return "You are an elder"


age = int(input("How old are you? "))
print(stage_of_life(age))


def affinity_fruits(fruit: str) -> str:
    """
    This function checks whether the fruit requested
    is part of the liked fruits list.
    """
    fruit_list = ["oranges", "bananas", "apples"]
    fruit = fruit.lower()

    if fruit in fruit_list:
        return f"You really like {fruit}"
    else:
        return f"{fruit} is not part of the fruits you like"


fruit = input("What fruit do you want? ")
print(affinity_fruits(fruit))


def user_greeting(username: str) -> str:
    """
    Determines the greeting message based on username.
    """
    usernames = ["Admin", "habeeb", "nafist", "fatimah", "aisha"]

    if username == "Admin":
        return "Hello admin, would you like to see a status report?"
    elif username in usernames:
        return "Welcome back user"
    else:
        return "You need to register as a user"


name = input("Enter your username: ")
print(user_greeting(name))


def username_status(your_username: str) -> list | str:
    """
    Checks if the username already exists.
    """
    old_users = ["Admin", "habeeb", "nafisat", "fatimah", "aisha"]

    if your_username in old_users:
        return "Username already taken"
    else:
        old_users.append(your_username)
        return old_users


name = input("Enter username: ")
print(username_status(name))
