'''
Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).

For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.

'''
a = int(input("Enter the number of minutes that is passed since midnight: "))
hr=a//60
min=a%60
print(hr,min)

'''
H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.

'''

h = int(input("Enter the number of hours: "))
m = int(input("Enter the number of minutes: "))
s = int(input("Enter the number of seconds: "))
ang=(h*30)+(m*0.5)+(s*(1/120))
print(ang)

'''
Hour hand turned by b degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.

'''

b = float(input("Enter the angle by which hour hand turned since the midnight: "))
ang1=(b/30-int(b/30))*60*6
print(ang1)