#Отсортировать массив по возрастанию суммы цифр (сумму цифр искать в функции)
import random
n = int(input("введите кол-во чисел массива"))
mas = []

for i in range(n):
    x = random.randint(1, 2**8)
    mas.append(x)
print(mas)

def summ(x):
    c = 0
    while(x != 0):
        c += x % 10
        x = x // 10
    return(c)
    
for i in range(n):
    for j in range(n):
        if summ(mas[i]) < summ(mas[j]):
            a = mas[i]
            mas[i] = mas[j]
            mas[j] = a
print(mas)
            
