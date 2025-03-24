from selene import browser, have, be, command
from hw_data.test_data.users import User


class AccountManager:
    @staticmethod
    def open_login_registration_page():
        browser.element('.nav>li:nth-child(4)').click()

    @staticmethod
    def logout():
        browser.element('.nav>li:nth-child(4)').click()

    def check_logout(self):
        browser.element('.login-form').should(have.text('Login to your account'))

    @staticmethod
    def delete_account():
        browser.element('.nav>li:nth-child(5)').click()

    def check_deletion(self):
        browser.element('[data-qa="account-deleted"]').should(have.text('ACCOUNT DELETED!'))


class LoginPage(AccountManager):

    def fill_login_page(self, login, password):
        browser.element('[data-qa="login-email"]').type(login)
        browser.element('[data-qa="login-password"]').type(password)
        return self

    @staticmethod
    def submit_login():
        browser.element('[data-qa="login-button"]').click()

    def check_login(self):
        browser.element('.nav>li:nth-child(4)').should(be.visible)
        browser.element('.nav>li:nth-child(10)').should(have.text('Logged in as'))


class RegistrationPage(AccountManager):

    def fill_first_registration_form(self, user: User):
        browser.element('[data-qa="signup-name"]').type(user.name)
        browser.element('[data-qa="signup-email"]').type(user.email)
        return self

    @staticmethod
    def submit_first_registration_form():
        browser.element('[data-qa="signup-button"]').click()

    def fill_full_registration_form(self, user: User):
        if user.gender == 'Male':
            browser.element('#id_gender1').click()
        else:
            browser.element('#id_gender2').click()

        browser.element('#password').type(user.password
                                          )
        browser.element('#days').send_keys(user.date_of_birth.strftime("%d"))
        browser.element('#months').send_keys(user.date_of_birth.strftime('%B'))
        browser.element('#years').send_keys(user.date_of_birth.year)
        browser.element('#first_name').type(user.first_name)
        browser.element('#last_name').type(user.last_name)
        browser.element('#address1').type(user.address)
        browser.element('#country').send_keys(user.country)
        browser.element('#state').type(user.state)
        browser.element('[data-qa="create-account"]').perform(command.js.scroll_into_view)
        browser.element('#city').type(user.city)
        browser.element('#zipcode').type(user.zipcode)
        browser.element('#mobile_number').type(user.number)

        return self

    def submit_registration(self):
        browser.element('[data-qa="create-account"]').click()

    def check_registration(self):
        browser.element('[data-qa="account-created"]').should(have.text('ACCOUNT CREATED!'))
