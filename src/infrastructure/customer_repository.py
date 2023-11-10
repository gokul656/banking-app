from src.domain.customer import Customer


class CustomerRepository:
    __customer_count: int
    # Declared as dictionary so that elements can be access at O(1) tc.
    __customers = {int: Customer}

    def __init__(self):
        self.__customer_count = 0
        self.__customers = {}

    def find_by_customer_id(self, customer_id: int) -> Customer | None:
        try:
            return self.__customers[customer_id]
        except KeyError:
            return None

    def save_customer(self, customer: Customer) -> Customer:
        self.__customers[customer.customer_id] = customer
        return self.__customers[customer.customer_id]

    def increment_and_get(self) -> int:
        self.__customer_count += 1
        return self.__customer_count
