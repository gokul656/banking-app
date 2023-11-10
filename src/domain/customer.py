import re

from src.exception.customer_exception import InvalidCustomerNameException, InvalidCustomerEmailException


class Customer:
    def __init__(self, customer_id: int, name: str, email: str, phone_number: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def validate(self):
        if self.name is None:
            raise InvalidCustomerNameException()

        expression = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        if re.match(expression, self.email) is None:
            raise InvalidCustomerEmailException()

        if not self.phone_number.isnumeric():
            raise InvalidCustomerNameException()
