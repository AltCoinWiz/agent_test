from payments.infrastructure.memory import Payments,Processed,Balances,Refunds,Notifications,Audit
from payments.services.processor import PaymentProcessor
def create_app():
    p=Payments(); d=Processed(); b=Balances(); r=Refunds(); n=Notifications(); a=Audit()
    return PaymentProcessor(p,d,b,r,n,a),p,d,b,r,n,a
