def triangle_fun(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        print('Invalid input')
    elif x + y <= z or x + z <= y or y + z <= x:
        print('Invalid input')
    elif x == y == z:
        print('This is equilateral triangle')
    elif x == y or x == z or y == z:
        print('This is isosceles triangle')
    else:
        print('This is a scalene')

a = int(input('Type first edge: '))
b = int(input('Type second edge: '))
c = int(input('Type third edge: '))
triangle_fun(a, b, c)