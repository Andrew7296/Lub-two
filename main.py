def a1(): #Задача на проверку соответствия пароля
    p1 = str(input()) #Объявление строковых переменных через ввод
    p2 = str(input())
    if p1!=p2:
        print('Пароль не принят') #функция print
    else:
        print('Пароль принят')
# a1() если хочу вызвать часть кода

def b1():
    num = int(input("введите номер места в вагоне"))

    if num % 2 == 0 and (num < 37):
        print("нижнее место в купе")
    elif (num % 2 != 0) and (num < 37):
        print("верхнее место в купе")
    for num in range(36, 55):
        print("боковое место")

def c1():
    year = int(input())
    if (year % 4 == 0) and (year % 100!= 0) or (year % 400!= 0): #обязательно : после условия!
        print (f'Год year не високосный')
    else: #обязательно : после условия!
        print(f'Год year високосный')
#a1() # не должно быть отступа!
#b1() # не должно быть отступа!

def d1():
     a = str(input("введите цвет:"))
     b = str(input("введите второй цвет: "))
     if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
         print("фиолетовый")
     elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
         print("оранжевый")
     elif (a == 'желтый' and b == 'синий') or (a == 'синий' and b == 'желтый'):
         print("зеленый")
     else:
         print("ошибка")
def e1():
    n = int(input("Количество слов\n"))
    stroka = ""
    for i in range(n):
        word = input("Введите слово: ")
        if i == 0:
            stroka += word
        else:
            stroka += " " + word
    print(stroka)
a1()
b1()
c1()
d1()
e1()
