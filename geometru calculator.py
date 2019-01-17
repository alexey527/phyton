
def kvadrat(a):
    return a**2

def pramoug(x, y):
    return x * y

def pramtre(n, m):
    return (a * b) /2

print("Геометрический калькулятор.")
print("выберите фигуру:")
print(" квадрат - 1 \n прямоугольник - 2 \n прямоугольный треугольник - 3")
figure = input("\nвыберите фигуру: ")

if (figure == "1") or (figure == "квадрат"):
    a = int(input("введите длину = "))
    s = kvadrat(a)
    print("площадь квадрата = ", s)
elif (figure == "2") or (figure == "прямогальник"):
    a = int(input("длинна = "))
    b = int(input("ширина = "))
    s = pramoug(a, b)
    print("площадь прямоугольника = ", s)
elif (figure == "3") or (figure == "треугольник"):
    a = int(input("введите первый катет: "))
    b = int(input("введите второй катет: "))
    s = pramtre(a, b)
    print("площадь треугольника = ", s)
else:
    print("Ты слепой!")

