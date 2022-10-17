# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите X')
x = int(input())
print('Введите Y')
y = int(input())
print('Введите Z')
z = int(input())
a = [x,y,z]       

def checkPredicate(a):
    left = not (a[0] or a[1] or a[2])
    right = not a[0] and not a[1] and not a[2]
    result = left == right
    return result

if checkPredicate(a) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
