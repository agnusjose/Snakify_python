'''
Chocolate bar has the form of a rectangle divided into n×m
 portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.
The program reads three integers: n, m, and k. It should print YES or NO.

'''
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
k = int(input("Enter the number of squares: "))
if k%n==0 and k//n<m or k%m==0 and k//m<n:
    print('YES')
else:
    print('NO')
