'''
A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

'''
import math
n = int(input("Enter the distance the car can cover in a day: "))
m = int(input("Enter the distance of the route: "))
days=m/n
print(math.ceil(days))

