# Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения.
# Дополнительные входыне данные, которые учитывались:
# Списки хранятся в файлах, в виде строки чисел разделенных запятой. В файле должны быть только числа.
# Имена файлов передаются, как аргументы командной строки при запуске скрипта.
# Если файл не существует, то список будет пустым.
# Если скрипт запущен с неполным набором аргументов командной строки, то списки считываются из файлов по умолчанию, которые дожны быть в одном катологе со скриптом.

# Эффективность решения O(n + m), где n-количество элементов в списке А, m-количество элементов в списке Б.

__author__ = 'olegk'

import os
import sys

def read_list_from_file(file_path):
    result = []
    if os.path.exists(file_path) == True:
        with open(file_path, "r") as f:
            s =  f.readline()
        result = s.split(',')
    return result

def intersect_list(a, b):
    b_unique_items = {}
    result = []
    for b_item in b:
        b_unique_items[b_item] = True

    for a_item in a:
        if not(a_item in b_unique_items):
            result.append(a_item)

    return result


def main(file_a, file_b):
    a_list = read_list_from_file(file_a)
    b_list = read_list_from_file(file_b)
    return intersect_list(a_list, b_list)

file_a = "input_a.txt"
file_b = "input_b.txt"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: wrong args count. Using default file names.")
    else:
        file_a = sys.argv[1]
        file_b = sys.argv[2]

result = main(file_a, file_b)
print(result)
