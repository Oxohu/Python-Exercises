"""
this is a function that prints a sentence,
using the name of a pizza from a list of my favourite pizzas, the pizza_list
"""
def Favourite_pizza(pizza: list[str]) -> str:
    for i in pizza:
        print(f"{i} is my favourite type of pizza")
    print("I really love pizza")
    return()

'''
this is a function that loops through a list of pets and if there is a dog in the list,
It prints the sentence: a dog would make a great pet
'''
def pets(animals : list[str]) -> str:
    for animal in animals:
        if animal == "dog":
            print("A dog would make a good pet")
        else:
            print(" I dont think we have a pet for you right now")
            print(" Maybe try the next shop")
    print("we hope to see you again soon")
    return()


#creating the list to be passed as arguement to the function
pizza_types =['pepperoni', 'Olive', 'chicken']

#calling the function Favourite_pizza
Favourite_pizza(pizza_types)
print("I would like to order one of all")


#creating a list to be passed to the function "pets"

