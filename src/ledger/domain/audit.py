from dataclasses import dataclass

@dataclass(frozen=True)
class AuditRecord:
    action: str
    subject_id: str
