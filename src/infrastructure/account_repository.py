from src.domain.account import Account


class AccountRepository:
    __account_count: int
    # Declared as dictionary so that elements can be access at O(1) tc.
    __accounts: {int: Account}

    def __init__(self):
        self.__accounts = {}
        self.__account_count = 0

    def find_account_by_id(self, account_id) -> Account | None:
        try:
            return self.__accounts[account_id]
        except KeyError:
            return None

    def find_accounts_by_customer_id(self, customer_id):
        return [account for account in self.__accounts.values() if account.get_customer_id() == customer_id]

    def save_account(self, account) -> Account:
        self.__accounts[account.get_account_id()] = account
        return self.find_account_by_id(account.get_account_id())

    def increment_and_get(self) -> int:
        self.__account_count += 1
        return self.__account_count
