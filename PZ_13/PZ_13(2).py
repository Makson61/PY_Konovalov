#В двумерном списке найти сумму элементов второй половины матрицы.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

half = len(matrix) // 2

second_half = matrix[half:]

total = sum(sum(row) for row in second_half)

print(total)