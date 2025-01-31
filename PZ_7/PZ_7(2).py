def possitive(box):
    """Преобразует каждое слово в строке так, чтобы оно начиналось с заглавной буквы."""
    words = box.split()
    possitivest = []

    for word in words:
        if word and word[0].isalpha():
            possitivest.append(word.capitalize())
        else:
            possitivest.append(word)

    return ' '.join(possitivest)


try:

    box = input("Введите предложение: ")


    if not box.strip():
        print("Ошибка: Ввод не должен быть пустым.")
    else:

        result = possitive(box)


        print("Результат:", result)

except ValueError:
    print(f"Произошла ошибка: ")