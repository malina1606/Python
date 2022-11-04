# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Числа Фибоначчи – это ряд чисел, в котором каждое следующее число равно сумме двух предыдущих.

list = [0,1,1]
list2 = []
fib1 = 1
fib2 = 1
N = int(input("Введите число:"))
i = 0
while i < N - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    list.append(fib2)
    f = ((-1)**(N+1))*fib2
    list2.append(f)
    i = i + 1
    
list2.reverse()
list2.extend(list)
print(list2)