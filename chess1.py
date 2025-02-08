'''
Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise

'''
a = int(input("Enter the column number of the first cell: "))
b = int(input("Enter the row number of the first cell: "))
c = int(input("Enter the column number of the second cell: "))
d = int(input("Enter the row number of the second cell: "))
if a==c or b==d:
    print('YES')
else:
    print('NO')

'''
Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

'''
a = int(input("Enter the column number of the first cell: "))
b = int(input("Enter the row number of the first cell: "))
c = int(input("Enter the column number of the second cell: "))
d = int(input("Enter the row number of the second cell: "))
if a==b==1:
    if d%c==0:
        print('YES')
    else:
        print('NO')
elif a==1 or b==1:
    if a%2!=0 and b%2!=0:
        if d%c!=0:
            print('YES')
        else:
            print('NO')
    else:
        if d%c!=0:
            print('YES')
        else:
            print('NO')
else :
    if b%a==0:
        if d==1 or c==1:
            if d%2!=0 and c%2!=0:
                print('YES')
            else:
                print('NO')
        else:
            if d%c==0:
                 print('YES')
            else:
                 print('NO')
    else:
        if d==1 or c==1:
             if d%2!=0 or c%2!=0:
                print('YES')
             else:
                print('NO')
        else:
           if d%c!=0:
              print('YES')
           else:
              print('NO')
