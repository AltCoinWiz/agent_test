from ledger.infrastructure.in_memory import InMemoryLedgerRepository, InMemoryEventRepository
from ledger.services.payment_processor import PaymentProcessor
from ledger.services.account_service import AccountService

def create_app():
    ledger = InMemoryLedgerRepository()
    events = InMemoryEventRepository()
    processor = PaymentProcessor(ledger, events)
    return AccountService(ledger, processor), ledger, events
