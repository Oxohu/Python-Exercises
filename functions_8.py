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

print(make_shirt("Medium", "Stay curious"))
print(make_shirt(size="Large", message="Code with confidence"))


def make_shirt(size: str = "Large", message: str = "I like Python progrmming") -> str:
    """
    this function returns a summary of a shirt with
    default size and default message
    
    :param size: size of the shirt
    :param message: message printed on the shirt
    :return: summary sentence
    :rtype: str
    """
    return f"The shirt size is {size} and the message printed on it is '{message}'."


print(make_shirt())
print(make_shirt(size="Medium"))
print(make_shirt(size="Small", message="Python is fun"))


def describe_city(city: str, country: str = "Nigeria") -> str:
    """
    this function returns a sentence describing
    which country a city is in a country
    
    :param city: name of the city
    :param country: name of the country
    :return: description sentence
    :rtype: str
    """
    return f"{city} is in {country}."

print(describe_city("Ilorin"))
print(describe_city("Lagos"))
print(describe_city("Reykjavik", "Iceland"))

def city_country(city: str, country: str) -> str:
    """
    this function returns a formatted string
    containing a city and its country

    :param city: name of the city
    :param country: name of the country
    :return: formatted city-country string
    :rtype: str
    """
    return f"{city}, {country}"


print(city_country("Santiago", "Chile"))
print(city_country("Lagos", "Nigeria"))
print(city_country("Tokyo", "Japan"))


def make_album(artist: str, title: str, songs: int | None = None) -> dict:
    """
    this function builds and returns a dictionary
    describing a music album

    :param artist: name of the artist
    :param title: album title
    :param songs: optional number of songs
    :return: album dictionary
    :rtype: dict
    """
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album


print(make_album("Adele", "30"))
print(make_album("Burna Boy", "African Giant"))
print(make_album("Coldplay", "Parachutes", 10))


while True:
    artist = input("Enter artist name (or 'q' to quit): ")
    if artist.lower() == "q":
        break
    title = input("Enter album title (or 'q' to quit): ")
    if title.lower() == "q":
        break
    print(make_album(artist, title))


def show_messages(messages: list[str]) -> str:
    """
    this function prints each message
    from a list of messages

    :param messages: list of messages
    :return: confirmation string
    :rtype: str
    """
    for message in messages:
        print(message)
    return "Messages displayed"


messages = ["Hello", "How are you?", "Python is fun"]
print(show_messages(messages))


def send_messages(messages: list[str], sent_messages: list[str]) -> str:
    """
    this function prints messages and moves them
    to another list

    :param messages: list of messages
    :param sent_messages: list to store sent messages
    :return: confirmation string
    :rtype: str
    """
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
    return "Messages sent"


messages = ["Hi", "Good morning", "Good night"]
sent_messages = []
print(send_messages(messages, sent_messages))
print(messages)
print(sent_messages)


messages = ["Reminder", "Meeting at 5", "Submit assignment"]
sent_messages = []
print(send_messages(messages[:], sent_messages))
print(messages)
print(sent_messages)


def make_sandwich(*items: str) -> str:
    """
    this function summarizes a sandwich order

    :param items: items to include in the sandwich
    :return: summary sentence
    :rtype: str
    """
    return f"Sandwich with the following items: {', '.join(items)}"


print(make_sandwich("bread", "egg"))
print(make_sandwich("bread", "chicken", "lettuce"))
print(make_sandwich("bread", "tuna", "cheese", "tomato"))


def build_profile(first_name: str, last_name: str, user_info) -> dict:
    """
    this function builds a user profile dictionary

    :param first_name: user's first name
    :param last_name: user's last name
    :param user_info: additional user information
    :return: profile dictionary
    :rtype: dict
    """
    profile = {"first_name": first_name, "last_name": last_name}
    profile.update(user_info)
    return profile


print(build_profile(
    "Nafisat",
    "Abdulsalam",
    field="Mechatronics Engineering",
    interest="Data Engineering",
    country="Nigeria"
))


def make_car(manufacturer: str, model: str, car_info) -> dict:
    """
    this function stores car information
    in a dictionary

    :param manufacturer: car manufacturer
    :param model: model name
    :param car_info: additional car details
    :return: car dictionary
    :rtype: dict
    """
    car = {"manufacturer": manufacturer, "model": model}
    car.update(car_info)
    return car


print(make_car("subaru", "outback", color="blue", tow_package=True))
