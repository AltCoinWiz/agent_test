class PaymentQuery:
    def __init__(self,p,b,r): self.payments=p; self.balances=b; self.refunds=r
    def payment(self,k): return self.payments.get(k)
    def balance(self,k): return self.balances.get(k)
    def refund_total(self,k): return self.refunds.total_for(k)
