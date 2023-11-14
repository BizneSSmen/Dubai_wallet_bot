from enum import Enum
from math import ceil, trunc

from pydantic import (
    BaseModel,
    confloat,
    field_validator,
    Field,
    conint)


class OperationTypes(str, Enum):
    change: str = 'change'


class OperationStatuses(str, Enum):
    created: str = 'created'
    approved: str = 'approved'


class Currency(str, Enum):
    dirhams: str = 'AED'
    rubles: str = 'RUB'


class ClaimModel(BaseModel):
    operationType: str = Field(default=OperationTypes.change.value, serialization_alias='operation_type')
    description: str = None
    phoneNumber: str | None = Field(pattern=r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}", default=None, serialization_alias='tel')
    status: str = Field(default=OperationStatuses.created.value)
    targetAmount: conint(gt=0) = Field(default=0, serialization_alias='sum_A')
    finalAmount: conint(gt=0) = Field(default=0, serialization_alias='sum_B')
    currencyA: str | None = Field(default=None, serialization_alias='currency_A')
    currencyB: str | None = Field(default=None, serialization_alias='currency_B')
    exchangeAppliedRate: confloat(gt=0) = Field(default=0, serialization_alias='exchange_applied_rate')
    fee: float = Field(default=0)

    class Config:
        validate_assignment = True

    @field_validator('currencyB', 'currencyA')
    @classmethod
    def roundTargetAmount(cls, _str: str):
        if _str in Currency.__members__.values():
            return _str
        else:
            raise ValueError("Received a string that is not a valid currency")

    @field_validator('currencyB', 'currencyA')
    @classmethod
    def roundTargetAmount(cls, _str: str):
        if _str in OperationStatuses.__members__.values():
            return _str
        else:
            raise ValueError("The application cannot have the specified status")

