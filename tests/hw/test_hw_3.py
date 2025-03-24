from datetime import time
import allure


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени.
    """
    with allure.step("Выставлям время"):
        current_time = time(hour=23)

    with allure.step("Выставляем темную темы"):
        is_dark_theme = 22 <= current_time.hour or current_time.hour < 6

    with allure.step("Проверяем правильность выставленной темы"):
        assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя.
    """
    with allure.step("Выставляем время"):
        current_time = time(hour=16)

    with allure.step("Выставляем темную тему"):
        dark_theme_enabled_by_user = True

    with allure.step("Меняем тему в зависимости от времени и выбора пользователя"):
        if dark_theme_enabled_by_user is not None:
            is_dark_theme = dark_theme_enabled_by_user
        else:
            is_dark_theme = 22 <= current_time.hour or current_time.hour < 6

    with allure.step("Проверяем правильность выставленой темы"):
        assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей.
    """
    with allure.step("Создаем список пользовател1"):
        users = [
            {"name": "Oleg", "age": 32},
            {"name": "Sergey", "age": 24},
            {"name": "Stanislav", "age": 15},
            {"name": "Olga", "age": 45},
            {"name": "Maria", "age": 18},
        ]

    with allure.step("Берем первый элемент из списка"):
        suitable_users = next(user for user in users if user["name"] == "Olga")

    with allure.step("Проверяем корректность выбора"):
        assert suitable_users == {"name": "Olga", "age": 45}

    with allure.step("Фильтруем пользователей старше 20 лет"):
        suitable_users = [user for user in users if user["age"] < 20]

    with allure.step("Проверяем корректность фильтрации"):
        assert suitable_users == [
            {"name": "Stanislav", "age": 15},
            {"name": "Maria", "age": 18},
        ]


def readable_function(func, *args, **kwargs):
    """
    Преобразует имя функции и её аргументы в читаемый формат.
    """
    with allure.step("Возвращаем имя функции"):
        readable_name = func.__name__.replace("_", " ").title()
    # - `func.__name__` возвращает имя функции.
    # - `.replace("_", " ")` заменяет символы "_" на пробелы.
    # - `.title()` делает первую букву каждого слова заглавной.

    with allure.step("Возвращаем аргументы в виде строки"):
        args_repr = ", ".join([repr(arg) for arg in args])
        kwargs_repr = ", ".join([f"{key}={repr(value)}" for key, value in kwargs.items()])
    # - `repr(arg)` возвращает строковое представление каждого аргумента.
    # - `", ".join(...)` объединяет все элементы в строку, разделённую запятыми.

    with allure.step("объеденяем результат в строку"):
        all_args = ", ".join(filter(None, [args_repr, kwargs_repr]))
    # - `filter(None, ...)` убирает пустые строки.
    # - `", ".join(...)` объединяет результат в строку.

    with allure.step("Получаем конечный преобразованый результат"):
        return f"{readable_name} [{all_args}]"


def test_readable_function():
    with allure.step("Проверяем открытие браузера"):
        assert readable_function(open_browser, browser_name="Chrome") == "Open Browser [browser_name='Chrome']"

    with allure.step("Проверяем открытие домашей страницы"):
        assert readable_function(go_to_companyname_homepage, page_url="https://companyname.com") == \
               "Go To Companyname Homepage [page_url='https://companyname.com']"

    with allure.step("Проверяем наличие кнопки регистрации"):
        assert readable_function(find_registration_button_on_login_page, page_url="https://companyname.com/login",
                                 button_text="Register") == \
               "Find Registration Button On Login Page [page_url='https://companyname.com/login', button_text='Register']"


def open_browser(browser_name):
    with allure.step("Переопределяем открытие браузера"):
        actual_result = readable_function(open_browser, browser_name=browser_name)

    with allure.step("Проверяем открытие браузера"):
        assert actual_result == "Open Browser [browser_name='Chrome']"


def go_to_companyname_homepage(page_url):
    with allure.step("Переопределяем переход на главную страницу"):
        actual_result = readable_function(go_to_companyname_homepage, page_url=page_url)

    with allure.step("Проверяем открытие главной страницы"):
        assert actual_result == "Go To Companyname Homepage [page_url='https://companyname.com']"


def find_registration_button_on_login_page(page_url, button_text):
    with allure.step("Переопределяем нахождение кнопки регистрации"):
        actual_result = readable_function(find_registration_button_on_login_page, page_url=page_url,
                                          button_text=button_text)

    with allure.step("Првоеряем наличие кнопки регистрации"):
        assert actual_result == "Find Registration Button On Login Page [page_url='https://companyname.com/login', button_text='Register']"
