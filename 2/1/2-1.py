# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
print('Введите число')
N = float(input())

def sumNumbers(N):
    sum = 0
    for i in str(N):
        if i != ".":
            sum += int(i)
    return sum

result = sumNumbers(N)
print(f"Сумма цифр = {result}")
