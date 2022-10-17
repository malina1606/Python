# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
print('Введите число')
N = int(input())
A = []
def multiNum(N):
    if N == 1:
        return 1
    else: 
        return N*multiNum(N-1)
        

for i in range(1,N+1):
    A.append(multiNum(i))
print(A)