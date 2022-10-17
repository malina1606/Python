# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from operator import length_hint


print('Введите координаты точки А')
xa = int(input())
xb = int(input())
print('Введите координаты точки B')
ya = int(input())
yb = int(input())
A = [xa,xb]
B = [ya,yb]
print(A)
print(B)

def CalculateDistance(xa,xb,ya,yb):
    result = ((xb - xa)**2 + (yb - ya)**2)**0.5
    return result

len_segment = CalculateDistance(xa,xb,ya,yb)
print(len_segment)