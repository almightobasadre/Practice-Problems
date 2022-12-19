"""
Find PI to the Nth Digit:
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.
"""

import math #can also use numpy for large data

n = int(input("Enter number of decimal places (1-15): ")) #get user input and convert it from string to float

print(round(math.pi, n)) #call round(<float>, <round nth>) function and pi from math library