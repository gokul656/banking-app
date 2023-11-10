from datetime import datetime
import uuid

from src.domain.transaction import Transaction
from src.infrastructure.account_repository import AccountRepository
from src.infrastructure.transaction_repository import TransactionRepository


class TransactionUseCase:
    def __init__(self, account_repository: AccountRepository, transaction_repository: TransactionRepository):
        self.__account_repository = account_repository
        self.__transaction_repository = transaction_repository

    def make_transaction(self, account_id: int, amount: float, transaction_type: str):
        # Validating the transaction
        self.validate_txn(account_id, amount, transaction_type)

        # TODO: should be done as a transactional event
        account = self.__account_repository.find_account_by_id(account_id)
        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)

        # generating receipt for the transaction
        tx_id = uuid.uuid1().__str__()
        txn_receipt = Transaction(tx_id, account_id, account.get_customer_id(), amount, transaction_type,
                                  datetime.utcnow())

        return self.__transaction_repository.save(txn_receipt)

    def validate_txn(self, account_id: int, amount: float, transaction_type: str):
        balance: float = 0
        account = self.__account_repository.find_account_by_id(account_id)
        transaction = self.__transaction_repository.find_all_by_account_id(account_id)

        # just for double-checking the balance we're aggregating the total from transactions
        for txn in transaction:
            if txn.txn_type == "withdraw":
                balance -= txn.amount
            elif txn.txn_type == "deposit":
                balance += txn.amount

        if transaction_type == "withdraw" and (amount > balance or account.get_balance() < amount):
            raise Exception("insufficient funds")
