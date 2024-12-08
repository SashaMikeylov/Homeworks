import math
#  Задача 1
P = float(input("Введите процент P (0 < P < 25): "))


deposit = 1000
target = 1100 
months = 0 
current = deposit

while current <= target:
    current *= (1 + P / 100)
    months += 1 

print("Количество месяцев:" , months)
print("Итоговый размер вклада: ", current)

#  Задача 2

X0 = float(input("Введите начальную точку: "))
X1 = float(input("Введите конечную точку: "))
dX = float(input("Введите шаг: "))


x = X0

while x <= X1:
    if x < 0:
        z = x**2
    if 0 < x <= 1:
        z = math.sin(x) 
    else:
        z = math.cos(x) 

    print(x, z)
    x += dX

N = int(input("Введите целое число N (> 0): "))

#  Задача 3
while N > 0:
    d = N % 10 
    print(d) 
    N //= 10 
