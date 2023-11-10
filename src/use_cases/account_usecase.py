import uuid

from src.domain.account import Account
from src.exception.customer_exception import AccountNotFoundException, InvalidCustomerException
from src.infrastructure.account_repository import AccountRepository


class AccountUseCase:
    def __init__(self, repository: AccountRepository):
        self.__repository = repository

    def create_account(self, customer_id: int, name: str, email: str, phone_number: str) -> Account:
        """ Creates a new account for customer
            Assuming a customer can have multiple accounts.
        :param phone_number:
        :param email:
        :param name:
        :param customer_id:
        :return: Account
        """

        # validations for existing customer
        if customer_id is None or name is None or email is None or phone_number is None:
            raise InvalidCustomerException()

        account_number = self.__generate_account_number()
        account_id = self.__repository.increment_and_get()
        account = Account(customer_id, account_id, account_number)

        return self.__repository.save_account(account)

    def get_account(self, account_id: int) -> Account:
        """Returns customer Account if present or else AccountNotFoundException is thrown
        :param account_id: customer account_id
        :return: Account
        """

        account = self.__repository.find_account_by_id(account_id)
        if account is None:
            raise AccountNotFoundException()
        return account

    def get_all_customer_accounts(self, customer_id: int) -> [Account]:
        return self.__repository.find_accounts_by_customer_id(customer_id)

    @staticmethod
    def __generate_account_number() -> int:
        return int(str(uuid.uuid1().int >> 64)[:16])
