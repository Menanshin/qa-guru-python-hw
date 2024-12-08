import math
import random
import pytest
from hamcrest import assert_that, equal_to, has_length, is_


def test_greeting():
    name = "Анна"
    age = 25

    actual_output = f"Привет, {name}! Тебе {age} лет."
    expected_output = "Привет, Анна! Тебе 25 лет."

    assert_that(actual_output, equal_to(expected_output), "Ошибка в функции приветствия")

    print("УСПЕШНО")



def test_rectangle():
    a = 10
    b = 20

    perimeter = 2 * (a + b)
    area = a * b

    assert_that(perimeter, equal_to(60), "Ошибка в вычислении периметра")
    assert_that(area, equal_to(200), "Ошибка в вычислении площади")


def test_circle():
    r = 23

    area = math.pi * r ** 2
    length = 2 * math.pi * r

    assert_that(area, equal_to(1661.9025137490005), "Ошибка в вычислении площади круга")
    assert_that(length, equal_to(144.51326206513048), "Ошибка в вычислении длины окружности")


def test_random_list():
    l = sorted(random.randint(1, 100) for _ in range(10))

    assert_that(l, has_length(10), "Ошибка в длине списка")
    assert_that(all(l[i] <= l[i + 1] for i in range(len(l) - 1)), is_(True), "Список не отсортирован")


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    unique_l = sorted(set(l))

    expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert_that(unique_l, equal_to(expected_list), "Ошибка в удалении дубликатов")
    assert_that(unique_l, has_length(10), "Ошибка в длине списка")


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    d = dict(zip(first, second))

    assert_that(d, has_length(5), "Ошибка в длине словаря")
    assert_that(list(d.keys()), equal_to(first), "Ошибка в ключах словаря")
    assert_that(list(d.values()), equal_to(second), "Ошибка в значениях словаря")
