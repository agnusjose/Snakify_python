'''

For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.
To do that, you can use the sep and end arguments for the function print().


'''
a = int(input("Enter the limit: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,sep='',end='')
    print()

