'''

Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.



'''

a = int(input("Enter the column number of the first cell: "))
b = int(input(" Enter the row number of the first cell: "))
c = int(input("Enter the column number of the second cell: "))
d = int(input("Enter the row number of the second cell: "))
if a==c:
    if d==b-1 or d==b+1:
        print('YES')
    else:
        print('NO')
elif b==d:
    if c==a-1 or c==a+1:
        print('YES')
    else:
        print('NO')
elif c==a+1:
    if d==b+1 or d==b-1:
        print('YES')
    else:
        print('NO')
elif c==a-1:
    if d==b+1 or d==b-1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

'''
In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.
The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.



'''

a = int(input("Enter the column number of the first cell: "))
b = int(input("Enter the row number of the first cell: "))
c = int(input("Enter the column number of the second cell: "))
d = int(input("Enter the row number of the second cell: "))
if abs(a - c) == abs(b - d):
    print('YES')
else:
    print('NO')

'''
Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.



'''
a = int(input("Enter the column number of the first cell: "))
b = int(input("Enter the row number of the first cell: "))
c = int(input("Enter the column number of the second cell: "))
d = int(input("Enter the row number of the second cell: "))
if abs(a-c)==abs(b-d):
    print('YES')
elif a==c or b==d:
    print('YES')
else:
    print('NO')

'''
Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.

'''
a = int(input("Enter the column number of the first cell: "))
b = int(input("Enter the row number of the first cell: "))
c = int(input("Enter the column number of the second cell: "))
d = int(input("Enter the row number of the second cell: "))
if abs(c-a)==1 and abs(d-b)==2 or abs(c-a)==2 and abs(d-b)==1:
    print('YES')
else:
    print('NO')
   
