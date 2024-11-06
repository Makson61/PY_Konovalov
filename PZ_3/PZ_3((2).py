#Даны три целых числа, одно из которых отлично от двух других, равных между собой.
def possitivest():
    try:
        # Пример использования
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        if a == b:
            return 3
        elif a == c:
            return 2
        else:
            return 1
    except ValueError:
        print("Произошла ошибка")
possitive = possitivest()
print(f"Порядковый номер числа:{possitive}")