try:
    
    n = int(input("введите кол-во элементов массива"))
    mas = []
    for i in range(n):
        x = int(input("введите элемент массива"))
        mas.append(x)
    
    print(mas)
    m = int(input("введите добавляемый элемент"))
    mas.append(m)
    mas = sorted(mas)
    print(mas)
except ValueError:
    print("будь внимательнее")
