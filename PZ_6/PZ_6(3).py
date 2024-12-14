#Дан список A размера N и целое число K (1 < K < 4, K < N ).
# Осуществить циклический сдвиг элементов списка вправо на K позиций
# (при этом A1 перейдет в AK+1, A2 — в AK+2, ..., AN — в AK).
# Допускается использовать вспомогательный список из 4 элементов.

def possitive(A, K):
    N = len(A)

    # Проверка на корректность
    if K < 1 or K >= 4 or K >= N:
        return None  # Возвращаем None при некорректном K

    # Вспомогательный список для хранения последних K элементов
    aux = [0] * K

    # Сохранение последних K элементов
    for i in range(K):
        aux[i] = A[N - K + i]

    # Сдвиг элемента вправо
    for j in range(N - 1, K - 1, -1):
        A[j] = A[j - K]

    # Копируем последние K элементов в начало списка
    for i in range(K):
        A[i] = aux[i]

    return A


N = input("Введите размер списка N: ")
A = []

try:
    N = int(N)
    if N <= 0:
        print("Ошибка: Размер списка должен быть положительным целым числом.")
    else:
        # Заполнение списка A
        for i in range(N):
            value = int(input(f"Введите элемент A[{i + 1}]: "))
            A.append(value)

        K = input("Введите значение K (1 < K < 4, K < N): ")
        K = int(K)

        # Выполнение циклического сдвига
        result = possitive(A, K)

        if result is None:
            print("Ошибка: Неверное значение K. Убедитесь, что 1 < K < 4 и K < N.")
        else:
            # Вывод результата
            print("Список после циклического сдвига:", result)

except ValueError:
    print("Ошибка: Пожалуйста, введите допустимые целые числа.")