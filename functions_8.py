def display_message() -> str:
    """
    this functions returns a message that talks about what i am currently learning
    
    :return: message
    :rtype: str
    """
    return "In this chapter, I am learning about functions"

print(display_message())

def favourite_book() -> str:
    """
    this function prompts the user for the name of their favourite book
    and prints a statement using that name
    
    :return: a sentence saying the book title given by the user is one ofmy favourites
    :rtype: str
    """
    title = input("What is the name of your favourite book? ")
    return f"One of my favourite books is {title}"

print(favourite_book())


def make_shirt(size: str, message: str) -> str:
    """
    this function returns a summary of a shirt size
    and the message printed on the shirt
    
    :param size: size of the shirt
    :param message: message printed on the shirt
    :return: summary sentence
    :rtype: str
    """
    return f"The shirt size is {size} and the message printed on it is '{message}'."

# positional arguments
print(make_shirt("Medium", "Stay curious"))

# keyword arguments
print(make_shirt(size="Large", message="Code with confidence"))


def make_shirt(size: str = "Large", message: str = "I love Python") -> str:
    """
    this function returns a summary of a shirt with
    default size and default message
    
    :param size: size of the shirt
    :param message: message printed on the shirt
    :return: summary sentence
    :rtype: str
    """
    return f"The shirt size is {size} and the message printed on it is '{message}'."

# large shirt with default message
print(make_shirt())

# medium shirt with default message
print(make_shirt(size="Medium"))

# shirt of any size with a different message
print(make_shirt(size="Small", message="Python is fun"))


def describe_city(city: str, country: str = "Nigeria") -> str:
    """
    this function returns a sentence describing
    which country a city is in
    
    :param city: name of the city
    :param country: name of the country
    :return: description sentence
    :rtype: str
    """
    return f"{city} is in {country}."

print(describe_city("Ilorin"))
print(describe_city("Lagos"))
print(describe_city("Reykjavik", "Iceland"))


