def people_data() -> list:
    """
    Returns a list of dictionaries containing information about people.
    """
    return [
        {"first_name": "Aisha", "last_name": "Sadiq", "age": 20, "city": "Minna"},
        {"first_name": "Habeeb", "last_name": "Lawal", "age": 22, "city": "Ilorin"},
        {"first_name": "Fatimah", "last_name": "Yusuf", "age": 19, "city": "Zaria"}
    ]


people = people_data()

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()
