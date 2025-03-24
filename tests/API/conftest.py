import uuid
import allure
import pytest
from hw_data.api_models.create_account import create_account
from hw_data.api_models.delete_account import delete_account
from hw_data.utils.helpers import log_request_and_response_to_allure


@pytest.fixture
def base_url():
    return 'https://automationexercise.com/'


@pytest.fixture
def unique_test_email():
    """Создание уникального email для тестов."""
    unique_id = str(uuid.uuid4())[:8]
    return f"test.user.{unique_id}@example.com"


@pytest.fixture
def test_password():
    """Создание пароля для тестов."""
    return "TestPassword123!"


@pytest.fixture
def created_test_user(base_url, unique_test_email, test_password):
    """Создание тестового пользователя и последующего удаления."""
    # Создаем пользователя
    create_result = create_account(base_url, unique_test_email, test_password)
    assert create_result.status_code == 200, f"Не удалось создать тестового пользователя: {create_result.text}"
    log_request_and_response_to_allure(create_result.request, create_result)

    # Возвращаем учетные данные для использования в тестах
    yield {"email": unique_test_email, "password": test_password}

    # Удаляем пользователя после тестов
    try:
        delete_result = delete_account(base_url, unique_test_email, test_password)
        log_request_and_response_to_allure(delete_result.request, delete_result)
        if delete_result.status_code != 200:
            allure.attach(
                f"Не удалось удалить тестового пользователя: {delete_result.text}",
                name="cleanup_error",
                attachment_type=allure.attachment_type.TEXT
            )
    except Exception as e:
        allure.attach(
            f"Ошибка при удалении тестового пользователя: {str(e)}",
            name="cleanup_error",
            attachment_type=allure.attachment_type.TEXT
        )
