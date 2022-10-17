# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

print('Введите число')
N = int(input())
a =[]  
for i in range(1,N+1):
    a.append((1+1/i)**i)

def sumNumbers(a, N):
    sum = 0
    for i in range(N):
        sum = sum + a[i]
    return sum
print(a)
res = sumNumbers(a, N)
print(res)