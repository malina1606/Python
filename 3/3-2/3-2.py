# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
p=1
A=[]
print('Введите число')
N = int(input())
if N % 2 ==0:
    list = [random.randint(1, N) for _ in range(N)]
    print(list)

    for i  in range(0, N//2):
        p = list[i]*list[N-i-1]
        A.append(p)

    print(A)
else:
    print('Введите четное число')