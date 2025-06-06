# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество
# полученных элементов.
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def count_prices(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().split()
        prices = list(filter(lambda x: x.replace('.', '', 1).isdigit(), words))
        valid_prices = list(filter(is_float, prices))

    return len(valid_prices)


filename = 'price.txt'
price_count = count_prices(filename)
print(f"Количество цен в файле: {price_count}")