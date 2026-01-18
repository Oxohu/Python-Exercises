# TASK 1: Stings
"""
this is a function that prints a sentence,
using the name of a pizza from a list of my favourite pizzas, the pizza_list
"""
def Favourite_pizza(pizza: list[str]) -> str:
    for i in pizza:
        print(f"{i} is my favourite type of pizza")
    print("I really love pizza")
    return

'''
this is a function that loops through a list of pets and if there is a dog in the list,
It prints the sentence: a dog would make a great pet
'''
def pets(animals : list[str]) -> None:
    for animal in animals:
        if animal == "dog":
            print("A dog would make a good pet")
            return
        else:
            print(f"there are no dogs, we only have a {animal} \n Try the next shop")

#creating the list to be passed as arguement to the function
pizza_types =['pepperoni', 'Olive', 'chicken']

#calling the function Favourite_pizza
Favourite_pizza(pizza_types)
print("I would like to order one of all")

'''copying the list of pizza types into a friend's pizza 
and appending a new pizza type to the list
'''
friends_pizza = pizza_types[:]
friends_pizza.append('nutmeg')
print(friends_pizza)

#creating a list to be passed to the function "pets"
animals = ['cat', 'dog', 'snake', 'spider']
#calling the function "pets"
pets(animals)


#TASK 2 : Integers

'''
this function uses a for loop to print numbers within the range of the argument passed
'''
def counting(numbers:int) -> int:
    for i in range (numbers):
        print(i)
    return

counting(20)

"""
this function sums all numbers within the given range
"""
def sum_of_million(value : int) -> int:
    summation = sum(i for i in range(value))
    print (summation)
    return summation

sum_of_million(1000001)

"""
the function below makes a list cubes within the range passes
"""
def cubes(number: int) -> list[int]:
    values = [i**3 for i in range (number)]
    print (values)
    print (values[:3])
    print (values[2:6])
    print(values[-3:])
    return 

cubes(10)
"""
creating a tuple of buffet food and testing the mutability of the tuple
"""
buffet = ('rice', 'noodles', 'yam', 'fruits', 'mac')
print(buffet)

#a tuple cannot be modified but a new value can be assigned to a tuple

buffet= ("pasta")
print (buffet)
