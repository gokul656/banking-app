from src.exception.customer_exception import AccountNotFoundException, AccountAlreadyExistsException
from src.config.context import BaseContext

ctx = BaseContext()


def test_banking_scenario():
    try:
        customer = ctx.customer_use_case.create_customer("customer_1", "customer@gmail.com", "537458377")
        account = ctx.account_use_case.create_account(1, customer.name, customer.email, customer.phone_number)

        ctx.transaction_use_case.make_transaction(account.get_account_id(), 15, "deposit")
        ctx.transaction_use_case.make_transaction(account.get_account_id(), 10, "withdraw")

        # Assuming account statement as account balance
        # Overall transactions list can be fetched using get_account_transactions method
        account_statement = ctx.account_statement_use_case.generate_account_statement(1)
        print(f"Account balance : {account_statement}")
    except AccountAlreadyExistsException as e:
        pass
    except AccountNotFoundException as e:
        pass


if __name__ == "__main__":
    test_banking_scenario()
