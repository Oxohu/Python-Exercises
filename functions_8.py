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