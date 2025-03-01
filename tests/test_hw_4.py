import pytest
from tests.models import Product, Cart

class TestProducts:
    def test_product_check_quantity(self, product):
        """Проверяем, что метод check_quantity работает корректно"""
        assert product.check_quantity(500) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        """Проверяем успешную покупку товара"""
        product.buy(500)
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        """Проверяем, что при покупке большего количества, чем есть в наличии, возникает ValueError"""
        with pytest.raises(ValueError, match="Недостаточно товара на складе"):
            product.buy(2000)

class TestCart:
    def test_add_product(self, cart, product):
        """Тестируем добавление товаров в корзину"""
        cart.add_product(product, 2)
        assert cart.products[product] == 2

        cart.add_product(product, 3)
        assert cart.products[product] == 5  # Проверяем, что количество увеличилось

    def test_remove_product(self, cart, product):
        """Тестируем удаление товаров из корзины"""
        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        assert cart.products[product] == 3

        cart.remove_product(product, 3)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):
        """Тестируем очистку корзины"""
        cart.add_product(product, 5)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        """Тестируем вычисление итоговой стоимости корзины"""
        cart.add_product(product, 2)
        assert cart.get_total_price() == 200  # 100 * 2

    def test_buy_success(self, cart, product):
        """Тестируем успешную покупку, когда товара достаточно"""
        cart.add_product(product, 5)
        cart.buy()
        assert product.quantity == 995  # 1000 - 5
        assert len(cart.products) == 0  # Корзина должна очиститься

    def test_buy_not_enough_stock(self, cart, product):
        """Тестируем, что при нехватке товара выбрасывается ValueError"""
        cart.add_product(product, 1500)  # Больше, чем есть на складе
        with pytest.raises(ValueError, match=f"Товара {product.name} недостаточно на складе"):
            cart.buy()
