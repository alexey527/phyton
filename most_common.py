




n = int(input('сколько элементов?'))
mas = []
for i in range(n):
    x = int(input('введите элемент: '))
    mas.append(x)

max_k = 0
for g in range(n):
    h = mas[g]
    k = 0
    for j in range(n):
        print(h, "<>", mas[j])
        if h == mas[j]:
            k += 1

    if max_k < k:
        max_k = k
        chislo = h
print(max_k, chislo)
        
            
