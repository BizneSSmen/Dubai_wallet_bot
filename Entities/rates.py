from _decimal import Decimal
from pydantic import BaseModel, Field


class Official(BaseModel):
    value: float | None = Field(serialization_alias='value', default=None)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class Sell(BaseModel):
    value: float | None = Field(serialization_alias='value', default=0)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class Buy(BaseModel):
    value: float | None = Field(serialization_alias='value', default=0)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class SellBig(BaseModel):
    value: float = Field(serialization_alias='value', default=0)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class BuyBig(BaseModel):
    value: float | None = Field(serialization_alias='value', default=0)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class Rates(BaseModel):
    official: Official = Field(default=Official())
    sell: Sell = Field(default=Sell())
    buy: Buy = Field(default=Buy())
    sellBig: SellBig = Field(default=SellBig(), alias='sellbig')
    buyBig: BuyBig = Field(default=BuyBig(), alias='buybig')
