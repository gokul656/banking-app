from src.domain.transaction import Transaction


class TransactionRepository:
    # Declared as dictionary so that elements can be access at O(1) tc.
    __transactions: {str: Transaction}

    def __init__(self):
        self.__transactions = {}

    def save(self, txn: Transaction) -> Transaction:
        self.__transactions[txn.txn_id] = txn
        return self.__transactions[txn.txn_id]

    def find_all_by_account_id(self, account_id) -> [Transaction]:
        return [txn for txn in self.__transactions.values() if txn.account_id == account_id]
