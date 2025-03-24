import dataclasses
import datetime


@dataclasses.dataclass
class User:
    name: str
    email: str
    gender: str
    password: str
    date_of_birth: datetime.date
    first_name: str
    last_name: str
    address: str
    country: str
    state: str
    city: str
    zipcode: str
    number: str


def __init__(self, name, email, gender, password, date_of_birth, first_name, last_name, address, country,
             state, city, zipcode, number):
    self.name = name
    self.email = email
    self.gender = gender
    self.password = password
    self.date_of_birth = date_of_birth
    self.first_name = first_name
    self.last_name = last_name
    self.address = address
    self.country = country
    self.state = state
    self.city = city
    self.zipcode = zipcode
    self.number = number
