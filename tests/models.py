class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        Проверяет, достаточно ли товара на складе
        Возвращает True, если товара достаточно, иначе False
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        Метод покупки товара
        Если товара недостаточно, выбрасывает исключение ValueError
        Если товара хватает, уменьшает его количество
        """
        if not self.check_quantity(quantity):
            raise ValueError("Недостаточно товара на складе")
        self.quantity -= quantity

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    def __init__(self):
        """
        Инициализация пустой корзины
        """
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Добавляет продукт в корзину
        Если продукт уже есть, увеличивает его количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Удаляет продукт из корзины
        Если remove_count не задано, удаляет весь продукт
        Если remove_count больше текущего количества, удаляет весь продукт
        """
        if product in self.products:
            if remove_count is None or remove_count >= self.products[product]:
                del self.products[product]
            else:
                self.products[product] -= remove_count

    def clear(self):
        """
        Очищает корзину
        """
        self.products.clear()

    def get_total_price(self) -> float:
        """
        Подсчитывает общую стоимость всех товаров в корзине
        """
        return sum(product.price * count for product, count in self.products.items())

    def buy(self):
        """
        Осуществляет покупку всех товаров в корзине
        Если какого-то товара недостаточно, выбрасывает исключение
        Если покупка успешна, очищает корзину
        """
        for product, count in self.products.items():
            if not product.check_quantity(count):
                raise ValueError(f"Товара {product.name} недостаточно на складе")

        for product, count in self.products.items():
            product.buy(count)

        self.clear()
