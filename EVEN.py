
def EVEN(k):
    if  k % 2 == 0:
        return 1
    else:
        return 0

n = int(input("введите количество чисел массива"))
mas = []
for i in range(n):
    x = int(input())
    mas.append(x)


otv = 0
for i in range(n):
    s = EVEN(mas[i])
    if s == True:
        otv += 1
print(otv)
    
