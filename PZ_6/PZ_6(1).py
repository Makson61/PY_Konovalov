#Дан список A размера N. Вывести его элементы в следующем порядке: A1, A2, AN,
#AN-1, A3, A4, AN-2, AN-3, … .


def possitive(A):
    n = len(A)
    result = []
    left = 0
    right = n - 1
    secret = True

    while left <= right:
        if secret:
            # Берём до двух элементов спереди
            if left <= right:
                result.append(A[left])
                left += 1
            if left <= right:
                result.append(A[left])
                left += 1
        else:
            # Берём до двух элементов сзади.
            if left <= right:
                result.append(A[right])
                right -= 1
            if left <= right:
                result.append(A[right])
                right -= 1
        secret = not secret

    return result

try:
    N = int(input("Введите размер списка N: "))
    if N <= 0:
        print("Ошибка: Размер списка должен быть положительным целым числом.")
    else:
        A = []
        for i in range(N):
            value = int(input(f"Введите элемент A[{i + 1}]: "))
            A.append(value)

        box = possitive(A)
        print("Элементы списка в новом порядке:")
        print(box)
except ValueError:
    print("Ошибка: Пожалуйста, введите целое число.")