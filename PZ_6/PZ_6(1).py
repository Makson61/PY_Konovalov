#Дан список A размера N. Вывести его элементы в следующем порядке: A1, A2, AN,
#AN-1, A3, A4, AN-2, AN-3, … .


def possitive(A):
    n = len(A)
    result = []
    left = 0
    right = n - 1

    while left <= right:
        if left == right:
            result.append(A[left])
        else:
            result.append(A[left])
            result.append(A[right])

        left += 1
        right -= 1

    return result

# Пример использования
try:
    N = int(input("Введите размер списка N: "))
    if N <= 0:
        print("Ошибка: Размер списка должен быть положительным целым числом.")
    else:
        A = []

        # Заполняем список A
        for i in range(N):
            value = int(input(f"Введите элемент A[{i + 1}]: "))
            A.append(value)

        box = possitive(A)

        # Выводим результат
        print("Элементы списка в новом порядке:")
        print(box)
except ValueError:
    print("Ошибка: Пожалуйста, введите целое число.")