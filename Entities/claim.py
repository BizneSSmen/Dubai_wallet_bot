from enum import Enum
from dataclasses import dataclass
from typing import Optional
from pydantic import (
    BaseModel,
    confloat, 
    field_validator,
    Field,
    conint)

print(int(150.23))
# class OperationTypes(str, Enum):
#     change: str = 'change'


# class OperationStatuses(str, Enum):
#     created: str = 'created'
#     approved: str = 'approved'


# class Currency(str, Enum):
#     dirhams: str = 'AED'
#     rubles: str = 'RUB'


# class Claim1(BaseModel):
#     operationType: str = Field(default=OperationStatuses.change.value, serialization_alias='operation_type')
#     description: str = None
#     phoneNumber: str | None = Field(pattern=r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}", default=None, serialization_alias='tel')
#     status: str = Field(default=OperationTypes.created.value)
#     targetAmount: conint(gt=0) = Field(default=0, serialization_alias='sum_A')
#     finalAmount: conint(gt=0) = Field(default=0, serialization_alias='sum_B')
#     currencyA: str | None = Field(default=None, serialization_alias='currency_A')
#     currencyB: str | None = Field(default=None, serialization_alias='currency_B')
#     exchangeAppliedRate: confloat(gt=0) = Field(default=0, serialization_alias='exchange_applied_rate')
#     fee: float = Field(default=0)
    
#     class Config:
#         validate_assignment = True
    
#     @field_validator('currencyB', 'currencyA')
#     @classmethod
#     def roundTargetAmount(cls, _str: str):
#         if _str in Currency.__members__.values():
#             return _str
#         else:
#             raise ValueError("Received a string that is not a valid currency")   
        
#     @field_validator('currencyB', 'currencyA')
#     @classmethod
#     def roundTargetAmount(cls, _str: str):
#         if _str in OperationStatuses.__members__.values():
#             return _str
#         else:
#             raise ValueError("The application cannot have the specified status") 
    

# a = Claim1()


# a.currencyB = 'AED'
# a.currencyA = 'RUB'
# a.phoneNumber = '89773932154'
# print(Currency.dirhams)



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
    


