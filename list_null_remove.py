# Задача 2. Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти
# Дополнительные входыне данные, которые учитывались:
# Список хранятся в файле, в виде строки чисел разделенных запятой. В файле должны быть только числа.
# Имя файла передается, как аргумент командной строки при запуске скрипта.
# Если файл не существует, то список будет пустым.
# Если скрипт запущен с неполным набором аргументов командной строки, то список считываются из файла по умолчанию, который дожны быть в одном катологе со скриптом.

# Эффективность решения O(n*n), где n-количество элементов в списке.

__author__ = 'olegk'

import os
import sys

def read_list_from_file(file_path):
    result = []
    if os.path.exists(file_path) == True:
        with open(file_path, "r") as f:
            s =  f.readline()
        result = s.split(',')

    for i in range(len(result)):
        result[i] = int(result[i])
    return result

def remove_null_list(a):
    index = 0
    null_index = -1

    while index < len(a):
        if a[index] == 0:
            if null_index == -1:
                null_index = index
                index += 1
            else:
                index += 1
        elif null_index != -1:
            a[null_index] = a[index]
            a[index] = 0
            index = null_index + 1
            null_index = -1
        else:
            index += 1

    null_count = 0
    index = len(a)-1
    while index >= 0:
        if a[index] == 0:
            null_count += 1
        else:
            break
        index -= 1

    return a[:len(a)-null_count]


def main(file_name):
    input_list = read_list_from_file(file_name)
    return remove_null_list(input_list)

file_name = "null_remove_input.txt"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: wrong args count. Using default file names.")
    else:
        file_name = sys.argv[1]

result = main(file_name)
print(result)

