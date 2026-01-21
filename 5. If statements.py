

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

def check_score(alien_colour: str):
    '''
    this function uses an if statement to verify whether or not the 
    gamer guessed the correct colour of the alien that was shot down
    alien_colour  is a variable that stores the gamer's choice of colour
    '''
    if alien_colour == "green":
        print("you just earned 5 points")
    else:
        print("you got the alien colour wrong")

alien_colour = "green"
check_score(alien_colour)