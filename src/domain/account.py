class Account:
    def __init__(self, customer_id: int, account_id: int, account_number: int):
        self.__account_id = account_id
        self.__customer_id = customer_id
        self.__account_number = account_number
        # For simplicity, we're maintaining balance inside account object
        self.__balance = 0.0

    def deposit(self, amount: float) -> None:
        # validations are done in use_case layer
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        # since balance get go to negatives, validations are done in use_case layer
        self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance

    def get_account_id(self) -> int:
        return self.__account_id

    def get_customer_id(self) -> int:
        return self.__customer_id
