import allure
from hw_data.pages.account_management_page import LoginPage
from hw_data.pages.product_page import ProductManager
from hw_data.test_data.data import auth_email, auth_password, credit_card

product_page = ProductManager()
login_page = LoginPage()
login = auth_email
password = auth_password
credit_card = credit_card


@allure.tag("web")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'WEB')
@allure.title("Поиск товара через UI")
@allure.feature("Search")
def test_search():
    with allure.step("Открыть продуктовую страницу"):
        product_page.open_product_page()
    with allure.step("Поиск 'Polo'"):
        product_page.search_product()
    with allure.step("Проверка результата поиска"):
        product_page.check_search()


@allure.tag("web")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'WEB')
@allure.title("Проверка фильтра женской одежды через UI")
@allure.feature("Filters")
def test_filters():
    with allure.step("Открыть продуктовую страницу"):
        product_page.open_product_page()
    with allure.step("Выставить фильтр женской одежды"):
        product_page.filter_women_dresses()
    with allure.step("Проверить работу фильтра"):
        product_page.check_filter()


@allure.tag("web")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'WEB')
@allure.title("Проверка покупки через UI")
@allure.feature("Purchase")
def test_purchase():
    with allure.step("Вход в свой аккаунт"):
        login_page.open_login_registration_page()
        login_page.fill_login_page(login, password)
        login_page.submit_login()
    with allure.step("Открытие продуктовой страницы"):
        product_page.open_product_page()
    with allure.step("Добавление 'Blue top'"):
        product_page.add_item_to_cart()
    with allure.step("Подтверждение покупки"):
        product_page.confirm_purchase()
    with allure.step("Заполнение карточки покупки"):
        product_page.fill_card_data(credit_card)
    with allure.step("Оплата покупки"):
        product_page.pay_for_chosen_item()
    with allure.step("Проверка покупки"):
        product_page.check_purchase()