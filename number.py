'''
Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.

'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)

'''
10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.

'''
sum=0
for i in range(10):
    ai = int(input("Enter the number: "))
    sum+=ai
print(sum)

'''
For the given integer N calculate the following sum:
1^3+2^3+…+N^3

'''
sum=0
n=int(input("Enter the number: "))
for i in range(1,n+1):
    c=i**3
    sum+=c
print(sum)

'''
Given an integer n
, print the sum 1!+2!+3!+...+n!
.
This problem has a solution with only one loop, so try to discover it. And don't use the math library :)

'''

n = int(input("Enter the limit: "))
sum=0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum+=fact
print(sum)

'''
Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
You need to count the number of numbers that are equal to zero, not the number of zero digits.

'''
n = int(input("Enter the limit: "))
c=0
for i in range(n):
    a=int(input("Enter the number: "))
    if a==0:
        c+=1
print(c)
