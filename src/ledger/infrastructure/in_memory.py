from ledger.domain.models import LedgerEntry

class InMemoryLedgerRepository:
    def __init__(self):
        self._entries: list[LedgerEntry] = []

    def append(self, entry: LedgerEntry) -> None:
        self._entries.append(entry)

    def entries_for(self, account_id: str) -> list[LedgerEntry]:
        return [e for e in self._entries if e.account_id == account_id]

    def contains_entry(self, entry_id: str) -> bool:
        return any(e.entry_id == entry_id for e in self._entries)

class InMemoryEventRepository:
    def __init__(self):
        self._processed: set[str] = set()

    def is_processed(self, event_id: str) -> bool:
        return event_id in self._processed

    def mark_processed(self, event_id: str) -> None:
        self._processed.add(event_id)
