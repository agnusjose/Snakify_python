'''
A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

'''
a = int(input("Enter the cost of a cupcake in dollars: "))
b = int(input("Enter the cost of a cupcake in cents: "))
n = int(input("Enter the number of cupcakes: "))
d=a*n
c=b*n
if c>100:
    add=c//100
    d+=add
    print(d,(c-(add*100)))
else:
    print(d,c)
