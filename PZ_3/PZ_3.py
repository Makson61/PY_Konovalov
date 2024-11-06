#Даны три целых числа: A, B, C. Проверить истинность высказывания
def possitivest():
     try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        C = int(input("Введите число C: "))
        possitive = 0
        if A > 0:
            possitive += 1
        if B > 0:
            possitive += 1
        if C > 0:
            possitive += 1
        return possitive == 2
     except:
         print("Произошла ошибка, повторите попытку")
if possitivest():
    print("Ровно два из чисел A,B,C являются положительными")
else:
    print("Высказывание неверно")