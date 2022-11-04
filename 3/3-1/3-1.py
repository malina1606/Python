# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [1,2,6,5,8,9,7,1,5,6,99,4]


def Summa(list):
    sum = 0
    for i in range(len(list)):
        if i%2!= 0:
            sum = sum + list[i]
    return sum

B = Summa(list)
print(B)