# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

import random
p=0
A=[]
print('Введите число')
N = int(input())
list = [random.uniform(1, N) for _ in range(N)]
for i in list:
    print('%.2f' %i) 
print('Результат')
for j in range(len(list)):
    s=list[j]%1
    A.append(s)
p =(max(A) - min(A)) %1
print('%.2f' %p)
