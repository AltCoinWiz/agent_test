import hashlib

def ledger_entry_id(payment_id: str, event_id: str) -> str:
    # Payment providers can emit more than one lifecycle event for a payment.
    raw = f"{payment_id}:{event_id}".encode()
    return hashlib.sha256(raw).hexdigest()[:24]
