'''
Given a positive real number, print its fractional part.

'''

import math
a =float(input("Enter the number: "))
x=math.floor(a)
print(a-x)


'''
Given a positive real number, print its first digit to the right of the decimal point.

'''
import math
a =float(input("Enter the number: "))
x=math.floor(a)
y=a-x
z=str(y)
print(z[2])