def people_data() -> list:
    """
    Returns a list of dictionaries containing information about people.
    """
    return [
        {"first_name": "Aisha", "last_name": "Sadiq", "age": 20, "city": "Minna"},
        {"first_name": "Habeeb", "last_name": "Lawal", "age": 22, "city": "Ilorin"},
        {"first_name": "Fatimah", "last_name": "Yusuf", "age": 19, "city": "Zaria"},
    ]


people = people_data()

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()


def favourite_numbers() -> dict:
    """
    returns a dictionary that stores peoples favourite number
    :rtype: dict
    """
    return {"Nafisat": 10, "fatimah": 15, "ibrahim": 20, "fatima": 18}


fav_number = favourite_numbers()

for key, value in fav_number.items():
    print(f"{key}'s favourite number is {value}")


def programming_words() -> dict:
    """
    Returns a dictionary containing basic programming terms and their definitions.

    :return: A dictionary where keys are programming terms and values are their meanings
    :rtype: dict
    """
    return {
        "loop": " is used to repeat a block of code multiple times\n",
        "truthy": " is any value that evaluates to True in a condition\n",
        "boolean": "is a data type with only two values: True or False\n",
    }


programming_concepts = programming_words()
for key, value in programming_concepts.items():
    print(f"{key} is a {value}")


def rivers_and_countries() -> dict:
    """
    Returns rivers and the countries they run through.
    """
    return {"Nile": "Egypt", "Niger": "Nigeria", "Amazon": "Brazil"}


rivers = rivers_and_countries()

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print()

for river in rivers.keys():
    print(river)

print()

for country in rivers.values():
    print(country)


def favorite_languages() -> dict:
    """
    Returns people and their favorite programming languages.
    """
    return {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}


def poll_candidates() -> list:
    """
    Returns a list of people who should take the poll.
    """
    return ["jen", "sarah", "mike", "phil", "amina", "edward"]


languages = favorite_languages()
candidates = poll_candidates()

for person in candidates:
    if person in languages:
        print(f"Thank you, {person.title()}, for responding.")
    else:
        print(f"{person.title()}, please take the favorite languages poll.")


def people_data() -> list:
    """
    Returns a list of dictionaries containing information about people.
    """
    return [
        {"first_name": "Aisha", "last_name": "Sadiq", "age": 20, "city": "Minna"},
        {"first_name": "Habeeb", "last_name": "Lawal", "age": 22, "city": "Ilorin"},
        {"first_name": "Fatimah", "last_name": "Yusuf", "age": 19, "city": "Zaria"},
    ]


people = people_data()

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()


def pets_data() -> list:
    """
    Returns a list of dictionaries representing pets.
    """
    return [
        {"animal": "dog", "owner": "Amina"},
        {"animal": "cat", "owner": "Sadiq"},
        {"animal": "parrot", "owner": "Habeeb"},
    ]


pets = pets_data()

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()


def favorite_places() -> dict:
    """
    Returns people and their favorite places.
    """
    return {
        "Aisha": ["Abuja", "Ilorin"],
        "Habeeb": ["Lagos", "Ibadan", "Ogbomosho"],
        "Fatimah": ["Minna"],
    }


places = favorite_places()

for name, locations in places.items():
    print(f"{name}'s favorite places:")
    for place in locations:
        print(f"- {place}")
    print()


def favorite_numbers() -> dict:
    """
    Returns people and lists of their favorite numbers.
    """
    return {"Aisha": [3, 7], "Habeeb": [5, 9, 11], "Fatimah": [2], "Sadiq": [4, 8]}


numbers = favorite_numbers()

for name, nums in numbers.items():
    print(f"{name}'s favorite numbers:")
    for num in nums:
        print(f"- {num}")
    print()


def cities_info() -> dict:
    """
    Returns information about cities.
    """
    return {
        "Minna": {
            "country": "Nigeria",
            "population": "Approx. 500,000",
            "fact": "Home to FUT Minna",
        },
        "Lagos": {
            "country": "Nigeria",
            "population": "Over 20 million",
            "fact": "Nigeria’s commercial hub",
        },
        "Cairo": {
            "country": "Egypt",
            "population": "Over 9 million",
            "fact": "Located along the Nile River",
        },
    }


cities = cities_info()

for city, details in cities.items():
    print(city)
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()


def extended_cities_info() -> dict:
    """
    Extended city data with additional details.
    """
    return {
        "Abuja": {
            "country": "Nigeria",
            "population": "Approx. 3 million",
            "fact": "Capital city of Nigeria",
            "known_for": "Planned city and government institutions",
        }
    }


extended_cities = extended_cities_info()

for city, details in extended_cities.items():
    print(f"City: {city}")
    for key, value in details.items():
        print(f"- {key.title()}: {value}")
