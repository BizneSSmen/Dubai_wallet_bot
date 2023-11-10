import io
from dataclasses import dataclass


@dataclass
class OperationTypes:
    change: str = 'change'


@dataclass
class OperationStatuses:
    created: str = 'created'
    approved: str = 'approved'


class Claim:
    def __init__(self):
        self.operationType: str = OperationTypes.change
        self.description: str = None
        self.phoneNumber: str = None
        self.status: str = OperationStatuses.created
        self.targetAmount: float = 0
        self.finalAmount: float = 0
        self.exchangeAppliedRate: float = 0
        self.fee: float = 0
        self.currency_A: str = None
        self.currency_B: str = None
