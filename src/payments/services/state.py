from payments.domain.models import PaymentStatus,EventKind
STATUS={EventKind.CREATED:PaymentStatus.CREATED,EventKind.AUTHORIZED:PaymentStatus.AUTHORIZED,
EventKind.CAPTURED:PaymentStatus.CAPTURED,EventKind.REFUND:PaymentStatus.REFUNDED,EventKind.VOIDED:PaymentStatus.VOIDED}
def status_for(k): return STATUS[k]
def newer(e,p): return p is None or e.sequence>p.sequence
