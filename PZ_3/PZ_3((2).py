#Даны три целых числа, одно из которых отлично от двух других, равных между собой.
try:
    # Ввод трех целых чисел
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    # Проверка, какое число отличается
    if a == b:
        result = 3  # c отличается
    elif a == c:
        result = 2  # b отличается
    else:
        result = 1  # a отличается

    # Вывод результата
    print(f"Порядковый номер числа: {result}")

except ValueError:
    print("Произошла ошибка. Пожалуйста, введите целые числа.")