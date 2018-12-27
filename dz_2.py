n = int(input())
mas = []
for i in range(n):
    x = int(input())
    mas.append(x)

m = 0 # сумма
b = 0
a = 0
maxim = 0
for i in range(n):
    if mas[i] > 0 or mas[i] % 3 == 0:
        m += mas[i]
        b += 1
    if mas[i] > 0 or mas[i] % 3 == 0 and mas[i] > b:
        maxim = mas[i]
sred_ar = m / b
print(m, b, maxim, sred_ar)
