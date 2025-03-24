import allure
import jsonschema
import pytest
from hw_data.api_models.create_account import create_account
from hw_data.api_models.delete_account import delete_account
from hw_data.api_models.get_account_data_by_email import get_account_data_by_email
from hw_data.api_models.update_account import update_account
from hw_data.api_models.verify_login import verify_login
from hw_data.test_data.data import (auth_email, auth_password, COMPANY, incorrect_email,
                                    incorrect_pass)
from hw_data.utils.helpers import (load_schema, log_request_and_response_to_allure,
                                   log_request_and_response_to_console)


@allure.tag("api")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'API')
@allure.title("Проверка входа через API для зарегистрированных и незарегистрированных пользователей")
@allure.feature("User account")
@pytest.mark.parametrize("email,password,expected_status,response_code,expected_message", [
    (auth_email, auth_password, 200, 200, "User exists!"),
    (incorrect_email, incorrect_pass, 200, 404, "User not found!"),
])
def test_verify_login_various_cases(base_url, email, password, expected_status, response_code, expected_message):
    schema = load_schema('post_verify_login.json')

    try:
        with allure.step(f"Отправка запроса на верификацию логина (email: {email})"):
            result = verify_login(base_url, email, password)
            log_request_and_response_to_allure(result.request, result)
            log_request_and_response_to_console(result)

        with allure.step("Проверка результата"):
            assert result.status_code == expected_status, f"Ожидался статус {expected_status}, получен {result.status_code}"
            assert result.json()[
                       "responseCode"] == response_code, f"Ожидался код ответа {response_code}, получен {result.json()['responseCode']}"
            assert result.json()[
                       "message"] == expected_message, f"Ожидалось сообщение '{expected_message}', получено '{result.json()['message']}'"
            jsonschema.validate(result.json(), schema)

    except Exception as e:
        allure.attach(
            f"Ошибка при выполнении теста verify_login: {str(e)}",
            name="test_error",
            attachment_type=allure.attachment_type.TEXT
        )
        raise


@allure.tag("api")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'API')
@allure.title("Проверка получения данных аккаунта по email")
@allure.feature("User account")
def test_get_account_data_by_email_successfully(base_url):
    schema = load_schema('get_user_account_by_email.json')

    try:
        with allure.step(f"Отправка запроса на получение данных аккаунта (email: {auth_email})"):
            result = get_account_data_by_email(base_url, auth_email)
            log_request_and_response_to_allure(result.request, result)
            log_request_and_response_to_console(result)

        with allure.step("Проверка результата"):
            assert result.status_code == 200, f"Ожидался статус 200, получен {result.status_code}"
            assert result.json()['user'][
                       'email'] == auth_email, f"Ожидался email {auth_email}, получен {result.json()['user']['email']}"
            jsonschema.validate(result.json(), schema)

    except Exception as e:
        allure.attach(
            f"Ошибка при выполнении теста get_account_data_by_email: {str(e)}",
            name="test_error",
            attachment_type=allure.attachment_type.TEXT
        )
        raise


@allure.tag("api")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'API')
@allure.title("Проверка получения данных по несуществующему email")
@allure.feature("User account")
def test_get_account_data_by_invalid_email(base_url, unique_test_email):
    try:
        with allure.step(f"Отправка запроса на получение данных несуществующего аккаунта (email: {unique_test_email})"):
            result = get_account_data_by_email(base_url, unique_test_email)
            log_request_and_response_to_allure(result.request, result)
            log_request_and_response_to_console(result)

        with allure.step("Проверка результата"):
            assert result.status_code == 404, f"Ожидался статус 404, получен {result.status_code}"
            assert "User not found" in result.text, f"Ожидалось сообщение содержащее 'User not found', получено '{result.text}'"

    except Exception as e:
        allure.attach(
            f"Ошибка при выполнении теста get_account_data_by_invalid_email: {str(e)}",
            name="test_error",
            attachment_type=allure.attachment_type.TEXT
        )
        raise


@allure.tag("api")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'API')
@allure.title("Проверка создания нового аккаунта через API")
@allure.feature("User account")
def test_create_account_successfully(base_url, unique_test_email, test_password):
    schema = load_schema('post_create_user.json')

    try:
        with allure.step(f"Отправка запроса на создание аккаунта (email: {unique_test_email})"):
            result = create_account(base_url, unique_test_email, test_password)
            log_request_and_response_to_allure(result.request, result)
            log_request_and_response_to_console(result)

        with allure.step("Проверка результата"):
            assert result.status_code == 200, f"Ожидался статус 200, получен {result.status_code}"
            assert result.json()[
                       "message"] == "User created!", f"Ожидалось сообщение 'User created!', получено '{result.json()['message']}'"
            jsonschema.validate(result.json(), schema)

        with allure.step("Проверка возможности входа с созданными учетными данными"):
            login_result = verify_login(base_url, unique_test_email, test_password)
            log_request_and_response_to_allure(login_result.request, login_result)
            assert login_result.status_code == 200, f"Ожидался статус 200, получен {login_result.status_code}"
            assert login_result.json()[
                       "message"] == "User exists!", f"Ожидалось сообщение 'User exists!', получено '{login_result.json()['message']}'"

        # Очистка - удаление созданного пользователя
        with allure.step("Очистка - удаление созданного пользователя"):
            cleanup_result = delete_account(base_url, unique_test_email, test_password)
            log_request_and_response_to_allure(cleanup_result.request, cleanup_result)
            assert cleanup_result.status_code == 200, f"Ожидался статус 200, получен {cleanup_result.status_code}"

    except Exception as e:
        # В случае ошибки попытаемся удалить пользователя
        try:
            delete_account(base_url, unique_test_email, test_password)
        except:
            pass

        allure.attach(
            f"Ошибка при выполнении теста create_account: {str(e)}",
            name="test_error",
            attachment_type=allure.attachment_type.TEXT
        )
        raise


