from src.domain.transaction import Transaction
from src.infrastructure.account_repository import AccountRepository
from src.infrastructure.transaction_repository import TransactionRepository


class AccountStatementUseCase:
    def __init__(self, transaction_repository: TransactionRepository, account_repository: AccountRepository):
        self.__transaction_repository = transaction_repository
        self.__account_repository = account_repository

    def generate_account_statement(self, account_id: int) -> float:
        return self.__account_repository.find_account_by_id(account_id).get_balance()

    def get_account_transactions(self, account_id: int) -> [Transaction]:
        return self.__transaction_repository.find_all_by_account_id(account_id)
