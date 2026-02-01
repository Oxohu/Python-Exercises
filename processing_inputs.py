import math
"""
this file contains functions which take inputs from users and performs certain processes on it to
give the user an informative output e.g converting degrees to radians and vice versa
canculating the area of a circle from inputted radius
determining the type of file based on the file name
"""

def radians_converter() -> float:
    """
    this function collects input degree from the use and returns an output in radians
    
    :return: radian value of the degree given
    :rtype: float
    """
    degrees = float(input("What is the angle in degrees? "))
    if degrees:
      radians = float(degrees * (math.pi / 180))
      return radians
    

def degrees_converter() -> float:
    """
    this function collects input radian from the use and returns an output in degrees
    
    :return: the degree equivalent of the radian value given
    :rtype: float
    """
    radians = float(input("What is the angle in radians? "))
    if radians:
      degrees = float(radians * ( 180 / math.pi))
      return degrees
    
    
print(radians_converter())
print(degrees_converter())


#the next functions calculates the area of a circle

def circle_area() -> float:
   """
   this function prompts user for radius of a circle and uses it to  calculate the area of the circle
   
   :return: area of the circle
   :rtype: float
   """
   radius = float(input("what is the radius of the circle?: "))
   if radius:
      area = float( math.pi * (radius ** 2))

      return area
   
print(circle_area())


#the folloeing function determines what type of file throught the file name
def identify_file_type() -> str:
    """
    Prompts the user to enter a file name and determines the file type
    based on its extension.

    :return: file type in a sentence
    :rtpye: str
    """
    filename = input("Enter a file name: ")

    if '.' not in filename:
        return "Unknown file type"

    file_types = {
        'py': 'Python file',
        'js': 'JavaScript file',
        'html': 'HTML file',
        'css': 'CSS file'
    }

    extension = filename.split('.')[-1]
    return file_types.get(extension, "Unsupported file type")


print(identify_file_type())

