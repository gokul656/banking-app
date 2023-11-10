from src.infrastructure.account_repository import AccountRepository
from src.infrastructure.customer_repository import CustomerRepository
from src.infrastructure.transaction_repository import TransactionRepository
from src.use_cases.account_statement_usecase import AccountStatementUseCase
from src.use_cases.account_usecase import AccountUseCase
from src.use_cases.customer_usecase import CustomerUseCase
from src.use_cases.transaction_usecase import TransactionUseCase


class BaseContext:
    def __init__(self):
        # Repositories
        self.__account_repo = AccountRepository()
        self.__customer_repo = CustomerRepository()
        self.__txn_repo = TransactionRepository()

        # Use cases
        self.customer_use_case = CustomerUseCase(self.__customer_repo)
        self.account_use_case = AccountUseCase(self.__account_repo)
        self.transaction_use_case = TransactionUseCase(self.__account_repo, self.__txn_repo)
        self.account_statement_use_case = AccountStatementUseCase(self.__txn_repo, self.__account_repo)
