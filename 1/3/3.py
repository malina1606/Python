# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

print('Введите X')
x = int(input())
print('Введите Y')
y = int(input())

def checkCoordinate(x,y):
    if x > 0 and y >0: 
        result = 1
    elif x < 0 and y > 0:
        result = 2
    elif x < 0 and y < 0:
        result = 3
    elif x > 0 and y < 0:
        result = 4
    return result

value = checkCoordinate(x,y)
print()
print(value)