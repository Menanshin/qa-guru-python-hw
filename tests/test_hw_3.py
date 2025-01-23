from datetime import time

# Задача 1: Переключение темной темы по времени
def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени.
    """
    current_time = time(hour=23)
    is_dark_theme = 22 <= current_time.hour or current_time.hour < 6
    assert is_dark_theme is True


# Задача 2: Учет выбора пользователя при переключении темной темы
def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя.
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        is_dark_theme = 22 <= current_time.hour or current_time.hour < 6

    assert is_dark_theme is True


# Задача 3: Поиск пользователей по условиям
def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей.
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = next(user for user in users if user["name"] == "Olga")
    # Используем `next`, чтобы взять первый (и единственный) элемент из списка

    assert suitable_users == {"name": "Olga", "age": 45}
    suitable_users = [user for user in users if user["age"] < 20]
    # Используем списковое включение (list comprehension), чтобы отфильтровать пользователей с возрастом < 20.

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Задача 4: Преобразование имени функции в читаемый формат
def readable_function(func, *args, **kwargs):
    """
    Преобразует имя функции и её аргументы в читаемый формат.
    """
    readable_name = func.__name__.replace("_", " ").title()
    # - `func.__name__` возвращает имя функции.
    # - `.replace("_", " ")` заменяет символы "_" на пробелы.
    # - `.title()` делает первую букву каждого слова заглавной.

    args_repr = ", ".join([repr(arg) for arg in args])
    kwargs_repr = ", ".join([f"{key}={repr(value)}" for key, value in kwargs.items()])
    # - `repr(arg)` возвращает строковое представление каждого аргумента.
    # - `", ".join(...)` объединяет все элементы в строку, разделённую запятыми.

    all_args = ", ".join(filter(None, [args_repr, kwargs_repr]))
    # - `filter(None, ...)` убирает пустые строки.
    # - `", ".join(...)` объединяет результат в строку.

    return f"{readable_name} [{all_args}]"


def test_readable_function():
    assert readable_function(open_browser, browser_name="Chrome") == "Open Browser [browser_name='Chrome']"
    assert readable_function(go_to_companyname_homepage, page_url="https://companyname.com") == \
           "Go To Companyname Homepage [page_url='https://companyname.com']"
    assert readable_function(find_registration_button_on_login_page, page_url="https://companyname.com/login",
                             button_text="Register") == \
           "Find Registration Button On Login Page [page_url='https://companyname.com/login', button_text='Register']"


# Реализация функций для тестирования:
def open_browser(browser_name):
    actual_result = readable_function(open_browser, browser_name=browser_name)
    assert actual_result == "Open Browser [browser_name='Chrome']"


def go_to_companyname_homepage(page_url):
    actual_result = readable_function(go_to_companyname_homepage, page_url=page_url)
    assert actual_result == "Go To Companyname Homepage [page_url='https://companyname.com']"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = readable_function(find_registration_button_on_login_page, page_url=page_url, button_text=button_text)
    assert actual_result == "Find Registration Button On Login Page [page_url='https://companyname.com/login', button_text='Register']"
