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
    return f"the shirt is size {size} and it has the following written on it : {message}"

size = input("What size do you wear? ")
message = input("What do you want printed on the shirt? ")

result = make_shirt(size, message)
print(result)

def make_shirt(size = "L", message = "I love python") -> str:
    """
    this function returns a summary of a shirt size
    and the message printed on the shirt
    
    :param size: size of the shirt
    :param message: message printed on the shirt
    :return: summary sentence
    :rtype: str
    """
    return f"the shirt is size {size} and it has the following written on it : {message}"


result = make_shirt()
print(result)


def describe_city(city: 'str', country = "spain") -> str:
    """
    this function accepts the name of a city and it's country and
    prints a simple sentence that says the city is in that country

    :param city: name of a city
    :param country: name of the country the city is in
    :return: summary sentence
    :rtype: str
    """
    return f"{city} is in {country}"

city = "madrid"
result = describe_city(city)
print(result)

def city_country(city, country="Nigeria"):
    return f"{city}, {country}"


cities = {
    "Brazil": ["Rio"],
    "Nigeria": ["Lagos", "Abuja"]
}

for country in cities:
    for city in cities[country]:
        print(city_country(city, country))