# Функция для преобразования строки
def convert_case(input_string):
    return input_string.lower()  # Приводим строку к нижнему регистру

# Основной блок программы
try:
    # Запрашиваем ввод от пользователя
    user_input = input("Введите строку: ")

    # Проверяем, что ввод не пустой
    if user_input == "":
        print("Ошибка: Ввод не должен быть пустым.")
    else:
        # Преобразуем строку
        converted_string = convert_case(user_input)

        # Выводим результат
        print("Преобразованная строка:", converted_string)

except ValueError:
    print("Ошибка: Неверный ввод.")