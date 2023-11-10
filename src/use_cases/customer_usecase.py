from src.domain.customer import Customer
from src.exception.customer_exception import CustomerNotFoundException
from src.infrastructure.customer_repository import CustomerRepository


class CustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.__repository = repository

    def create_customer(self, name: str, email: str, phone_number: str) -> Customer:
        customer_id = self.__repository.increment_and_get()
        customer = Customer(customer_id, name, email, phone_number)

        # Implemented only DTO level validations
        # TODO : need to implement validations for unique fields like email & phone number.
        customer.validate()

        return self.__repository.save_customer(customer)

    def get_customer(self, customer_id: int) -> Customer:
        customer = self.__repository.find_by_customer_id(customer_id)
        if customer is None:
            raise CustomerNotFoundException()
        return customer
