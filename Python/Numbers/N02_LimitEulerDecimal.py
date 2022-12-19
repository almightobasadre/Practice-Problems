"""
Find e to the Nth Digit:
Just like the previous problem, but with e instead of PI.
Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
"""

import math

n = int(input("Enter number of decimal places (1-15) "))

print(round(math.e, n))