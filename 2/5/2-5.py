# Реализуйте алгоритм перемешивания списка.

import random

print('Введите число')
N = int(input())
list = [random.randint(-N, N) for _ in range(N)]
print(list)
random.shuffle(list)
print(list)