#Дан список A размера N и целое число K (1 < K < 4, K < N ).
# Осуществить циклический сдвиг элементов списка вправо на K позиций
# (при этом A1 перейдет в AK+1, A2 — в AK+2, ..., AN — в AK).
# Допускается использовать вспомогательный список из 4 элементов.

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
            # Берём до двух элементов сзади
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