#Написать программу, которая вставляет в массив число, которое ввел пользователь. Использовать только пройденный материал.
#Реализовать 2 варианта программы. 1 вар - введенное число вставляется на указанное место(пользователь дополнительно вводит).
#2 вар - алгоритм сам должен понять куда вставлять число (при этом число должно стоять на таком месте, чтобы быть больше предыдущего и меньше следующего).

#1v
try:
    
    n = int(input("введите кол-во элементов массива"))
    mas = []
    for i in range(n):
        x = int(input("введите элемент массива"))
        mas.append(x)
    mas.insert(2, 22)
    print(mas)
    m = int(input("введите добавляемый элемент"))
    h = int(input("введите позицию добавляемого элемента"))
    mas.append(0)
    print(mas)

    for i in range(n, h -1,  -1):
        mas[i] = mas[i -1]
    mas[h -1] = m
    print(mas)
except ValueError:
    print("будь внимательнее")