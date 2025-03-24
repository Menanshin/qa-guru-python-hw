import dataclasses


@dataclasses.dataclass
class CreditCard:
    card_holder: str
    card_number: str
    cvc: str
    expiration_month: str
    expiration_year: str


def __init__(self, card_holder, card_number, cvc, expiration_month, expiration_year):
    self.card_holder = card_holder
    self.card_number = card_number
    self.cvc = cvc
    self.expiration_month = expiration_month
    self.expiration_year = expiration_year
