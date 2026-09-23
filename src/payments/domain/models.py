from dataclasses import dataclass
from decimal import Decimal
from enum import IntEnum,Enum
class PaymentStatus(IntEnum):
    CREATED=10; AUTHORIZED=20; CAPTURED=30; REFUNDED=40; VOIDED=90
class EventKind(str,Enum):
    CREATED="created"; AUTHORIZED="authorized"; CAPTURED="captured"; REFUND="refund"; VOIDED="voided"
@dataclass(frozen=True)
class ProviderEvent:
    event_id:str; payment_id:str; merchant_id:str; kind:EventKind; amount:Decimal; sequence:int
@dataclass
class Payment:
    payment_id:str; merchant_id:str; status:PaymentStatus; sequence:int; captured:Decimal; refunded:Decimal
