from selene import browser, have, command
from hw_data.test_data.creditcards import CreditCard


class ProductManager:

    @staticmethod
    def open_product_page():
        browser.element('.nav>li:nth-child(2)').click()

    def search_product(self):
        browser.element('#search_product').type('polo')
        browser.element('#submit_search').click()
        return self

    def check_search(self):
        browser.element('.product-image-wrapper').perform(command.js.scroll_into_view)
        browser.element('.product-image-wrapper').should(have.text('Premium Polo T-Shirts'))
        return self

    def filter_women_dresses(self):
        browser.element('[data-toggle="collapse"]').click()
        browser.element('a[href="/category_products/1"]').click()

    def check_filter(self):
        browser.element('.features_items').perform(command.js.scroll_into_view)
        browser.element('.features_items').should(have.text('Sleeveless Dress'))
        browser.element('.features_items').should(have.text('Stylish Dress'))
        browser.element('.features_items').should(have.text('Rose Pink Embroidered Maxi Dress'))

    def add_item_to_cart(self):
        browser.element("a[href='/product_details/1']").click()
        browser.element('//button[@class="btn btn-default cart"]').click()
        browser.element("a[href='/view_cart']").click()

    def confirm_purchase(self):
        browser.element('.btn').click()
        browser.element('a[href="/payment"]').perform(command.js.scroll_into_view)
        browser.element('a[href="/payment"]').click()

    def fill_card_data(self, creditcard: CreditCard):
        browser.element('[data-qa="name-on-card"]').send_keys(creditcard.card_holder)
        browser.element('[data-qa="card-number"]').send_keys(creditcard.card_number)
        browser.element('[data-qa="cvc"]').send_keys(creditcard.cvc)
        browser.element("input[name='expiry_month']").send_keys(creditcard.expiration_month)
        browser.element("input[name='expiry_year']").send_keys(creditcard.expiration_year)

    def pay_for_chosen_item(self):
        browser.element('#submit').click()

    def check_purchase(self):
        browser.element('[data-qa="order-placed"]').should(have.text('ORDER PLACED!'))
