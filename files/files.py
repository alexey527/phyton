import sys
import os

def menu2(file_name):
    work2 = True
    choice2 = 0
    while work2 == True:
        if(choice2 == 0):
            print(" 1 - вывод содержимого \n 2 - добавление строки \n 3 - удаление строки \n 4 - возвращение")
            choice2 = int(input("ввод: "))
            print("\n \n")
        elif(choice2 == 1):
            f = open(file_name, "r")
            for line in f:
                print("      ", line[:-1])
            print("\n")
            f.close()
            choice2 = 0
        elif(choice2 == 2):
            f = open(file_name, "r")
            mesto = int(input("введите место добавления строки: "))
            stroka = str(input("введите строку для добавления: "))+"\n"

            
                
            mas = []
            for line in f:
                mas.append(line)
        
            if(mesto < 0 or mesto > len(mas)):
                print("этого места не существует. Вводи место в диапазоне от {} до {}".format(1, len(mas)))
                choice2 = 0
            else:
                mas.insert(mesto-1, stroka)
            f.close()


            f = open(file_name, "w")
            for i in range(len(mas)):
                f.write(mas[i])
            f.close()
            choice2 = 0
            
        elif(choice2 == 3):
            f = open(file_name, "r")

            mas = []
            for line in f:
                mas.append(line)
            f.close()
            mesto = int(input("введите место удаления строки: "))
            if(mesto < 0 or mesto > len(mas)):
                print("этого места не существует. Вводи место в диапазоне от {} до {}".format(1, len(mas)))
                choice2 = 0
            else:
                del mas[mesto -1]

            f = open(file_name, "w")
            for i in range(len(mas)):
                f.write(mas[i])
            f.close()
            choice2 = 0
            
        
            
        elif(choice2 == 4):
            return
            

try:
    work = True
    choice = 0
    while work == True:
        if(choice == 0):
            print("Привет Выбери, что ты хочешь сделать:")
            print(" 1 - создать новый файл \n 2 - выбрать файл \n 3 - выход")
            choice = int(input("  Ввод: "))
            print("\n \n")

        elif(choice == 1):
            name_new_file = str(input("Введите название файла: "))
            file_name = name_new_file + ".txt"
            f = open(file_name, "w")
            f.close()
            menu2(file_name)
            choice = 0
            
        elif(choice == 2):
            directory = os.listdir(path=".")
            mas = []
     
            for i in range(len(directory)):
                name = directory[i]
                if(name[-4:] == ".txt"):
                    mas.append(directory[i])
                    
            for i in range(len(mas)):
                print(str(i+1) + "." + mas[i])
            print("\n")

            
            vibor = int(input("Введите номер файла: "))
            if(vibor > len(mas) or vibor < 0):
                print("будь внимательнее!!!!!!!")
                choice = 0
            else:
                menu2(mas[vibor - 1])
                choice = 0
        elif(choice == 3):
            work = False
        
    sys.exit()
            
        

            
except IOError:
    print("ошибка файла")
except ValueError:
    print("подумай ещё")
