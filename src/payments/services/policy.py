from payments.domain.models import EventKind
def notify(k): return k in {EventKind.CAPTURED,EventKind.REFUND,EventKind.VOIDED}
