import math
import random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25

    output = f"Привет, {name}! Тебе {age} лет."
    print(output)

    expected_output = "Привет, Анна! Тебе 25 лет."

    if output != expected_output:
        error_message_test_greeting = f"ОШИБКА! Ожидалась строка '{expected_output}', но получено: {output}"
        print(error_message_test_greeting)
        raise AssertionError(error_message_test_greeting)

    print("УСПЕШНО.")


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    output = f"Длинна {a} и ширина {b}"
    print(output)

    perimeter = 2 * (a + b)
    print(f"Периметр = {perimeter}")
    expected_perimeter = 60

    area = a * b
    print(f"Площадь = {area}")
    expected_area = 200

    if perimeter != expected_perimeter:
        error_message_test_rectangle_perimeter = f"ОШИБКА! Ожидался периметр {expected_perimeter}, но получен периметр {perimeter}"
        print(error_message_test_rectangle_perimeter)
        raise AssertionError(error_message_test_rectangle_perimeter)

    if area != expected_area:
        error_message_test_rectangle_area = f"ОШИБКА! Ожидалась площадь {expected_area}, но получена площадь {area}"
        print(error_message_test_rectangle_area)
        raise AssertionError(error_message_test_rectangle_area)

    print("УСПЕШНО")


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    print(f"Радиус круга = {r} ")

    area = math.pi * r ** 2
    print(f"Площадь круга = {area}")
    expected_area = 1661.9025137490005

    length = 2 * math.pi * r
    print(f"Длинна окружности = {length}")
    expected_length = 144.51326206513048

    if expected_area != area:
        error_message_test_circle_area = f"ОШИБКА! Ожидалась площадь круга {expected_area}, но получена площадь {area}"
        print(error_message_test_circle_area)
        raise AssertionError(error_message_test_circle_area)

    if expected_length != expected_length:
        error_message_test_circle_length = f"ОШИБКА! Ожидалась длина круга {expected_length}, но получена длина {length}"
        print(error_message_test_circle_length)
        raise AssertionError(error_message_test_circle_length)

    print("УСПЕШНО")


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """

    l = sorted(random.randint(1, 100) for _ in range(10))
    print(f"Сгенерированый список {l}")

    len_l = len(l)
    expected_len = 10

    expected_range = all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    if expected_len != len_l:
        error_message_test_random_list_len = f"ОШИБКА! Ожидалась длина списка {expected_len}, но получена длина {len_l}"
        print(error_message_test_random_list_len)
        raise AssertionError(error_message_test_random_list_len)

    if not expected_range:
        error_message_test_random_list_range = f"ОШИБКА! Ожидалась сортировка, но список не отсортирован"
        print(error_message_test_random_list_range)
        raise AssertionError(error_message_test_random_list_range)

    print("УСПЕШНО")


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    l = sorted(set(l))
    print(f"Список без дубликатов {l}")

    expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    len_l = len(l)
    expected_len = 10

    if expected_list != l:
        error_test_unique_elements_list = f"ОШИБКА! Ожидался список {expected_list}, но получен список {l}"
        print(error_test_unique_elements_list)
        raise AssertionError(error_test_unique_elements_list)

    if not isinstance(l, list):
        error_test_unique_elements_instance = f"ОШИБКА! Ожидался тип list, но получен тип {type(l)}"
        print(error_test_unique_elements_instance)
        raise AssertionError(error_test_unique_elements_instance)

    if expected_len != len_l:
        error_test_unique_elements_len = f"ОШИБКА! Ожидалась длинна списка {expected_len}, но получена длинна {len_l}"
        print(error_test_unique_elements_len)
        raise AssertionError(error_test_unique_elements_len)

    print("УСПЕШНО")


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    d = dict(zip(first, second))
    print(f"Созданный словарь: {d}")

    len_d = len(d)
    expected_len = 5

    list_d_keys = list(d.keys())
    expected_keys = first

    list_d_values = list(d.values())
    expected_values = second

    if not isinstance(d, dict):
        error_message_test_dicts_isinstance = f"ОШИБКА! Ожидался тип dict, но получен тип {type(d)}"
        print(error_message_test_dicts_isinstance)
        raise AssertionError(error_message_test_dicts_isinstance)

    if expected_len != len_d:
        error_message_test_dicts_len = f"ОШИБКА! Ожидалась длина словая {expected_len}, но получена длина {len_d}"
        print(error_message_test_dicts_len)
        raise AssertionError(error_message_test_dicts_len)

    if expected_keys != list_d_keys:
        error_message_test_dicts_keys = f"ОШИБКА! Ожидался ключ {expected_keys}, но получен {list_d_keys}"
        print(error_message_test_dicts_keys)
        raise AssertionError(error_message_test_dicts_keys)

    if expected_values != list_d_values:
        error_message_test_dicts_values = f"ОШИБКА! Ожидалось значение {expected_values}, но получено {list_d_values}"
        print(error_message_test_dicts_values)
        raise AssertionError(error_message_test_dicts_values)

    print("УСПЕШНО")
