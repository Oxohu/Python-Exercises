def display_message() -> str:
    """
    this functions returns a message that talks about what i am currently learning
    
    :return: message
    :rtype: str
    """
    return "In this chapter, I am learning about functions"

print(display_message())

def favourite_book() -> str:
    title = input("What is the name of your favourite book? ")
    return f"One of my favourite books is {title}"

print(favourite_book())
