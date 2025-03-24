import datetime
import os
from dotenv import load_dotenv
from hw_data.test_data.users import User
from hw_data.test_data.creditcards import CreditCard

COMPANY = "Nomad"

load_dotenv()

registration_ui_email = os.getenv('REGISTRATION_UI_LOGIN')
registration_ui_password = os.getenv('REGISTRATION_UI_LOGIN')

registration_api_email: str | None = os.getenv('REGISTRATION_API_LOGIN')
registration_api_password = os.getenv('REGISTRATION_API_PASSWORD')

auth_email = os.getenv('AUTHORIZATION_LOGIN')
auth_password = os.getenv('AUTHORIZATION_PASSWORD')

card_number = os.getenv('CARD_NUMBER')
cvc = os.getenv('CVC')
expiration_month = os.getenv('EXPIRATION_MONTH')
expiration_year = os.getenv('EXPIRATION_YEAR')

incorrect_email = "nepravilno@test.com"
incorrect_pass = "nepravilno"

user_to_registrate_ui = User(
    name='Evgeniy',
    email=registration_ui_email,
    gender='Male',
    password=registration_ui_password,
    date_of_birth=datetime.date(day=11, month=11, year=1977),
    first_name='Evgeniy',
    last_name='Menanshin',
    address='88 Happy st',
    country='United States',
    state='Massachusetts',
    city='Boston',
    zipcode='123456',
    number='1234567890'
)

user_to_registrate_api = User(
    name='Ciri',
    email=registration_api_email,
    gender='Female',
    password=registration_api_password,
    date_of_birth=datetime.date(day=1, month=1, year=2020),
    first_name='Ciri',
    last_name='Bakovka',
    address='88 Happy st',
    country='United States',
    state='Massachusetts',
    city='Boston',
    zipcode='123456',
    number='0987654321'
)

credit_card = CreditCard(
    card_holder='Evgeniy Menanshin',
    card_number=card_number,
    cvc=cvc,
    expiration_month=expiration_month,
    expiration_year=expiration_year
)