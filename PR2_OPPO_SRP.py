import re

def read_file(filename):  # считывание файла и возвращение списка строк
    with open(filename, 'r') as file:
        return file.readlines()


def remove_extra_spaces(line):  # удаление лишних пробелов в строке
    return line.strip()


def split_data(line):  # разбивка строки на отдельные элементы
    return re.split(r'\s+', line)


def validate_data(data):  # проверка корректности данных
    if len(data) != 3:  # проверка что 3 элемента (дата, название продукта и цена целым числом)
        return False, "Ошибка при вводе данных"

    date, product, amount_string = data

    if not re.match(r'\d{4}\.\d{2}\.\d{2}', date):  # проверка правильного написания даты формата гггг/мм/дд
        return False, "Ошибка при вводе даты"

    if not re.match(r'^[a-zA-Z]+$', product):  # проверка правильного написания продукта на латинице
        return False, "Ошибка при вводе продукта"

    if not re.match(r'^\d+$', amount_string):  # проверка правильного написания цены, что число целое
        return False, "Ошибка при вводе суммы"

    return True, None


def convert_amount(amount_string):  # приведение строки к целому числу
    return int(amount_string)


def process_data(lines):  # обработка данных и вывод результатов
    total_amount = 0

    for line in lines:
        line = remove_extra_spaces(line)
        data = split_data(line)

        is_valid, error_message = validate_data(data)
        if not is_valid:
            print(error_message)
            continue

        date, product, amount_string = data
        amount = convert_amount(amount_string)
        total_amount += amount

        print(f"Date: {date} Product: \"{product}\" Amount: {amount}")

    print(f"Total amount: {total_amount}")


def process_file(filename):
    lines = read_file(filename)
    process_data(lines)

process_file("in.txt")
