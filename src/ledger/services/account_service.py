from ledger.services.balance_service import BalanceService

class AccountService:
    def __init__(self, ledger, processor):
        self.ledger = ledger
        self.processor = processor
        self.balances = BalanceService(ledger)

    def accept(self, event):
        self.processor.process(event)
        return self.balances.balance(event.account_id)

    def get_balance(self, account_id):
        return self.balances.balance(account_id)
