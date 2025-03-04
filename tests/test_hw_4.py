import allure
import pytest
from tests.models import Product, Cart

class TestProducts:
    def test_product_check_quantity(self, product):
        """Проверяем, что метод check_quantity работает корректно"""
        with allure.step("Проверяем при значении 500"):
            assert product.check_quantity(500) is True

        with allure.step("Проверяем при значении 1000"):
            assert product.check_quantity(1000) is True

        with allure.step("Проверяем при значении 1001"):
            assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        """Проверяем успешную покупку товара"""
        with allure.step("Выставляем значение 500"):
            product.buy(500)

        with allure.step("Проверяем корректность работы"):
            assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        with allure.step("Проверяем, что при покупке большего количества, чем есть в наличии, возникает ValueError"):
            with pytest.raises(ValueError, match="Недостаточно товара на складе"):
                product.buy(2000)

class TestCart:
    def test_add_product(self, cart, product):
        """Тестируем добавление товаров в корзину"""
        with allure.step("Выставляем значение 2"):
            cart.add_product(product, 2)

        with allure.step("Проверяем корректность работы"):
            assert cart.products[product] == 2

        with allure.step("Выставляем значение 3"):
            cart.add_product(product, 3)

        with allure.step("Проверяем, что количество увеличилось"):
            assert cart.products[product] == 5

    def test_remove_product(self, cart, product):
        """Тестируем удаление товаров из корзины"""
        with allure.step("Добавляем 5 товаров"):
            cart.add_product(product, 5)

        with allure.step("Удаляем 2 товара"):
            cart.remove_product(product, 2)

        with allure.step("Проверям корректность оставшегося кол-ва товара"):
            assert cart.products[product] == 3

        with allure.step("Удаляем оставшиеся товары"):
            cart.remove_product(product, 3)

        with allure.step("Проверяем что в корзине не осталось товаров"):
            assert product not in cart.products

    def test_clear_cart(self, cart, product):
        """Тестируем очистку корзины"""
        with allure.step("Добавляем товар в корзину"):
            cart.add_product(product, 5)

        with allure.step("Очищаем корзину"):
            cart.clear()

        with allure.step("Проверяем, что корзина очистилась"):
            assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        """Тестируем вычисление итоговой стоимости корзины"""
        with allure.step("Добавляем товар в корзину"):
            cart.add_product(product, 2)

        with allure.step("Проверяем общую стоимость"):
            assert cart.get_total_price() == 200

    def test_buy_success(self, cart, product):
        """Тестируем успешную покупку, когда товара достаточно"""
        with allure.step("Добавляем товар в корзину"):
            cart.add_product(product, 5)

        with allure.step("Покупаем товар"):
            cart.buy()

        with allure.step("Проверяем остаток товара"):
            assert product.quantity == 995

        with allure.step("Проверяем, что корзина очистилась"):
            assert len(cart.products) == 0

    def test_buy_not_enough_stock(self, cart, product):
        """Тестируем, что при нехватке товара выбрасывается ValueError"""
        with allure.step("Добавляем товара больше, чем есть на складе"):
            cart.add_product(product, 1500)

        with allure.step("Проверяем наличие ответ о нехватки товара на складе"):
            with pytest.raises(ValueError, match=f"Товара {product.name} недостаточно на складе"):
                cart.buy()