@allure.tag("api")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'API')
@allure.title("Проверка невозможности создания дубликата аккаунта")
@allure.feature("User account")
def test_create_duplicate_account(base_url, created_test_user):
    """Проверка невозможности создания дубликата аккаунта."""
    email = created_test_user["email"]
    password = created_test_user["password"]

    try:
        with allure.step(f"Попытка создать аккаунт с уже существующим email ({email})"):
            result = create_account(base_url, email, password)
            log_request_and_response_to_allure(result.request, result)
            log_request_and_response_to_console(result)

        with allure.step("Проверка результата"):
            assert result.status_code == 400, f"Ожидался статус 400, получен {result.status_code}"
            assert "Email already exists" in result.text, f"Ожидалось сообщение о существующем email, получено '{result.text}'"

    except Exception as e:
        allure.attach(
            f"Ошибка при выполнении теста create_duplicate_account: {str(e)}",
            name="test_error",
            attachment_type=allure.attachment_type.TEXT
        )
        raise


@allure.tag("api")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'API')
@allure.title("Проверка успешного обновления данных аккаунта")
@allure.feature("User account")
def test_update_account_data_successfully(base_url, created_test_user):
    schema = load_schema('put_update_user_account.json')
    email = created_test_user["email"]
    password = created_test_user["password"]

    try:
        with allure.step(f"Отправка запроса на обновление аккаунта (email: {email})"):
            result = update_account(base_url, email, password)
            log_request_and_response_to_allure(result.request, result)
            log_request_and_response_to_console(result)

        with allure.step("Проверка результата обновления"):
            assert result.status_code == 200, f"Ожидался статус 200, получен {result.status_code}"
            assert result.json()[
                       "message"] == "User updated!", f"Ожидалось сообщение 'User updated!', получено '{result.json()['message']}'"
            jsonschema.validate(result.json(), schema)

        with allure.step("Проверка обновленных данных"):
            check_result = get_account_data_by_email(base_url, email)
            log_request_and_response_to_allure(check_result.request, check_result)
            assert check_result.status_code == 200, f"Ожидался статус 200, получен {check_result.status_code}"
            assert check_result.json()['user'][
                       'company'] == COMPANY, f"Ожидалась компания {COMPANY}, получено '{check_result.json()['user'].get('company', 'не указано')}'"

    except Exception as e:
        allure.attach(
            f"Ошибка при выполнении теста update_account_data: {str(e)}",
            name="test_error",
            attachment_type=allure.attachment_type.TEXT
        )
        raise


@allure.tag("api")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'API')
@allure.title("Проверка успешного удаления аккаунта")
@allure.feature("User account")
def test_delete_account_successfully(base_url, created_test_user):
    schema = load_schema('delete_delete_account.json')
    email = created_test_user["email"]
    password = created_test_user["password"]

    try:
        with allure.step(f"Отправка запроса на удаление аккаунта (email: {email})"):
            result = delete_account(base_url, email, password)
            log_request_and_response_to_allure(result.request, result)
            log_request_and_response_to_console(result)

        with allure.step("Проверка результата удаления"):
            assert result.status_code == 200, f"Ожидался статус 200, получен {result.status_code}"
            assert result.json()[
                       "message"] == "Account deleted!", f"Ожидалось сообщение 'Account deleted!', получено '{result.json()['message']}'"
            jsonschema.validate(result.json(), schema)

        with allure.step("Проверка невозможности входа с удаленными учетными данными"):
            check_result = verify_login(base_url, email, password)
            log_request_and_response_to_allure(check_result.request, check_result)
            assert check_result.status_code == 200, f"Ожидался статус 200, получен {check_result.status_code}"
            assert check_result.json()[
                       "message"] == "User not found!", f"Ожидалось сообщение 'User not found!', получено '{check_result.json()['message']}'"
            assert check_result.json()[
                       "responseCode"] == 404, f"Ожидался код ответа 404, получен {check_result.json()['responseCode']}"

    except Exception as e:
        allure.attach(
            f"Ошибка при выполнении теста delete_account: {str(e)}",
            name="test_error",
            attachment_type=allure.attachment_type.TEXT
        )
        raise


@allure.tag("api")
@allure.label("owner", "e.maslov")
@allure.label('layer', 'API')
@allure.title("Проверка попытки удаления несуществующего аккаунта")
@allure.feature("User account")
def test_delete_nonexistent_account(base_url, unique_test_email, test_password):
    try:
        with allure.step(f"Попытка удалить несуществующий аккаунт (email: {unique_test_email})"):
            result = delete_account(base_url, unique_test_email, test_password)
            log_request_and_response_to_allure(result.request, result)
            log_request_and_response_to_console(result)

        with allure.step("Проверка результата"):
            assert result.status_code == 404, f"Ожидался статус 404, получен {result.status_code}"
            assert "User not found" in result.text, f"Ожидалось сообщение о ненайденном пользователе, получено '{result.text}'"

    except Exception as e:
        allure.attach(
            f"Ошибка при выполнении теста delete_nonexistent_account: {str(e)}",
            name="test_error",
            attachment_type=allure.attachment_type.TEXT
        )
        raise
