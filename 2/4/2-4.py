# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.



import random
p=1
A=[]
print('Введите число')
N = int(input())
list = [random.randint(-N, N) for _ in range(N)]
print(list)
f=open('file.txt', 'r')
for line in f:
    A.append([int(x) for x in line.split()])
print(A)
f.close()
for i in A:
    p *= list[i]
print(p)