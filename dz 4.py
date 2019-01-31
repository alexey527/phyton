#написать функцию, которая находит количество цифр в каждом числе массива. результат записывается в новый массив
def kolvo(a):
    k = 0
    while(a != 0):
        a = a // 10
        k += 1
    return(k)


n = int(input())
mas = []
for i in range(n):
    x = int(input())
    mas.append(x)

itg = []
g = 0
for j in range(n):
    s = kolvo(mas[j])
    itg.append(s)
print(itg)
    
