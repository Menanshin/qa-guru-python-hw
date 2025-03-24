import allure
from hw_data.pages.account_management_page import LoginPage, RegistrationPage
from hw_data.test_data.data import user_to_registrate_ui, auth_email, auth_password

login_page = LoginPage()
registration_page = RegistrationPage()
user = user_to_registrate_ui
login = auth_email
password = auth_password


@allure.tag("web")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'WEB')
@allure.title("Проверка входа через UI")
@allure.feature("User account")
def test_login():
    with allure.step("Открыть страницу входа"):
        login_page.open_login_registration_page()
    with allure.step("Заполнить форму"):
        login_page.fill_login_page(login, password)
    with allure.step("Подтвердить авторизацию"):
        login_page.submit_login()
    with allure.step("Проверить авторизацию"):
        login_page.check_login()


@allure.tag("web")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'WEB')
@allure.title("Проверка входа в свой аккаунт через UI")
@allure.feature("User account")
def test_logout():
    with allure.step("Войти в свой аккаунт"):
        login_page.open_login_registration_page()
        login_page.fill_login_page(login, password)
        login_page.submit_login()
    with allure.step("Нажать logout"):
        login_page.logout()
    with allure.step("Проверить выход из аккаунта"):
        login_page.check_logout()


@allure.tag("web")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'WEB')
@allure.title("Проверка регистрации нового пользователя через UI")
@allure.feature("User account")
def test_signup():
    with allure.step("Открыть страницу регистрации"):
        registration_page.open_login_registration_page()
    with allure.step("Заполнить короткую форму регистрации"):
        registration_page.fill_first_registration_form(user)
    with allure.step("Подтвердить заполнение короткой формы регистрации"):
        registration_page.submit_first_registration_form()
    with allure.step("Заполнить полную форму регистрации"):
        registration_page.fill_full_registration_form(user)
    with allure.step("Подтвердить заполнение полной формы регистрации"):
        registration_page.submit_registration()
    with allure.step("Проверить регистрацию"):
        registration_page.check_registration()


@allure.tag("web")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'WEB')
@allure.title("Проверка удаление аккаутна через UI")
@allure.feature("User account")
def test_delete_account():
    with allure.step("Войти в аккаунт"):
        login_page.open_login_registration_page()
        login_page.fill_login_page(user.email, user.password)
        login_page.submit_login()
    with allure.step("Нажать delete account"):
        registration_page.delete_account()
    with allure.step("Проверить удаление аккаунта"):
        registration_page.check_deletion()