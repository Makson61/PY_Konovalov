#Дано вещественное числр А и целое число N (>0).
# Используя один цикл, найти значение выражения 1 - А + А^2 - А^3 + ... +(-1)^N А^N. Условный оператор неиспользовать.
try:
    A = float(input("Введите число A: "))
    N = int(input("Введите целое число N (>0): "))

    result = 0
    sign = 1

    for i in range(N + 1):
        result += sign * A ** i
        sign *= -1

    print("Результат:", result)

except ValueError:
    print("Ошибка: Введите корректные данные (вещеdsadwsdawственное число для A и целое положительное для N).")