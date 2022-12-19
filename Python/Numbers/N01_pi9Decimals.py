import math #can also use numpy for large data

n = float(input("Enter a number: ")) #get user input and convert it from string to float

decimal9 = (math.pi*n) #call pi using math.pi in math library

print(round(decimal9, 9)) #call round(<decimal number>, <round nth>) function from math library

#Note: There's a problem with round() not rounding up decimal 5