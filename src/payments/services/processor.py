from decimal import Decimal
from payments.domain.models import Payment,EventKind
from payments.domain.money import money
from payments.services.state import status_for,newer
from payments.services.policy import notify
class PaymentProcessor:
    def __init__(self,payments,processed,balances,refunds,notifications,audit):
        self.payments=payments; self.processed=processed; self.balances=balances
        self.refunds=refunds; self.notifications=notifications; self.audit=audit
        self.pending_refunds={}
    def process(self,event):
        if self.processed.contains(event.event_id): return False
        current=self.payments.get(event.payment_id)
        if event.kind==EventKind.REFUND:
            if current is None or current.captured<event.amount:
                self.pending_refunds.setdefault(event.payment_id,[]).append(event)
                self.processed.add(event.event_id); return False
            amount=money(event.amount)
            self.refunds.add(event.event_id,event.payment_id,amount)
            self.balances.move(event.event_id,event.merchant_id,-amount)
            current.refunded=money(current.refunded+amount)
            current.status=status_for(event.kind); current.sequence=max(current.sequence,event.sequence)
            self.payments.save(current)
            if notify(event.kind): self.notifications.send(event.event_id,event.payment_id,"refund")
            self.audit.append(event.event_id,event.payment_id,"refund")
            self.processed.add(event.event_id); return True
        if current is not None and not newer(event,current):
            self.processed.add(event.event_id); return False
        captured=current.captured if current else Decimal("0")
        refunded=current.refunded if current else Decimal("0")
        if event.kind==EventKind.CAPTURED:
            captured=money(captured+event.amount)
            self.balances.move(event.event_id,event.merchant_id,money(event.amount))
        payment=Payment(event.payment_id,event.merchant_id,status_for(event.kind),event.sequence,captured,refunded)
        self.payments.save(payment)
        if notify(event.kind): self.notifications.send(event.event_id,event.payment_id,event.kind.value)
        self.audit.append(event.event_id,event.payment_id,event.kind.value)
        self.processed.add(event.event_id)
        if event.kind==EventKind.CAPTURED:
            queued=self.pending_refunds.pop(event.payment_id,[])
            for refund in queued: self._apply_queued_refund(refund)
        return True
    def _apply_queued_refund(self,event):
        current=self.payments.get(event.payment_id); amount=money(event.amount)
        if current is None or current.captured<amount:
            self.pending_refunds.setdefault(event.payment_id,[]).append(event); return
        self.refunds.add(event.event_id,event.payment_id,amount)
        self.balances.move(event.event_id,event.merchant_id,-amount)
        current.refunded=money(current.refunded+amount)
        current.status=status_for(EventKind.REFUND); current.sequence=max(current.sequence,event.sequence)
        self.payments.save(current)
        self.notifications.send(event.event_id,event.payment_id,"refund")
        self.audit.append(event.event_id,event.payment_id,"refund")
