from datetime import datetime


class Transaction:
    def __init__(self, txn_id: str, account_id: int, customer_id: int, amount: float, txn_type: str,
                 executed_at: datetime):
        self.txn_id = txn_id
        self.customer_id = customer_id
        self.account_id = account_id
        self.amount = amount
        self.txn_type = txn_type
